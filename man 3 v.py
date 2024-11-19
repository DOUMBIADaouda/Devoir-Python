import random

# Base de données des régions et leurs chefs-lieux
regions = {
    "Abidjan": "Abidjan",
    "Bas-Sassandra": "San Pedro",
    "Comoé": "Abengourou",
    "Denguélé": "Odienné",
    "N'zi": "Dimbokro",
    "Yamoussoukro": "Yamoussoukro",
    "Poro": "Korhogo",
    "Haut-Sassandra": "Daloa",
    "Nawa": "Soubré",
    "Goh": "Gagnoa"
    # Vous pouvez ajouter plus de régions ici
}

# Gestion des scores
scores = []

def afficher_meilleurs_scores():
    print("\n=== Meilleurs scores ===")
    meilleurs_scores = sorted(scores, reverse=True)[:5]
    for i, score in enumerate(meilleurs_scores, 1):
        print(f"{i}. {score} points")
    print("========================\n")

def poser_question(region, chef_lieu):
    print(f"Quel est le chef-lieu de la région {region}?")
    reponse = input("Votre réponse : ").strip()
    if reponse.lower() == chef_lieu.lower():
        print("Bonne réponse !")
        return True
    else:
        print(f"Mauvaise réponse. La bonne réponse est : {chef_lieu}.")
        return False

def jouer():
    afficher_meilleurs_scores()

    questions = random.sample(list(regions.items()), min(10, len(regions)))  # 10 questions max ou moins si peu de régions
    score = 0

    for region, chef_lieu in questions:
        if poser_question(region, chef_lieu):
            score += 1

    print(f"\nPartie terminée ! Votre score est : {score}/10\n")
    scores.append(score)

# Programme principal
while True:
    print("\n=== Jeu des Régions de la Côte d'Ivoire ===")
    print("1. Jouer une partie")
    print("2. Quitter")
    choix = input("Votre choix : ").strip()

    if choix == "1":
        jouer()
    elif choix == "2":
        print("Merci d'avoir joué !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
