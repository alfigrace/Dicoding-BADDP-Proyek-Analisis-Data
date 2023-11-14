import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime

def create_season_bike_sharing_df(df):
    byseason_df = df.groupby(by="season").instant.nunique().reset_index()
    byseason_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byseason_df

def create_year_bike_sharing_df(df):
    byyear_df = df.groupby(by="yr").instant.nunique().reset_index()
    byyear_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byyear_df

def create_holiday_bike_sharing_df(df):
    byholiday_df = df.groupby(by="holiday").instant.nunique().reset_index()
    byholiday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    
    return byholiday_df

def create_workingday_bike_sharing_df(df):
    byworkingday_df = df.groupby(by="workingday").instant.nunique().reset_index()
    byworkingday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    
    return byworkingday_df

def create_weathersit_bike_sharing_df(df):
    byweathersit_df = df.groupby(by="weathersit").instant.nunique().reset_index()
    byweathersit_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byweathersit_df

def sidebar(df):
    df["dteday"] = pd.to_datetime(df["dteday"])
    min_date = df["dteday"].min()
    max_date = df["dteday"].max()

    with st.sidebar:
        st.image("https://github.com/alfigrace/Dicoding-BADDP-Proyek-Analisis-Data/assets/44216877/00095f52-1ab9-4f55-87d3-fa7cb5c0b772")

        def on_change():
            st.session_state.date = date

        date = st.date_input(
            label="Rentang Waktu", 
            min_value=min_date, 
            max_value=max_date,
            value=[min_date, max_date],
            on_change=on_change
        )

    return date

def season(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Musim")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="season",
        y="sum",
        data=df.sort_values(by="season", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def year(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Tahun")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="yr",
        y="sum",
        data=df.sort_values(by="yr", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def month(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Bulan")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="mnth",
        y="cnt",
        data=df.sort_values(by="mnth", ascending=False),
        palette="hls",
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def holiday(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Hari Libur")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="holiday",
        y="sum",
        data=df.sort_values(by="holiday", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def workingday(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Hari Kerja")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="workingday",
        y="sum",
        data=df.sort_values(by="workingday", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

def weathersit(df):
    st.subheader("Penyewaan Sepeda Berdasarkan Cuaca")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.barplot(
        x="weathersit",
        y="sum",
        data=df.sort_values(by="weathersit", ascending=False),
        palette='tab10',
        ax=ax
    )
    ax.set_title(None)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)
    
def temp(df):
    st.subheader("Hubungan antara Jumlah Penyewa dengan Temperatur (suhu)")

    fig, ax = plt.subplots(figsize=(20, 10))
    sns.regplot(
        x=day_df["temp"],
        y=day_df["cnt"],
        line_kws={"color": "r"},
        ax=ax)
    ax.set_title(None)
    ax.set_ylabel("Number of users", fontsize=20)
    ax.set_xlabel("Temperature", fontsize=20)
    ax.tick_params(axis="y", labelsize=20)
    ax.tick_params(axis="x", labelsize=15)
    st.pyplot(fig)

if __name__ == "__main__":
    sns.set(style="dark")

    st.header("Bike Sharing Dashboard :sparkles:")

    day_df = pd.read_csv("https://raw.githubusercontent.com/alfigrace/Dicoding-BADDP-Proyek-Analisis-Data/main/submission/dashboard/main_data.csv")

    date = sidebar(day_df)
    if(len(date) == 2):
        main_df = day_df[(day_df["dteday"] >= str(date[0])) & (day_df["dteday"] <= str(date[1]))]
    else:
        main_df = day_df[(day_df["dteday"] >= str(st.session_state.date[0])) & (day_df["dteday"] <= str(st.session_state.date[1]))]

    col1, col2 = st.columns(2)  
 
    with col1:
        total_penyewa = main_df['cnt'].sum()
        st.metric(label="Total Rental from all user", value=total_penyewa)
    
    with col2:
        total_record = main_df['instant'].count()
        st.metric(label="Total Record", value=total_record)

    season_df = create_season_bike_sharing_df(main_df)
    season(season_df)
    year_df = create_year_bike_sharing_df(main_df)
    year(year_df)
    month(main_df)
    holiday_df = create_holiday_bike_sharing_df(main_df)
    holiday(holiday_df)
    workingday_df = create_workingday_bike_sharing_df(main_df)
    workingday(workingday_df)
    weathersit_df = create_weathersit_bike_sharing_df(main_df)
    weathersit(weathersit_df)
    temp(main_df)

    st.caption("© 2023" + " By Alfi Nazilah")
