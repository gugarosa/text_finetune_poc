from sklearn.model_selection import train_test_split
from textfier.core import Dataset, Runner
from textfier.tasks import SequenceClassificationTask

import utils.data as d

# Loads training and testing samples
X, Y = d.load_csv('data/output.csv', delimiter='\\')

# Creates labeled sentences from pre-loaded samples
X_tok, Y_tok = d.create_labeled_sentences(X, Y)

# Splitting data into training and testing labels
X_train_tok, X_test_tok, Y_train_tok, Y_test_tok = train_test_split(X_tok, Y_tok, test_size=0.5, random_state=0)

# Creates the sequence classification task with pre-trained model
task = SequenceClassificationTask(model='neuralmind/bert-large-portuguese-cased', num_labels=5)

# Encodes the training and testing samples
X_enc_train = task.tokenizer(X_train_tok, return_tensors='pt', padding=True, truncation=True, max_length=512)
X_enc_test = task.tokenizer(X_test_tok, return_tensors='pt', padding=True, truncation=True, max_length=512)

# Creates the datasets
train_dataset = Dataset(input_ids=X_enc_train['input_ids'],
                        attention_mask=X_enc_train['attention_mask'], labels=Y_train_tok)
test_dataset = Dataset(input_ids=X_enc_test['input_ids'],
                       attention_mask=X_enc_test['attention_mask'], labels=Y_test_tok)

# Creates the runner with the pre-trained model and training dataset
runner = Runner(task.model, train_dataset, num_train_epochs=1)

# Fine-tunes the runner
runner.train()

# Makes a prediction over a evaluation dataset
preds = runner.predict(test_dataset)

print(preds)
