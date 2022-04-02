#!/usr/bin/env python3
"""
@Filename:    convert_excel_to_csv.py
@Author:      dulanj
@Time:        02/04/2022 11:24
"""
import os

import pandas as pd

excel_filepath = "/home/dulanj/Documents/LSR Annotations Clean.xlsx"
total_events = {
    "scrum": 0,
    "ruck": 0,
    "lineout": 0
}

output_dir = "match_csv_files"


def main():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for match_id in range(1, 60):
        try:
            df = pd.read_excel(excel_filepath, sheet_name=f"M{match_id}")
        except ValueError:
            print("No sheet named {}".format(match_id))
            continue
        output_csv = f"{output_dir}/match#{match_id}.csv"
        try:
            for event in ["scrum", "ruck", "lineout"]:
                _count = df[df["Activity"] == event].count()["Activity"]
                print(f"{event}: {_count}")
                total_events[event] += _count
        except KeyError:
            print(f"Match {match_id} has no events")
            break
        df.to_csv(output_csv, index=False)
        print("Converted match#{} to csv - {}\n".format(match_id, output_csv))

    print(f"Total events: {' '.join([f'{key} - {val}' for key, val in total_events.items()])}")


if __name__ == '__main__':
    main()
