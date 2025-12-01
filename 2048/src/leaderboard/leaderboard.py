import csv
import os

def init_leaderboard():
    filepath = "src/leaderboard/leaderboard.csv"
    fields = ["Player", "Score"]
    with open(filepath, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(fields)

def add_score_to_lb(username, score):
    filepath = "src/leaderboard/leaderboard.csv"
    if not os.path.exists(filepath):
        init_leaderboard()

    row = [username, score]
    with open(filepath, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(row)
