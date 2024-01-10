from math import exp as EXP, log as LOG, sqrt as SQRT
from Donnees.conversion import PA_ATM

G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1


def VITESSE_ECHAPE(planete, altitude):
    "La vites nécessaire pour échapper au puits de gravité d'une planète donnée."
    return SQRT(2 * G * planete.mss / (planete.dmtr / 2 + altitude))


def GRAVITE(planete, altitude):
    return G * planete.mss / (planete.dmtr / 2 + altitude) ** 2


def HAUTEUR_ECHALLE(planete):
    "l'augmentation d'altitude pour laquelle la pression aslosphérique diminue d'un facteur expodentiel"
    return R * planete.klvn / planete.mol / GRAVITE(planete, 0)


def PRESSION(planete, altitude):
    "Pression atmospherique (Pa)"
    if altitude > planete.atm:
        "on sort de l'atmosphere"
        return 0
    else:
        return planete.prssn * EXP(-altitude / HAUTEUR_ECHALLE())


def DENSITER(planete, altitude):
    return PRESSION(altitude) / R / planete.klvn


def IMPULSION(fuse, altitude):
    "L'impulsion spécifique définit l'efficacité d'un moteur."
    return fuse.nmbr * fuse.mtr.isp_vac + PA_ATM(PRESSION(altitude)) * (
        fuse.mtr.isp_asl - fuse.mtr.isp_vac
    )


def VITESSE_DELTA(planete, fuse):
    return IMPULSION(fuse, 0) * GRAVITE(planete, 0) * LOG(fuse.kg_ttl / fuse.kg_vide)


def POUSSE(planete, fuse, altitude):
    "la poussée est la force exercée par l'accélération de gaz"
    return IMPULSION(fuse, altitude) * GRAVITE(planete, 0) * fuse.kg_d


def POUSSEE_POIDS(planete, fuse, altitude):
    "il définit la puissance des moteurs d'un engin par rapport à son propre poids."
    return fuse.nmbr * POUSSE(planete, fuse) / (fuse.mss * GRAVITE(planete, altitude))


def A(planete, fuse, altitude):
    return GRAVITE(altitude) * (POUSSEE_POIDS(planete, fuse, altitude) - 1)
