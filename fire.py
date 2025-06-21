from etfe import etfe
from gvalue import gvalue
import streamlit as st
from termcolor import colored, cprint
import sqlite3
import pandas as pd
import random
import smtplib
from email.message import EmailMessage
import email.message
from PIL import Image

from mail import emailnote

def fire():
	
	
	menue = ["Select The Membrane Kind","ETFE","PTFE","PVC"]
	choice = st.selectbox("Select membrane kind", menue)
	PTFE = """ <h3>PTFE fire behavior:</h3>

<p> Unlike PVC or ETFE membrane, since PTFE membrane usually needed for stronger structural characteristics the yarns/substrata of PTFE coated membrane is usually woven from almost non-combustible fiberglass-almost because some standards does not give it this rating specially if processed or mixed with some polymers-. That’s alone kills big mass of fire, and accordingly the smoke behavior of PTFE coated fiberglass membrane is s1 not s2 -s2 is the case in PVC-, this equal to almost no smoke. The PTFE and ETFE are commonly blessed with s1 rating of smoke and therefore used intensively in ceiling linings or closed envelopes roofs and many more applications where fire safety is highlighted.</p>

<p> Nevertheless, to quickly grasp the difference, imagine a fire burning brand test aiming to burn and consume identical samples of PTFE, PVC and ETFE. The ignition time of PTFE coated fiberglass is of much interest, it takes approximately 1 minute to start, and observation would be mere peeling of coating has started and it takes approximately 25 minutes to consume test sample comparing to approximately 3 minutes to consume same sample of PVC and few seconds to consume same sample of ETFE. Although PTFE coating itself is polymer too but since the time of ignition and progress of combustion is of enormous importance, the PTFE coated fiberglass stand out versus other kinds of membranes.</p>

<p>However, it’s worth to mention that in terms of classification, the time or progress of combustion is not the main criteria, example on this reference to ASTM E108, a Class A conditions of classifications for a roof covering material must meet the following conditions when subjected to the particular class of fire tests:</p>
	
	<h5> At no time during or after the intermittent flame, spread of flame, or burning brand tests shall:</h5>

1- Any portion of roof covering material be blown or fall off the test deck in the form of flaming or glowing brands that continue to glow after reaching the floor, or 

2- The roof deck be exposed, or

3- Portions of the roof deck fall away in the form of particles that continue to glow after reaching the floor.

4- At no time during the Class A intermittent flame and burning brand test shall there be sustained flaming of underside of the deck. 

5- At the test conclusion of spread of flame tests, the flaming shall not have spread beyond 6ft for Class A and there shall have been no significant lateral spread of flame from the path directly exposed to the test flame 


6- In the flying brand test, no flying, flaming brands, nor particles that continue to glow after reaching the floor may be produced. 








<h6>PTFE coated fiberglass is classified as follows:</h6> 

ASTM E108                   [Class A, Passed] 

EN13501-1                     [B s1 d0]



"""
	PVC =""" <h3>PVC fire behavior:</h3>
Concerning philosophy of PVC fire safety, any PVC membrane combustion process can be divided into five stages as follows:


-Softening 

-Melting 

-Pyrolysis 

-Charring 

-Fully combustion and burning out


The softening and melting temperature of the PVC membrane material is about 164 ◦C, and the critical temperature of the membrane material is about 257 ◦C. The membrane material burns through to form holes of the same size as the flame contact surface. A standard properly made PVC membrane product shall not show any dripping/drops during combustion(zero). 
Perhaps the particular risk in PVC membrane products, is the carbon monoxide which is main toxic gas in the gas produced in the process of combustion, which is considered the major cause of victims during fire. It is believed that standard PVC membrane products comes with PVDF film above the PVC coating helps reducing this gas during initial ignition until the membrane itself has melted open to allow smoke out, yet it could be in the range of 25% reduction only. This is why careful considerations must be addressed when PVC membrane is used as inner ceiling liner to another hard cladding (e.g., a kind of false ceiling, or stretched ceiling)  

<h6>A standard PVC membrane complies to following international fire standards:</h6>


EN13501-1                         [B s2 d0] 


NFPA 701-10                        [PASSED] 
 """
	ETFE = """ 

​

<h3>Abstract on ETFE fire behavior:</h3>

This report addresses two main issues as following:

<p>1. The fire behavior and compliance of ETFE materials to recognized international standard.</p>

 

<p>2. Conclusion of report reference to some legislators concerning fire protections is advising designers that all hard roofs building envelopes facades, doors and windows have to be NON-COMBUSTIBLE with fire resistance X-hours. This is causing big confusion or mix up when fabric, membrane or foils(ETFE) are being used as elevated skylights and facades. The ETFE accordingly is being confused with hard materials facades/roofs non-combustibility x-hours and accordingly some consultants and firms-unfortunately- thinks that ETFE shall not be used confusing it with hard materials envelop which is flagrant wrong understanding to legislators intent in regulations and the ETFE super safe fire behavior.</p>

 

 

​

 

<h6>1- The fire behavior and compliance of ETFE materials to recognized international standard.</h6>

 

 

<p>ETFE Foil as material (with a melting point of approx. 280° C) is classified as a low flammable material and is considered as self-extinguishing. In the event of a fire, the heat of smoke will cause the foil to soften and shrink away from the fire source and create a natural ventilation. However, if there is any concern that smoke at the ETFE-surface won’t reach the ETFE melting temperature,then, in such a case it is worth considering the installation of smoke vents in roofing-areas in order to ventilate the space of smoke if proved required by fire engineer. The weight of the ETFE-material used in a roof or in a façade is insignificant regarding to its fire load.</p>

<h6>ETFE foil fire behavior is classified as follows:</h6>

DIN 4102                                          [Class B1] 

EN 13501-1                                      [Class B-s1,d0]

NFP 92-505                                       [M2]

NFPA 701                                          [Pass]

UL94                                                  [V-0]

UL 723 / (ASTM E84)                        [Pass/Class A]

JIS A 1322                                         [Class 1]

JIS K 7201-2 (ISO 4590-2)              [Limited Oxygen Index 29.1% (nonflammable in air)] 

 

 <h6>The philosophy of ETFE fire safety can be described as follows:</h6>

 

<p>ETFE-foil need not to have any fire resistance duration, because the ETFE melts at a certain temperature, opens and works as a natural smoke vent. No burning droplets occur, no impermissible smoke develops and it is self-extinguishing when the flame goes out or the fire is far enough away from the ETFE-foil. Consequently, the fire behavior of ETFE-foil, applied in a roof or in a façade area, can be described as very safe, referring to the flame spread and fire propagation.</p>

  

<p>This philosophy has been applied successfully many times over many years in many countries all over the world without any problems supports that the application of ETFE-foil as building envelope material in roof- and façade areas is possible and outstandingly safe, even the foil doesn’t comply with the requested standard of a so called “hard roof”.</p>

​

<h6>2- Conslusions on why ETEF does comply with legislators regulations generally:</h6>

<p>The concept of legislators intent mainly is to minimize the risk of fire and safe guard souls and properties. From aforementioned report, the fire behavior of ETFE material is safe and compliant with wide range of international recognized fire codes.</p>

 

 <p>X-hours fire resistance or non combustibility does not apply on ETFE or any kind of thin polymer membrane-as such strict regulations on facades or elevations which are starting from walkable/habitated/usable ground levels(less than 2.0m proximity) and extending further(in other words main building envelop close to ground < 2m), such strict regulations could be needed in main outer doors or windows.Nevertheless, ETFE applications in elevated skylights or facades are always far from usable ground levels(greater than 2.0m from ground/walkable ground), that is perfectly safe.</p>  

 

<p>There is no alternative polymer to ETFE which have ETFE charasteristics properties- especially transparency, solar transmittance and low weight- and at the same time non-combustible, that is not possible.

 

<p>The ETFE is self-extinguished materials in few seconds, does not spread flames, does not emit considerable amount of smoke and does not form any drops after burning. It is very light material (100 times lighter than glass), melts immediately without drops and accordingly there is no risk of heavy falling objects which should be considered as super plus safety value than any other conventional hard transparent material.</p>

Caution: This report addresses strictly the foil materials only(i.e. does not address profile frames rubbers and any other accessories in ETFE roof, make sure all other accessories used are equal to superior in fire behavior too</p>"""

	if choice == "ETFE":
		st.markdown(ETFE,unsafe_allow_html=True)
	if choice == "PVC":
		st.markdown(PVC, unsafe_allow_html=True)
	if choice == "PTFE":
		st.markdown(PTFE, unsafe_allow_html=True)