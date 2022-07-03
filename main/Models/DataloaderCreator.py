from cgi import test
import numpy as np
from io import BytesIO
from PIL import Image
import torch
import torchvision
from sklearn.model_selection import train_test_split

class DataloaderCreator:

    def __init__(self, image_data, labels):

        self.image_data = image_data

        self.labels = labels

    def create_pixel_tensor(self):

        img_array = np.array([list(Image.open(BytesIO(img[0])).getdata()) for img in self.image_data]).reshape(-1, 1, 100, 100)

        img_tensor = torch.from_numpy(img_array)

        return img_tensor

    def create_labels_tensor(self):

        labels_array = np.array([x[0] for x in self.labels]).reshape(-1, 1)

        # create pytorch tensor of labels
        labels_tensor = torch.from_numpy(labels_array)

        return labels_tensor

    def dataloader_creator(self, batch_size, train_size=0.8):

        img_tensor = self.create_pixel_tensor()

        labels_tensor = self.create_labels_tensor()

        X_train, X_test, y_train, y_test = train_test_split(img_tensor, labels_tensor, train_size=train_size, random_state=0)

        train_dataset = torch.utils.data.TensorDataset(X_train, y_train)

        test_dataset = torch.utils.data.TensorDataset(X_test, y_test)

        train_loader = torch.utils.data.DataLoader(train_dataset, 
                                                   batch_size=batch_size, 
                                                   shuffle=True, 
                                                   num_workers=2)

        test_loader = torch.utils.data.DataLoader(test_dataset,
                                                  batch_size=batch_size,
                                                  shuffle=False,
                                                  num_workers=2)

        return train_loader, test_loader