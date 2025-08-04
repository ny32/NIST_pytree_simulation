from py_trees.composites import Sequence
from py_trees.decorators import Inverter
from behaviors.actions import Pickup, PutDown
from behaviors.conditions import PartTraySufficient, KitTrayFull
from behaviors.base import Action

def make_bt() -> Sequence:
    root = Sequence(name="rootSequence", memory=False)
    isPartTraySufficient = PartTraySufficient("PartTrayQtyCheck")
    kitTrayNotFull = Inverter(name="KitTrayNotFull", child=KitTrayFull("KitTrayFull"))
    putDown = PutDown("PutPartDown")
    pickup = Pickup("PickUpPart")
    moveToKitTray = Action("MoveToKitTray")
    moveToPartTray = Action("MoveToPartTray")
    
    sequenceA = Sequence(name="sequenceA", memory=False)
    sequenceA.add_children([
        isPartTraySufficient,
        kitTrayNotFull
    ])

    sequenceB = Sequence(name="sequenceB", memory=False)
    sequenceB.add_children([
        moveToPartTray,
        pickup,
        moveToKitTray,
        putDown
    ])

    root.add_children([
        sequenceA,
        sequenceB
    ])
    return root