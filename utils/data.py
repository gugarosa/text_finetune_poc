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
