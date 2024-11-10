import pickle
import pandas as pd
import streamlit as st

st.title("Mushroom Edibility Prediction App")

cap_surface = st.selectbox(
    "Cap Surface", ["t", "d", "h", "k", "g", "s", "y", "e", "Other", "w"]
)
cap_color = st.selectbox("Cap Color", ["n", "o", "w", "e", "g", "Other", "y", "p"])
gil_attachment = st.selectbox("Gill Attachment", ["s", "p", "a", "d", "x", "e"])
gil_color = st.selectbox("Gill Color", ["n", "Other", "g", "p", "w", "o", "y"])
stem_height = st.slider("Stem Height", min_value=0, max_value=15, value=10, step=1)
stem_width = st.slider("Stem Width", min_value=0, max_value=50, value=25, step=1)
stem_color = st.selectbox("Stem Color", ["w", "y", "o", "n", "Other", "g", "e"])

data = [[cap_surface, cap_color, gil_attachment, gil_color, stem_height, stem_width, stem_color]]
df = pd.DataFrame(
    data,
    columns=[
        "cap-surface",
        "cap-color",
        "gil-attachment",
        "gil-color",
        "stem-height",
        "stem-width",
        "stem-color",
    ],
)

filename = "../Models/Transformations/transformations.pkl"
with open(filename, "rb") as file:
    minmax, labelEncoder = pickle.load(file)

filename = "../Models/ML/Deployment/xgb_bayes.pkl"
with open(filename, "rb") as file:
    model_list = pickle.load(file)
model = model_list[0]

filename = "../Models/Transformations/variables.pkl"
with open(filename, "rb") as file:
    variables = pickle.load(file)

df[['stem-height', 'stem-width']] = minmax.transform(df[['stem-height', 'stem-width']])
categorical = ['cap-surface', 'cap-color', 'gil-attachment', 'gil-color', 'stem-color']
df = pd.get_dummies(df, columns=categorical, drop_first=False, dtype=int)
df = df.reindex(columns=variables, fill_value=0)

if st.button("Classify Mushroom"):
    prediction = model.predict(df)[0]

    prediction = labelEncoder.inverse_transform([prediction])[0]
    # Mostrar el resultado
    if prediction == "e":
        st.success("This mushroom is likely **edible**.")
    else:
        st.error("This mushroom is likely **poisonous**.")
