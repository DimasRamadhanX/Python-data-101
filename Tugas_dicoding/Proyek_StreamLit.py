#impor lib
import numpy as np
import scipy as sc
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import streamlit as st

#impor data

dfclean=pd.read_csv("C:/Users/luxha/Python data 101/Data Buat Latihan/biking/dfclean.csv")

#graf 1
fig1, axs = plt.subplots(2, 2, figsize=(16, 16))


weather_agg = dfclean.groupby('weathersit')['cnt'].sum().reset_index()
day_agg = dfclean.groupby('day')['cnt'].sum().reset_index()


axs[0, 0].hist(dfclean['temp']*41, weights=dfclean['cnt'], bins=50)
axs[0, 0].set_title("Temperature")


bars = axs[0, 1].bar(weather_agg['weathersit'], weather_agg['cnt'])
axs[0, 1].set_title('Weather Situation')

for bar, count in zip(bars, weather_agg['cnt']):
    height = bar.get_height()
    axs[0, 1].text(bar.get_x() + bar.get_width() / 2, height, str(count), ha='center', va='bottom')


bars_day = axs[1, 0].bar(day_agg['day'], day_agg['cnt'])
axs[1, 0].set_title('Day')

for bar, count in zip(bars_day, day_agg['cnt']):
    height = bar.get_height()
    axs[1, 0].text(bar.get_x() + bar.get_width() / 2, height, str(count), ha='center', va='bottom')


axs[1, 1].hist(dfclean['hum']*100, weights=dfclean['cnt'], bins=50)
axs[1, 1].set_title('Humidity')
axs[1, 1].legend()


plt.tight_layout()
st.pyplot(fig1)

# Graf 2
fig2 = plt.figure(figsize=(22, 6))

sns.lineplot(data=dfclean, x='dtedaymnth', y='cnt', marker='o', color='red', label='trend', ci=None)


plt.axvline(x='12-01', color='blue', linestyle='--', label='Divider')

plt.xlabel('Month')
plt.ylabel('Total Bike Rentals')
plt.title('Monthly Bike Rentals Trend (2011 vs 2012)')


st.pyplot(fig2)

# Graf3
fig3 = plt.figure(figsize=(7, 7))

dataplot = sns.heatmap(dfclean.loc[:, ['atemp', 'temp', 'hum', 'windspeed', 'CasulRatio', 'cnt']].corr(), cmap="YlGnBu", annot=True)
plt.tight_layout()


st.pyplot(fig3)