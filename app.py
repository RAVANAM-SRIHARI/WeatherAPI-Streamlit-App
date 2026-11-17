import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("WEATHER_API_KEY")
if not api_key:
    try:
        api_key=st.secrets["WEATHER_API_KEY"]
    except Exception:
        api_key=none

st.set_page_config(
    page_title="weather application",
    page_icon="⛅",
    layout="wide"
)
st.title=("⛅ Real-Time weather application")
st.write=("Get curent weather information for any city:")
city=st.text_input(
    "enter city name",
    placeholder="example hyd"
)
st.subheader("selecte weather information")
col1,col2,col3=st.columns(3)
with col1:
    show_temp=st.checkbox("temperature",value=True)
    show_feels=st.checkbox("feels like",value=True)
    show_humidity=st.checkbox("humidity",value=True)
with col2:
    show_condition=st.checkbox("weather condition",value=True)
    show_wind=st.checkbox("wind_speed",value=True)
    show_wind_dir=st.checkbox("wind direction")
with col3:
    show_pressure=st.checkbox("pressure")
    show_visibility=st.checkbox("visibility")
    show_updated=st.checkbox("last updated")

if st.button("Get weather"):
    if not city.strip():
        st.warning("please enter a city name")
    elif not api_key:
        st.error("API key not found . Check your .env configuration.")
    url="https://api.weatherapi.com/v1/current.json"
    params={
        "key":api_key,
        "q":city.strip()
    }
    try:
        response=requests.get(url,params=params,timeout=5)
        response.raise_for_status()
        print("status code :",response.status_code)
        result=response.json()
        location=result["location"]
        current=result["current"]
        weather_data={
            "temparature":(show_temp,current["temp_c"],"°C"),
            "feels like":(show_feels,current["feelslike_c"],"°C"),
            "humidity":(show_humidity,current["humidity"],"%"),
            "weather condition":(show_condition,current["condition"]["text"],""),
            "wind speed":(show_wind,current["wind_kph"],"km/h"),
            "wind direction":(show_wind_dir,current["wind_dir"],""),
            "pressure":(show_pressure,current["pressure_mb"],"mb"),
            "visibility":(show_visibility,current["vis_km"],"km"),
            "last updated":(show_updated,current["last_updated"],"")

        }
        selected_data=[(name,value,unit)for name,(selected,value,unit) in weather_data.items() if selected ]
        if selected_data:
            columns=st.columns(3)
            for index,(name,value,unit) in enumerate(selected_data):
                with columns[index%3]:
                    st.metric(label=name,value=f"{value}{unit}")
        else:
            st.warning("select at least one weather detail.")
    except requests.exceptions.HTTPError:
        st.error("unable to find weather information.Check the city name or API KEY")
    except requests.exceptions.RequestException as e:
        st.error(f"connecto=ion error:{e}")
    except (KeyError,ValueError):
        st.error("unexpected response received from the weather api")
