from behaviors.custom_blackboard import initalize_blackboard
from py_trees.blackboard import Blackboard
from create_tree import make_bt
import py_trees as pt
import time
from behaviors.constants import DEBUG_PAUSE, CARRYING_AMOUNT, GOAL_AMOUNT_MOVED
from py_trees.common import Status

bb = initalize_blackboard()

if __name__ == "__main__":
    root = make_bt()
    tree = pt.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    tick_count = 0
    while True:
        tick_count += 1
        print(f"\n--- Tick {tick_count} ---")
        tree.tick()
        current_tree_status = root.status 
        print(f"Status: {current_tree_status}, PartTray: {bb.get('partTrayQty')} parts, KitTray: {bb.get('kitTrayQty')} parts, Carrying Capacity: {CARRYING_AMOUNT} parts")
        if  bb.get("partsMoved") == GOAL_AMOUNT_MOVED:
            print(f"✅ Goal reached --> {bb.get('kitTrayQty')} parts now in Kit Tray")
            break
        elif current_tree_status == Status.FAILURE:
            print("❌ Tree Failure - Terminating")
            break
        elif current_tree_status == Status.INVALID:
            print("⚠️ Tree Invalid - Terminating")
            break

        time.sleep(DEBUG_PAUSE * 10)

    print("--- Behavior Tree Terminated ---")
