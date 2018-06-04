import pandas as pd
import numpy as np


def parse_amazon():
    data = pd.read_json("data/amazon.json", lines=True)
    # print(data.describe())

    # print(data["reviewText"])
    # print(data["overall"])

    x_train = np.copy(data["reviewText"])
    y_train = np.divide(data["overall"], 5)

    # df = pd.DataFrame(y_train)
    # # print(df)
    # print(np.divide(df["overall"].value_counts(), 2786.77))
    return x_train, y_train

