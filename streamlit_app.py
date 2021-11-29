import streamlit as st
import requests 
import geocoder
import plotly.graph_objects as go


def verwerk_neerslag(sWeer):
    lRows = sWeer.split("\n")
    dRet = {"Tijd":[],"Neerslag":[]}

    for sRow in lRows :
        st.write(sRow)
        lRes = sRow.split("|")
        dRet["Tijd"].append(lRes[1])
        dRet["Neerslag"].append(lRes[0])

    return dRet

    


st.markdown("# Basic buien radar")
sLocation = st.text_input("Plaats:","Amsterdam")

lLocation = geocoder.osm(sLocation).latlng
st.markdown("Locatie lat long: {}".format(lLocation))

resp = requests.get("https://gpsgadget.buienradar.nl/data/raintext?lat=%s&lon=%s" 
        % (lLocation[0], lLocation[1]))

st.markdown("## Weather info")
dData = verwerk_neerslag(resp.text)
st.write(dData)
