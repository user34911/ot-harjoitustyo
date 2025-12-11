import csv
import os
from datetime import datetime
from enums import Leaderboard

def add_to_leaderboard(fields, leaderboard: Leaderboard):
    filepath = _get_filepath(leaderboard)
    with open(filepath, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(fields)

def get_leaderboard(leaderboard: Leaderboard):
    filepath = _get_filepath(leaderboard)
    entries = []
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            entries.append(row)
    return _sort_entries(entries, leaderboard)

def _get_filepath(leaderboard: Leaderboard):
    if leaderboard is Leaderboard.STANDARD:
        return "src/leaderboard/standard_leaderboard.csv"
    if leaderboard is Leaderboard.TIMED:
        return "src/leaderboard/timed_leaderboard.csv"

def _sort_entries(entries, leaderboard: Leaderboard):
    if leaderboard is Leaderboard.STANDARD:
        return sorted(entries, key=lambda x: int(x[-1]), reverse=True)
    if leaderboard is Leaderboard.TIMED:
        return sorted(entries, key=lambda entry: datetime.strptime(entry[-1], "%M:%S"))
