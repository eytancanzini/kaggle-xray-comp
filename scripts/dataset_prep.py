'''
File for creating the PyTorch dataset from the initial dataset of PNG images and labels
'''

import os
import numpy as np
import pandas as pd
import cv2

TRAIN_DATASETS = '../data/images/train'

TARGETS = {
    0: "abdomen",
    1: "ankle",
    2: "cervical spine",
    3: "chest",
    4: "clavicles",
    5: "elbow",
    6: "feet",
    7: "finger",
    8: "forearm",
    9: "hand",
    10: "hip",
    11: "knee",
    12: "lower leg",
    13: "lumbar spine",
    14: "others",
    15: "pelvis",
    16: "shoulder",
    17: "sinus",
    18: "skull",
    19: "thigh",
    20: "thoracic spine",
    21: "wrist"
}

COLUMN_NAMES = [
    'SOPInstanceUID',
    'class_id',
    'class_name'
]

def append_dataframe(dict, img_df):
    '''
    Appends the dataframe with the new entry
    '''
    dict = pd.DataFrame(temp, index=[0])
    return pd.concat([img_df, dict], ignore_index=True, axis=0)

if __name__ == "__main__":
    df = pd.read_csv('../datasets/train_df.csv')
    
    img_df = pd.DataFrame(columns=COLUMN_NAMES)
    
    for filename in os.listdir(TRAIN_DATASETS):
        f = os.path.join(TRAIN_DATASETS, filename)
        if os.path.isfile(f):
            img_name = filename[:len(filename)-6]
            x = df.loc[df['SOPInstanceUID'] == img_name]
            try:
                id = int(x.iloc[0]['Target'])
                name_id = TARGETS[id]
                temp = {
                    'SOPInstanceUID': img_name,
                    'class_id': id, 
                    'class_name': name_id
                }
                img_df = append_dataframe(temp, img_df)
            except Exception as e:
                print(e)
    
    print(img_df.head())
            