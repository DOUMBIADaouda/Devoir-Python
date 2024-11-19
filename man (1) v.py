def generate_calendar(num_days, start_day):
    # Liste des jours de la semaine (Lun à Dim)
    days_of_week = ["LUN", "MAR", "MER", "JEU", "VEN", "SAM", "DIM"]

    # Préparation de l'en-tête du calendrier
    header = " ".join(days_of_week)
    print(header)

    # Création d'une liste vide pour représenter le mois
    calendar = ["   "] * (start_day - 1)  # Espaces pour les jours avant le début du mois
    calendar += [f"{day:2}" for day in range(1, num_days + 1)]  # Formatage fixe à 2 caractères

    # Remplissage en lignes de 7 jours
    for i in range(0, len(calendar), 7):
        week = calendar[i:i + 7]
        print(" ".join(week).rstrip())  # Supprime les espaces à droite


# Entrée des paramètres : nombre de jours et jour de départ
num_days = int(input("Entrez le nombre de jours dans le mois : "))
start_day = int(input("Entrez le numéro du jour de début (1 pour Lundi, 7 pour Dimanche) : "))

# Génération du calendrier
generate_calendar(num_days, start_day)

