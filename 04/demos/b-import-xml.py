import xml.etree.ElementTree as ET

# Parse into an ElementTree
tree = ET.parse('data\\users-100.xml')
print(tree)
# print(dir(tree))

# Get the root, children, and review one Element
users_root = tree.getroot()
print(users_root)
print(users_root.tag)

# NOW SURE HOW THIS WORKS
# print(list(users_root))
# children = list(users_root)[0].attrib['AccountId']
# len(list(users_root.getchildren()))
# print(f"Printing children: {children}")
# len(list(users_root.getchildren()))


# users_root[0]
# users_root[0].tag
# users_root[0].attrib

