#<-------      SINGLE WORD TRANSLATOR HELPERS    ------>#

def isVowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' \
        or char == 'u' or char == 'A' or char == 'E' or char == 'O' \
        or char == 'I' or char == 'U' or char == 'y' or char == 'Y' 

def qIsVowel(char):
    return char == 'a' or char == 'e' or char == 'i' or char == 'o' \
        or char == 'A' or char == 'E' or char == 'O' or char == 'I' \
        or char == 'y' or char == 'Y'

def isCaps(char):
    return char == char.upper()

def findCons(word):
    cnt = 0
    if word[0] == "q" or word[0] == "Q":
        while len(word) > cnt and (not qIsVowel(word[cnt])):
            cnt += 1
    else:
        while len(word) > cnt and (not isVowel(word[cnt])):
            cnt += 1
    return cnt

def allCons(word):
    cnt = 0
    while cnt < len(word):
        if isVowel(word[cnt]):
            return False
        cnt += 1
    return True

#<------    SINGLE WORD TRANSLATOR    ------>#
def translateWord(word):
    strt=findCons(word)
    if isVowel(word[0]):
        return word + "way"
    elif not isCaps(word[0]):
        return word[strt:] + word[:strt] + "ay"
    elif len(word) == 1:
        return word + "ay"
    if allCons(word):
        return word + "ay"
    else:
        return word[strt].upper() + word[strt+1:] + word[0].lower() + \
               word[1:strt] + "ay"


#<------    MAIN FUNCTION HELPERS    ------>#
def isAlpha(char):
    num=ord(char)
    return (num >= 97 and num <= 122) or (num >= 65 and num <= 90)

def startWord(string):
    cnt = 0
    while cnt < len(string) and (not isAlpha(string[cnt])):
        cnt += 1
    return cnt

def endWord(string, strt):
    cnt = strt
    while cnt < len(string) and (isAlpha(string[cnt]) or ord(string[cnt]) == ord("'")):
        cnt += 1
    return cnt

def anyAlpha(string):
    cnt = 0
    while cnt < len(string):
        if isAlpha(string[cnt]):
            return True
        cnt += 1
    return False


#<------    MAIN FUNCTION    ------>#
def translate(string):
    old = string
    new = ""
    while anyAlpha(old):
        strt = startWord(old)
        end = endWord(old,strt)
        word = old[strt:end]
        strtNext = end + startWord(old[end+1:])
        new += translateWord(word) + old[end:strtNext+1]
        old = old[strtNext:]
    return string[:startWord(string)] + new
