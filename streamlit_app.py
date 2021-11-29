import streamlit as st
import requests 
import geocoder

st.markdown("# Hello streamlit")
lLocation = geocoder.osm("Amsterdam").latlng
st.markdown("Your location: {}".format(lLocation))

resp = requests.get("https://gpsgadget.buienradar.nl/data/raintext?lat=%s&lon=%s" 
        % (lLocation[0], lLocation[1]))
st.markdown("## Weather info")
st.text(resp.text)