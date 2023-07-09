import streamlit as st
from sympy import symbols, solve

page_title = "Polynomial Solver"

layout = "centered"

# -----
st.set_page_config(page_title=page_title,layout=layout)
st.title(page_title)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
with st.form("entry_form",clear_on_submit=True):
    expr = st.text_area("",placeholder="Enter A Polynomial (Eg: 5x^2+2x-10)")     
    submitted = st.form_submit_button("Answer")

    if submitted:
        x = symbols('x')
        if expr.startswith("x"):
            new= "1"+expr
            print(new)
            final_expr = new.replace('x', '*x' )
            sol = list(solve(final_expr))
            print(sol)
            st.write("Zeros Of The Equation Are")
            for i in sol:
                sol = str(i)
                final = sol.replace('sqrt', u"\u221A").replace('*', u"\u00D7")
                
                st.write(final)
        
                 


        else:
            final_expr = expr.replace('x', '*x' )
            sol = list(solve(final_expr))
            print(sol)
            st.write("Zeros Of The Equation Are")
            for i in sol:
                sol = str(i)
                newsol = sol.replace('sqrt', u"\u221A")
                final = sol.replace('sqrt', u"\u221A").replace('*', u"\u00D7")
               
                st.write(final)
        
            
            
