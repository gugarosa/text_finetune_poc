import textfier.utils.loader as l
from textfier.core import Dataset, Runner
from textfier.tasks import SequenceClassificationTask

import utils.data as d

# Loads training and testing samples
X_train, Y_train = l.load_csv('data/train.csv')
X_test, Y_test = l.load_csv('data/test.csv')

# Creates labeled sentences from pre-loaded samples
X_train_tok, Y_train_tok = d.create_labeled_sentences(X_train, Y_train)
X_test_tok, Y_test_tok = d.create_labeled_sentences(X_test, Y_test)

# Creates the sequence classification task with pre-trained model
task = SequenceClassificationTask(model='neuralmind/bert-base-portuguese-cased', num_labels=2)

# Encodes the training and testing samples
X_enc_train = task.tokenizer(X_train_tok, return_tensors='pt', padding=True, truncation=True)
X_enc_test = task.tokenizer(X_test_tok, return_tensors='pt', padding=True, truncation=True)

# Creates the datasets
train_dataset = Dataset(input_ids=X_enc_train['input_ids'],
                        attention_mask=X_enc_train['attention_mask'], labels=Y_train_tok)
test_dataset = Dataset(input_ids=X_enc_test['input_ids'],
                       attention_mask=X_enc_test['attention_mask'], labels=Y_test_tok)

# Creates the runner with the pre-trained model and training dataset
runner = Runner(task.model, train_dataset, num_train_epochs=3)

# Fine-tunes the runner
runner.train()

# Makes a prediction over a evaluation dataset
preds = runner.predict(test_dataset)

print(preds)
