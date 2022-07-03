from Net import Net
import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path
import os

class ModelTrainEval:

    def __init__(self):

        self.net = Net()
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.net.parameters(), lr=0.001)

    def train_net(self, num_epochs, train_loader):

        self.net.train()
        
        losses_over_time = []
        
        for epoch in range(num_epochs):

            running_loss = 0.0

            for batch_i, data in enumerate(train_loader, 0):
                
                # getting inputs and labels from train_loader
                inputs, labels = data

                # zeroing gradient
                self.optimizer.zero_grad()

                outputs = self.net(inputs.float())

                loss = self.criterion(outputs, labels.float())

                # calculating gradients for the iteration
                loss.backward()

                # taking a step based on calculated gradients
                self.optimizer.step()

                running_loss += loss.item()

                # printing the loss every 2000 mini batches
                if batch_i % 2000 == 1999:
                    print(f'[{epoch + 1}, {batch_i + 1:5d}] training loss: {running_loss/2000:.3f}')
                    losses_over_time.append(running_loss)
                    running_loss = 0.0
        
        return losses_over_time
                    
        print('Finished Training')

    def eval(self, test_loader):
        
        self.net.eval()
        
        test_loss_total = 0
        
        for data in test_loader:
            
            test_image, test_label = data
        
            y_pred = self.net(test_image.float())

            test_loss = self.criterion(y_pred, test_label.float())
            
            test_loss_total += test_loss.item()

        print('Average test loss is {}'.format(test_loss_total/(len(test_loader) * test_loader.batch_size)))
        
        return test_loss_total/(len(test_loader) * test_loader.batch_size)

    def save_model(self, model_name):

        model_path = Path(os.getcwd()) / "Models" / f"{model_name}.pth".format(model_name)

        torch.save(self.net.state_dict(), model_path)
