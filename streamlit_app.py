import streamlit as st
import requests 
import geocoder

st.markdown("# Basic buien radar")
sLocation = st.text_input("Plaats:","Amsterdam")

lLocation = geocoder.osm(sLocation).latlng
st.markdown("Locatie lat long: {}".format(lLocation))

resp = requests.get("https://gpsgadget.buienradar.nl/data/raintext?lat=%s&lon=%s" 
        % (lLocation[0], lLocation[1]))
st.markdown("## Weather info")
st.text(resp.text)