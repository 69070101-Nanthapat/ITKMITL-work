"""muddled menu"""
menu = []

while True:
    line = input().strip()

    if line == "DONE":
        break
    if line == "CLOSED":
        menu.clear()
        break
    if line == "SOMETHING'S WRONG":
        menu.clear()
    elif line.startswith("Can't do: "):
        item = line.replace("Can't do: ", "")
        while item in menu:
            menu.remove(item)
    elif "#" in line:
        name, pos = line.rsplit("#", 1)
        name = name.strip()
        pos = pos.strip()

        if pos == "N":
            menu.append(name)
        else:
            idx = int(pos) - 1
            menu.insert(idx, name)

print(f"Full Course: {menu} Reversed: {list(reversed(menu))}")
