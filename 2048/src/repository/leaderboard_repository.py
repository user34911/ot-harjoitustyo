import csv
import os
from datetime import datetime
from enums import Mode

def add_to_leaderboard(fields, mode: Mode):
    filepath = _get_filepath(mode)
    with open(filepath, "a", newline="", encoding="utf-8") as file:
        csv.writer(file).writerow(fields)

def get_leaderboard(mode: Mode):
    filepath = _get_filepath(mode)
    entries = []
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            entries.append(row)
    return _sort_entries(entries, mode)

def _get_filepath(mode: Mode):
    if mode is Mode.STANDARD:
        return "src/leaderboard/standard_leaderboard.csv"
    if mode is Mode.TIMED:
        return "src/leaderboard/timed_leaderboard.csv"
    return None

def _sort_entries(entries, mode: Mode):
    if mode is Mode.STANDARD:
        return sorted(entries, key=lambda x: int(x[-1]), reverse=True)
    if mode is Mode.TIMED:
        return sorted(entries, key=lambda entry: datetime.strptime(entry[-1], "%M:%S"))
    return None
