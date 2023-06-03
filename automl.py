import streamlit as stt
with stt.sidebar:
    stt.image("./logo.png")
    stt.title("AutoML")
    choice = stt.radio("Navigation",["Data Processing", "Data profiling" , "CASH", "Download"])
    stt.info("You can navigate through eacch of the selections")
stt.write("This is bla bla bla")

if choice == "Data Processing":
        stt.write("Data Processing: This selection is under developement please make sure tha the data is processed accodingly")
        stt.info("Only processed data can be make good resoults")
        options = ["Upload your data", "Defalut Data Test"]
        input = stt.selectbox("Select a choice", options)
        pass
if input =="upload your data":
    uploaded_file=stt.file_uploader("upload Data")
    if uploaded_file is not None:
        st.write("processing uploaded file")
        if uploaded_fileis not None:
            df=pd.read_csd(uploaded_file)
            stt.dataframe(df)

if choice == "Data profiling":
        stt.write("Data profiling: This selection is under developement please make sure tha the data is processed accodingly")
        stt.info("Only processed data can be make good resoults")
        pass
if choice == "CASH":
        stt.write("CASH: This selection is under developement please make sure tha the data is processed accodingly")
        stt.info("Only processed data can be make good resoults")
        pass

if choice == "Download":
        stt.write("Download: This selection is under developement please make sure tha the data is processed accodingly")
        stt.info("Only processed data can be make good resoults")
        pass