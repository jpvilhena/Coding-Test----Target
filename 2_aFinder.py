import re

def FindA(sentence):
    #usando regex, vamos achar todos 'A', colocar numa lista e contar a lista
    occurrencesA = re.findall("a|A", sentence)
    return len(occurrencesA)

TestSentence = ("IMPORTANTE: Essa string pode ser informada")
numberOfAs = (FindA(TestSentence))
if numberOfAs:
    print(f"Existem {numberOfAs} As na frase")
else:
    print("Nao existem As na frase...")