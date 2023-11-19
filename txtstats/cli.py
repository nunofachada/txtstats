import sys
from .stats_functions import text_stats

def main():
    s = sys.argv[1]
    s_stats = text_stats(s)
    for stat_name in s_stats:
        print(f"\t{stat_name} : {s_stats[stat_name]}")