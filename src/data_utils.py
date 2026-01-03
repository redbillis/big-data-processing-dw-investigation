import os
import pandas as pd

def load_csv(DATA_DIR, filename, encoding="latin1"):
    return pd.read_csv(os.path.join(DATA_DIR, filename), encoding=encoding)



def data_dir():
    # Try both possible data directory paths
    possible_dirs = ["../data/raw", "data/raw"]
    DATA_DIR = None

    # Find the first existing data directory
    for d in possible_dirs:
        # Check if the directory exists
        if os.path.isdir(d):
            DATA_DIR = d
            break

    # Raise an error if no data directory is found
    if DATA_DIR is None:
        raise FileNotFoundError("Could not find the data/raw directory. Checked: {}".format(possible_dirs))

    # Confirm the resolved data directory
    return DATA_DIR