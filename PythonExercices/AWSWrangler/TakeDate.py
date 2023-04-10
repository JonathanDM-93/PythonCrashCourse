import json
from pathlib import Path
import boto3
import pandas as pd
import numpy as np

from datetime import datetime, timedelta
date = (datetime.today() - timedelta(days=1)).strftime("%Y/%m/%d")
print(date)

