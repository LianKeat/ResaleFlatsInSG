import streamlit as st

st.title("Resale HDB Flat Predictor")

# from PIL import Image
# image = Image.open('sunrise.jpg')
# st.image(image, caption='')

# streamlit.metric(label, value, delta=None, delta_color='normal')

town_list=[]
model_list=[]

# Town
town = st.selectbox("Preferred Location",
                    town_list)

# Flat Type
flat_type = st.selectbox("Preferred Flat Type Option",
                        ["1 ROOM", "2 ROOM",
                        "3 ROOM", "4 ROOM",
                        "5 ROOM","EXECUTIVE"])

# Flat Size
meansize_bool = st.checkbox(f"Pick mean flat size for {flat_type}",
                            value=False)
if meansize_bool:
    flat_model = st.selectbox("Preferred Flat Model Option",
                            model_list)
else:
    meansize = 0
    st.write(f"Mean flat size: {meansize}")

# Model Type
flat_model = st.selectbox("Preferred Flat Model Option",
                        ["1 ROOM", "2 ROOM",
                        "3 ROOM", "4 ROOM",
                        "5 ROOM", "MULTI-GENERATION",
                        "EXECUTIVE"])



# Storey range
storey_range = st.selectbox("Preferred Floor Option",
                            ["01 TO 03", "04 TO 06",
                            "07 TO 09", "10 TO 12",
                            "13 TO 15", "16 TO 18"])