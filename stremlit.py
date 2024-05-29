import streamlit as st
import requests
import pandas as pd

st.title('Geofence ID Deleteig and Viewer')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# token = 'RA7yf3GAldLcVHFm4eNIYy3HBxaxOA+NQa0nF31fIKElHJUy+KV6FoKDt57BMaSr'
st.title('Token Input App')

# Token input field
token = st.text_input('Enter your token:', '')




headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'access_token': token,
    'access_type': '1',
    'accountid': '11070',
    'authorization': f'Bearer {token}',
    'cookie': 'HttpOnly; HttpOnly; _ga=GA1.2.18109101.1716187206; _gid=GA1.2.331077234.1716738783; _d28=1717048389120; _d29=1717133374876; _ga_3DJQ70P2DW=GS1.2.1716960575.28.1.1716961601.0.0.0',
    'origin': 'https://intouch.mapmyindia.com',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'userid': ''
}


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
