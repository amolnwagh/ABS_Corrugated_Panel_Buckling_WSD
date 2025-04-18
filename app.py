import streamlit as st
import calculations.ABS_Plate_Buckling as ABS
import calculations.ABS_Corrugated_Panel_Buckling as ABScorr
import pandas as pd
import calculations.utils as utils

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
st.image(r"figures/corrugated_panel_dimensions.jpg","Figure 3: Typical Dimensions of a Corrugated Bulkhead Panel")
st.divider()


st.markdown("#### Step 1: Download the sample CSV file for input template.")
st.download_button(
    label="Download Sample CSV File",
    data= open("sample_csv/sample.csv","r"),
    file_name="sample.csv",
    mime="text/csv",
)

st.divider()

 
stf_type = "LOCAL PLATE OF CORRUGATED PANELS"
st.markdown("#### Step 2: Select the Load Case Type from the dropdown below.")
lc = st.selectbox("Select type of load case",["NORMAL OPERATION","SEVERE STORM"])

st.markdown("#### Step 3: Update the downloaded sample CSV file in Excel or any Text Editor with your data and upload the updated file here.")
st.markdown("Note: Once the updated file is uploaded, the data in the uploaded file will be shown in tabulated format below.")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    df=df.astype(float)
    st.dataframe(df)
else:
    st.markdown("#### Note: Step 4 and Step 5 will be activated once input file is uploaded.")
    st.divider()

if uploaded_file is not None:

    csv_file = df.to_csv("input.csv",index=False)
    csv_list = utils.read_csv_file("input.csv")
    num_data = []
    for lst in csv_list:
        num_lst = []
        for inner_item in lst:
            num_lst.append(utils.str_to_float(inner_item))
        num_data.append(num_lst)

    # st.write(num_data)
        
    new_col_heads = [
    "panel_a_UC_buckling_state_limit",
    "panel_b_UC_buckling_state_limit",
    "panel_c_UC_buckling_state_limit",
    "sigma_EC_unit_c",
    "sigma_EB_unit_c",
    "sigma_CA_unit_c",
    "sigma_CB_unit_c",
    "UC_unit_c",
    "sigma_E_x_cbhd",
    "sigma_E_y_cbhd",
    "tau_E_cbhd",
    "sigma_G_x_cbhd",
    "sigma_G_y_cbhd",
    "tau_G_cbhd",
    "UC_cbhd",]

    cols = num_data[0] + new_col_heads

    calculated_data = []
    for lst in num_data[1:]:

        L = lst[0]
        B = lst[1]
        a = lst[2]
        b = lst[3]
        c = lst[4]
        t = lst[5]
        phi = lst[6]
        sigma_0 = lst[7]
        E = lst[8]
        nu = lst[9]
        
        sigma_ax_a = lst[10]
        sigma_ay_a = lst[11]
        sigma_bx_a = lst[12]
        sigma_by_a = lst[13]
        tau_a = lst[14]
        
        sigma_ax_b = lst[15]
        sigma_ay_b = lst[16]
        sigma_bx_b = lst[17]
        sigma_by_b = lst[18]
        tau_b = lst[19]
        
        sigma_ax_c = lst[20]
        sigma_ay_c = lst[21]
        sigma_bx_c = lst[22]
        sigma_by_c = lst[23]
        tau_c = lst[24]
        
        sigma_a_unit_c = lst[25]
        sigma_b_unit_c = lst[26]
        
        sigma_x_cbhd = lst[27]
        sigma_y_cbhd = lst[28]
        tau_cbhd = lst[29]
        
        panel_a = ABScorr.Corr_Panel(
                                    lc,
                                    stf_type,
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
                                    tau_cbhd
                                    )

        panel_b = ABScorr.Corr_Panel(
                                    lc,
                                    stf_type,
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
                                    tau_cbhd
                                    )

        panel_c = ABScorr.Corr_Panel(
                                    lc,
                                    stf_type,
                                    c,
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
                                    tau_cbhd
                                    )
        
        # st.write(panel_a)
        
        new_cols = [
            panel_a.UC_buckling_state_limit(),
            panel_b.UC_buckling_state_limit(),
            panel_c.UC_buckling_state_limit(),
            panel_a.sigma_EC_unit_c(),
            panel_a.sigma_EB_unit_c(),
            panel_a.sigma_CA_unit_c(),
            panel_a.sigma_CB_unit_c(),
            panel_a.UC_unit_c(),
            panel_a.sigma_E_x_cbhd(),
            panel_a.sigma_E_y_cbhd(),
            panel_a.tau_E_cbhd(),
            panel_a.sigma_G_x_cbhd(),
            panel_a.sigma_G_y_cbhd(),
            panel_a.tau_G_cbhd(),
            panel_a.UC_cbhd(),   
        ]
        lst_updt = lst + new_cols
        calculated_data.append(lst_updt)
            

    st.divider()

    st.markdown("#### Step 4: Review the Buckling Checks in Tabulated Format below.")
    results_df = pd.DataFrame(calculated_data,columns=cols)
    st.dataframe(results_df)

    st.divider()

    st.markdown("#### Step 5: Download the Results in Table (CSV) format using download button below.")
    st.download_button(
        label="Download Results CSV File",
        data= results_df.to_csv(index=False).encode("utf-8"),
        file_name="Results.csv",
        mime="text/csv",
    )

    st.divider()

