#! /usr/bin/env python

import _pickle as cPickle, gzip
import numpy as np
from tqdm import tqdm
import torch
import torch.autograd as autograd
import torch.nn.functional as F
import torch.nn as nn
import sys
sys.path.append("..")
#sys.path.append("/Users/eeshans/dev/datascience/mit_stats/mnist")
#print(sys.path)
import utils
from utils import *
from train_utils import batchify_data, run_epoch, train_model

def main():
    # Load the dataset
    num_classes = 10
    X_train, y_train, X_test, y_test = get_MNIST_data()

    # Split into train and dev
    dev_split_index = int(9 * len(X_train) / 10)
    X_dev = X_train[dev_split_index:]
    y_dev = y_train[dev_split_index:]
    X_train = X_train[:dev_split_index]
    y_train = y_train[:dev_split_index]

    permutation = np.array([i for i in range(len(X_train))])
    np.random.shuffle(permutation)
    X_train = [X_train[i] for i in permutation]
    y_train = [y_train[i] for i in permutation]

    # Split dataset into batches
    batch_size = 32
    train_batches = batchify_data(X_train, y_train, batch_size)
    dev_batches = batchify_data(X_dev, y_dev, batch_size)
    test_batches = batchify_data(X_test, y_test, batch_size)

    #################################
    ## Model specification TODO
    model = nn.Sequential(
              nn.Linear(784, 128),
              nn.ReLU(),
              nn.Linear(128, 10),
            )
    lr=0.1
    momentum=0
    ##################################

    train_model(train_batches, dev_batches, model, lr=lr, momentum=momentum)

    ## Evaluate the model on test data
    loss, accuracy = run_epoch(test_batches, model.eval(), None)
    print ("Loss on test set:"  + str(loss) + " Accuracy on test set: " + str(accuracy))

    ## Evaluate the model on validation data
    val_loss, val_accuracy = run_epoch(dev_batches, model.eval(), None)
    print ("Loss on val set:"  + str(val_loss) + " Accuracy on val set: " + str(val_accuracy))
    


if __name__ == '__main__':
    # Specify seed for deterministic behavior, then shuffle. Do not change seed for official submissions to edx
    np.random.seed(12321)  # for reproducibility
    torch.manual_seed(12321)  # for reproducibility
    main()

### Results
## Baseline: 
    # Loss on test set:0.26722687603129697 Accuracy on test set: 0.9204727564102564
    # Loss on val set:0.2283876604963353 Accuracy on val set: 0.9324866310160428

## batch size 64: 
    # Loss on test set:0.24579500876522312 Accuracy on test set: 0.9298878205128205
    # Loss on val set:0.21121166152779453 Accuracy on val set: 0.9398521505376344

## learning rate 0.01: 
    # Loss on test set:0.27886551584248453 Accuracy on test set: 0.9206730769230769
    # Loss on val set:0.23326757895874786 Accuracy on val set: 0.9344919786096256

## momentum 0.9: 
    # Loss on test set:0.5153845530122709 Accuracy on test set: 0.8869190705128205
    # Loss on val set:0.46924964677203784 Accuracy on val set: 0.8942179144385026

## Leakly ReLU: 
    # Loss on test set:0.26892609388466016 Accuracy on test set: 0.9207732371794872
    # Loss on val set:0.22761470489303537 Accuracy on val set: 0.9319852941176471


## Hidden 128 Results:
## Baseline: 
# Loss on val set:0.07199907880505226 Accuracy on val set: 0.9779411764705882

## batch size 64: 
# Loss on val set:0.07938297807929977 Accuracy on val set: 0.9766465053763441

## learning rate 0.01: 
# Loss on val set:0.16906875872954646 Accuracy on val set: 0.9550467914438503

## momentum 0.9: 
# Loss on val set:0.22582119571974557 Accuracy on val set: 0.9644050802139037

## Leakly ReLU: 
# Loss on val set:0.07138669198686456 Accuracy on val set: 0.9791109625668449