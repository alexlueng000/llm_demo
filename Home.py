import streamlit as st 


st.set_page_config(layout="wide", page_title="Code Demo")
st.title("Welcome to this Demo")

st.sidebar.success("Select a demo above.")


openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
openai_api_key = openai_api_key.lstrip()

st.session_state['openai_api_key'] = openai_api_key


st.markdown(
    """
    Welcome to our Code Review and Job Description Analyzer application!
    
    This application leverages the power of AI to provide two primary functionalities:
    1. **Code Review**: Enter your code snippets and receive immediate, insightful feedback.
    2. **JD Analyzer**: Input a Job Description, and the system will analyze it, providing key insights.
    
    The project is built with Python, Streamlit, LangChain, and the OpenAI API. 
    **👈 Use the sidebar** to navigate between functionalities and see what our application can do!
    
    ### Want to learn more?
    - Explore the project on [GitHub](https://github.com/<username>/<project>)  # Replace with your repository URL
    - Check out our [documentation](https://<docs-url>)  # Replace with your documentation URL
    - Join the discussion in our [community forum](https://<forum-url>)  # Replace with your community forum URL
    
    ### See more complex demos
    - Have a look at our [Code Review Example](https://github.com/<username>/<project>/blob/main/code_review_example.py)  # Replace with your file URL
    - Explore our [JD Analyzer Example](https://github.com/<username>/<project>/blob/main/jd_analyzer_example.py)  # Replace with your file URL
    """
)

st.write("\n")
st.markdown("### Note: It's better to use your own OpenAI API Key")
st.markdown("### but you also can use this share key to explore(have a rate limit issue): ")
st.info("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")