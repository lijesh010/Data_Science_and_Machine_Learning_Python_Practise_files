import re
#regex grouping
string = "Today is 2023-04-11"
pattern = "(\d{4})-(\d{2})-(\d{2})"
#\d \D any non-digit, \s-space \S-non-whitespace \w-alphanumeric \Wnon-alpha
match = re.search(pattern, string)
if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    print(f"Year: {year}, Month: {month}, Day: {day}")
else:print("Match not found.")