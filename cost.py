import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
import requests as req
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from mail import email
from Uvalue import uvalue 

from mail import emailnote
from mail import emailme
import mail





if "parameters" not in st.session_state:
	st.session_state ["parameters"] = "false"



def cost():
	
	st.warning("""ETFE construction cost depends on many factors assesed by ETFE specialist, this application advice is beleived to be on fair level/initial budgetary for educational purposes only and shall
	not substitute firm analysis by specialist:""")

	st.header('ETFE skylight construction cost')
	

	skylight = Image.open('images/cushion-app_cost1.png')
	st.image(skylight,
		 caption='Typical rectangualr ETFE Skylight ',
		 use_container_width=150)

	st.write("Lets adjust below system specifications to get the expected cost")

	

	slider_val = st.slider("Cushion width(m):", min_value=1.0, max_value=4.5, value=(1.0))
	cushion_width= slider_val
	span_of_cushion = st.slider("Cushion span (m):", min_value=1.0, max_value=100.0, value=(1.0), step=1.0)
	no_of_layers = st.slider("Cushion number of layers (no):", min_value=1, max_value=5, value=(1), step=1)
	total_area = st.slider("Total area of ETFE skylight/facade (m2):", min_value=4000, max_value=70000, value=(4000),step=100)
	st.warning("Insert valid email below, wrong emails will produce errors, simply insert any proper email")
	person=st.text_input("Insert your Email")


	def calculate():
		st.session_state ["parameters"] = "true"
		

	submit = st.button("Calculate")

	if submit:
		calculate()


		if st.session_state ["parameters"] == "true":

	


			if person:

				s = (1+ span_of_cushion/500)
				w = 1+((4.5-cushion_width)/4.5)*0.5
				
				if total_area == 4000:
					if no_of_layers <=3:
						cost = round(1500*s*w)
					elif no_of_layers == 4:
						cost = round(1700*s*w)
					elif no_of_layers == 5:
						cost = round(1900*s*w)

					 
				elif total_area != 4000:
					if no_of_layers <=3:
						x = (800/64000)*(70000-total_area)
						cost = round((700 + x)*s*w)
					elif no_of_layers == 4:
						x = (800/64000)*(70000-total_area)
						cost = round((900 + x)*s*w)
					elif no_of_layers == 5:
						x = (800/64000)*(70000-total_area)
						cost = round((1100 + x)*s*w)


				
						
				email(person,cushion_width, span_of_cushion, no_of_layers, total_area,cost)
				
				st.success('well done check your email for cost info')
				
			else:
				st.warning('insert your email above!')


if __name__ == '__main__':
	cost()