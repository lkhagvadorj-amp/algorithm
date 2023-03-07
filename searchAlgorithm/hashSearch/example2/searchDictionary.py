items = {
    "item1": ["tag1", "tag2", "tag3"],
    "item2": ["tag2", "tag4"],
    "item3": ["tag1", "tag5"],
    "item4": ["tag2", "tag3", "tag5"],
    "item5": ["tag4", "tag5"]
}

def search_items_by_tags(tags):
    matching_items = []
    for item, item_tags in items.items():
        if all(tag in item_tags for tag in tags):
            matching_items.append(item)
    return matching_items
