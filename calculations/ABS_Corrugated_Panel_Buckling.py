import calculations.ABS_Plate_Buckling as ABS
from dataclasses import dataclass
from math import pi, sqrt, sin, cos, tan, radians

@dataclass
class Corr_Panel(ABS.Panel):
    """
    L: float # Length of entire corrugated panel (in) 
    B: float # width of entire corrugated panel (in)
    a: float # width of flange panel "a" (in)
    b: float # width of flange panel "b" (in)
    c: float # inclined width of web panel "c" (in)
    phi: float # angle of web of corrugated panel with respect to flange (degrees)
    sigma_a_unit_corr: float # maximum compressive stress in unit corrugation (psi)
    sigma_b_unit_corr: float # maximum bending compressive stress in unit corrugation due to hydrostatic pressure (psi)
    sigma_x_panel: float # calculated average compressive stress in the corrugation direction for entire corrugated panel (psi)
    sigma_y_panel: float # calculated average compressive stress in the transverse direction for entire corrugated panel (psi)
    tau_panel_panel: float # in-plane shear stress for entire corrugated panel (psi)
    """
    L: float # Length of entire corrugated panel (in) 
    B: float # width of entire corrugated panel (in)
    a: float # width of flange panel "a" (in)
    b: float # width of flange panel "b" (in)
    c: float # inclined width of web panel "c" (in)
    phi: float # angle of web of corrugated panel with respect to flange (degrees)
    sigma_a_unit_c: float # maximum compressive stress in unit corrugation (psi)
    sigma_b_unit_c: float # maximum bending compressive stress in unit corrugation due to hydrostatic pressure (psi)
    sigma_x_cbhd: float # calculated average compressive stress in the corrugation direction for entire corrugated panel (bulkhead) (psi)
    sigma_y_cbhd: float # calculated average compressive stress in the transverse direction for entire corrugated panel (bulkhead) (psi)
    tau_cbhd: float # in-plane shear stress for entire corrugated panel (bulkhead) (psi)

    def d(self):
        return calc_d(self.c, self.phi)    
    
    def spc_unit_c(self):
        return calc_spc(self.a, self.b, self.c, self.phi)
    
    def A_unit_c(self):
        return calc_A(self.a, self.b, self.c, self.t)
    
    def Asx_unit_c(self):
        return calc_Asx(self.c, self.t, self.phi)
    
    def tx_unit_c(self):
        return calc_tx(self.spc_unit_c(), self.t, self.Asx_unit_c())
    
    def z0_unit_c(self):
        return calc_z0(self.a, self.c, self.d(), self.t, self.A_unit_c())
    
    def Iy_unit_c(self):
        return calc_Iy(self.a, self.b, self.c, self.d(), self.t, self.A_unit_c(), self.z0_unit_c())
    
    def SM_unit_c(self):
        return calc_SM(self.Iy_unit_c(), self.d(), self.z0_unit_c())
    
    def r_unit_c(self):
        return calc_r(self.Iy_unit_c(), self.A_unit_c())
    
    def kc_unit_c(self):
        return calc_kc(self.a, self.b, self.c)
    
    def sigma_EC_unit_c(self):
        return calc_sigma_EC(self.E, self.r_unit_c(), self.L)
    
    def sigma_EB_unit_c(self):
        return calc_sigma_EB(self.kc_unit_c(), self.t, self.a, self.b, self.E, self.nu)
    
    def sigma_CA_unit_c(self):
        return ABS.calc_stress_C(self.sigma_0, self.sigma_EC_unit_c())
    
    def sigma_CB_unit_c(self):
        return ABS.calc_stress_C(self.sigma_0, self.sigma_EB_unit_c())
    
    def UC_unit_c(self):
        return calc_UC_unit_corr(
            self.sigma_a_unit_c,
            self.sigma_b_unit_c,
            self.sigma_CA_unit_c,
            self.sigma_CB_unit_c,
            self.sigma_EC_unit_c,
            self.eta()
        )
        

#+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---

    
def calc_spc(a:float, b:float, c:float, phi:float) -> float:
    """calculates spacing of unit corrugation

    Args:
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        c (float): inclined width of web panel "c" (in)
        phi (float): angle of web of corrugated panel with respect to flange (degrees)

    Returns:
        spc (float): spacing of unit corrugation (in)
    """  
    spc = a + b + 2*c*cos(radians(phi))
    return spc


def calc_d(c:float, phi:float) -> float:
    """calculates dimension "d" of the corrugated panel

    Args:
        c (float): inclined width of web panel "c" (in)
        phi (float): angle of web of corrugated panel with respect to flange (degrees)

    Returns:
        d (float): dimension "d" of the corrugated panel (in)
    """
    d = c*sin(radians(phi))
    return d


def calc_tx(spc:float, t:float, Asx:float) -> float:
    """Calculates equivalent thickness of the corrugation in the corrugation direction

    Args:
        spc (float): spacing of unit corrugation (in)
        t (float): thickness of plating (in)
        Asx (float): section property "Asx" of the corrugated panel (in^2)

    Returns:
        tx (float): equivalent thickness of the corrugation in the corrugation direction (in)
    """
    tx = (spc*t + Asx)/spc
    return tx


def calc_A(a:float, b:float, c:float, t: float) -> float:
    """Calculates Area of unit corrugation

    Args:
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        c (float): inclined width of web panel "c" (in)
        t (float): thickness of plating (in)

    Returns:
        A (float): Area of unit corrugation (in^2)
    """
    A = (a+b+2*c)*t
    return A


def calc_Asx(c:float, t:float, phi:float) -> float:
    """calculates section property "Asx" of the corrugated panel

    Args:
        c (float): inclined width of web panel "c" (in)
        t (float): thickness of plating (in)
        phi (float): angle of web of corrugated panel with respect to flange (degrees)

    Returns:
        Asx (float): section property "tx" of the corrugated panel (in^2)
    """
    Asx = 2*c*t*sin(radians(phi))
    return Asx


def calc_z0(a:float, c:float, d:float, t:float, A:float) -> float:
    """Calculates centroidal distance of the corrugated panel about its weak axis

    Args:
        a (float): width of flange panel "a" (in)
        c (float): inclined width of web panel "c" (in)
        d (float): dimension "d" of the corrugated panel (in)
        t (float): thickness of plating (in)
        A (float): Area of unit corrugation (in^2)

    Returns:
        z0 (float): centroidal distance of the corrugated panel about its weak axis (in)
    """
    z0 = d*t*(a+c)/A
    return z0


def calc_Iy(a:float, b:float, c:float, d:float, t:float, A:float, z0:float)  -> float:
    """Calculates moment of inertia of unit corrugation about its weak axis

    Args:
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        c (float): inclined width of web panel "c" (in)
        d (float): dimension "d" of the corrugated panel (in)
        t (float): thickness of plating (in)
        A (float): Area of unit corrugation (in^2)
        z0 (_type_): centroidal distance of the corrugated panel about its weak axis (in)

    Returns:
        Iy (float): moment of inertia of unit corrugation about its weak axis (in^4)
    """
    Iy = (a+b)*(t**3)/12 + a*(d**2)*t + (2/3)*c*(d**2)*t - A*(z0**2)
    return Iy


def calc_SM(Iy:float, d:float, z0:float) -> float:
    """Calculates section modulus of unit corrugation about its weak axis

    Args:
        Iy (float): moment of inertia of unit corrugation about its weak axis (in^4)
        d (float): dimension "d" of the corrugated panel (in)
        z0 (float): centroidal distance of the corrugated panel about its weak axis (in)

    Returns:
        SM (float): section modulus of unit corrugation about its weak axis (in^3)
    """
    SM = min(Iy/z0, Iy/(d-z0))
    return SM


def calc_r(Iy:float, A:float) -> float:
    """Calculates radius of gyration of unit corrugation

    Args:
        Iy (float): moment of inertia of unit corrugation about its weak axis (in^4)
        A (float): Area of unit corrugation (in^2)

    Returns:
        r (float): Radius of gyration of unit corrugation (in)
    """
    r = (Iy/A)**0.5
    return r


def calc_kc(a:float, b:float, c:float) -> float:
    """calculates coefficient "kc" for unit corrugation

    Args:
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        c (float): inclined width of web panel "c" (in)

    Returns:
        kc (float): coefficient "kc" for unit corrugation
    """
    kc = (7.65 - 0.26*(c/min(a,b))**2)**2
    return kc


def calc_sigma_EC(E:float, r:float, L:float) -> float:
    """Calculates elastic buckling stress for unit corrugation (psi)

    Args:
        E (float): modulus of elasticity (psi)
        r (float): Radius of gyration of unit corrugation (in)
        L (float): Length (height of bulkhead) of entire corrugated panel (in)

    Returns:
        sigma_EC (float): Elastic buckling stress for unit corrugation (psi)
    """

    sigma_EC = (pi**2)*E*(r**2)/(L**2)
    return sigma_EC


def calc_sigma_EB(kc:float, t:float, a:float, b:float, E:float=30.0e6, nu:float=0.3) -> float:
    """Calculates Elastic buckling stress of unit corrugation

    Args:
        kc (float): coefficient "kc" for unit corrugation
        t (float): thickness of plating (in)
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        E (float,optional): modulus of elasticity. Defaults to 30.0e6, psi.
        nu (float,optional): Poisson's ratio. Defaults to 0.3 for steel.

    Returns:
        sigma_EB (float): Elastic buckling stress of unit corrugation (psi)
    """
    bf = max(a,b)
    sigma_EB = ABS.calc_stress_E(kc,t,bf,E,nu)
    return sigma_EB


def calc_UC_unit_corr(sigma_a:float, sigma_b:float, sigma_CA:float, sigma_CB:float, sigma_EC:float, eta:float) -> float:
    """Calculates Utilization ratio for beam-column buckling of unit corrugation under 
    compressive stress and lateral hydrostatic pressure

    Args:
        sigma_a (float): maximum compressive stress in unit corrugation (psi)
        sigma_b (float): maximum bending compressive stress in unit corrugation due to hydrostatic pressure (psi)
        sigma_CA (float): critical buckling stress for unit corrugation (psi)
        sigma_CB (float): critical bending buckling stress for unit corrugation (psi)
        sigma_EC (float): Elastic buckling stress for unit corrugation (psi)
        eta (float): maximum allowable strength factor, eta

    Returns:
        UC_unit_corr (float): Unity Check ratio for beam-column buckling of unit corrugation 
        under compressive stress and lateral hydrostatic pressure
    """
    Cm = 1.0 # Bending moment factor considered for bensing stresses taken directly from Finite ELement Analysis
    UC_unit_corr = (sigma_a/(eta*sigma_CA)) + ((Cm*sigma_b)/(eta*sigma_CB*(1-(sigma_a/(eta*sigma_EC)))))
    return UC_unit_corr


def calc_Dx(Iy:float, spc:float, E:float = 30.0e6) -> float:
    """Calculates Dx

    Args:
        Iy (float): moment of inertia of unit corrugation about its weak axis (in^4)
        spc (float): spacing of unit corrugation (in)
        E (float,optional): modulus of elasticity. Defaults to 30.0e6, psi.

    Returns:
        Dx (float)
    """
    Dx = E*Iy/spc
    return Dx


def calc_Dy(a:float, b:float, c:float, t:float, spc:float, E:float, nu:float) -> float:
    """Calculates Dy

    Args:
        a (float): width of flange panel "a" (in)
        b (float): width of flange panel "b" (in)
        c (float): inclined width of web panel "c" (in)
        t (float): thickness of plating (in)
        spc (float): spacing of unit corrugation (in)
        E (float,optional): modulus of elasticity. Defaults to 30.0e6, psi.
        nu (float, optional): Poisson's ratio. Defaults to 0.3 for steel.

    Returns:
        Dy (float)
    """
    Dy = ((E*(t**3))/(12*(1-(nu**2))))*(spc/(a+b+2*c))
    return Dy


def calc_phi_x(L:float, B:float, Dx:float, Dy:float) -> float:
    """Calculates phi_x

    Args:
        L (float): Length of entire corrugated panel (bulkhead) (in) 
        B (float): Width of entire corrugated panel (bulkhead) (in)
        Dx (float)
        Dy (float)
    
    Returns:
        phi_x (float)
    """
    phi_x = (L/B) * (Dy/Dx)**(1/4)
    return phi_x


def calc_phi_y(L:float, B:float, Dx:float, Dy:float) -> float:
    """Calculates phi_y

    Args:
        L (float): Length of entire corrugated panel (bulkhead) (in) 
        B (float): Width of entire corrugated panel (bulkhead) (in)
        Dx (float)
        Dy (float)
    
    Returns:
        phi_y (float)
    """
    phi_y = (B/L) * (Dx/Dy)**(1/4)
    return phi_y


def calc_kx_cbhd(L:float, B:float, Dx:float, Dy:float, phi_x:float) -> float:
    """Calculates kx for entire corrugated bulkhead

    Args:
        L (float): Length of entire corrugated panel (bulkhead) (in) 
        B (float): Width of entire corrugated panel (bulkhead) (in)
        Dx (float)
        Dy (float)
        phi_x (float)
    
    Returns:
        kx_cbhd (float): kx for entire corrugated bulkhead
    """
    if (L/B) >= 0.5176 * (Dx/Dy)**(1/4):
        kx_cbhd = 4
    else:
        kx_cbhd = (1/(phi_x**2)) + phi_x**2  
    return kx_cbhd


def calc_ky_cbhd(L:float, B:float, Dx:float, Dy:float, phi_y:float) -> float:
    """Calculates ky for entire corrugated bulkhead

    Args:
        L (float): Length of entire corrugated panel (bulkhead) (in) 
        B (float): Width of entire corrugated panel (bulkhead) (in)
        Dx (float)
        Dy (float)
        phi_y (float)
    
    Returns:
        kx_cbhd (float): ky for entire corrugated bulkhead
    """
    if (B/L) >= 0.5176 * (Dy/Dx)**(1/4):
        ky_cbhd = 4
    else:
        ky_cbhd = (1/(phi_y**2)) + phi_y**2    
    return ky_cbhd


def calc_ks_cbhd() -> float:
    """Calculates ks for entire corrugated bulkhead

    Returns:
        ks (float): A constant value
    """
    ks_cbhd = 3.65
    return ks_cbhd

def calc_sigma_Ex_cbhd(kx:float, Dx:float, Dy:float, tx:float, B:float) -> float:
    """Calculates elastic buckling stress in the corrugation direction for entire corrugated panel (bulkhead)

    Args:
        kx (float)
        Dx (float)
        Dy (float)
        tx (float): equivalent thickness of the corrugation in the corrugation direction (in)
        B (float): Width of entire corrugated panel (bulkhead) (in)

    Returns:
        float: elastic buckling stress in the corrugation direction for entire corrugated panel (bulkhead) (psi)
    """
    sigma_Ex_cbhd = kx * (pi**2) * (Dx*Dy)**(1/2) / (tx*(B**2))
    return sigma_Ex_cbhd

def calc_sigma_Ey_cbhd(ky:float, Dx:float, Dy:float, t:float, L:float) -> float:
    """Calculates elastic buckling stress in the transverse direction for entire corrugated panel (bulkhead)

    Args:
        ky (float)
        Dx (float)
        Dy (float)
        t (float): thickness of plating (in)
        B (float): Length of entire corrugated panel (bulkhead) (in)

    Returns:
        float: elastic buckling stress in the transverse direction for entire corrugated panel (bulkhead) (psi)
    """
    sigma_Ey_cbhd = ky * (pi**2) * (Dx*Dy)**(1/2) / (t*(L**2))
    return sigma_Ey_cbhd

def calc_tau_E_cbhd(ks:float, Dx:float, Dy:float, t:float, L:float) -> float:
    """Calculates elastic shear buckling stress for entire corrugated panel (bulkhead)

    Args:
        ks (float)
        Dx (float)
        Dy (float)
        t (float): thickness of plating (in)
        B (float): Length of entire corrugated panel (bulkhead) (in)

    Returns:
        float: elastic shear buckling stress for entire corrugated panel (bulkhead) (psi)
    """
    tau_E_cbhd = ks * (pi**2) * (Dx**(3/4))*(Dy**(1/4)) / (t*(L**2))
    return tau_E_cbhd

def calc_UC_cbhd(sigma_x: float, sigma_y: float, tau: float, sigma_Gx: float, sigma_Gy: float, tau_G: float, eta: float) -> float:
    """_summary_

    Args:
        sigma_x (float): calculated average compressive stress in the corrugation direction for entire corrugated panel (bulkhead) (psi)
        sigma_y (float): calculated average compressive stress in the transverse direction for entire corrugated panel (bulkhead) (psi)
        tau (float): in-plane shear stress for entire corrugated panel (bulkhead) (psi)
        sigma_Gx (float): critical buckling stress for uniaxial compression in the corrugation direction (psi)
        sigma_Gy (float): critical buckling stress for uniaxial compression in the transverse direction (psi)
        tau_G (float): critical buckling stress for shear stress (psi)
        eta (float): maximum allowable strength factor, eta
    
    Returns:
        UC_cbhd (float): Unity check ratio for entire corrugated panel (bulkhead)
    """
    UC_cbhd = (sigma_x/(eta*sigma_Gx))**2 + (sigma_y/(eta*sigma_Gy))**2 + (tau/(eta*tau_G))**2
    return UC_cbhd


    

    



   
    

    