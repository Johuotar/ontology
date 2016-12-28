from collections import defaultdict
import codecs

f=codecs.open('testfile.txt', 'r','UTF-8')
words = f.readlines()
index = defaultdict(list)

def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

for pos, term in enumerate(words):
    spaces=len(term)-len(term.lstrip())
    
    if isBlank(term) ==False:
        index[term].append(pos)
        print (index[term], term)
    else:
        continue
        
    
'''
for key in sorted(index):
    print (key, index[key])
    
    spaces=len(key)-len(key.lstrip())
    print (spaces)
'''
