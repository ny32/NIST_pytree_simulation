from behaviors.base import Condition
from py_trees.common import Status
import time
from behaviors.constants import DEBUG_PAUSE, GOAL_AMOUNT_MOVED, TRAY_MAX_PARTS, CARRYING_AMOUNT
from behaviors.custom_blackboard import initalize_blackboard
from py_trees.blackboard import Blackboard

bb = initalize_blackboard()

class KitTrayFull(Condition):
    def update(self) -> Status:
        time.sleep(DEBUG_PAUSE)
        if (bb.get("kitTrayQty") <= TRAY_MAX_PARTS - CARRYING_AMOUNT):
            return Status.FAILURE
        else:
            return Status.SUCCESS

class PartTraySufficient(Condition):
    def update(self) -> Status:
        time.sleep(DEBUG_PAUSE)
        if (bb.get("partTrayQty") >= GOAL_AMOUNT_MOVED):
            bb.set("isSufficient", True)
            return Status.SUCCESS
        elif (bb.get("isSufficient")):
            return Status.SUCCESS
        else:
            return Status.FAILURE