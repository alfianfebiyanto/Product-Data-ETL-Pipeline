import pandas as pd
from src.utils import extract_csv,extract_multi_csv,load_csv
from config.setting import REQ_PATH, PRODUCTS_PATH, OUTPUT_PATH

# Extract
df_req = extract_csv(REQ_PATH)
df_product = extract_multi_csv(PRODUCTS_PATH)




