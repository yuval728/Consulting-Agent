import streamlit as st
from datetime import datetime
from src.consulting.crew import Consulting
from src.idea_validator.crew import IdeaValidator

st.set_page_config(page_title="AI Agent Startup Toolkit", layout="centered")
st.title("🚀 AI-Powered Startup & Consulting Toolkit")

option = st.selectbox("Choose Agent Group:", ["Startup Consulting", "Startup Idea Validation"])

if option == "Startup Consulting":
    st.subheader("🧠 Consulting Input Form")
    industry = st.text_input("Industry", "Web Development")
    region = st.text_input("Region", "India")
    company_size = st.text_input("Company Size", "3 people startup")
    product_type = st.text_input("Product Type", "SaaS")
    
    if st.button("Run Consulting Agents"):
        inputs = {
            'industry': industry,
            'region': region,
            'company_size': company_size,
            'product_type': product_type,
            "current_year": str(datetime.now().year)
        }
        with st.spinner("Running Consulting Crew..."):
            result = Consulting().crew().kickoff(inputs=inputs)
        st.success("Done!")
        st.markdown(result)

elif option == "Startup Idea Validation":
    st.subheader("🚀 Startup Idea Validation Input Form")
    idea = st.text_input("Startup Idea", "A web-based platform for remote team collaboration")
    industry = st.text_input("Industry/Domain", "Tech/Software")
    target_audience = st.text_input("Target Audience", "Remote teams and freelancers")
    region = st.text_input("Region/Market Location", "Global")

    if st.button("Run Idea Validation Agents"):
        inputs = {
            'idea': idea,
            'industry': industry,
            'target_audience': target_audience,
            'region': region,
            'current_year': str(datetime.now().year)
        }
        with st.spinner("Running Idea Validation Crew..."):
            result = IdeaValidator().crew().kickoff(inputs=inputs)
        st.success("Done!")
        st.markdown(result)
