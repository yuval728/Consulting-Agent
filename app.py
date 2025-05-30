import streamlit as st
from datetime import datetime
from src.consulting.crew import Consulting
from src.idea_validator.crew import IdeaValidator

st.set_page_config(page_title="AI Agent Startup Toolkit", layout="centered")
st.title("🚀 AI-Powered Startup & Consulting Toolkit")

option = st.selectbox("Choose Agent Group:", ["Startup Consulting", "Startup Idea Validation"])

def display_task_outputs(task_outputs):
    st.markdown("---")
    st.subheader("📝 Final Task Outputs")

    if isinstance(task_outputs, list):
        for idx, output in enumerate(task_outputs, 1):
            st.markdown(f"### 🔹 Task {idx}")
            st.markdown(output)
    elif isinstance(task_outputs, dict):
        for task_name, output in task_outputs.items():
            st.markdown(f"### 🔹 {task_name}")
            st.markdown(output)
    else:
        st.markdown("⚠️ Unexpected task output format.")
        st.write(task_outputs)

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

        with st.spinner("Running Consulting Agents..."):
            result = Consulting().crew().kickoff(inputs=inputs)

        # Parse and format task outputs
        outputs = result.tasks_output if hasattr(result, "tasks_output") else {}
        display_task_outputs(outputs)

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

        with st.spinner("Running Idea Validation Agents..."):
            result = IdeaValidator().crew().kickoff(inputs=inputs)

        outputs = result.tasks_output if hasattr(result, "tasks_output") else {}
        display_task_outputs(outputs)
