import re
text = "The rain in Spain stays mainly in the plain."

# Define a pattern to search for words starting with 'S' or 's'
pattern = r'\b[Ss]\w+'

matches = re.findall(pattern, text)

print("Matches:", matches)
