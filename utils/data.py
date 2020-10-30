import pandas as pd

import textfier.stream.tokenizer as t


def create_labeled_sentences(X, Y, language='portuguese'):
    """Creates labeled sentences from pre-loaded text.

    Args:
        X (list): List of non-tokenized samples.
        Y (list): List of labels.
        language (str): Tokenizer language.

    Returns:
        Lists of sentence-level samples and labels.

    """

    # Creates empty lists to hold tokenized X and Y
    X_tok, Y_tok = [], []

    # Iterates over every sample
    for (x, y) in zip(X, Y):
        # Tokenizes the sample into sentences
        x_tok = t.tokenize_to_sentences(x, language=language)

        # Gathers its labels and concatenates to final list
        Y_tok += [y] * len(x_tok)

        # Concatenates the tokenized sentences to final list
        X_tok += x_tok

    return X_tok, Y_tok


def load_csv(file_name, delimiter=','):
    """Loads a .csv file using Pandas.

    Args:
        file_name (str): The file name to be loaded.

    Returns:
        Lists of samples and their labels.

    """

    print('Loading labels and samples from: %s ...', file_name)

    # Tries to load the file
    try:
        # Loads a .csv file using Pandas
        csv = pd.read_csv(file_name, delimiter=delimiter)

        # Gathers the labels
        labels = csv['label'].tolist()

        # Gathers the samples
        samples = csv['sample'].tolist()

        print('Labels and samples loaded.')

        return samples, labels

    # If file can not be loaded
    except FileNotFoundError:
        raise