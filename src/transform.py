import pandas as pd
import numpy as np

# Tools Salary Month
def get_salary_month(salary):
    unit_map = {
        'year' : ['/year','/yr'],
        'month' : ['/month','/mo'],
        'hour' : ['/hour','/hr']
    }
    
    # jika kolom kosong return jadi nan
    if pd.isnull(salary):
        return np.nan
    
    s = salary.replace('$','').replace(',','')
    
    for unit, x in unit_map.items():
        if any(alias in s for alias in x):
            for alias in x:
                s = s.replace(alias,'')
            try:
                value = float(s)
            except ValueError:
                return np.nan

            if unit == "year":
                salary = value / 12
                return round(salary,2)
            elif unit == "month":
                salary = value
                return round(salary,2)
            elif unit == "hour":
                salary = value * 173 # rata2 jam kerja di us dalam 1 bulan
                return round(salary,2)
    
    return np.nan            

# transfrom data Product
def transform_data_products(df_products):
    # df_products
    #ratings
    df_products.drop(columns='Unnamed: 0', inplace=True)
    df_products['ratings'] = pd.to_numeric(df_products['ratings'], errors='coerce').astype(float)

    #no_ratings
    #same treat as 'ratings' column
    df_products['no_of_ratings'] = pd.to_numeric(df_products['no_of_ratings'].str.replace(",", ""),errors='coerce')
    df_products['no_of_ratings'] = df_products['no_of_ratings'].fillna(0)

    #convert datatype from float to Integer
    df_products['no_of_ratings'] = df_products['no_of_ratings'].astype('Int64')

    # discount_price
    df_products['discount_price'] = pd.to_numeric(df_products['discount_price'].str.replace(r'[₹,]','', regex=True),errors='coerce')

    # actual price
    df_products['currency']= df_products['actual_price'].str[:1]
    df_products['actual_price'] = df_products['actual_price'].str.replace(r'[₹,]','', regex=True).astype(float)
    df_products = df_products.replace(0, np.nan)

    # Membuat discount_percentage
    df_products['discount_percentage'] = ((df_products['actual_price'] - df_products['discount_price']) / df_products['actual_price'] * 100).round(1)

    return df_products

# transform data req
def transform_data_req(df_req):
    # data set 'df_req'
    # Drop row tanpa nama company
    df_req.dropna(subset=['company'], inplace=True)

    # Bersihin spasi & newline dari nama company
    df_req['company'] = df_req['company'].str.strip()
    df_req['company'] = df_req['company'].str.replace(r'\n.*','',regex=True)

    # --- Location (City & State) ---
    # Pisahin kolom 'location' jadi 'city' & 'state'
    df_req[['city','state']] = df_req['location'].str.split(",", n=1, expand=True)

    # Isi state kosong dengan "Remote"
    df_req['state'] = df_req['state'].fillna("Remote")
    df_req = df_req.drop(columns=['location'])

    # --- Dates ---
    # Convert kolom 'dates' jadi tipe datetime
    df_req['dates'] = pd.to_datetime(df_req['dates'],utc=True)

    # Ubah timezone ke America/New_York (karena ini data us)
    df_req['dates'] = df_req['dates'].dt.tz_convert('America/New_York')

    # --- Salary ---
    # Bersihin string "(est.)" dari salary
    df_req['salary_estimate'] = df_req['salary_estimate'].str.replace(r'\(.*','',regex= True)

    # Konversi salary ke monthly salary (USD)
    df_req['salary_estimate'] = df_req['salary_estimate'].apply(get_salary_month)

    # --- Company Demographics ---
    # Isi missing values dengan kategori "Unknown"
    df_req['company_size'] = df_req['company_size'].fillna('Unknown')
    df_req['company_revenue'] =  df_req['company_revenue'].fillna('Unknown / Non-Applicable')
    df_req['company_type'] =  df_req['company_type'].fillna('Unknown')
    
    return df_req