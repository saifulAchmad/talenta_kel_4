import streamlit as st
import pandas as pd


df = pd.read_csv("umkm.csv")
# df = df.drop(columns=" ")
columns_to_remove = [col for col in df.columns if col == '']
if columns_to_remove:
    df = df.drop(columns=columns_to_remove)
st.title("hello world")



st.sidebar.title("Pilih Lokasi")

with st.sidebar:
    selected_province = st.multiselect("Pilih Provinsi :", df['provinsi'].unique())

    
    if selected_province:
        filtered_cities = df[df['provinsi'].isin(selected_province)]['kota'].unique()
    else:
        filtered_cities = df['kota'].unique()

    selected_cities = st.multiselect("Pilih Kota :", filtered_cities)

    if selected_cities:
        filtered_districts = df[df['kota'].isin(selected_cities)]['kecamatan'].unique()
    else:
        filtered_districts = df['kecamatan'].unique()

    selected_districts = st.multiselect("Pilih Kecamatan :", filtered_districts)

    
    if selected_districts:
        filtered_industries = df[df['kecamatan'].isin(selected_districts)]['bidang'].unique()
    else:
        filtered_industries = df['bidang'].unique()

    selected_industries = st.multiselect("Pilih bidang :", filtered_industries)


filtered_df = df.copy()

if selected_province:
    filtered_df = filtered_df[filtered_df['provinsi'].isin(selected_province)]

if selected_cities:
    filtered_df = filtered_df[filtered_df['kota'].isin(selected_cities)]

if selected_districts:
    filtered_df = filtered_df[filtered_df['kecamatan'].isin(selected_districts)]

if selected_industries:
    filtered_df = filtered_df[filtered_df['bidang'].isin(selected_industries)]

st.dataframe(filtered_df)