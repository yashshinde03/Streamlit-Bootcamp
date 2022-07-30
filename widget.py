import streamlit as st
st.title("Widgets")
if st.button("Car"):
    st.write("I love BMW")

name = st.text_input("Name")
st.write(name)
address = st.text_area("Address")
st.write(address)
st.date_input("date")
st.time_input("time")
if st.checkbox("You accept the T&C",value=False):
    st.write("Thank You")

v1 = st.radio("Colours",['r','g','b'],index=0)
v2 = st.selectbox('Colours',['r','g','b'],index=0)
st.write(v1,v2)
v3 = st.multiselect('COLOURS',['R','G','B'])
st.write(v3)
st.slider('age',min_value=18,max_value=60,value=21,step=1)
st.number_input('Numbers',min_value=18,max_value=60,value=21,step=1)#It can be float
img = st.file_uploader("Upload a file")
st.image(img)