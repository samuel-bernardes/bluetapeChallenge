import glob
import pandas as pd
from selenium import webdriver

for file in glob.glob('./*.xlsx'):
    if '~$' in file:
        continue
    else:
        df = pd.read_excel(
            file,
            engine='openpyxl'
        )

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=3")