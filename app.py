import streamlit as st 
import calculations.ABS_Corrugated_Panel_Buckling as ABScorr



stf_type = "LOCAL PLATE OF CORRUGATED PANELS"

lc = st.selectbox("Select type of load case",["NORMAL OPERATION","SEVERE STORM"])

L = 94.488
B = 188.976
a = 11.811
b = 15.748
c = 7.874
t = 0.750
phi = 75.000
    

corr_panel_a = ABScorr.Corr_Panel(lc,stf_type,a,L,t,11000,8000,1e-5,1e-5,4000,51475,30e6,0.3,L,B,a,b,c,phi)
corr_panel_b = ABScorr.Corr_Panel(lc,stf_type,b,L,t,10000,7000,1e-5,1e-5,3000,51475,30e6,0.3,L,B,a,b,c,phi)
corr_panel_c = ABScorr.Corr_Panel(lc,stf_type,c,L,t,9000,6000,1e-5,1e-5,2000,51475,30e6,0.3,L,B,a,b,c,phi)

UC_a = round(corr_panel_a.UC_buckling_state_limit(),3)
UC_b = round(corr_panel_b.UC_buckling_state_limit(),3)
UC_c = round(corr_panel_c.UC_buckling_state_limit(),3) 

st.write(f"UC Panel c = {UC_a}")
st.write(f"UC Panel b = {UC_b}")
st.write(f"UC Panel c = {UC_c}")
