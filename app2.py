#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import streamlit as st


# In[ ]:


#loading the trained model
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@st.cache_data()

#defining the function which will make the prediction using the data which the user inputs
def prediction(email):
    
    #Making predictions
    prediction=classifier2.predict(vectorizer.transform([s]))
    
    if prediction==0:
        pred='Not Spam'
    else:
        pred='Spam'
    return pred

#this is the main function in which we define our webpage
def main():
    #front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit email scan spam App</h1>
    </div>
    """
    #display the front end aspect
    st.markdown(html_temp,unsafe_allow_html=True        
        

    st.form(key='test_email'):
    msg =st.text_area("write your email here")
    submit_code = st.form_submit_button("Execute")
    if submit_code:
        st.info("Query Result")
        if model.predict(vectorizer.transform([msg]))[0]==1:
            st.write('Your message is a spam')
        else:
            st.write('Your message is a normal email')
        
if __name__ == '__main__':
	main()
    
    

