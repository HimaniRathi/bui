import numpy as np

from parseAmazon import parse_amazon
from models import getEmbedding
from parseKaggle import parse_kaggle
from splitter import splitData

x,y = parse_amazon()
word_index, data, embedding_matrix = getEmbedding((x,y))
# x,y = parse_kaggle()
# # print(x)
# word_index2, data2, embedding_matrix2 = getEmbedding((x,y))
x_train, y_train, x_val, y_val = splitData(data, split_value=0.3)
# x_train, y_train, x_val, y_val = data[0], data[1], data2[0], data2[1]
print(x_train)
print(y_train)
print(x_val)
print(y_val)
np.save('data/x_train', x_train)
np.save('data/y_train', y_train)
np.save('data/x_val', x_val)
np.save('data/y_val', y_val)
