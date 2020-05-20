import os
import random
import numpy as np

try:
    import tensorflow as tf
except:
    pass


def seed_everything(seed: int = 0):
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    try:
        tf.random.set_seed(seed)
    except:
        pass
    print(f'call seed_everything(),the seed is : {seed}')
seed_everything()
