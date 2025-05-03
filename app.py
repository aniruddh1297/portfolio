import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aniruddh Sahukar | Portfolio", layout="wide")

# CSS for max width + text formatting
st.markdown("""
<style>
    .centered-container {
        max-width: 800px;
        margin: auto;
        line-height: 1.7;
        padding: 20px 30px;
    }
    .centered-container h1, .centered-container h2, .centered-container h3 {
        text-align: center;
        margin-top: 1.2em;
    }
    .centered-container ul {
        padding-left: 1.2em;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Load profile photo
image = Image.open("assets/profile.jpg")

st.markdown("""
<style>
/* Center the tabs */
[data-baseweb="tab-list"] {
    justify-content: center !important;
}

/* Tab font size and spacing */
[data-baseweb="tab"] {
    padding: 0.5rem 1.2rem;
    font-size: 16px;
    font-weight: 600;
    color: #ffffff;
    background-color: #1c1f26;
    border-radius: 8px 8px 0 0;
    margin: 0 5px;
}

/* Active tab */
[data-baseweb="tab"][aria-selected="true"] {
    background-color: #4f8bf9;
    color: #fff;
}

/* Hover effect */
[data-baseweb="tab"]:hover {
    background-color: #31333F;
}
</style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🏠 Home", "🧑 About", "💼 Projects", "📄 Resume", "📬 Contact"]
)

# -------------
# HOME TAB
# -------------
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='centered-container'>", unsafe_allow_html=True)

        col_img, col_txt = st.columns([1, 2])
        with col_img:
            st.markdown("###")  # spacer to align with text height
            st.image(image, width=200)

        with col_txt:
            st.markdown("### 👋 Hello, I’m")
            st.markdown("<h1 style='margin-top: 0;'>Aniruddh Sahukar Srinivas</h1>", unsafe_allow_html=True)
            st.markdown("""
Experienced Software Engineer with over six years of expertise spanning Machine Learning, DevOps, Software Development, and Testing. Proficient in LLMs, Prompt Engineering, CI/CD, and backend development. Adept at delivering end-to-end ML/AI solutions, optimizing software pipelines, and implementing robust DevOps and Automation strategies. Passionate about driving innovation and contributing to dynamic technology teams to support organizational growth.

- 🌍 Based in Karlsruhe, Germany
""")

        st.markdown("</div>", unsafe_allow_html=True)


# -------------
# ABOUT TAB
# -------------
with tab2:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='centered-container'>", unsafe_allow_html=True)
        st.title("About Me")

        st.markdown("""
I'm **Aniruddh Sahukar Srinivas**, a Machine Learning Engineer with **6+ years of experience** across Machine Learning, MLOps, DevOps, Software Development, and Quality Assurance.

🔍 I specialize in designing and deploying AI/ML pipelines, integrating LLMs into production systems, and streamlining DevOps workflows to enable scalable, intelligent solutions.

🧠 **Current Role**:  
**MLOps Engineer at GetItDone Technologies GmbH**, where I:
- Developed scalable FastAPI/Flask-based ML services (YOLO, GPT-4o)
- Deployed models with Kubernetes and Docker
- Boosted chatbot accuracy through advanced prompt engineering
- Led MLOps from ingestion to production

🔧 **Prior Experience**:
- As a **DevOps Engineer**, built CI/CD pipelines, API test automation (Postman), and anomaly detection dashboards (SQL + Metabase)
- As a **Senior QA Engineer at NTT Data**, led ETL migrations, optimized data workflows, and introduced automated testing across massive data warehouses

🎓 **Education**:
- M.Sc. in Applied Computer Science – SRH Hochschule Heidelberg (2025)  
- B.E. in Information Science – VTU Bengaluru (2018)

🛠 **Skills**:
- **AI/ML & LLMs**: GPT-4o, Prompt Engineering, n8n Agents  
- **DevOps**: GitLab CI/CD, GitHub Actions, Docker, Kubernetes  
- **Backend**: Python, Flask  
- **Frontend**: Vue.js  
- **Testing**: Postman, Swagger  
- **Databases**: PostgreSQL, MySQL  
- **Cloud & Tools**: AWS, Azure, Metabase  
- **OS**: Linux, Windows

🌐 **Languages**:  
English (Professional) | German (Basic)

🎸 **Hobbies**:  
Guitarist 🎶 | Music Production 🎧

📍 **Based in** Karlsruhe, Germany | Open to remote-first roles.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# -------------
# PROJECTS TAB
# -------------
with tab3:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='centered-container'>", unsafe_allow_html=True)
        st.title("🚀 Projects")

        st.subheader("🧠 ChefGPT – AI Recipe Generator (RAG + LLMs)")
        st.markdown("""
**Description:**  
ChefGPT is a fun and useful AI assistant that suggests creative meal recipes using the ingredients you already have.

**Tech Stack:**  
`LangChain`, `FAISS`, `Mistral 7B (via OpenRouter)`, `HuggingFace`, `Streamlit`

**Highlights:**  
- Uses Retrieval-Augmented Generation (RAG) to fetch and ground responses in real recipe data  
- UI built in Streamlit with multiple cooking modes (vegan, student, hangover)  
- Embedded search with FAISS and HuggingFace embeddings  
- GPT-style interactive streaming output  
- Fully deployable and open-source  
[🔗 GitHub Repo](https://github.com/aniruddh1297/FridgeGPT)
""")

        st.markdown("---")

        st.subheader("💼 MLOps & DevOps Projects (at GetItDone Technologies GmbH)")
        st.markdown("""
**GPT-4o Conversational Layer**  
- Built a scalable Flask API to integrate GPT-4o for customer query handling  
- Achieved 35% faster resolution times via AI automation  

**FastAPI Model Deployments (YOLO)**  
- Containerized ML models using Docker + Kubernetes  
- Integrated real-time computer vision into cloud-native backend  

**Prompt Engineering + Frontend Agent Integration**  
- Led GPT-3.5/4o prompt workflows powering task-completion bots  
- Boosted end-user satisfaction by 20%  

**CI/CD Automation + Monitoring**  
- Designed GitLab pipelines, Slack alerting, and Postman test monitoring  
- Increased test coverage to 98%, reduced downtime by 50%
""")

        st.markdown("---")

        st.subheader("🧪 QA & ETL Automation (at NTT Data)")
        st.markdown("""
**ETL Migration & Optimization**  
- Migrated large-scale insurance workflows from Eclipse to Java stack  
- Reduced report latency by 35%, delivered 2 weeks ahead of deadline  

**Test Automation & Data Quality**  
- Automated 120+ hours/month of repetitive SQL test cases  
- Used Redgate, SAP BO, and custom scripts to validate large-scale DWHs  
- Improved data accuracy to 97% with regression and performance testing
""")

        st.markdown("</div>", unsafe_allow_html=True)
# -------------
# RESUME TAB
# -------------
with tab4:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='centered-container'>", unsafe_allow_html=True)
        st.title("📄 Resume")
        with open("assets/resume.pdf", "rb") as f:
            st.download_button("📥 Download My Resume", f, file_name="Aniruddh_Sahukar_Resume.pdf")
        st.markdown("</div>", unsafe_allow_html=True)

# -------------
# CONTACT TAB
# -------------
with tab5:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='centered-container'>", unsafe_allow_html=True)
        st.title("📬 Contact Me")

        st.markdown("""
If you'd like to get in touch, collaborate, or chat about opportunities, feel free to reach out through any of the channels below:

- 📧 **Email**: aniruddh1297@gmail.com  
- 📞 **Phone**: [+49 1590 6446469](tel:+4915906446469)  
- 💼 **LinkedIn**: [linkedin.com/in/aniruddh-ss](https://www.linkedin.com/in/aniruddh-ss/)  
- 🐙 **GitHub**: [github.com/aniruddh1297](https://github.com/aniruddh1297)
        """)
        st.markdown("</div>", unsafe_allow_html=True)
