import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(five_data_file,four_data_file,three_data_file,two_data_file,one_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    five_examples = list(open(five_data_file, "r").readlines())
    five_examples = [s.strip() for s in five_examples]
    four_examples = list(open(four_data_file, "r").readlines())
    four_examples = [s.strip() for s in four_examples]
    three_examples = list(open(three_data_file, "r").readlines())
    three_examples = [s.strip() for s in three_examples]
    two_examples = list(open(two_data_file, "r").readlines())
    two_examples = [s.strip() for s in two_examples]
    one_examples = list(open(one_data_file, "r").readlines())
    one_examples = [s.strip() for s in one_examples]
    #positive_examples = list(open(positive_data_file, "r").readlines())
    #positive_examples = [s.strip() for s in positive_examples]
    #negative_examples = list(open(negative_data_file, "r").readlines())
    #negative_examples = [s.strip() for s in negative_examples]
    #neutral_examples = list(open(neutral_data_file, "r").readlines())
    #neutral_examples = [s.strip() for s in neutral_examples]
    # Split by words
    x_text = five_examples + four_examples + three_examples + two_examples + one_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    five_labels = [[0, 1] for _ in five_examples]
    four_labels = [[1, 0] for _ in four_examples]
    three_labels = [[2, 0] for _ in three_examples]
    two_labels = [[3, 0] for _ in two_examples]
    one_labels = [[4, 0] for _ in one_examples]
    y = np.concatenate([five_labels, four_labels,three_labels,two_labels,one_labels], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
