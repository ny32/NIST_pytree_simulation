import xml.etree.ElementTree as ET
from create_tree import make_bt  # 👈 import your tree

def export_to_dict(behaviour):
    node = {
        "name": behaviour.name,
        "type": behaviour.__class__.__name__,
        "children": []
    }
    if hasattr(behaviour, "children"):
        for child in behaviour.children:
            node["children"].append(export_to_dict(child))
    return node

def dict_to_xml(node_dict):
    element = ET.Element(node_dict["type"], name=node_dict["name"])
    for child in node_dict.get("children", []):
        child_elem = dict_to_xml(child)
        element.append(child_elem)
    return element

def save_tree_to_xml(root_behavior, filename="behavior_tree.xml"):
    tree_dict = export_to_dict(root_behavior)
    xml_element = dict_to_xml(tree_dict)
    tree = ET.ElementTree(xml_element)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Behavior tree saved to {filename}")

if __name__ == "__main__":
    root = make_bt()  # 👈 get your actual root node
    save_tree_to_xml(root, "my_behavior_tree.xml")
