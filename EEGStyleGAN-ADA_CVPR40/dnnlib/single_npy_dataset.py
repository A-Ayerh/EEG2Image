# single_npy_dataset.py
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
import torch

class SingleNpyFileDataset(Dataset):
    def __init__(self, npy_path):
        self.data = np.load(npy_path)
        self.transform = transforms.Compose([
            transforms.ToTensor(),
            # Add any other transformations here
        ])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image = self.data[idx]
        image = self.transform(image)
        return image
