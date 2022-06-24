import numpy as np
from  torch.utils.data import Dataset
import os
import torch
from skimage import io
from PIL import Image

class EventDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, data_info, root_dir, transform=None):
        """
        Args:
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied
                on a sample.
        """
        self.data_info = data_info
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        _, _, files = next(os.walk(self.root_dir))
        return len(files)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # for reading images
        image_name = None
        with open(self.data_info) as f:
            content = f.readlines()
            image_name = content[idx].split()[0]

        img_path = os.path.join(self.root_dir, image_name)
        image = Image.open(img_path)

        if self.transform:
            image = self.transform(image)

        return image, 0

        # for reading events
        # data_name = None
        # with open(self.data_info) as f:
        #     content = f.readlines()
        #     data_name = content[idx].split()[0]

        # data = np.load(os.path.join(self.root_dir, data_name))
        # return data