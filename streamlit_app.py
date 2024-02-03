import pandas
import streamlit

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


my_soil_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/LU_SOIL_TYPE.tsv",sep='\t', header=0)
streamlit.dataframe(my_soil_list)
