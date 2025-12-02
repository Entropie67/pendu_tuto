from random import choice

mots = [
    "pierre", "plante", "fleur", "valeur", "voyage", "avenir", "esprit",
    "souris", "nuages", "soleil", "lumiere", "torrent", "defi", "cendre",
    "dragon", "cheval", "panier", "douces", "lecture", "musique",
    "secret", "charme", "honneur", "espoir", "sagesse", "mirage",
    "eclipse", "destin", "diamant", "galaxy", "boheme", "velours",
    "orchid", "legende", "orages", "sirene", "voyant", "promet",
    "auteur", "danser", "libres", "image", "parfum", "traces",
    "sakura", "samedi", "hacker", "python", "machine", "rouges"
]

def valide(mot: str, secret: list[str], lettre: str) -> bool:
    """
        Vérifie si la lettre est présente dans le mot et pas
        encore découverte
    """
    if lettre in mot and lettre not in secret:
        return True
    else:
        return False
    
# tests  dffds
assert valide("sucre", ['s','_', '_'], 's') == False
assert valide("sucre", ['s','_', '_'], 'u') == True
assert valide("sucre", ['s','_', '_'], 'w') == False

def remplace(mot: str, secret: list[str], lettre: str) -> None:
    for i in range(len(mot)):
        if mot[i] == lettre:
            secret[i] = lettre


def affichage(secret):
    print("".join(secret))


def main(liste_mot):
    mot = choice(liste_mot)
    secret = [" _ " for l in mot]
    essais = 5
    lettre_proposee = set()
    while essais > 0 and ' _ ' in secret:
        
        print("*" * 50)
        # print(mot, secret) # Mode triche
        affichage(secret)
        lettre = input("\nQuelle lettre proposes-tu ? \n")
        print("*" * 50)
        if valide(mot, secret, lettre):
            print('Tu as trouvé une lettre')
            remplace(mot, secret, lettre)
        else:
            print('non')
            essais -= 1
            if lettre in lettre_proposee:
                print("En plus c'est un lettre que tu as déjà proposée!!!!!!")
        lettre_proposee.add(lettre)
        # print(lettre_proposee)
    if ' _ ' in secret:
        print("Perdu !!!")
    else:
        print("Gagné !!")
main(mots)
        
