import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset


class OilPriceDataset(Dataset):
    def __init__(self, data, min_data=None, max_data=None, step=365):
        data = data if isinstance(data, np.ndarray) else data.values
        self.min_data = np.min(data) if min_data is None else min_data
        self.max_data = np.max(data) if max_data is None else max_data
        self.data = (data - self.min_data) / (self.max_data - self.min_data)
        self.data = torch.FloatTensor(self.data)
        self.step = step

    def __len__(self):
        return len(self.data) - self.step

    def __getitem__(self, i):
        data = self.data[i : i + self.step]
        label = self.data[i + self.step].squeeze()
        return data, label


class OilPriceModel(nn.Module):
    def __init__(self, hidden_size, num_layers, step):
        super().__init__()
        self.rnn = nn.GRU(
            input_size=1,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )
        self.fc1 = nn.Linear(in_features=hidden_size * step, out_features=64)
        self.fc2 = nn.Linear(in_features=64, out_features=1)

    def forward(self, x):
        x, _ = self.rnn(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        return torch.flatten(x)
