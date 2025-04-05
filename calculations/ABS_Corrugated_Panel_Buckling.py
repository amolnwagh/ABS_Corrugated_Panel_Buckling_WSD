import calculations.ABS_Plate_Buckling as ABS
from dataclasses import dataclass
from math import pi, sqrt, sin, cos, tan, radians

@dataclass
class Corr_Panel(ABS.Panel):
    L: float # Length of entire corrugated panel (in) 
    B: float # width of entire corrugated panel (in)
    a: float # width of flange panel "a" (in)
    b: float # width of flange panel "b" (in)
    c: float # inclined width of web panel "c" (in)
    phi: float # angle of web of corrugated panel with respect to flange (degrees)
    


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
    """calculates section property "tx" of the corrugated panel

    Args:
        spc (float): spacing of unit corrugation (in)
        t (float): thickness of plating (in)
        Asx (float): section property "Asx" of the corrugated panel (in^2)

    Returns:
        tx (float): section property "tx" of the corrugated panel
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


def calc_Asx(c:float ,t:float ,phi:float) -> float:
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


def calc_z0(a:float ,c:float ,d:float ,t:float ,A:float) -> float:
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


def calc_Iy(a,b,c,d,t,A,z0) -> float:
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


def calc_SM(Iy:float ,d:float ,z0:float) -> float:
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


def calc_r(Iy:float ,A:float) -> float:
    """Calculates radius of gyration of unit corrugation

    Args:
        Iy (float): moment of inertia of unit corrugation about its weak axis (in^4)
        A (float): Area of unit corrugation (in^2)

    Returns:
        r (float): Radius of gyration of unit corrugation (in)
    """
    r = (Iy/A)**0.5
    return r






   
    

    