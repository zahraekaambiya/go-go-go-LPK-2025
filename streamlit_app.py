import streamlit as st

st.title(":red[My project LPK 2025"])
st.write(":orange[NTP], *IS COOL!* :sunglasses:")

number = st.number_input("Insert a number",min_value=0, max_value=0)
if number%2==1:
  st.write("Bilangan",number,"termasuk bilangan ganjil")
else:
  st.write("Bilangan",number,"termasuk bilangan genap")
