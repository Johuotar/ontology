from collections import defaultdict
import codecs

f=codecs.open('testfile.txt', 'r','UTF-8')
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

#Choose word. TODO

chosenw = input('Choose a word: ')
chosenwline = None

def search(values,searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                print("found it at " + k)
                chosenwline=k
                return chosenwline
            print (searchFor + " not found at " + k)
            
search(index,chosenw)#returns relevant key

i=chosenwline
print("nyt while loop alkaa arvolla: "+str(i))
while i>0:
    i=i-1
    i2=i-1 #no support for indent amount variations atm
    if spacesindex[i] < spacesindex[i2]: #Skip blanks here
        print (str(i) + " upperclass of " + str(i2))
    else:
        print("baa")
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
    '''
