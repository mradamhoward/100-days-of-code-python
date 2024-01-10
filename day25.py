import pandas as p

import numpy as np

squirrels = p.read_csv("squirrels.csv")

num_colors = squirrels["Primary Fur Color"].value_counts()

print(squirrels["Primary Fur Color"].value_counts())

num_colors.to_csv("num_colors.csv")