import streamlit as st
import calculations.ABS_Plate_Buckling as ABS
import calculations.ABS_Corrugated_Panel_Buckling as ABScorr
from io import StringIO
import pandas as pd

st.markdown("# ABS Corrugated Bulkhead Buckling Checks")
st.markdown("### (WSD Method) - *July 2022 Edition*")
st.markdown("#### Readme")
st.markdown("* Link to ABS Buckling Requirements: https://pub-rm20.apps.eagle.org/r/4/2022-07-01/Buckling-and-Ultimate-Strength-Assessment-for-Offshore-Structures")
st.markdown("* This app calculates the buckling state limit of corrugated bulkhead panel as per Section 3 of the ABS reference as mentioned above.")
st.markdown("* Such corrugated panels are typically used in hulls of ships and floating offshore structures like jack-up rigs and semi-submersibles, especially as vertical bounding walls of mud tanks.")
st.markdown("* Generally, the inputs are details regarding corrugated panel dimensions and material properties.")
st.markdown("* Instead of loads, the inputs are stresses, since these buckling check calculations are used typically after extracting stresses from a detailed finite element analysis model of the mentioned structures.")
st.markdown("* Once you enter the stresses, the app gives buckling state limit (UC) checks at individual web and flange panel levels, unit corrugation (beam-column) level, as well as entire corrugated panel level checks. Thus, this is a complete buckling check for the corrugated bulkheads as per ABS Buckling Rules.")
st.markdown("* Input is given by uploading a `.csv` file. A downloadable sample `.csv` file is also provided with the app. The calculations are populated in a `DataFrame` format and can be downloaded as a `.csv` file.")

st.divider()

st.image(r"figures/typ_stiffened_panel.png","Figure 1: Typical Stiffened Panel")
st.divider()

st.image(r"figures/loads_on_panel.png","Figure 2: Typical Loads on a Stiffened Panel")
st.divider()


st.download_button(
    label="Download Sample CSV File",
    data= open("sample_csv\sample.csv","r"),
    file_name="sample_input_data.csv",
    mime="text/csv",
)

st.divider()

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    df=df.astype(float)
    st.dataframe(df,    )

st.divider()
    
stf_type = "LOCAL PLATE OF CORRUGATED PANELS"
lc = st.selectbox("Select type of load case",["NORMAL OPERATION","SEVERE STORM"])

st.divider()


L = 94.488
B = 188.976
a = 11.811
b = 15.748
c = 7.874
t = 0.750
phi = 75
sigma_0 = 51475
E = 30e6
nu = 0.3

sigma_ax_a = 11000
sigma_ay_a = 8000
sigma_bx_a = 1e-5
sigma_by_a = 1e-5
tau_a = 4000

sigma_ax_b = 10000
sigma_ay_b = 7000
sigma_bx_b = 1e-5
sigma_by_b = 1e-5
tau_b = 3000

sigma_ax_c = 9000
sigma_ay_c = 6000
sigma_bx_c = 1e-5
sigma_by_c = 1e-5
tau_c = 2000

sigma_a_unit_c = 12500
sigma_b_unit_c = 10000

sigma_x_cbhd = 10000
sigma_y_cbhd = 7500
tau_cbhd = 5000
    
panel_a = ABScorr.Corr_Panel(lc,stf_type,
                                  a,
                                  L,
                                  t,
                                  sigma_ax_a,
                                  sigma_ay_a,
                                  sigma_bx_a,
                                  sigma_by_a,
                                  tau_a,
                                  sigma_0,
                                  E,
                                  nu,
                                  L,
                                  B,
                                  a,
                                  b,
                                  c,
                                  phi,
                                  sigma_a_unit_c,
                                  sigma_b_unit_c,
                                  sigma_x_cbhd,
                                  sigma_y_cbhd,
                                  tau_cbhd)

panel_b = ABScorr.Corr_Panel(lc,stf_type,
                                  b,
                                  L,
                                  t,
                                  sigma_ax_b,
                                  sigma_ay_b,
                                  sigma_bx_b,
                                  sigma_by_b,
                                  tau_b,
                                  sigma_0,
                                  E,
                                  nu,
                                  L,
                                  B,
                                  a,
                                  b,
                                  c,
                                  phi,
                                  sigma_a_unit_c,
                                  sigma_b_unit_c,
                                  sigma_x_cbhd,
                                  sigma_y_cbhd,
                                  tau_cbhd)

panel_c = ABScorr.Corr_Panel(lc,stf_type,
                                  a,
                                  L,
                                  t,
                                  sigma_ax_c,
                                  sigma_ay_c,
                                  sigma_bx_c,
                                  sigma_by_c,
                                  tau_c,
                                  sigma_0,
                                  E,
                                  nu,
                                  L,
                                  B,
                                  a,
                                  b,
                                  c,
                                  phi,
                                  sigma_a_unit_c,
                                  sigma_b_unit_c,
                                  sigma_x_cbhd,
                                  sigma_y_cbhd,
                                  tau_cbhd)



st.write(f"Checks for Panel A:\n"
f"{panel_a.UC_cbhd()=}\n"
f"{panel_a.Dx_cbhd()=}\n"
f"{panel_a.Dy_cbhd()=}\n"
f"{panel_a.phi_x_cbhd()=}\n"
f"{panel_a.phi_y_cbhd()=}\n"
f"{panel_a.kx_cbhd()=}\n"
f"{panel_a.ky_cbhd()=}\n"
f"{panel_a.ks_cbhd()=}\n"
f"{panel_a.sigma_E_x_cbhd()=}\n"
f"{panel_a.sigma_E_y_cbhd()=}\n"
f"{panel_a.tau_E_cbhd()=}\n"
f"{panel_a.sigma_G_x_cbhd()=}\n"
f"{panel_a.sigma_G_y_cbhd()=}\n"
f"{panel_a.tau_G_cbhd()=}\n"
f"{panel_a.UC_cbhd()=}\n"
)

st.write(f"Checks for Panel B:\n"
f"{panel_b.UC_cbhd()=}\n"
f"{panel_b.Dx_cbhd()=}\n"
f"{panel_b.Dy_cbhd()=}\n"
f"{panel_b.phi_x_cbhd()=}\n"
f"{panel_b.phi_y_cbhd()=}\n"
f"{panel_b.kx_cbhd()=}\n"
f"{panel_b.ky_cbhd()=}\n"
f"{panel_b.ks_cbhd()=}\n"
f"{panel_b.sigma_E_x_cbhd()=}\n"
f"{panel_b.sigma_E_y_cbhd()=}\n"
f"{panel_b.tau_E_cbhd()=}\n"
f"{panel_b.sigma_G_x_cbhd()=}\n"
f"{panel_b.sigma_G_y_cbhd()=}\n"
f"{panel_b.tau_G_cbhd()=}\n"
f"{panel_b.UC_cbhd()=}\n"
)

st.write(f"Checks for Panel C:\n"
f"{panel_c.UC_cbhd()=}\n"
f"{panel_c.Dx_cbhd()=}\n"
f"{panel_c.Dy_cbhd()=}\n"
f"{panel_c.phi_x_cbhd()=}\n"
f"{panel_c.phi_y_cbhd()=}\n"
f"{panel_c.kx_cbhd()=}\n"
f"{panel_c.ky_cbhd()=}\n"
f"{panel_c.ks_cbhd()=}\n"
f"{panel_c.sigma_E_x_cbhd()=}\n"
f"{panel_c.sigma_E_y_cbhd()=}\n"
f"{panel_c.tau_E_cbhd()=}\n"
f"{panel_c.sigma_G_x_cbhd()=}\n"
f"{panel_c.sigma_G_y_cbhd()=}\n"
f"{panel_c.tau_G_cbhd()=}\n"
f"{panel_c.UC_cbhd()=}\n"
)

