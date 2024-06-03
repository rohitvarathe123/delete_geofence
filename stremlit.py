import streamlit as st
import requests
import pandas as pd

st.title('Geofence ID Deleteig and Viewer')
st.write('please Name the column in the CSV file * geofence_id * ')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# token = 'RA7yf3GAldLcVHFm4eNIYy3HBxaxOA+NQa0nF31fIKElHJUy+KV6FoKDt57BMaSr'
st.title('Input header')






headers = st.text_input('Enter your token:', '')


base_url = 'https://intouch.mapmyindia.com/apis/api/geofence/'

def delete_geofence(geofence_id):
    url = f"{base_url}{geofence_id}"
    try:
        response = requests.delete(url, headers=headers)
        if response.status_code == 200:
            result = ('Success', geofence_id, response.status_code, '')
        else:
            result = ('Failed', geofence_id, response.status_code, response.text)
    except Exception as e:
        result = ('Error', geofence_id, None, str(e))
    
    return result


results = []


if headers:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'geofence_id' in df.columns:
            g_list = df['geofence_id'].tolist() 
            st.write("List of Geofence IDs:")
            st.write(str(g_list))
            for geofence_id in g_list:
                result = delete_geofence(geofence_id)
                st.write(result)
                results.append(result)
    else:
        st.error("The uploaded CSV file does not contain a 'geofence_id' column.")

    


df1 = pd.DataFrame(results, columns=["Result", "Geofence ID", "Status Code", "Error Message"])
st.write(df1)
st.write("Lengh of deleted Geofence IDs - ", len(df1))
