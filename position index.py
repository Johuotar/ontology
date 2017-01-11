from collections import defaultdict
import codecs

f=codecs.open('testfile2.txt', 'r','UTF-8')
words = f.read().splitlines()#remove end characters
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
        #use spaces to slice beginning characters
        index[str(pos)].append(term[spaces:])
        spacesindex[pos].append(spaces)
        
    else:
        continue

def search(values,searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                print("found it at " + k)
                return k
            print (searchFor + " not found at " + k)
            
print (search(index,'polvi'))#returns relevant key
#Choose word. TODO


'''
i=-1
while i<=26:
    i=i+1
    i2=i+1#no support for indent amount variations atm
    if spacesindex[i] < spacesindex[i2]:#Skip blanks here
        print (str(i) + " upperclass of " + str(i2))#Test code pls ignore
'''
for key in index.keys():
    print ('key: ' + key + ' ' , end="")
    print('value: ', end="")
    print (index[key])

for key in spacesindex.keys():
    print('key: ', end="")
    print (key, end=" ")
    print('value: ', end="")
    print (spacesindex[key])
