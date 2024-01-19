from math import exp as EXP, pi, pow as POW, sqrt as SQRT

G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1


def GEOSTATIONAIR(astre):
    "renvois l'altitude geostationaire"
    return POW(G * astre.mss * astre.day**2 / pi / 4)


def VITESSE_ORBITAL(astre, radiale):
    "Pour le moment on suposera que tout orbite est parfaitement circulaire"
    return SQRT(G * astre.mss / radiale)


def VITESSE_LIBERATION(astre):
    "La vites nécessaire pour échapper au puits de gravité de l'astre donnée."
    return SQRT(2) * VITESSE_ORBITAL(astre, astre.dmtr / 2)


def GRAVITE(astre, altitude):
    return G * astre.mss / altitude**2


def HAUTEUR_ECHALLE(astre):
    "l'augmentation d'altitude pour laquelle la pression aslosphérique diminue d'un facteur expodentiel"
    return R * astre.klvn / astre.mol / GRAVITE(astre, astre.dmtr / 2)


def PRESSION(astre, altitude):
    "Pression atmospherique (Pa)"
    if altitude > astre.atm:
        "on sort de l'atmosphere"
        return 0
    else:
        return astre.prssn * EXP(-altitude / HAUTEUR_ECHALLE(astre))


def DENSITER(astre, altitude):
    return PRESSION(astre, altitude) / R / astre.klvn


def TRANSFERT(astre, radiale0, radiale1):
    "revois la vitesse pourle chegement d'orbite et le temps d'execution."
    r = radiale0 + radiale1
    return VITESSE_ORBITAL(astre, radiale0) * (
        SQRT(2 * radiale1 / r) - 1
    ) + VITESSE_ORBITAL(astre, radiale1) * (1 - SQRT(2 * radiale0 / r)), pi * SQRT(
        r / astre.mss / G / 8
    )
