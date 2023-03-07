items = {
    "item1": ["tag1", "tag2", "tag3"],
    "item2": ["tag2", "tag4"],
    "item3": ["tag1", "tag5"],
    "item4": ["tag2", "tag3", "tag5"],
    "item5": ["tag4", "tag5"]
}

def search_items_by_tags(tags):
    matching_items = set()
    tag_dict = {}
    for item, item_tags in items.items():
        for tag in item_tags:
            if tag not in tag_dict:
                tag_dict[tag] = set()
            tag_dict[tag].add(item)
    if all(tag in tag_dict for tag in tags):
        matching_items = set.intersection(*[tag_dict[tag] for tag in tags])
    return matching_items
