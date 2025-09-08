# Import Library
import pandas as pd
from config.setting import REQ_PATH, PRODUCTS_PATH, OUTPUT_PATH
from src.transform import transform_data_products,transform_data_req
from src.utils import extract_csv,extract_multi_csv,load_csv

# #extract
# df_req = extract_csv(REQ_PATH)
# df_product = extract_multi_csv(PRODUCTS_PATH)

# # Transform
# df_req_final = transform_data_req(df_req)
# df_product_final = transform_data_products(df_product)

# # load
# load_csv(df_req_final,OUTPUT_PATH,"requirement_final.csv")
# load_csv(df_product_final,OUTPUT_PATH,"product_final.csv")

# 07-09-2025 jam 22.08 masih pr di Alert kalo yang lain di note book tinggal copas aja bro
from src.alert import send_discord

def run_etl():
    data = [1, 2, 3]
    result = [x * 2 for x in data]
    return result

if __name__ == "__main__":
    try:
        print("🚀 Mulai ETL...")
        hasil = run_etl()
        print("✅ ETL sukses:", hasil)

        send_discord(f"✅ ETL Success! Hasil: {hasil}")
    except Exception as e:
        print("❌ ETL gagal BRO BANGUNNN:", e)

        send_discord(f"❌ ETL Failed! Error: {e}")
        raise