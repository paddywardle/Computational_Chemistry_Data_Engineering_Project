import torch.nn as nn
import torch.nn.functional as F
import torch

class Net(nn.Module):
    
    def __init__(self):
        super().__init__()
        self.dropout1 = nn.Dropout(p=0.2)
        self.conv1 = nn.Conv2d(1, 3, 5)
        self.batchnorm1 = nn.BatchNorm2d(3)
        self.pool = nn.MaxPool2d(2, 2)
        self.dropout2 = nn.Dropout(p=0.2)
        self.conv2 = nn.Conv2d(3, 5, 5)
        self.batchnorm2 = nn.BatchNorm2d(5)
        self.fc1 = nn.Linear(5*22*22, 100)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 1)
        
    def forward(self, x):
        x = self.dropout1(x)
        x = self.conv1(x)
        x = self.batchnorm1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.dropout2(x)
        x = self.conv2(x)
        x = self.batchnorm2(x)
        x = F.relu(x)
        x = self.pool(x)
        x = torch.flatten(x, start_dim=1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x