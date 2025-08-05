import re

def solution(files):
      
    return sorted(files, key=sortFileKey)

def sortFileKey(filename):
    match = re.match(r'([^0-9]+)(\d+)', filename)
    if match:
        text = match.group(1).lower()
        number = int(match.group(2) if match.group(2) else 0)
        print(text, number)
        return (text, number)

