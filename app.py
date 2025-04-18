import streamlit as st
import calculations.ABS_Plate_Buckling as ABS
import calculations.ABS_Corrugated_Panel_Buckling as ABScorr

st.download_button(
    label="Download Sample CSV File",
    data= open("sample_csv\sample.csv","r"),
    file_name="sample_input_data.csv",
    mime="text/csv",
)

stf_type = "LOCAL PLATE OF CORRUGATED PANELS"

lc = st.selectbox("Select type of load case",["NORMAL OPERATION","SEVERE STORM"])

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

