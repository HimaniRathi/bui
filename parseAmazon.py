import pandas as pd
import numpy as np


def parse_amazon():
    """
    parse amazon data set subset(~200,000 reviews) where positive is 5 star reviews and negative is 1 star reviews.
    Input is amazon.json which contains all reviews(including 1-5 star reviews) and other meta data
    :return: x_train, y_train
    """
    # read the reviews from amazon.json and we get a dataframe
    data = pd.read_json("data/amazon.json", lines=True)

    # in data["overall"], the rating is given for each corresponding index in data["reviewText"]
    # 1 means negative reponse and 5 means positive response
    neg = data.loc[data["overall"] == 1]
    pos = data.loc[data["overall"] == 5][0:neg.shape[0]]

    # parse it into numpy array and store the reviewText in x_train and the rating in y_train
    x_train = np.copy(neg["reviewText"])
    x_train = np.append(x_train, np.copy(pos["reviewText"]))
    y_train = np.subtract(neg["overall"], 1)
    y_train = np.append(y_train, np.subtract(pos["overall"], 4))

    # another way of performing the above
    # x_train = []
    # y_train = []
    # i = 0
    # count1 = 0
    # count5 = 0
    # for x in data["overall"]:
    #     if x == 5 and count5 < count1:
    #         x_train.append(data["reviewText"][i])
    #         y_train.append(1)
    #         count5 += 1
    #     if x == 1:
    #         x_train.append(data["reviewText"][i])
    #         y_train.append(0)
    #         count1 += 1
    #     i += 1
    # x_train = np.copy(x_train).transpose()
    # y_train = np.copy(y_train).transpose()
    #
    # df = pd.DataFrame(y_train)
    # # print(df.describe())
    # print(np.divide(df[0].value_counts(), 1))  # 2786.77))

    # print(x_train)
    # print(y_train)
    return x_train, y_train


def parse_amazon_medium():
    """
        parse amazon data(~20,000,000 reviews) where positive is 5 star reviews and negative is 1 star reviews.
        Input is slightly preprocessed amazon data in form of amazon-1m-pos.json which is 1 million positive reviews and
        amazon-1m-neg.json which is 1m negative reviews.
        :return: x_train, y_train,
    """
    with open('data/amazon-500k-pos.json') as json_file:
        data = json_file.readlines()
        data = list(map(pd.json.loads, data))

    pos = pd.DataFrame(data)

    print("pos loaded")

    with open('data/amazon-500k-neg.json') as json_file:
        data = json_file.readlines()
        data = list(map(pd.json.loads, data))

    neg = pd.DataFrame(data)

    print("neg loaded")
    # pos = pd.read_json("data/amazon-large-pos.json", lines=True)
    # neg = pd.read_json("data/amazon-large-neg.json", lines=True)

    # parse it into numpy array and store the reviewText in x_train and the rating in y_train
    x_train = np.copy(neg["reviewText"])
    x_train = np.append(x_train, np.copy(pos["reviewText"]))
    print("over")
    y_train = np.subtract(neg["overall"], 1)
    y_train = np.append(y_train, np.subtract(pos["overall"], 4))

    return x_train, y_train


def parse_amazon_large():
    """
        parse amazon data(~20,000,000 reviews) where positive is 5 star reviews and negative is 1 star reviews.
        Input is slightly preprocessed amazon data in form of amazon-1m-pos.json which is 1 million positive reviews and
        amazon-1m-neg.json which is 1m negative reviews.
        :return: x_train, y_train,
    """
    with open('data/amazon-1m-pos.json') as json_file:
        data = json_file.readlines()
        data = list(map(pd.json.loads, data))

    pos = pd.DataFrame(data)

    print("pos loaded")

    with open('data/amazon-1m-neg.json') as json_file:
        data = json_file.readlines()
        data = list(map(pd.json.loads, data))

    neg = pd.DataFrame(data)

    print("neg loaded")
    # pos = pd.read_json("data/amazon-large-pos.json", lines=True)
    # neg = pd.read_json("data/amazon-large-neg.json", lines=True)

    # parse it into numpy array and store the reviewText in x_train and the rating in y_train
    x_train = np.copy(neg["reviewText"])
    x_train = np.append(x_train, np.copy(pos["reviewText"]))
    print("over")
    y_train = np.subtract(neg["overall"], 1)
    y_train = np.append(y_train, np.subtract(pos["overall"], 4))

    return x_train, y_train


def main():
    parse_amazon()


if __name__ == "__main__":
    main()
