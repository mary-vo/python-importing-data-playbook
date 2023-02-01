import xml.etree.ElementTree as ET

# Parse into an ElementTree
tree = ET.parse('data\\users-100.xml')
print(tree)
# print(dir(tree))

# Get the root
users_root = tree.getroot()
print(users_root.tag)

# Get children (or subnodes)
print(list(users_root))
# Count to see how many subnodes there are
print(len(list(users_root)))
# To fetch one element
print(users_root[0])
# Fetch all the attributes of the first element
print(users_root[0].attrib)

