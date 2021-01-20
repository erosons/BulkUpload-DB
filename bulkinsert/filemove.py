import csv
from glob import glob
from pathlib import Path
import pandas as pd
import os
import shutil


source = os.listdir("C:/Users/gw/Documents/")
destination = "C:/Users/gw/Documents/Archive"
for files in source:
    if files.endswith(".xlsx"):
        print(files)
        shutil.move(os.path.join(
            'C:/Users/gw/Documents/', files), destination)
