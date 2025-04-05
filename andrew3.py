from PIL import Image

# Open an image file
image = Image.open("C:\\Users\\maker\\Downloads\\poop\\default\\semantic\\IMG_6438.png")


x, y = 2650, 2550  # Example coordinates
pixel_value = image.getpixel((x, y))

print(f"The pixel value at ({x}, {y}) is: {pixel_value}")

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
        self.fc1 = nn.Linear(5, 3)  # Assuming input size is (input_height, input_width)

    def forward(self, x):
        # Apply Convolutional Layer
        x = self.conv1(x)
        x = F.relu(x)  # Apply ReLU activation

        # Flatten the output for the fully connected layer
        x = x.view(x.size(0), -1)  # Flatten the output

        # Apply Fully Connected Layer to 3 classes
        x = self.fc1(x)

        return x


# Example Input Size (e.g., 28x28 grayscale images)
input_height = 28
input_width = 28

# Create the model
model = SimpleCNN()

# Example input tensor with a batch size of 4 and image size 28x28 (grayscale)
input_tensor = torch.randn(4, 1, input_height, input_width)  # (batch_size, channels, height, width)

# Forward pass
output = model(input_tensor)

# Print the output size
print("Output shape:", output.shape)  # Should be (batch_size, 3) for 3 class labels
from torch.utils.data import DataLoader, Dataset
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
# class DummyDataset(Dataset):
#     def __init__(self, num_samples=100, image_size=(3, 64, 64), num_classes=3):
#         self.num_samples = num_samples
#         self.image_size = image_size
#         self.num_classes = num_classes
#
#     def __len__(self):
#         return self.num_samples
#
#     def __getitem__(self, idx):
#         # Create random images and random labels
#         image = torch.randn(*self.image_size)  # Random image
#         label = torch.randint(0, self.num_classes, (self.image_size[1], self.image_size[2]))  # Random labels
#         return image, label

# Hyperparameters
num_epochs = 10
batch_size = 8
learning_rate = 0.001

# Create dataset and dataloaders
train_dataset = DummyDataset(num_samples=100, image_size=(3, 64, 64), num_classes=3)
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

    for i, (images, labels) in enumerate(image_generator(images)):
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Compute the loss (CrossEntropyLoss expects shape (N, C, H, W) for input and (N, H, W) for target)
        loss = criterion(outputs, labels)
        running_loss += loss.item()

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        # Calculate accuracy (pixel-wise accuracy)
        _, predicted = torch.max(outputs, 1)  # Get the class with the highest probability for each pixel
        correct += (predicted == labels).sum().item()  # Count correct predictions
        total += labels.numel()  # Total number of pixels

    # Print loss and accuracy for each epoch
    epoch_loss = running_loss / len(train_loader)
    epoch_accuracy = 100 * correct / total
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss:.4f}, Accuracy: {epoch_accuracy:.2f}%")

# Save the model after training
torch.save(model.state_dict(), 'trained_model.pth')
