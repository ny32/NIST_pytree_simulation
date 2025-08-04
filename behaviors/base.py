from py_trees.behaviour import Behaviour
from py_trees.common import Status
import time
from behaviors.constants import DEBUG_PAUSE

# ChatGPT Snippet - Handling Logging
import logging
from py_trees import logging as py_tree_logging

py_tree_logging.level = py_tree_logging.Level.DEBUG

logger = logging.getLogger("py_trees")
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
#ChatGPT Snippet

class Action(Behaviour):
    def __init__(self, name: str) -> None:
        super(Action, self).__init__(name)
    
    def setup(self) -> None:
        self.logger.debug(f"Action::Setup --> {self.name}")
        time.sleep(DEBUG_PAUSE)
    
    def initialise(self):
        self.logger.debug(f"Action::Initialize --> {self.name}")
        time.sleep(DEBUG_PAUSE)
    
    def update(self) -> Status:
        self.logger.debug(f"Action::Update --> {self.name}")
        time.sleep(DEBUG_PAUSE)
        return Status.SUCCESS
    def terminate(self, new_status: Status) -> None:
        self.logger.debug(f"Action::Terminate --> {self.name} is {new_status}")
        time.sleep(DEBUG_PAUSE)

class Condition(Action):
    pass