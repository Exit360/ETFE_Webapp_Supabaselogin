import math
import streamlit as st
from PIL import Image

from mail import emailnote


def uvalue():

	emailnote()
	import math

	ther_exp = 3.2717E-3
	ther_con = 0.026526
	kin_v = 1.6271E-5
			
	ther_dif = 2.2810E-5
	Pr = 0.71332
	k = 1

	


	skylight = Image.open('images/uvalue.png')
	st.image(skylight,
		 caption='General ETFE cushion set up',
		 use_container_width=150)
	intro = """<h6> What to do? its simple,A- Select the heat source temprature T1 and cooling source temprature T2, B- select the cushion thickness refer to the sketch above
			  , C- Finally select the width of cushion and angle of inclination(e.g a typical roof in summer angle would = 180 degrees, the same roof in winter angle would = 0, if facade select any angle e.g 90 degrees or any angle around just mind that angle measured from heating source<h6>""" 
	st.markdown(intro,unsafe_allow_html=True)

	

	T1 = st.slider("Heating source temp Degrees Celsius:", min_value=20, max_value=50, value=(45))
	T2 = st.slider("Cooling source temp Degrees Celsius:", min_value=-15, max_value=25, value=(20))
	L = st.slider("Thickness of cushion (m):", min_value=0.25, max_value=1.08, value=(0.5))
	H = st.slider("Width of cushion (m):", min_value=1.0, max_value=4.5, value=(3.0))
	angle = st.slider("Angle of inclination degrees:", min_value=0, max_value=180, value=(180))
	
	chkbox = st.checkbox("Do you wish to add middle layer?")
	
	if chkbox:
		L = 0.5 * L
	


	

	T1 = T1+ 273.15  # kelvin
	T2 = T2+ 273.15 #kelvin
	Tf = (T1+T2)/2

	theta = angle * (math.pi/180)
	theta_c = 67 * (math.pi/180)

	def nu90():
		Ra = (9.81 * ther_exp * (T1-T2) * L ** 3) / (ther_dif * kin_v)
		Nu = (0.22*((Pr*Ra)/(0.2 + Pr))**0.28)*(H/L)**-0.25
	   
		return Nu 
		
	def nu0():
		
		Ra = (9.81 * ther_exp * 25 * L ** 3) / (ther_dif * kin_v)
		if  3*10**5<= Ra <= 7*10**9:
			Nu = 0.069*Ra**0.333 * Pr**0.074
		else:
			Nu = 1
			
		
		return Nu     

	if angle == 90:
		Nu = nu90()
		hcv = (Nu * ther_con) / L
		hrd = (4 * 5.67E-8 * Tf ** 3)/1.25
		R = (1 / (hcv + hrd))+0.17
		U = (1 / R)*k
		U = round(U, 2)
		
	elif angle == 0:
		Nu = nu0()
		hcv = (Nu * ther_con) / L
		hrd = (4 * 5.67E-8 * Tf ** 3) / 1.25
		R = (1 / (hcv + hrd))+0.14
		U = (1 / R)*k
		U = round(U, 2)

	elif  0 < angle <= 67:
		Nu = (nu0()*(nu90()/nu0())**(theta/theta_c))*math.sin(theta_c)**(theta/(4*theta_c))

		hcv = (Nu * ther_con) / L
		hrd = (4 * 5.67E-8 * Tf ** 3)/1.25
		R = (1 / (hcv + hrd))+0.14
		U = (1 /R)*k
		U = round(U, 2)
		
	elif 67 < angle < 90:
		Nu = nu90()*(math.sin(theta))**0.25
		hcv = (Nu * ther_con) / L
		hrd = (4 * 5.67E-8 * Tf ** 3)/1.25
		R = (1 / (hcv + hrd)) + 0.14
		U = (1 / R)*k
		U = round(U, 2)
		
	elif 90 < angle <= 180:
		Nu = 1 + (nu90() - 1)*math.sin(theta) 
	   
		hcv = (Nu * ther_con) / L
		hrd = (4 * 5.67E-8 * Tf **3) / 1.25
		R = (1/(hrd + hcv)) + 0.21
		U = (1 / R)*k
		U = round(U, 2)
		
	if chkbox:
		
		hrd2= (4 * 5.67E-8 * (Tf-10) ** 3)/1.25 
		R2 = (1/(hrd2 + hcv))
		R = R + R2
		U = (1 / R)*k
		U = round(U, 2)
		
		result = f'<h3>U value = {U} W/K.m2    ||with added middle layer/ 3 layers|| <h3>' 

		st.markdown(result,unsafe_allow_html=True)
	else:
		result = f'<h3>U value = {U} W/K.m2     ||Double layers||<h3>' 
		st.markdown(result,unsafe_allow_html=True)
		

	
	st.info("""The above is based on pure theoritical correlations. Although they are
		in agreement -approximately- with common practice but note that theortical correlations in 
		theromdynamics texts are based on stagnant fluid unlike ETFE cushion where air keeps 
		circulating, furthermore ETFE cushion doesn't have constant thickness which ends at zero
		at edges, on the top of that, ETFE cushions have wide range of diversity in terms of width and projected shape. Hence, the best way to know precise U value is to test it experimentally. 
		Some experts in industry have developed their own method based on series of experimental trials. Therefore, note that thoritical correlations could be
		useful at planning stages but if you have substantially sensitive project and precesion in thermal conductivity is needed, then
		remember that theory might be under or over estimating the actual performance. We hope you enjoy this effort!
		""")

	
	
