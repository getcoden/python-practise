

import os
import sys
import pandas
from datetime import datetime


for root, dirs, files in os.walk(r"D:\1 - 副本", topdown=False):
    for file in files:
        print(os.path.join(root, file))
