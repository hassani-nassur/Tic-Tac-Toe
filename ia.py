import random,time
def ia(list,symbole):
    caseVide = []
    for key,value in enumerate(list):
        if value == None:
            caseVide.append(key)
    random.shuffle(caseVide)
    indexChose = random.choice(caseVide)
    jeux = [indexChose,symbole]
   
    return jeux