from collections import defaultdict
import codecs

f=codecs.open('testfile.txt', 'r','UTF-8')
words = f.read().splitlines()
index = defaultdict(list)
spacesindex = defaultdict(list)

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

for pos, term in enumerate(words):
    spaces=len(term)-len(term.lstrip())
    
    if isBlank(term) ==False:
        #remove indentation here, after counting them, before storing string
        #remove 2 symbols * spaces and 2 from both ends?
        index[str(pos)].append(term)
        
        spacesindex[pos].append(spaces)
        
    else:
        continue

for key in index.keys():
    print ('key: ' + key , end="")
    print('value ', end="")
    print (index[key])

for key in spacesindex.keys():
    print('key ', end="")
    print (key)
    print('value ', end="")
    print (spacesindex[key])

print (index['2']) # delete this
'''
for key in sorted(index):
    print (key, index[key])
    
    spaces=len(key)-len(key.lstrip())
    print (spaces)
'''
