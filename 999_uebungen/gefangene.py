import random

# Funktion, um die Simulation für einen Gefangenen durchzuführen
def search_drawers(drawers, prisoner_number):
    attempts = 0
    next_drawer = prisoner_number
    while attempts < 50:
        if drawers[next_drawer] == prisoner_number:
            return True
        next_drawer = drawers[next_drawer]
        attempts += 1
    return False

# Funktion, um das Experiment für alle Gefangenen durchzuführen
def run_simulation():
    # Liste der Gefangenen-Nummern und Schubladen-Nummern (1 bis 100)
    prisoner_numbers = list(range(100))
    
    # Plättchen zufällig in die Schubladen verteilen
    drawers = prisoner_numbers[:]
    random.shuffle(drawers)
    
    # Überprüfen, ob alle Gefangenen ihre Nummer finden
    for prisoner in prisoner_numbers:
        if not search_drawers(drawers, prisoner):
            return False  # Wenn ein Gefangener seine Nummer nicht findet, scheitert der Versuch
    return True  # Alle Gefangenen haben ihre Nummer gefunden

# Simulation 10.000 Mal durchführen
def simulate_prisoner_game(trials=10000):
    successful_trials = 0
    for _ in range(trials):
        if run_simulation():
            successful_trials += 1
    return successful_trials

# Hauptprogramm
if __name__ == "__main__":
    trials = 10000
    success_count = simulate_prisoner_game(trials)
    print(f"Die Gefangenen wurden in {success_count} von {trials} Versuchen alle befreit.")
