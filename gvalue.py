from etfe import etfe
import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
from PIL import Image
from PIL import ImageDraw

from mail import emailnote






def gvalue():

	
	w,h = 400,300
	slider_val = st.slider("G value through ETFE cushions skylight, slide the bar and see how sky view differs by comparing pictures", min_value=0.2, max_value=0.95, value=(0.5))
	g = slider_val
	remark(g)
	col1, col2 = st.columns(2)
	with col2:

		skyview = Image.open('images/sky.jpg')
		st.image(skyview,
			 caption='Natural sky view' ,
			 use_container_width=100)
		

	with col1:
	
		img = Image.open('images/sky.jpg')
		if 0.25 < g <= 0.33:

			g1 = g/4
			
			# draw = ImageDraw.Draw(img)
			# step =3
			# for n in range(step,w,step):
			# 		for y in range(step,h,step):
			# 			draw.regular_polygon(((n),(y),1), 6, rotation=0, fill="#A9A9A9", outline="silver")
			imgfrit = Image.new("RGB",(w,h), "#808080")
			imgsk=Image.blend(imgfrit,img,(g1))

			return st.image(imgsk,
				caption=f'G value = {g} (Typical viewer standing below skylight)',
				use_container_width=100)

		elif 0.2<=g <= 0.25:
			g1 = 0.98
			imgfrit = Image.new("RGB",(w,h), "#808080")
			imgsk=Image.blend(img,imgfrit,(g1))

			return st.image(imgsk,
				caption=f'G value = {g} (Typical viewer standing below skylight)',
				use_container_width=100)

			
		elif g > 0.85:
			 
			img_no_frits = Image.open('images/sky.jpg')
			imgfrit = Image.new("RGB",(w,h), "#808080")
			imgsk=Image.blend(imgfrit,img,(g))
			return st.image(imgsk,
				caption=f'G value = {g} (Typical viewer standing below skylight)',
				use_container_width=100)
			


		


		else:
			g1 = 0.8*g
			draw = ImageDraw.Draw(img)
			step =3
			# for n in range(step,w,step):
			# 		for y in range(step,h,step):
			# 			draw.regular_polygon(((n),(y),1), 6, rotation=0, fill="silver", outline="silver")
			imgfrit = Image.new("RGB",(w,h), "#808080")
			imgsk=Image.blend(imgfrit,img,(g1))

			return st.image(imgsk, 
				caption=f'G value = {g}(Typical viewer standing below skylight)',
				use_container_width=100)
		



def remark(g):

	

	if 0.25< g <= 0.33:
		st.info("ETFE cushion can achieve this G value range,but sky view goes to opaqueness ")
	elif 0.2<= g <= 0.25:
		st.info("ETFE cushion can achieve this G value range,opaque(colored ETFE or colored & fritted), it remains translucent though ")	
	elif 0.33< g < 0.55:
		st.success("Well done!, this is within optimal G value range and sky view ")
	elif g == 0.2:
		st.info("Typically, this is the lowest G value achievable by ETFE cushion")
	elif g==0.95:
		st.info("Typically, this is the highest possible G value on clear foil ")
	else:
		st.info("This is within quite high amount of sun radiation range unless you want that(e.g, living in Canada)")





# st.sidebar.markdown(f'<h1 style="color:#F63366;font-size:24px;">Want to know more? Send us message below:</h1>', unsafe_allow_html=True)

# useremail = st.sidebar.text_input("Please insert your email")
# message = st.sidebar.text_area("Please insert your info and message")
# submit = st.sidebar.button("mail your message")

# if submit:
# 	if not useremail:
# 		st.warning("Please insert your email address")
# 	if not message:
# 		st.warning("Please insert your message")

# 	else:

# 		st.success("Your message has been sent, thank you!")
# 		email(useremail,message)
	



			
			



				
			# with col1:
				
			# 	skyfrit = imgsk.show()


			# with col2:
				
			# 	skyview = Image.open('images/sky.jpg')
			# 	st.image(skyview,
			# 		 caption='Natural sky view' ,
			# 		 use_container_width=150)

