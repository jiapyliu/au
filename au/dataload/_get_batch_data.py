import cv2
import numpy as np

def get_batch_data(image_path_list, label_list, batch_size,NB_CLASSES):
    batch_x = []
    batch_y = []
    while len(batch_x) < batch_size:
        index = np.random.randint(len(image_path_list))
        img = cv2.imread(image_path_list[index])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        label = np.zeros(NB_CLASSES)
        label[label_list[index]] = 1
        img = cv2.resize(img, (256, 256))
        batch_x.append(img)
        batch_y.append(label)
    return np.array(batch_x), np.array(batch_y)