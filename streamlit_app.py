import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pickle

st.title("Resale HDB Flat Predictor")

# from PIL import Image
# image = Image.open('sunrise.jpg')
# st.image(image, caption='')

# streamlit.metric(label, value, delta=None, delta_color='normal')

st.header("Parameter Selection")
df = pd.read_csv("dataset/df_final.csv",
                usecols=['floor_area_sqm','remaining_lease',
                        'town', 'storey_range',
                        'flat_model', 'flat_type'])

# Expected Remaining Lease
remaining_lease = st.slider("Expected Remaining Lease",
                min_value=40,max_value=95)

# Expected Transaction Date
expect_date = st.date_input("Expected Date of Purchase")

month_offset = round((expect_date-datetime.strptime("2021-09-01", '%Y-%m-%d').date()).days/30)

# Town
town_list= df.town.unique()
town = st.selectbox("Preferred Location",
                    town_list)

# Flat Type
flat_type_list = df.flat_type.unique()
flat_type = st.selectbox("Preferred Flat Type Option",
                        flat_type_list)

# Storey range
storey_range_list = df.storey_range.unique()
storey_range = st.selectbox("Preferred Floor Option",
                            storey_range_list)

# Model Type
model_list= df.loc[df.flat_type==flat_type,"flat_model"].unique()
flat_model = st.selectbox("Preferred Flat Model Option",
                        model_list)

# Flat Size
possible_sizes = df.loc[(df.flat_model==flat_model) & (df.flat_type==flat_type)
                        ,"floor_area_sqm"]
floor_area_sqm = st.slider("Pick flat size for a {} ({})".format(flat_type,flat_model),
                            min_value=float(np.min(possible_sizes.values)),
                            max_value=float(np.max(possible_sizes.values)),
                            step=0.1)


# Model Load
# pipeline = joblib.load('pipeline.pkl')
with open("pipeline.pkl","rb") as pickle_file:
        pipeline = pickle.load(pickle_file)


# Pre-process new data
parameters = {"floor_area_sqm":[floor_area_sqm],
                "remaining_lease":[remaining_lease],
                "month_offset":[month_offset],
                "town":[town],
                "storey_range":[storey_range],
                "flat_model":[flat_model],
                "flat_type":[flat_type]}
df_pred = pd.DataFrame(data=parameters)

# Prediction
y_pred = pipeline.predict(df_pred)

st.header("Prediction Model")
st.subheader("Selected parameters:")
st.write(parameters)
st.write(f"It is predicted that your house would cost around an estimate of\n")

st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f'<p class="big-font">SGD${y_pred[0]:.1f}k!</p>', unsafe_allow_html=True)
