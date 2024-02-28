## JAMIJAM
## Developed by Clovis Schneider & Chloé Lere

import pandas as pd

def get_degrees_by_feeling(feeling):
    file_result = pd.read_csv("./data/MusicalScaleTable.csv")
    match_row = pd.DataFrame({})
    for index, row in file_result.iterrows():
        list_emotions = row["emotion"].replace(" ", "").split(',')
        for emotion in list_emotions:
            if emotion == feeling:
                match_row = pd.concat([match_row, row.to_frame().T], ignore_index=True)
    random_row = match_row.sample(n=1)
    return random_row["root"].values[0], random_row["name"].values[0], random_row["type"].values[0], match_row


def get_new_note(list_matching_degrees, name_degree, current_degree):
    if len(list_matching_degrees) == 1:
        return current_degree
    return list_matching_degrees[list_matching_degrees['name'] != name_degree].sample(n=1)["root"].values[0]