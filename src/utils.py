import pandas as pd
import os

def extract_csv(path):
    return pd.read_csv(path)

def extract_multi_csv(path):
    files_list = os.listdir(path)
    dfs = []
    for file in files_list:
        file_path = os.path.join(path,file)
        df_temp = pd.read_csv(file_path)
        dfs.append(df_temp)
    return pd.concat(dfs, ignore_index=True)

def load_csv(df,output_dir,file_name):
    path = os.path.join(output_dir,file_name) 
    os.makedirs(output_dir, exist_ok=True)
    print(f"file {file_name} sukses di load ")
    return df.to_csv(path,index=False)