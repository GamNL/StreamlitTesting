import streamlit as st
import requests 
import geocoder

st.markdown("# Hello streamlit")
lLocation = geocoder.ip("me").latlng
st.markdown("Your location: {}".format(lLocation))

resp = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=hourly,daily&appid=%s&units=imperial" 
        % (lLocation[0], lLocation[1], "43eda1fbcf0b07043eeeac93ae54e1e0"))
st.markdown("## Weather info")
st.write(resp.text)