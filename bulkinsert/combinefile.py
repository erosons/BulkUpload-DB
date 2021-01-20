import csv
from glob import glob
from pathlib import Path
import pandas as pd
import os
import shutil

path = Path('C:/Users/gw/Documents')
print(path.exists())


def concatfile(path):
    filelist = [paths for paths in path.glob("*.csv")]
    print(filelist)
    dflist = []
    columnsname = ["Draw Date", "Winning Numbers", "Bonus",
                   "Estimated Jackpot", "Jackpot Winners", "Jackpot Option"]
    for filename in filelist:
        df = pd.read_csv(filename, header=0)
        dflist.append(df)
    print(dflist)
    path2 = os.path.join('C:/Users/gw/Documents/combine2.csv')
    concatdf = pd.concat(dflist, axis=0)
    concatdf.columns = columnsname
    concatdf.to_csv(path_or_buf=path2, index=None)

    # files to archive

    source = os.listdir("C:/Users/gw/Documents/")
    destination = "C:/Users/gw/Documents/Archive"
    for files in source:
        if files.endswith(".xlsx"):
            print(files)
            shutil.move(os.path.join(
                'C:/Users/gw/Documents/', files), destination)


concatfile(path)


# Alternate 2
# merged = pd.concat(path, path)
# merged.to_csv('merged.csv', index=None, header=None)
