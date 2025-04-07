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

# def test_calc_UC_unit_corr():

# def test_calc_Dx():

# def test_calc_Dy():

# def test_calc_phi_x():

# def test_calc_phi_y():

# def test_calc_kx_cbhd():

# def test_calc_ky_cbhd():

# def test_calc_ks_cbhd():

# def test_calc_sigma_Ex_cbhd():

# def test_calc_sigma_Ey_cbhd():

# def test_calc_tau_E_cbhd():

# def test_calc_UC_cbhd():
