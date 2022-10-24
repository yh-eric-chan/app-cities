import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('Worls Cities by Eric')

df = pd.read_csv('worldcities.csv')

# add a slider

pop_filter = st.sidebar.slider('select minimal population', 0.0, 40.0, 4.0)

# add a capital multi select

capital_filter = st.sidebar.multiselect('capital select', df.capital.unique(), ['primary'])

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by population

df = df[df.population >= pop_filter]

# filter by capital

df = df[df.capital.isin(capital_filter)]

# filter by country
if country_filter != 'ALL':
    df = df[df.country == country_filter]

# show data on map

st.map(df)

# show dataframe

st.write(df)

# show total pop by country plot

fig, ax =  plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)

