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

chosenw = input('Choose a word: ')
chosenwline = None

def search(values,searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                print("found it at " + k)
                return int(k) #TODO: find all instances of word instead of just 1st found
            print (searchFor + " not found at " + k)
            
chosenwline=search(index,chosenw)
comparedline=chosenwline

while comparedline >= 0:
    if spacesindex[comparedline] < (spacesindex[chosenwline]):
        #print(spacesindex[comparedline] + spacesindex[chosenwline]) #test purposes only code
        print(index[str(comparedline)]) #comparedline turned to string because keys are str
        comparedline = comparedline-1
    else:
        #print(spacesindex[comparedline] + spacesindex[chosenwline]) test purpose code 2
        comparedline= comparedline-1
'''
for key in index.keys():
    print ('key: ' + str(key) + ' ' , end="")
    print('value: ', end="")
    print (index[key])

for key in spacesindex.keys():
    print('key: ', end="")
    print (str(key), end=" ")
    print('value: ', end="")
    print (spacesindex[key])
'''
