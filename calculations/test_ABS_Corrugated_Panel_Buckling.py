import ABS_Corrugated_Panel_Buckling as ABScorr
import math

def test_calc_spc():
    assert math.isclose(ABScorr.calc_spc(24,28,18,45),77.45584412271572)
    assert math.isclose(ABScorr.calc_spc(24,24,12,52),62.7758754078158)
    
def test_calc_d():
    assert math.isclose(ABScorr.calc_d(18,45),12.727922061357857)
    assert math.isclose(ABScorr.calc_d(12,52),9.456129043280665)
    
def calc_tx():
    assert math.isclose(ABScorr.calc_tx(72,0.5,15),0.7083333333333334)
    assert math.isclose(ABScorr.calc_tx(80,0.75,15),0.9375)

def calc_A():
    assert math.isclose(ABScorr.calc_A(24,28,18,0.5),44.0)
    assert math.isclose(ABScorr.calc_A(24,24,12,0.75),54.0)


# def calc_Asx(c:float, t:float, phi:float) -> float:


# def calc_z0(a:float, c:float, d:float, t:float, A:float) -> float:


# def calc_Iy(a:float, b:float, c:float, d:float, t:float, A:float, z0:float)  -> float:


# def calc_SM(Iy:float, d:float, z0:float) -> float:


# def calc_r(Iy:float, A:float) -> float:


# def calc_kc(a:float, b:float, c:float) -> float:


# def calc_sigma_EC(E:float, r:float, L:float) -> float:


# def calc_sigma_EB(kc:float, t:float, a:float, b:float, E:float=30.0e6, nu:float=0.3) -> float:


# def calc_UC_unit_corr(sigma_a:float, sigma_b:float, sigma_CA:float, sigma_CB:float, sigma_EC:float, eta:float) -> float:


# def calc_Dx(Iy:float, spc:float, E:float = 30.0e6) -> float:


# def calc_Dy(a:float, b:float, c:float, t:float, spc:float, E:float, nu:float) -> float:


# def calc_phi_x(L:float, B:float, Dx:float, Dy:float) -> float:


# def calc_phi_y(L:float, B:float, Dx:float, Dy:float) -> float:


# def calc_kx_cbhd(L:float, B:float, Dx:float, Dy:float, phi_x:float) -> float:


# def calc_ky_cbhd(L:float, B:float, Dx:float, Dy:float, phi_y:float) -> float:


# def calc_ks_cbhd() -> float:


# def calc_sigma_Ex_cbhd(kx:float, Dx:float, Dy:float, tx:float, B:float) -> float:


# def calc_sigma_Ey_cbhd(ky:float, Dx:float, Dy:float, t:float, L:float) -> float:


# def calc_tau_E_cbhd(ks:float, Dx:float, Dy:float, t:float, L:float) -> float:


# def calc_UC_cbhd(sigma_x: float, sigma_y: float, tau: float, sigma_Gx: float, sigma_Gy: float, tau_G: float, eta: float) -> float:
