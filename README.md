# ABS_Corrugated_Panel_Buckling_WSD

#### Calculations for corrugated panel buckling checks according to "Requirements for Buckling and Ultimate Strength Assessment for Offshore Structures (Working Stress Method)", published by American Bureau of Shipping (ABS), July 2022 Edition

* Link to ABS Buckling Requirements: https://pub-rm20.apps.eagle.org/r/4/2022-07-01/Buckling-and-Ultimate-Strength-Assessment-for-Offshore-Structures"
* This app calculates the buckling state limit of corrugated bulkhead panel as per Section 3 of the ABS reference as mentioned above.
* Such corrugated panels are typically used in hulls of ships and floating offshore structures like jack-up rigs and semi-submersibles, especially as vertical bounding walls of mud tanks.
* Generally, the inputs are details regarding corrugated panel dimensions and material properties.
* Instead of loads, the inputs are stresses, since these buckling check calculations are used typically after extracting stresses from a detailed finite element analysis model of the mentioned structures.
* Once you enter the stresses, the app gives buckling state limit (UC) checks at individual web and flange panel levels, unit corrugation (beam-column) level, as well as entire corrugated panel level checks. Thus, this is a complete buckling check for the corrugated bulkheads as per ABS Buckling Rules.
* Input is given by uploading a `.csv` file. A downloadable sample `.csv` file is also provided with the app. The calculations are populated in a `DataFrame` format and can be downloaded as a `.csv` file.
"* Input units are Imperial - 'inches' for length, 'degree' for angles and 'psi' for stress."

Streamlit app link: https://abs-corrugated-panel-buckling-wsd.streamlit.app/