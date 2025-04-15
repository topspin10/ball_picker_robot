from PIL import Image
import os
import numpy as np
from torch.utils.data import DataLoader, Dataset
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

# Define the CNN architecture


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()

        # Convolutional Layer: 5 filters of size 7x7
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=5, kernel_size=7, stride=1, padding=3)

        # Fully Connected Layer to 3 output classes
        # After applying the convolution, we need to compute the flattened size
        # defines a fully connected layer
        self.fc1 = nn.Linear(5 * 300 * 200, 3)  # Assuming input size is (input_height, input_width)

    def forward(self, x):
        # Apply Convolutional Layer
        x = self.conv1(x)
        x = F.relu(x)  # Apply ReLU activation

        # Flatten the output for the fully connected layer
        x = x.view(x.size(0), -1)  # Flatten the output

        # Apply Fully Connected Layer to 3 classes
        x = self.fc1(x)
        x = F.softmax(x, dim=1)

        return x


# def image_generator(files, batch_size=32, sz=(256, 256)):
#     while True:
#
#         # extract a random batch
#         batch = np.random.choice(files, size=batch_size)
#
#         # variables for collecting batches of inputs and outputs
#         batch_x = []
#         batch_y = []
#
#         for f in batch:
#
#             # get the masks. Note that masks are png files
#             mask = Image.open(f'data/Masks/{f[:-4]}.png')
#             mask = np.array(mask.resize(sz))
#
#             # preprocess the mask
#             # mask[mask >= 2] = 0
#             # mask[mask != 0] = 1
#
#             batch_y.append(mask)
#
#             # preprocess the raw images
#             raw = Image.open(f'data/Images/{f}')
#             raw = raw.resize(sz)
#             raw = np.array(raw)
#
#             # check the number of channels because some of the images are RGBA or GRAY
#             if len(raw.shape) == 2:
#                 raw = np.stack((raw,) * 3, axis=-1)
#
#             else:
#                 raw = raw[:, :, 0:3]
#
#             batch_x.append(raw)
#
#         # preprocess a batch of images and masks
#         # creates n
#         batch_x = np.array(batch_x) / 255.
#         batch_y = np.array(batch_y)
#         batch_y = np.expand_dims(batch_y, 3)
#
#         yield batch_x, batch_y
#

# Example Input Size (e.g., 28x28 grayscale images)
# input_height = 28
# input_width = 28

# Create the model
model = SimpleCNN()

# Print the output size
#
# # Simple CNN Model for pixel-wise classification
# class SimpleCNNModel(nn.Module):
#     def __init__(self, num_classes=3):
#         super(SimpleCNNModel, self).__init__()
#         self.conv1 = nn.Conv2d(in_channels=3, out_channels=5, kernel_size=7, padding=3)
#         self.fc1 = nn.Linear(5 * 64 * 64, num_classes)  # Assuming 64x64 input image size
#
#     def forward(self, x):
#         x = self.conv1(x)
#         batch_size, channels, height, width = x.size()
#         x = x.view(batch_size, -1)  # Flatten the spatial dimensions
#         x = self.fc1(x)
#         x = x.view(batch_size, 3, height, width)  # Reshape back to (batch_size, num_classes, height, width)
#         return x
#
# # Dummy dataset for the purpose of this example (replace with your dataset)


# class returns images and masks
class DummyDataset(Dataset):
    # every time an instance of DummyDataset is created, it runs __init__
    def __init__(self, folder='data//Images'):
        # TODO remember to store folder in self DONE
        # TODO jpg_files = [file for file in self.files if file.lower().endswith('.jpg')]
        self.files = os.listdir(folder)
        self.folder = folder
        print(self.folder)

    # called
    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        # # Create random images and random labels
        # image = torch.randn(*self.image_size)  # Random image
        # label = torch.randint(0, self.num_classes, (self.image_size[1], self.image_size[2]))  # Random labels
        if idx > (len(self.files)-1):
            raise IndexError("index is too long")
        # TODO join folder to name DONE
        image = Image.open(os.path.join(self.folder, self.files[idx]))
        # TODO remove /Images replace with /Masks
        # TODO add resize for both DONE
        # TODO given the folder and the self.files[idx] think what happens if folder is completely different
        # what assumptions are you making for self.folder[:-6] to make sense
        label = Image.open(os.path.join(f'{self.folder[:-6]}Masks//', f'{self.files[idx][:-4]}.png'))
        new_width = 300
        new_height = 200
        new_size = (new_width, new_height)
        # Resize the image
        image = image.resize(new_size)
        label = label.resize(new_size)
        image = np.array(image) / 255.
        label = np.array(label) / 255.
        image = torch.from_numpy(image).float().permute(2, 0, 1)  # Convert to Tensor (C, H, W)
        label = torch.from_numpy(label).long()  # Convert to Tensor (H, W), crucial for CrossEntropyLoss
        return image, label


# Hyperparameters
num_epochs = 10
batch_size = 8
learning_rate = 0.001

# Create dataset and dataloaders
train_dataset = DummyDataset()
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

# Initialize model, loss function, and optimizer
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()  # CrossEntropyLoss is used for multi-class classification
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    model.train()  # Set the model to training mode
    running_loss = 0.0
    correct = 0
    total = 0

# TODO not needed anymore
    image_folder = 'data//Images'
    mask_folder = 'data//Masks'
    image_files = os.listdir('data//Images')
    mask_files = os.listdir('data//Masks')
    # List all image files in the images folder
    images_list = [f for f in image_files if os.path.isfile(os.path.join(image_folder, f))]

    # Create a list of corresponding mask filenames based on image filenames
    masks_list = [f for f in mask_files if os.path.isfile(os.path.join(mask_folder, f))]

# TODO make sure enumerate works on train_loader
for i, (images_list, masks_list) in enumerate(train_loader):
    # Zero the gradients
    optimizer.zero_grad()

    # Forward pass
    outputs = model(images_list)

    # Compute the loss (CrossEntropyLoss expects shape (N, C, H, W) for input and (N, H, W) for target)
    loss = criterion(outputs, masks_list)
    running_loss += loss.item()

    # Backward pass and optimization
    loss.backward()
    optimizer.step()

    # Calculate accuracy (pixel-wise accuracy)
    _, predicted = torch.max(outputs, 1)  # Get the class with the highest probability for each pixel
    correct += (predicted == masks_list).sum().item()  # Count correct predictions
    total += masks_list.numel()  # Total number of pixels

    # Print loss and accuracy for each epoch
    epoch_loss = running_loss / len(train_loader)
    epoch_accuracy = 100 * correct / total
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}, Accuracy: {epoch_accuracy:.2f}%")

# Save the model after training
torch.save(model.state_dict(), 'trained_model.pth')
