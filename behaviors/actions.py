from behaviors.base import Action
from py_trees.common import Status
import time
from behaviors.constants import DEBUG_PAUSE, CARRYING_AMOUNT
from behaviors.custom_blackboard import initalize_blackboard
from py_trees.blackboard import Blackboard

bb = initalize_blackboard()

class Pickup(Action):
    def update(self) -> Status:
        bb.set("partTrayQty", bb.get("partTrayQty") - CARRYING_AMOUNT)
        print(f"{bb.get('partTrayQty')} parts in Part Tray")
        time.sleep(DEBUG_PAUSE)
        return super(Pickup, self).update()

class PutDown(Action):
    def update(self) -> Status:
        bb.set("kitTrayQty", bb.get("kitTrayQty") + CARRYING_AMOUNT)
        bb.set("partsMoved", bb.get("partsMoved") + CARRYING_AMOUNT)
        print(f"{bb.get('kitTrayQty')} parts in Kit Tray")
        time.sleep(DEBUG_PAUSE)
        return super(PutDown, self).update()