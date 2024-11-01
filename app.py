import os
import openai
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention

st.set_page_config(page_title="News Summarizer Tool", page_icon="", layout="wide")

with st.sidebar:
    st.image('images/White_AI Republic.png')
    openai.api_key = st.text_input('Enter OpenAI API token:', type='password')
    if not (openai.api_key.startswith('sk-') and len(openai.api_key)==51):
        st.warning('Please enter your OpenAI API token!', icon='⚠️')
    else:
        st.success('Proceed to entering your news article!', icon='👉')
    with st.container():
        l, m, r = st.columns((1, 3, 1))
        with l: st.empty()
        with m: st.empty()
        with r: st.empty()

    options = option_menu(
        "Dashboard", 
        ["Home", "About Us", "News Summarizer"],
        icons = ['house', 'info-circle', 'newspaper'],
        menu_icon = "list", 
        default_index = 0,
        styles = {
            "icon": {"color": "#dec960", "font-size": "20px"},
            "nav-link": {"font-size": "17px", "text-align": "left", "margin": "5px", "--hover-color": "#262730"},
            "nav-link-selected": {"background-color": "#262730"}          
        })

# Options : Home
if options == "Home":
    st.title("Welcome to the News Summarizer Tool!")
    st.write("This tool helps you quickly summarize news articles.")
    st.write("Simply paste your article in the 'News Summarizer' section and get a concise summary.")
    st.write("Our AI-powered summarizer extracts key information to save you time!")
   
elif options == "About Us":
    st.title("About Us")
    st.write("# AI Republic News Summarizer")
    st.image('images/Pat.png')
    st.write("## Empowering readers with quick, accurate news summaries")
    st.text("Connect with us via LinkedIn: https://www.linkedin.com/in/rpdpscl/")
    st.text("For more information, visit our website: www.airepublic.com")
    st.write("\n")

# Options : News Summarizer
elif options == "News Summarizer":
    st.title("News Summarizer")
    
    System_Prompt = """
    You are an assistant that specializes in summarizing news articles. When the user provides an article or main points, analyze the content carefully to identify and extract the essential facts, key events, main participants, and core themes. Your summary should focus on delivering:

    Conciseness: Aim for a brief overview that captures the main points in 2-4 sentences, unless the user specifies a different length.
    Objectivity: Refrain from adding personal opinions, interpretations, or any information not in the article.
    Clarity: Use simple, direct language for easy readability, focusing on clear, neutral descriptions.
    Relevance: Prioritize primary details such as the who, what, when, where, why, and how of the article.
    For instance:

    If the article discusses a breaking news event, emphasize the incident, the time and location, key people involved, and any immediate outcomes.
    For business or financial news, highlight relevant companies, industry developments, market impacts, or financial figures.
    For political or policy-related topics, summarize the policy or issue, the stakeholders, and potential impacts on the public.
    If the article is complex, use bullet points for clarity if appropriate. Ensure that every summary remains informative and easy to understand, so the user quickly grasps the essential information without needing to read the full article.
    """

    user_message = st.text_area("Paste your news article here:", height=300)
    
    if st.button("Summarize"):
        if user_message:
            struct = [{"role": "system", "content": System_Prompt}]
            struct.append({"role": "user", "content": user_message})
            
            try:
                chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=struct)
                response = chat.choices[0].message.content
                st.subheader("Summary:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a news article to summarize.")