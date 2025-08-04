from py_trees.blackboard import Blackboard

def initalize_blackboard() -> Blackboard:
    bb = Blackboard()
    bb.set("partTrayQty", 3)
    bb.set("kitTrayQty", 0)
    bb.set("partsMoved", 0)
    bb.set("isSufficient", False)
    return bb