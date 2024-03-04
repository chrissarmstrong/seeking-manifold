import re

# Open the input file
with open('test.md', 'r') as file:
    content = file.readlines()

# Make substitutions
for i in range(len(content)):
    line = content[i]
    match = re.match(r'!\[.*\]\(/images/(.*\.png)\)', line)
    if match:
        alt_text = re.search(r'\[(.*?)\]', line).group(1)
        filename = match.group(1)
        new_line = f'![[{filename}|{alt_text}]]\n'
        content[i] = new_line

# Write the modified content back to the file
with open('test2.md', 'w') as file:
    file.writelines(content)

