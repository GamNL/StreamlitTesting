import streamlit as st
import requests 
import geocoder
import plotly.graph_objects as go


def verwerk_neerslag(sWeer):
    lRows = sWeer.split("\n")
    dRet = {"Tijd":[],"Neerslag":[]}

    for sRow in lRows :
        
        lRes = sRow.split("|")
        if len(lRes) > 1 :
            dRet["Tijd"].append(lRes[1])
            dRet["Neerslag"].append(float(lRes[0].replace(",",".")))
            if dRet["Neerslag"][-1]!= 0:
                dRet["Neerslag"][-1] = 10**((dRet["Neerslag"][-1]-109)/32)

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
st.plotly_chart(go.Figure(go.Bar(x=dData["Tijd"],y=dData["Neerslag"])))