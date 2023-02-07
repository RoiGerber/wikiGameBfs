import wikipedia



def bfs_wiki(input,target):
    wikipedia.set_lang("he")
    iter = 1
    used = {}
    queue = [input]
    while(True):
        curVal = queue.pop()
        try:
            wikiPage = wikipedia.page(curVal)
        except:
            pass
        for link in wikiPage.links:
            if((link not in used) and (not link.isdigit()) and (not link=="תקן בינלאומי למזהי שמות")):
                queue.append(link)
                used[link]=curVal
            if link == target:
                return used
        print("layer " + str(iter))
        iter+=1
    return


inputWord = input("insert a starting word\n")
targetWord = input("insert a target word\n")
used = bfs_wiki(inputWord , targetWord)

word = targetWord
path=[]

while(word!=inputWord):
    father = used[word]
    path.append(word)
    word = father

output =''
for w in path:
    output+=w
    output += ' <--'
output+=inputWord
print(output)

a = 0


