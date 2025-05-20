
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Sai Dhanush | Portfolio", layout="wide")

pages = ["Home", "Projects", "Skills", "Resume", "Contact"]
page = st.sidebar.radio("Navigate", pages)

if page == "Home":
    st.title("👋 Hi, I'm N. Sai Dhanush")
    st.subheader("M.Tech in Data Science | Ex-McKinsey & Accenture | Full-Stack Data Scientist")

    st.markdown("""
    I'm a results-driven data science professional with expertise in AI, supply chain optimization, and advanced analytics. 
    Passionate about transforming data into actionable insights to drive business decisions.
    """)

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[📄 View Resume](https://drive.google.com/viewerng/viewer?embedded=true&url=https://drive.google.com/uc?id=1GXbme8GG9iEONbTZsCpNwDlluRw_VO79&export=download)")
        st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/n-sai-dhanush-2b5683112/)")
        st.markdown("[💻 GitHub](https://github.com/dhanush-github)")

elif page == "Projects":
    st.title("📂 Projects")

    # 🔁 Replace or update the list below with your latest projects
    projects = [
        {
            "title": "Invoice Extraction Bot",
            "description": "AI-powered invoice parser using OpenAI & LangChain.",
            "tech": "Streamlit, Python, LangChain",
            "link": "https://github.com/dhanush-github/Invoice-Extractio-Chatbot"
        },
        {
            "title": "Conversational AI for Website Knowledge Retrieval",
            "description": "Chatbot using LangChain, HuggingFace, and Pinecone.",
            "tech": "LangChain, HuggingFace, Pinecone",
            "link": "https://github.com/dhanush-github/Conversational-AI-for-Website-Knowledge-Retrieval"
        },
        # 👉 ADD or REMOVE projects below as needed
    ]

    for project in projects:
        st.markdown(f"### [{project['title']}]({project['link']})")
        st.write(project['description'])
        st.markdown(f"**Tech Stack:** {project['tech']}")
        st.markdown("---")

elif page == "Skills":
    st.title("🧠 Skills & Tools")
    st.markdown("""
    **Languages**: Python, SQL  
    **Data Science**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
    **Visualization**: Power BI, Excel  
    **Tools**: Streamlit, LangChain, Git, Jupyter, Jira  
    **Soft Skills**: Communication, Client Engagement, Storytelling  
    **Domain Knowledge**: Supply Chain Analytics, AI Optimization, Forecasting  
    """)

elif page == "Resume":
    st.title("📄 Resume")
    st.write("You can view or download my resume below:")
    st.markdown("[Click to View My Resume](https://drive.google.com/viewerng/viewer?embedded=true&url=https://drive.google.com/uc?id=1GXbme8GG9iEONbTZsCpNwDlluRw_VO79&export=download)")

elif page == "Contact":
    st.title("📬 Contact Me")
    st.markdown("""
    Feel free to reach out via email or connect with me on LinkedIn.

    📧 Email: saidhanush.n@gmail.com  
    🔗 LinkedIn: [n-sai-dhanush](https://www.linkedin.com/in/n-sai-dhanush-2b5683112/)  
    💻 GitHub: [dhanush-github](https://github.com/dhanush-github)
    """)
