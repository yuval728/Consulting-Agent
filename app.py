import streamlit as st
import threading
from datetime import datetime
from src.consulting.crew import Consulting
from src.idea_validator.crew import IdeaValidator
from event_listener import StreamlitTaskListener

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

        # Create placeholders for each task
        task_placeholders = {
            "Market Analysis": st.empty(),
            "Financial Evaluation": st.empty(),
            "Technology Assessment": st.empty(),
            "Marketing Strategy": st.empty()
        }

        # Define the callback function to update the UI
        def update_ui(task_name, output):
            if task_name in task_placeholders:
                task_placeholders[task_name].markdown(f"**{task_name} Output:**\n{output}")

        # Initialize the event listener
        listener = StreamlitTaskListener(update_ui)

        # Run the crew in a separate thread
        def run_crew():
            crew = Consulting().crew()
            crew.kickoff(inputs=inputs)
        
        with st.spinner("Running Consulting Agents..."):
            run_crew()
            
        # threading.Thread(target=run_crew).start()


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
        
    
        task_placeholders = {}
        task_names = ["Idea Evaluation", "Customer Persona Building", "Lean Canvas Creation", "MVP Recommendation", "Validation Tracking"]
        for task_name in task_names:
            task_placeholders[task_name] = st.empty()
            
        def update_ui(task_name, output):
            if task_name in task_placeholders:
                task_placeholders[task_name].markdown(f"**{task_name} Output:**\n{output}")

        
        listener = StreamlitTaskListener(update_ui)

        # Run the crew in a separate thread
        def run_crew():
            crew = IdeaValidator().crew()
            crew.kickoff(inputs=inputs)
        
        with st.spinner("Running Agents..."):
            run_crew()
