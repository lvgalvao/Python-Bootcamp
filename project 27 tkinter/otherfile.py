import re

menu = ["coca cola","pepsi","suco"]
count_item_in_menu = []

def count_item(item_search):
    global count_item_in_menu
    for item in menu:
        match_item = re.fullmatch(item_search, item)
        count_item_in_menu.append(match_item)
    return count_item_in_menu

print(count_item("suco"))