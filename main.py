import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search of Happiness")
x_option = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"),
             help="X-axis is the horizontal axis")
y_option = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"),
                 help="Y-axix is the vertical axis")

df = pd.read_csv('happy.csv')

#match the value of the first option
match x_option:
    case "Happiness":
        x_array = df['happiness']
    case "GDP":
        x_array = df['gdp']
    case "Generosity":
        x_array = df['generosity']

#match the value of the seconde option
match y_option:
    case "Happiness":
        y_array = df['happiness']
    case "GDP":
        y_array = df['gdp']
    case "Generosity":
        y_array = df['generosity']

# Show users choices as subheader
st.subheader(f"{x_option} and {y_option}")

figure1 = px.scatter(x=x_array, y=y_array, 
                    labels={"x": x_option, "y": y_option})
st.plotly_chart(figure1)

st.subheader("See A Particular Country's Statistics")

#ask for input 
country = st.text_input("Type A Country Name")

if country:
    country_data = df[df['country'] == country]

#Check to see if the country is in the data and then output
    if not country_data.empty:
        st.dataframe(country_data, use_container_width=True)
        st.write("This table is interactive. Meaning you can widen columns and " \
         "use the scrollbar to see more information." "\n"
         "(Not: The higher the corruption number, the lower corruption in the country.)")
    else:
        st.error("Country not found in the database")






