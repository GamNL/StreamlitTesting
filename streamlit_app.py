import streamlit as st
import geocoder

st.markdown("# Hello streamlit")
st.markdown("Your location: {}".format(geocoder.ip("me").latlng))