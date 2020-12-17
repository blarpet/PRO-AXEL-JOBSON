import random as rnd

def skapaKortlek():
    kortNummer = [i for i in range(2,11)]
    klädKort = ["Kn", "D", "K", "A"]
    kortNummer += klädKort
    lek = 4*kortNummer
    blandaKort(lek)

    return lek

# blanda kort

def blandaKort(lek):
    return rnd.shuffle(lek)

