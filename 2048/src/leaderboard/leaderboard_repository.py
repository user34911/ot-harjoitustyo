import csv
import os

def add_score_to_lb(username, score):
    filepath = "src/leaderboard/leaderboard.csv"
    row = [username, score]
    with open(filepath, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(row)

def get_leaderboard():
    filepath = "src/leaderboard/leaderboard.csv"
    all_scores = []
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            all_scores.append(row)
    return sorted(all_scores, key=lambda x: int(x[-1]), reverse=True)
