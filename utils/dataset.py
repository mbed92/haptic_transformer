import os

import torch

from data import HapticDataset, QCATDataset


def load_samples_to_device(data, device):
    if len(data[0]) > 1:
        tensor_list = [s.to(device).float() for s in data[0]]
        s = torch.stack(tensor_list, -1)
    else:
        s = data[0][0].to(device).float()
        s.unsqueeze(1)
    labels = data[-1].to(device)
    return s, labels


def load_dataset(config, split_modalities):
    if config["dataset_type"].lower() == "put":
        dataset_path = os.path.join(config['dataset_folder'], config['dataset_file'])
        train_ds = HapticDataset(dataset_path, 'train_ds',
                                 signal_start=config['signal_start'],
                                 signal_length=config['signal_length'],
                                 split_modalities=split_modalities)

        val_ds = HapticDataset(dataset_path, 'val_ds',
                               signal_start=config['signal_start'],
                               signal_length=config['signal_length'],
                               split_modalities=split_modalities)

        test_ds = HapticDataset(dataset_path, 'test_ds',
                                signal_start=config['signal_start'],
                                signal_length=config['signal_length'],
                                split_modalities=split_modalities)

    elif config["dataset_type"].lower() == "qcat":
        train_ds = QCATDataset(config['dataset_folder'], 'train_ds',
                               signal_start=config['signal_start'],
                               signal_length=config['signal_length'],
                               split_modalities=split_modalities)
        val_ds = QCATDataset(config['dataset_folder'], 'val_ds',
                             signal_start=config['signal_start'],
                             signal_length=config['signal_length'],
                             split_modalities=split_modalities)
        test_ds = QCATDataset(config['dataset_folder'], 'test_ds',
                              signal_start=config['signal_start'],
                              signal_length=config['signal_length'],
                              split_modalities=split_modalities)

    else:
        raise NotImplementedError("Dataset not recognized. Allowed options are: QCAT, PUT")

    return train_ds, val_ds, test_ds
