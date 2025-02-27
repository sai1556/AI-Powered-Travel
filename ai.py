import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

API_KEY = os.getenv("AIzaSyAlCtdrEW48j2rPrVaBtmEEebaxDf-qf8M")

st.title("AI-Powered Travel Planner")
st.write("Enter your travel details to get estimated traveling cost details for various travel modes including cab, train, bus and flight.")

source = st.text_input("Source:")
destination = st.text_input("Destination:")

if st.button("Your Travel Plan"):
    if source and destination:
        with st.spinner("Compiling all travel options...."):
            chat_template = ChatPromptTemplate(messages= [
            ("system", """You are an AI-Powered Travel Planner assistant that provides users with the best travel options based on their requirement.
             Given source to destination, You must give the distance and provide information about best travel options like bike, cab, bus, train and flight.
             Each option should have the estimated cost, travel time, distance and any relevant details like stops, traffic details
             you can also give some information about food what are the food items best in between source and destination.
             Convince while presenting the results in a clear, easy-to-read format."""),

            ("human", "Find travel options from {source} to {destination} with estimated costs.")

            ])
            chat_model = ChatGoogleGenerativeAI(api_key = "AIzaSyAlCtdrEW48j2rPrVaBtmEEebaxDf-qf8M", model = "gemini-2.0-flash-exp")
            parser = StrOutputParser()
            
            chain = chat_template | chat_model | parser
            
            raw_input = {"source": source, "destination": destination}
            response = chain.invoke(raw_input)
            
            st.success("Estimated Travel and Costs:", icon="✅")
            travel_modes = response.split("\n")
            for mode in travel_modes:
                st.markdown(mode)
