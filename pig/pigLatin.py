#!/usr/bin/python3

##Team DJM: MD. Chowdhury, Justin Liu, Declan Breen
##IntroCS pd2
##HW33 —— Anslatingtray Englishway intoway Igpay Atinlay
##T 2019-04-02

'''
PIG LATIN RULES:
1. If the word begins with a vowel, “way” is suffixed.
2. If the word begins with two consonants, they are moved to the end and “ay” is suffixed.
3. If the word begins with only one consonant, the consonant is moved to the end and “ay” is suffixed.
4. If the word is capitalized, it is decapitalized and then capitalized after all other rules have been applied.

OUTLINE:
The function will translate a phrase in English to Pig Latin. The function will use two or three helper functions. The first helper function just changes an English word to pig Latin, the second checks for double consonants and adjusts the pig Latin accordingly. And the third check for vowel beginnings and also adjusts according to such. In this way the main function will call upon these three helper functions and create a hopefully working English to pig Latin translator.

DEVELOPMENT PLAN:
The first step is to create a basic pig Latin translator, which will take a word and change it to pig Latin, without considering the double consonants or vowel at the beginning.

Then we will make a function that checks for double consonants and outputs with the consonants moved to the end.

Third we will create a function to check for vowels at the beginning so that vowel words stay the same and add way.

Finally we will combine the three into one main function.



DEVELOPMENT LOG:
2019-04-01 5:20pm
Md, Justin: Recorded the first four rules of pig Latin

2019-04-01 9:16pm
MD: Finished development plan and outline of the function.

2019-04-01 10:12pm
Justin: Edited development plan and outline.

2019-04-02 9:20am
Declan, MD, Justin: Developed sep(string) function

2019-04-02 5:30pm
Justin: Developed pigLatin(word) function that works for single consonant-starting words

2019-04-02 9:04pm - 6:05pm
Justin: developed isAlpha(word), isVowel(char), transWord(word), translate(phrase), transSingCons(word), transVowel(word)

2019-04-02 9:04pm
MD: developed transDoubCons(word) function that works for words with double consonants at the beginning, ignoring words with y as third letter.
Declan: developed translate function

2019-04-02 10:03pm
Justin: finished translate function

2019-04-02 10:28pm
MD: checked over code and added examples
Justin: added changes to plan section

CHANGES TO PLAN:
We decided to add way more helper functions than expected. Instead of using the helper functions to check for cases (e.g. what a word starts with), we implemented case checking using boolean expressions in the transWord(word) function. We had a different helper functions do what to do in each case (e.g. a helper to translate a word beginning with a vowel, and a helper to translate a double consonant-starting word). We also added helpers to check whether a character is a letter and to check if the letter is a vowel. This way, it’s like having completed small pieces of a puzzle, and then putting them together in the end (the end being translate(phrase)) In addition, at first we decided to have a phrase-splitter function, but we decided to translate a sentence word by word, given a phrase, within the translate(word) function.
'''
import cgi
import cgitb

#cgitb.enable()

#isAlpha(char)
#returns True if character is a letter in the alphabet, False otherwise
def isAlpha(char):
    return ((ord(char) >= 65 and ord(char) <= 90)
            or (ord(char) >= 97 and ord(char) <= 122))

#isVowel(char)
#returns True if character is a vowel, upper or lower case, False otherwise
def isVowel(char):
    return (ord(char) == 65
            or ord(char) == 69
            or ord(char) == 73
            or ord(char) == 79
            or ord(char) == 85
            or ord(char) == 97
            or ord(char) == 101
            or ord(char) == 105
            or ord(char) == 111
            or ord(char) == 117)

#transVowel(word)
#returns Pig Latin equivalent of the string word if the first letter is a vowel
def transVowel(word):
    return word + 'way'

#transSingCons(word)
#returns Pig Latin equivalent of the strin word if only the first letter is a consonant
def transSingCons(word):
    new = ''
    first = word[0]
    new = word[1:]
    new += first + 'ay'
    return new

#transDoubCons(word)
#returns Pig Latin equivalent of the string word if the first two letters are consonants

def transDoubCons(word):
    new = ''
    first = word[0:2]
    new = word[2:]
    new += first + 'ay'
    return new

#transWord(word)
#returns Pig Latin equivalent of the string word

def transWord(word):
    new = ''
    caps = False
    upper = False
    punc = ''
    if not isAlpha(word[len(word) - 1]): ##if punctuated
        punc = word[len(word) - 1]
        word = word[:-1] ##word without punctuation
    if ((word != word.upper() ##if not all caps
        and word == word.capitalize()) ##if capitalized
        or (len(word) == 1 and word == word.upper())): ##if single caps
            caps = True
    elif word == word.upper(): ##if all caps
        upper = True
    word = word.lower()
    if isVowel(word[0]): ##if 1st letter is vowel
        new = transVowel(word)
    elif not isVowel(word[1]): ##if 2nd letter is consonant
        if word[1] == 'y': ##if 2nd letter is 'y'
            new = transSingCons(word)
        else:
            new = transDoubCons(word)
    elif isVowel(word[1]): ##if  2nd letter is vowel
        if word[0:2] == 'qu': ##if 1st two letters are 'qu'
            new = transDoubCons(word)
        else:
            new = transSingCons(word)
    if caps:
        new = new.capitalize() ##recapitalize
    if upper:
        new = new.upper()
    new += punc
    return new

# translate(phrase)
# returns Pig Latin equivalent of the string phrase

def translate(phrase):
    word = ''
    new = ''
    for x in phrase:
        if x == ' ':
            word = phrase[:phrase.find(x)]
            phrase = phrase[phrase.find(x) + 1:]
            new += transWord(word) + ' '
    new += transWord(phrase)
    return new

def dictify(x):
    d = {}
    keys = x.keys()
    for a in keys:
        d[a] = x.getvalue(a)
    return d

#print(translate("What are the rules of Pig Latin?"))
#sb "Atwhay areway ethay ulesray ofway Igpay Atinlay?"

#print(translate("the pope rocks red kicks"))
#sb "ethay opepay ocksray edray ickskay"

#print(translate("There’s a competition called the Tri-Wizard Tournament between three wizarding schools and it’s extremely dangerous. Someone nominates Harry’s name though he’s under-age and he’s chastised by people because they think he did it himself for fame. He survives the tournament and with another student of Hogwarts, Cedric, reached the trophy first. They both touch it at the same time and are transported to another place. That’s where Voldy is trying to come back to life. He and his side-kick (the rat in the third part who escaped) were expecting only Harry, so Cedric is killed. They take Harry’s blood and Voldy gets his body back (he did not have a proper one after the event described in the first part when Harry was an infant). Then Harry somehow escapes with Cedric’s body."))
#sb "Ere’sthay away ompetitioncay alledcay ethay i-wizardtray Ournamenttay etweenbay reethay izardingway hoolsscay andway it’sway extremelyway angerousday. Omeonesay ominatesnay Arry’shay amenay oughthay e’shay under-ageway andway e’shay astisedchay ybay eoplepay ecausebay eythay inkthay ehay idday itway imselfhay orfay amefay. Ehay urvivessay ethay ournamenttay andway ithway anotherway udentstay ofway Ogwartshay, Edriccay, eachedray ethay ophytray irstfay. Eythay othbay ouchtay itway atway ethay amesay imetay andway areway ansportedtray otay anotherway aceplay. At’sthay erewhay Oldyvay isway yingtray otay omecay ackbay otay ifelay. Ehay andway ishay ide-kicksay He(tay atray inway ethay irdthay artpay owhay escapedway) ereway expectingway onlyway Arryhay, osay Edriccay isway illedkay. Eythay aketay Arry’shay oodblay andway Oldyvay etsgay ishay odybay ackbay E(hay idday otnay avehay away operpray oneway afterway ethay eventway escribedday inway ethay irstfay artpay enwhay Arryhay asway anway infant)way. Enthay Arryhay omehowsay escapesway ithway Edric’scay odybay."

#print(translate("I love computer science and Mr. Brown. Mr. Brown is my favorite teacher and computer science is my favorite class. Life without Mr. Brown is summer without the Sun, heaven without Jah. Please let me in AP Comp Sci."))

foo = cgi.FieldStorage()
q = dictify(foo)

print("Content-Type: text/html")
print("")

print("""
<html>
<style>
html {
}

a {
 text-decoration: none
}
</style>

<a href='translate.html'>Anslatetray oremay uffstay!</a>
<br><br>
""")

#print(q)
#print(q[text])
try:
    print(translate(q["text"]))
except:
    print("<img src='error.jpg'>")

print("""
</html>
""")
