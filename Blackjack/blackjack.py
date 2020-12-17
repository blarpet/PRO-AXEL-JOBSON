import kortlek

lek = kortlek.skapaKortlek()

print(lek)

# behöver räkna ut kort

# hand
def skrivUtHanden(hand):
    print("Dina kort är:", end="")
    for kort in hand:
        print(str(kort) + ", ", end="")

# checka vinnaren

# spel-loop
while True:
    spela = input("Vill du spela blackjack. (Y/N) ")

    if spela != "Y":
        break

    lek = kortlek.skapaKortlek()

    print(lek)
    # Dealer tar 2 kort
    dealer = [lek.pop(0), lek.pop(0)]
    print(f"Dealerns första kort är {dealer[0]}")

    hand = [lek.pop(0), lek.pop(0)]
    print(f"Dina första två kort är: {hand[0]} och {hand[1]}")

    fortsätt = True
    # göra val (ta ett till kort eller stanna   )  
    while fortsätt:
        taKort = input("Ta ett till kort [Y/N]")
        if taKort == "Y":
            hand.append(lek.pop(0))
            skrivUtHanden(hand)
        else:
            fortsätt = False    