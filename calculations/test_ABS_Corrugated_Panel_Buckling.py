import ABS_Corrugated_Panel_Buckling as ABScorr
import math

def test_calc_spc():
    assert math.isclose(ABScorr.calc_spc(24,28,18,45),77.45584412271572)
    assert math.isclose(ABScorr.calc_spc(24,24,12,52),62.7758754078158)
    
def test_calc_d():
    assert math.isclose(ABScorr.calc_d(18,45),12.727922061357857)
    assert math.isclose(ABScorr.calc_d(12,52),9.456129043280665)
    
def test_calc_tx():
    assert math.isclose(ABScorr.calc_tx(72,0.5,15),0.7083333333333334)
    assert math.isclose(ABScorr.calc_tx(80,0.75,15),0.9375)

def test_calc_A():
    assert math.isclose(ABScorr.calc_A(24,28,18,0.5),44.0)
    assert math.isclose(ABScorr.calc_A(24,24,12,0.75),54.0)
    
def test_calc_Asx():
    assert math.isclose(ABScorr.calc_Asx(18,0.5,45),12.727922061357857)
    assert math.isclose(ABScorr.calc_Asx(12,0.75,52),14.184193564920996)

def test_calc_z0():
    assert math.isclose(ABScorr.calc_z0(24,18,12,0.5,15),16.8)
    assert math.isclose(ABScorr.calc_z0(24,12,10,0.75,12),22.5)

def test_calc_Iy():
    assert math.isclose(ABScorr.calc_Iy(24,28,18,12,0.5,5,16.8),1181.341666666667)
    assert math.isclose(ABScorr.calc_Iy(24,24,12,10,0.75,4,22.5),376.6875)

def test_calc_SM():
    assert math.isclose(ABScorr.calc_SM(96,24,12),8.0)
    assert math.isclose(ABScorr.calc_SM(40,20,11),3.6363636363636362)

def test_calc_r():
    assert math.isclose(ABScorr.calc_r(8,2),2.0)
    assert math.isclose(ABScorr.calc_r(625,25),5.0)

def test_calc_kc():
    assert math.isclose(ABScorr.calc_kc(24,28,18),56.3062640625)
    assert math.isclose(ABScorr.calc_kc(24,24,18),56.3062640625)

def test_calc_sigma_EC():
    assert math.isclose(ABScorr.calc_sigma_EC(3e7,12,144),2056167.5835602828)
    assert math.isclose(ABScorr.calc_sigma_EC(3e7,24,100),17054676.40508241)

def test_calc_sigma_EB():
    assert math.isclose(ABScorr.calc_sigma_EB(5,0.5,24,28,3e7,0.3),4380.186140390222)
    assert math.isclose(ABScorr.calc_sigma_EB(4,0.75,24,24,3e7,0.3),10731.456043956045)

def test_calc_UC_unit_corr():
    assert math.isclose(ABScorr.calc_UC_unit_corr(10000,5000,25000,45000,50000,0.6),0.9444444444444444)
    assert math.isclose(ABScorr.calc_UC_unit_corr(12000,7000,25000,45000,50000,0.6),1.2320987654320987)

def test_calc_Dx():
    assert math.isclose(ABScorr.calc_Dx(100,80,3e7),37500000.0)
    assert math.isclose(ABScorr.calc_Dx(80,60,3e7),40000000.0)

def test_calc_Dy():
    assert math.isclose(ABScorr.calc_Dy(24,28,18,0.5,80,3e7,0.3),312187.8121878122)
    assert math.isclose(ABScorr.calc_Dy(24,24,12,0.75,60,3e7,0.3),965831.043956044)

def test_calc_phi_x():
    assert math.isclose(ABScorr.calc_phi_x(100,144,100000,5000),0.32838250312610273)
    assert math.isclose(ABScorr.calc_phi_x(100,144,200000,8000),0.31056499687497074)

def test_calc_phi_y():
    assert math.isclose(ABScorr.calc_phi_y(100,144,100000,5000),3.0452292387088247)
    assert math.isclose(ABScorr.calc_phi_y(100,144,200000,8000),3.219937887599697)

def test_calc_kx_cbhd():
    assert math.isclose(ABScorr.calc_kx_cbhd(100,192,10000,10000,2),4.0)
    assert math.isclose(ABScorr.calc_kx_cbhd(100,100/0.5176,10000,10000,2),4.0)
    assert math.isclose(ABScorr.calc_kx_cbhd(100,194,10000,10000,2),4.25)

def test_calc_ky_cbhd():
    assert math.isclose(ABScorr.calc_ky_cbhd(192,100,10000,10000,2),4.0)
    assert math.isclose(ABScorr.calc_ky_cbhd(100/0.5176,100,10000,10000,2),4.0)
    assert math.isclose(ABScorr.calc_ky_cbhd(194,100,10000,10000,2),4.25)

def test_calc_ks_cbhd():
    assert math.isclose(ABScorr.calc_ks_cbhd(),3.65)

def test_calc_sigma_Ex_cbhd():
    assert math.isclose(ABScorr.calc_sigma_Ex_cbhd(4,10000,5000,0.75,144),17.949753599894237)
    assert math.isclose(ABScorr.calc_sigma_Ex_cbhd(4,10000,5000,0.75,100),37.220609064740685)    

def test_calc_sigma_Ey_cbhd():
    assert math.isclose(ABScorr.calc_sigma_Ey_cbhd(4,10000,5000,0.5,100),55.83091359711103)
    assert math.isclose(ABScorr.calc_sigma_Ey_cbhd(4,10000,5000,0.5,144),26.924630399841355)    

def test_calc_tau_E_cbhd():
    assert math.isclose(ABScorr.calc_tau_E_cbhd(4,10000,5000,0.5,100),66.3945196867866)
    assert math.isclose(ABScorr.calc_tau_E_cbhd(4,10000,5000,0.5,144),32.018962040309894)    

def test_calc_UC_cbhd():
    assert math.isclose(ABScorr.calc_UC_cbhd(10000,7500,5000,50000,30000,20000,0.6),0.45833333333333337)    
    assert math.isclose(ABScorr.calc_UC_cbhd(25000,7500,5000,50000,30000,20000,0.6),1.0416666666666667)
    assert math.isclose(ABScorr.calc_UC_cbhd(10000,7500,5000,50000,30000,20000,0.8),0.2578125)
    assert math.isclose(ABScorr.calc_UC_cbhd(25000,15000,10000,50000,30000,20000,0.8),1.171875)
    
lc = "NORMAL OPERATION"
# lc = "SEVERE STORM"
stf_type = "LOCAL PLATE OF CORRUGATED PANELS"

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

def test_panels():
# Checks for Panel a    
    assert math.isclose(panel_a.Dx_cbhd(),334694764.6104874)
    assert math.isclose(panel_a.Dy_cbhd(),846623.910741884)
    assert math.isclose(panel_a.phi_x_cbhd(),0.11213221654333758)
    assert math.isclose(panel_a.phi_y_cbhd(),8.918043634797085)
    assert math.isclose(panel_a.kx_cbhd(),79.54407590613171)
    assert math.isclose(panel_a.ky_cbhd(),4)
    assert math.isclose(panel_a.ks_cbhd(),3.65)
    assert math.isclose(panel_a.sigma_E_x_cbhd(),333191.4401694765)
    assert math.isclose(panel_a.sigma_E_y_cbhd(),99246.42796520483)
    assert math.isclose(panel_a.tau_E_cbhd(),403819.5636810955)
    assert math.isclose(panel_a.sigma_G_x_cbhd(),49566.42110710725)
    assert math.isclose(panel_a.sigma_G_y_cbhd(),45067.493321543516)
    assert math.isclose(panel_a.tau_G_cbhd(),29194.182420602425)
    assert math.isclose(panel_a.UC_cbhd(),0.2714718884572766)
    assert math.isclose(panel_a.UC_unit_c(),0.7751795348232511)
    assert math.isclose(panel_a.kc_unit_c(),56.767853086419755)
    assert math.isclose(panel_a.sigma_EC_unit_c(),360364.67417430255)
    assert math.isclose(panel_a.sigma_EB_unit_c(),353730.73849115527)
    assert math.isclose(panel_a.sigma_CA_unit_c(),49710.337158235394)
    assert math.isclose(panel_a.sigma_CB_unit_c(),49677.242325016654)
    assert math.isclose(panel_a.UC_unit_c(),0.7751795348232511)
# Checks for Panel b
    assert math.isclose(panel_b.Dx_cbhd(),334694764.6104874)
    assert math.isclose(panel_b.Dy_cbhd(),846623.910741884)
    assert math.isclose(panel_b.phi_x_cbhd(),0.11213221654333758)
    assert math.isclose(panel_b.phi_y_cbhd(),8.918043634797085)
    assert math.isclose(panel_b.kx_cbhd(),79.54407590613171)
    assert math.isclose(panel_b.ky_cbhd(),4)
    assert math.isclose(panel_b.ks_cbhd(),3.65)
    assert math.isclose(panel_b.sigma_E_x_cbhd(),333191.4401694765)
    assert math.isclose(panel_b.sigma_E_y_cbhd(),99246.42796520483)
    assert math.isclose(panel_b.tau_E_cbhd(),403819.5636810955)
    assert math.isclose(panel_b.sigma_G_x_cbhd(),49566.42110710725)
    assert math.isclose(panel_b.sigma_G_y_cbhd(),45067.493321543516)
    assert math.isclose(panel_b.tau_G_cbhd(),29194.182420602425)
    assert math.isclose(panel_b.UC_cbhd(),0.2714718884572766)
    assert math.isclose(panel_b.UC_unit_c(),0.7751795348232511)
    assert math.isclose(panel_b.kc_unit_c(),56.767853086419755)
    assert math.isclose(panel_b.sigma_EC_unit_c(),360364.67417430255)
    assert math.isclose(panel_b.sigma_EB_unit_c(),353730.73849115527)
    assert math.isclose(panel_b.sigma_CA_unit_c(),49710.337158235394)
    assert math.isclose(panel_b.sigma_CB_unit_c(),49677.242325016654)
    assert math.isclose(panel_b.UC_unit_c(),0.7751795348232511)
# Checks for Panel c   
    assert math.isclose(panel_c.Dx_cbhd(),334694764.6104874)
    assert math.isclose(panel_c.Dy_cbhd(),846623.910741884)
    assert math.isclose(panel_c.phi_x_cbhd(),0.11213221654333758)
    assert math.isclose(panel_c.phi_y_cbhd(),8.918043634797085)
    assert math.isclose(panel_c.kx_cbhd(),79.54407590613171)
    assert math.isclose(panel_c.ky_cbhd(),4)
    assert math.isclose(panel_c.ks_cbhd(),3.65)
    assert math.isclose(panel_c.sigma_E_x_cbhd(),333191.4401694765)
    assert math.isclose(panel_c.sigma_E_y_cbhd(),99246.42796520483)
    assert math.isclose(panel_c.tau_E_cbhd(),403819.5636810955)
    assert math.isclose(panel_c.sigma_G_x_cbhd(),49566.42110710725)
    assert math.isclose(panel_c.sigma_G_y_cbhd(),45067.493321543516)
    assert math.isclose(panel_c.tau_G_cbhd(),29194.182420602425)
    assert math.isclose(panel_c.UC_cbhd(),0.2714718884572766)
    assert math.isclose(panel_c.kc_unit_c(),56.767853086419755)
    assert math.isclose(panel_c.sigma_EC_unit_c(),360364.67417430255)
    assert math.isclose(panel_c.sigma_EB_unit_c(),353730.73849115527)
    assert math.isclose(panel_c.sigma_CA_unit_c(),49710.337158235394)
    assert math.isclose(panel_c.sigma_CB_unit_c(),49677.242325016654)
    assert math.isclose(panel_c.UC_unit_c(),0.7751795348232511)