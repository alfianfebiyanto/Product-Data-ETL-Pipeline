# Import Library
import pandas as pd
from config.setting import REQ_PATH, PRODUCTS_PATH, OUTPUT_PATH
from src.transform import transform_data_products,transform_data_req
from src.utils import extract_csv,extract_multi_csv,load_csv

# Extract
df_req = extract_csv(REQ_PATH)
df_product = extract_multi_csv(PRODUCTS_PATH)

# Transform
df_req_final = transform_data_req(df_req)
df_product_final = transform_data_products(df_product)

# Load
load_csv(df_req_final,OUTPUT_PATH,"requirement_final.csv")
load_csv(df_product_final,OUTPUT_PATH,"product_final.csv")

