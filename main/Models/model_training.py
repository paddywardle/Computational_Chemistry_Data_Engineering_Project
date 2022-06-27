import sys
import os
from getpass import getpass
sys.path.append(os.path.dirname(os.getcwd())+"\\MySQL Database")
from CreateDB import CreateDB

import torch
import torchvision

from io import BytesIO
from PIL import Image

import numpy as np
from sklearn.model_selection import train_test_split

if __name__ == "__main__":

    user = input("Enter username: ")
    password = getpass("Enter password: ")
    db_name = input("Enter database name: ")

    # query for image data
    img_query = "SELECT image FROM images"

    # query for labels
    labels_query = "SELECT HBondDonorCount FROM properties"

    # database object
    db = CreateDB(user, password)

    images = db.fetch_query(db_name, img_query)

    labels = db.fetch_query(db_name, labels_query)

    img_list = []

    # iterate though query results and add pixel values to img_list
    for i in range(len(images)):
        
        img_single = list(Image.open(BytesIO(images[i][0])).getdata())
        
        img_list.append(img_single)
        
    # array of images and reshape for conv net
    img_array = np.array(img_list).reshape(-1, 100, 100)

    # creating pytorch tensor of image data
    img_tensor = torch.from_numpy(img_array)

    # creating numpy array of labels
    labels_array = np.array([x[0] for x in labels])

    # create pytorch tensor of labels
    labels_tensor = torch.from_numpy(labels_array)

    # split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(img_tensor, labels_tensor, train_size=0.8, random_state=0)

    train_dataset = torch.utils.data.TensorDataset(X_train, y_train)

    test_dataset = torch.utils.data.TensorDataset(X_test, y_test)