from torch.utils.data import DataLoader
from torchvision import transforms

def train_test_transform():
    """
    直接得到train_transform, test_trainsform
    :return: train_transform, test_trainsform
    """
    train_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.RandomResizedCrop(256, scale=(0.6, 1.0), ratio=(0.8, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    test_trainsform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(256),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return train_transform, test_trainsform