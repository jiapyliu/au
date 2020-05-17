import pandas as pd
from pathlib import Path
from typing import Union,Any

def is_pathlike(x:Any):
    return isinstance(x,(str, Path))

def load_csv(path: Union[Path,str]

             ):
    pd.read_csv()

