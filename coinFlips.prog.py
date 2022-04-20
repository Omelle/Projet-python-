import random
print('Je vais lancer 1000 fois une pièce.Devinez combien de fois je vais obtenir face ( appuie sur Entrée pour commencer).')
input()
flips = 0
heads = 0
while flips <1000:
    if random.randint(0, 1) == 1:
        heads = heads +1
        flips = flips +1

        if flips == 900:
            print('900 lancers  et il y a eu' + str(heads) + 'fois face.')
            if flips == 100:
                print('Après 100 tentaives, j\'ai obtenu face ' + str(heads) +'fois.')
                if flips == 500 :
                    print('A mi-chemin, le côté face est sorti' + str(heads) +'fois.')

print()
print('Après les 1 000 lancers, j\'ai obtenu'+ str(heads)+'fois face !')
print('Etais-tu proche de la bonne solution ?')
                    
