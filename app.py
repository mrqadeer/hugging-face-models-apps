
import os
import streamlit as st
from streamlit_option_menu import option_menu
#from src.sentiment_analysis import sentiment_analysis
from src.huggingface import HuggingFace
from src.home import Home


st.set_page_config("HuggingFace",page_icon='🤗',layout='wide')

#main class
class App:
    def __init__(self) -> None:
        """
        Initializes the class by creating a Home and HuggingFace instances.
        """
        self.home=Home()
        self.huggingface=HuggingFace()
        # with open('src/utils/static/main.css','r') as stlye:
        #   st.markdown(f"<style>{stlye.read()}</style>",unsafe_allow_html=True)
        # st.markdown('<link rel="stylesheet" href="src/utils/static/styles.css">', unsafe_allow_html=True)
    
    def run(self):
        """
        Runs the application, setting up the sidebar with an option menu for 'Home' and 'HuggingFace Models'.
        If 'Home' is selected, it displays the home page. If 'HuggingFace Models' is selected, it initializes and displays the HuggingFace models section.
        """
        with st.sidebar:
            app=option_menu(
                menu_title='Introduction',
                options=['Home','HuggingFace Models'],
                icons=['house-heart','command'],
                menu_icon='info',
                default_index=0,
                styles={
                    "menu-title":{"color":'green',"font-size": "26px"},
                    "container": {"padding": "15!important", "background-color": 'black'},
                    "icon": {"color": "white ", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px",'font-weight':'bold', 
                                 "text-align": "left", "margin": "0px",
                                 "--hover-color": "magenta"},
                    "nav-link-selected": {"background-color": "#02ab21"}
                }
            )
        if app=='Home':
            self.home.home()
            
        if app=='HuggingFace Models':
            
            self.huggingface.huggingface()
            
            

            
if __name__=='__main__':
    app=App()
    app.run()

