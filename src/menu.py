# src/menu.py

def flatten_menu(node):
    """Recursively flatten all item names in a nested menu structure."""
    if not node or not isinstance(node, dict):
        return []

    node_type = node.get("type")

    # Case 1: Single menu item
    if node_type == "item":
        name = node.get("name")
        return [name] if name else []

    # Case 2: Category with children
    if node_type == "category":
        items = []
        for child in node.get("children", []):
            items.extend(flatten_menu(child))
        return items

    # Case 3: Unknown or missing type
    return []
