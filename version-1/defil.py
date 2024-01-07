# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:04:24 2022

@author: HP TG01
"""


G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

rayon = 1  # m
day = 2  # s
kelvin_0 = 3  # K
masse_moyen_mol = 4  # kg.mol-1
pression_pa_0 = 5  # kg⋅m −1⋅s −2
atm_limit = 6  # m
planet = [5.2915158e22, 6e+5, 21600, 288.15, 0.0289644, 101325, 70000, 'kerbin']

masse = 0  # kg
nom = -1
tail = -2  # m
haut = -3  # m
cout = -4
chut = [[ 75, 150, 0    , 0  , 'mk12-r'],
        [100, 422, 0.631, 0.6, 'mk16']]
what_d = 1
bodyne =[ 50, 1.7/60, 300, 1, 0.6, 'staysputnick']
pods = [800, 0.2, 635, 1.1, 1.3, 'mk1']
control = [50, 0.3, 600, 0.628, 0.6, 'SAS']
comm = [5, 20, 300, 0, 0, '16']
what = 1
elect = [5, 100, 80, 0, 0, 'z-100']
stack = [[ 10, 150, 0.625, 0.6, 'td-06'],
         [ 40, 200, 0    , 1.3, 'td-12'],
         [160, 300, 1    , 2.5, 'td-25'],
         [360, 375, 1    , 3.8, 'td-37']]
radial = [[ 25, 600, 0, 0, 'tt-38'],
          [ 50, 700, 0, 0, 'tt-70'],
          [400, 770, 0, 0, 'hdm']]
coupling = [stack, radial]

ergol = 1  # u.s-1
oxidizer = 2  # u.s-1
multipl = 3
tanks = [[  25  ,   18,   22, 0,  52  , 0.625, 0.6, 'oscar-b'],
         [  62.5,   45,   55, 8,  54.1, 0.5  , 1.3, 'fl'],
         [ 500  ,  360,  440, 8, 351.5, 1    , 2.5, 'x200'],
         [2250  , 1620, 1980, 3, 347.5, 2.665, 3.8, 's3']]

solid = 3
ergol_d = 4  # u.s-1
oxidizer_d = 5  # u.s-1
solid_d = 6
pousse_asl = 7  # kg.m.s-2
pousse_vac = 8  # kg.m.s-2
isp_asl = 9  # s
isp_vac = 10  # s
typ = 11
reacteurs = [[   75  , 0, 0,    40,   0    ,  0    ,   0.809,   11012,   12500, 185, 210, 1,    75,  1.8, 0.6, 'mite'],
             [   20  , 0, 0,     0,   0.058,  0.071,   0    ,     508,    2000,  80, 315, 0,   110,  0.3, 0.6, 'ant'],
             [  150  , 0, 0,    90,   0    ,  0    ,   1.897,   26512,   30000, 190, 215, 1,   150,  4  , 0.6, 'shrimp'],
             [  450  , 0, 0,   140,   0    ,  0    ,  15.821,  162909,  192000, 140, 165, 1,   200,  1.8, 1.3, 'flea'],
             [  130  , 0, 0,     0,   0.574,  0.701,   0    ,   16560,   20000, 265, 320, 0,   240,  0.4, 0.6, 'spark'],
             [  500  , 0, 0,     0,   1.596,  1.951,   0    ,   14780,   60000,  85, 345, 0,   390,  0.8, 1.3, 'terrier'],
             [  752.5, 0, 0,   375,   0    ,  0    ,  15.827,  197897,  227000, 170, 195, 1,   400,  2.9, 1.3, 'hammeur'],
             [ 1500  , 0, 0,   820,   0    ,  0    ,  19.423,  250000,  300000, 175, 210, 1,   850,  7.9, 1.3, 'thumper'],
             [ 1250  , 0, 0,     0,   7.105,  8.684,   0    ,  205161,  240000, 265, 310, 0,  1100,  1.7, 1.3, 'swivel'],
             [ 1500  , 0, 0,     0,   6.166,  7.536,   0    ,  167969,  215000, 250, 320, 0,  1200,  1.7, 1.3, 'reliant'],
             [ 1750  , 0, 0,     0,   6.555,  8.012,   0    ,   64286,  250000,  90, 350, 0,  1300,  2.7, 2.5, 'poodle'],
             [ 4500  , 0, 0,  2600,   0    ,  0    ,  41.407,  593854,  670000, 195, 220, 1,  2700, 14.9, 1.3, 'kickback'],
             [ 3000  , 0, 0,     0,  18.642, 22.784,   0    ,  658750,  650000, 280, 320, 0,  5300,  2.4, 2.5, 'skipper'],
             [ 9000  , 0, 0,  8000,   0    ,  0    , 100.494, 1515217, 1700000, 205, 230, 1,  9000, 12.3, 2.5, 'thoroughbred'],
             [ 6000  , 0, 0,     0,  40.407, 54.275,   0    , 1379032, 1500000, 285, 310, 0, 13000,  3  , 2.5, 'minsail'],
             [21000  , 0, 0, 16400,   0    ,  0    , 190.926, 2948936, 3300000, 210, 235, 1, 18500, 22.3, 2.5, 'clydesdal'],
             [ 9000  , 0, 0,     0,  53.985, 65.982,   0    , 1205882, 2000000, 205, 340, 0, 25000,  4.1, 3.8, 'rhino'],
             [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1]]

import numpy
import math

def HE():
    return R * planet[kelvin_0] / planet[masse_moyen_mol] / GRAVIT(0)

def PRESSION(altitud):  # pa
    if altitud >= planet[atm_limit] : return 0
    return planet[pression_pa_0] * math.exp(-altitud / HE())

def PA_atm(nombre)       : return nombre / 101325

def escap(altitud):  # m.s-1
    return math.sqrt(2*G*planet[masse]/(planet[rayon]+altitud))

def GRAVIT(altitud):  # m.s-2
    return G * planet[masse] / (planet[rayon] + altitud)**2

def vites_orbital(R, axe_grand_demi) :
    return math.sqrt(G * planet[masse] * (2 / R - 1 / axe_grand_demi))

def vites_ms(distance, temp) : return distance / temp
vites_k = vites_ms(2 * math.pi * planet[rayon], planet[day])

def ergol_u_kg(nombre)   : return nombre * 5
def oxidizer_u_kg(nombre): return nombre * 5
def solid_u_kg(nombre)   : return nombre * 2810 / 375
def ergol_u_c(nombre)    : return nombre * 0.8
def oxidizer_u_c(nombre) : return nombre * 0.18
def solid_u_c(nombre)    : return nombre * 225 / 375

def fuel(etage, mod = 'kg') :
    moteur = etage[nom]
    taille = etage[tail]
    nombre_moteur = etage[nbr_pop]
    nombre_tanks = etage[nbr_tank]
    if mod != 'kg' :
        return nombre_tanks * (ergol_u_c( tanks[taille][ergol]) + oxidizer_u_c( tanks[taille][oxidizer])) + nombre_moteur * solid_u_c( reacteurs[moteur][solid])
    return     nombre_tanks * (ergol_u_kg(tanks[taille][ergol]) + oxidizer_u_kg(tanks[taille][oxidizer])) + nombre_moteur * solid_u_kg(reacteurs[moteur][solid])

def fuel_d(etage) :
    moteur = etage[nom]
    nombre_moteur = etage[nbr_pop]
    nombre_moteur * (ergol_u_kg(reacteurs[moteur][ergol_d]) + oxidizer_u_kg(reacteurs[moteur][oxidizer_d]) + solid_u_kg(reacteurs[moteur][solid_d]))

def POUSSE(etage, altitud = 0):
    nombre_moteur = etage[nbr_pop]
    return nombre_moteur * ISP(etage, altitud) * GRAVIT(altitud) * fuel_d(etage)

def RPP(etage, altitud = 0):  # >1
    kg = etage[masse]
    return POUSSE(etage, altitud - hauteur / 2) / (kg * GRAVIT(altitud))

def a_GRAVIT(etage, altitud = 0) :
    hauteur = etage[haut]
    return GRAVIT(altitud) * (RPP(etage, altitud) - 1)

def ISP(etage, altitud = 0):  # s
    moteur = etage[nom]
    a = reacteurs[moteur][isp_vac] + PA_atm(PRESSION(altitud - hauteur / 2)) * (reacteurs[moteur][isp_asl] - reacteurs[moteur][isp_vac])
    if reacteurs[etage[nom]][typ] == 1 :
        return nombre * a
    return a

def vites_delta(etage, altitud = 0) :
    return ISP(etage, altitud) * GRAVIT(altitud) * math.log(etage[masse] / fuel(etage))

def rech_react(noms) :
    for i in range(len(reacteurs)) :
        if reacteurs[i][nom] == noms :
            return i
    return False

def position(liste, but, deb = 0) :
    for i in range(deb, len(liste)) :
        if liste[i] == but :
            return i
    return False


temp = 0
norm = 1
phi = 2
the = 3
objectif = 8e4
but_dv =  escap(80000)
def eulair(mod, fuse, etag, step=1, trajet=[], coord1=[], coord=[], vites=[]) :
    if mod % 2 == 1 and trajet == [] :
        if mod == 3 : 
            trajet, coord1, coord, vites = eulair(1, fuse, etag, step)
        else :
            trajet = [[0, base+sum(fuse[:,haut]), 0, 0]]
            coord1 = [[0, planet[rayon], 0, 0]]
            coord = [[0, planet[rayon], 0, 0]]
            vites = [[0, vites_k, 90, 0]]
    # print(coord1)
    # len_trajet_i = len(trajet[0])
    apog_temp, temp_demi = 0, 0
    # print(fuse,etag,nom)
    pop = int(fuse[etag][nom])
    kg_fuel_d = fuel_d(pop, fuse[etag][nbr_pop])
    kg_fuel = fuel(pop, fuse[etag][nbr_tank], fuse[etag][nbr_pop])
    kg_total = sum(fuse[:etag,masse]) + kg_fuel
    pousse = [0] * len(trajet[0])
    i = len(trajet) - 1
    while trajet[i][norm] >= 0 :
        if pousse[norm] != 0 :
            trajet1, coord2, coord1, vites1 = eulair(mod-1, fuse, etag, step, trajet, coord, coord, vites)
        # print('coord1',coord1)
        if len(coord1) > 1 :
            apog = max(coord1[:,norm])-planet[rayon]
            apog_i = position(coord1[:,norm], apog+planet[rayon])
            # print(coord1,trajet)
            if len(coord1) > len(trajet) : peri = min(coord1[len(trajet):,norm])-planet[rayon]
                # peri_i = position(coord1[:,norm], peri+planet[rayon], len(trajet))
        else :
            apog = coord1[0][norm]-planet[rayon]
            apog_i = 0
        if (   (mod == 1 and (kg_total == fuse[:etag,masse] or (typ == 0 and (apog >= objectif or trajet[i][norm] < trajet[i-1][norm]))))
            or (mod == 3 and (kg_total == fuse[:etag,masse] or (typ == 0 and peri > planet[atm_limit])))
            or (mod == 0 and (trajet[i][norm] < trajet[i-1][norm] or trajet[i][norm] >= objectif))
            or (mod == 2 and (trajet[i][norm] > planet[rayon] or (coord[i][phi]>=0 and coord[i-1][phi]<0)))) :
            return trajet, coord1, coord, vites
        i1 = i + 1
        if mod % 2 == 1 and kg_fuel != 0 and (reacteurs[pop][typ] == 1 or apog < objectif or (apog_temp != 0 and (trajet[i][temp]>=apog_temp-temp_demi or trajet[i][temp]<=apog_temp+temp_demi))) :
            pousse = [step * i1, POUSSE(pop, fuse[etag][nbr_pop], trajet[i][norm])/kg_total, trajet[i][phi], 0]
        else :
            pousse = [step * i1, 0, trajet[i][phi], 0]
        # print(pousse)
        if kg_fuel <= kg_fuel_d :
            kg_fuel = 0
        else :
            kg_fuel -= kg_fuel_d
        kg_total = fuse[:etag,masse] + kg_fuel
        gravit = [GRAVIT(coord[i][norm]), 180, 0]
        acceler = [step * i1,
                   math.sqrt(pousse[norm]**2 + gravit[norm]**2  - gravit[norm]*pousse[norm]*2*math.cos(math.radians(180-pousse[phi]+gravit[phi]))),
                   math.degrees(math.atan2(pousse[norm], gravit[norm])),
                   0]
        vites = numpy.append(vites, [[step * i1,
                                      math.sqrt((acceler[norm]*step)**2 + vites[i][norm]**2 - 2*acceler[norm]*vites[i][norm]*step*math.cos(math.radians(180-acceler[phi]+vites[i][phi]))),
                                      math.degrees(math.atan2(acceler[norm], vites[i][norm])),
                                      0]], 0)
        coord = numpy.append(coord, [[step * i1,
                                      math.sqrt((vites[i1][norm]*step)**2 + coord[i][norm]**2 - 2*vites[i1][norm]*coord[i][norm]*step*math.cos(math.radians(180-vites[i1][phi]+coord[i][phi]))),
                                      math.degrees(math.atan2(vites[i1][norm], coord[i][norm])),
                                      0]], 0)
        trajet = numpy.append(trajet, [[step * i1, coord[i1][norm]-planet[rayon], 0, 0]], 0)
        # print('trajet',trajet[i1])
        i = i1
        if trajet[i][norm] > 1e4 :
            if trajet[i][norm] <= planet[atm_limit] :
                trajet[i][phi] = 45
            else :
                trajet[i][phi] = 90
                if mod == 3 and apog_temp == 0 :
                    apog_temp = coord1[apog_i][temp]
                    vites_actu1, vites_actu = -1, 0
                    while vites_actu1 < vites_actu :
                        # print(vites_actu1, vites_actu)
                        vites_actu1 = vites_actu
                        kg_total1 = kg_total
                        temp_total = 0
                        vites_total = 0
                        vites_but = vites_orbital(planet[rayon]+objectif, planet[rayon]+objectif) - vites_actu
                        while vites_total < vites_but :
                            vites_total += POUSSE(pop, fuse[etag][nbr_pop], trajet[i][norm])/kg_total1
                            kg_total1 -= fuel_d(pop, fuse[etag][nbr_pop])
                            temp_total += step
                        temp_demi = temp_total / 2
                        if apog_i > int(temp_demi / step) : 
                            vites_i = apog_i - int(temp_demi / step)
                        else : vites_i = 1
                        vites_actu = coord1[vites_i][norm] - coord1[vites_i-1][norm]
    return trajet, coord1, coord, vites

def eulair_etag(mod, fuse, step=1) :
    trajet, coord1, coord, vites = eulair(mod, fuse, len(fuse)-1, step)
    for etag in [len(fuse)-i for i in range(2, len(fuse))] :
        trajet, coord1, coord, vites = eulair(mod, fuse, etag, step, trajet, coord1, coord, vites)
    return trajet, coord1, coord, vites

nbr_pop = 1
nbr_tank = 2
def fabriq_etag(fuse, etag=1, min_cout=0) :
    fuse1 = numpy.copy(fuse)
    pop = 0
    but = False
    # print(fuse1)
    while pop < len(reacteurs) and not(but) and (sum(fuse1[:,cout]) < min_cout or min_cout == 0) :
        # typ_i = reacteurs[pop][typ]
        tail_i = int(reacteurs[pop][tail])
        fuse1[etag][nom] = pop
        print("fuse1[etag][nom]",fuse1[etag][nom])
        fuse1[etag][nbr_pop] = 0
        while fuse1[etag][nbr_pop] < 9 and not(but) and (sum(fuse1[:,cout]) < min_cout or min_cout == 0) :
            fuse1[etag][nbr_pop] += 1
            print("fuse1[etag][nbr_pop]",fuse1[etag][nbr_pop])
            if fuse1[etag][nbr_pop] == 1 :
                fuse1[etag][masse] = coupling[0][tail_i][masse] + reacteurs[pop][masse]
                fuse1[etag][cout]  = coupling[0][tail_i][cout]  + reacteurs[pop][cout]
                fuse1[etag][haut]  = coupling[0][tail_i][haut]  + reacteurs[pop][haut]
            elif fuse1[etag][nbr_pop] == 2 :
                fuse1[etag][masse] = 2 * (coupling[1][tail_i][masse] + reacteurs[pop][masse])
                fuse1[etag][cout]  = 2 * (coupling[1][tail_i][cout]  + reacteurs[pop][cout])
                fuse1[etag][haut]  = 0
                fuse1[etag][tail]  = 2 * reacteurs[pop][tail]
            else :
                fuse1[etag][masse] = coupling[0][tail_i][masse] + reacteurs[pop][masse] + (fuse1[etag][nbr_pop] - 1) * (coupling[1][tail_i][masse] + reacteurs[pop][masse])
                fuse1[etag][cout]  = coupling[0][tail_i][cout]  + reacteurs[pop][cout]  + (fuse1[etag][nbr_pop] - 1) * (coupling[1][tail_i][cout]  + reacteurs[pop][cout])
                fuse1[etag][haut]  = coupling[0][tail_i][haut]  + reacteurs[pop][haut]
                fuse1[etag][tail]  = 2 * reacteurs[pop][tail]
            print("reacteurs[pop][typ]",reacteurs[pop][typ])
            if reacteurs[pop][typ] == 1 :
                # fuse1[etag][masse] += solid_u_kg(reacteurs[pop][solid])
                fuse1[etag][cout] += fuel(pop, fuse1[etag][nbr_tank], fuse1[etag][nbr_pop], 'c')
                print(fuse1[etag])
                if len(fuse1) - etag != 1 :
                    fuse1, min_cout, but = fabriq_etag(fuse1, etag+1, min_cout)
                else :
                    trajet, coord1, coord, vites = eulair_etag(3, fuse1)
                    if coord1[-1][phi]>=0 and coord1[-2][phi]<0 and min(coord1[len(trajet):,norm]) > planet[atm_limit] :
                        but = True
                        sum_cout = sum(fuse1[:,cout])
                        if min_cout < sum_cout : min_cout = sum_cout
            else :
                fuse1[etag][nbr_tank] = 0
                print("a_gravit",a_GRAVIT(pop, fuse1[etag][nbr_pop], 0, sum(fuse1[:,masse])))
                while a_GRAVIT(pop, fuse1[etag][nbr_pop], 0, sum(fuse1[:,masse])) > 1 and not(but) and (sum(fuse1[:,cout]) < min_cout or min_cout == 0) :
                    fuse1[etag][nbr_tank] += 1
                    print("fuse1[etag][nbr_tank]",fuse1[etag][nbr_tank])
                    fuse1[etag][masse]    += tanks[tail_i][masse] # + solid_u_kg(reacteurs[pop][solid])
                    fuse1[etag][cout]     += tanks[tail_i][cout] + fuel(pop, fuse1[etag][nbr_tank], fuse1[etag][nbr_pop], 'c')
                    fuse1[etag][haut]     += tanks[tail_i][haut]
                    if len(fuse1) - etag != 1 :
                        fuse1, min_cout, but = fabriq_etag(fuse1, etag+1, min_cout)
                    else :
                        #trajet, coord1, coord, vites = eulair_etag(3, fuse1)
                        if but_dv
                        if coord1[-1][phi]>=0 and coord1[-2][phi]<0 and min(coord1[len(trajet):,norm]) > planet[atm_limit] :
                            but = True
                            sum_cout = sum(fuse1[:,cout])
                            if min_cout < sum_cout : min_cout = sum_cout
        pop += 1
    return fuse1, min_cout, but

def fabriq_fuse() :
    min_cout1 = 0
    fuse = [[pods[masse], 0, 0, pods[cout], pods[haut], pods[tail], -1]]
    # print(numpy.append([[1,2,3]],[[4,5,6]],0))
    fuse1 = numpy.append(fuse, [[0]*len(fuse[0])], 0)
    fuse2, min_cout, but = fabriq_etag(fuse1)
    # while but == True :
    #     if min_cout < min_cout1 or min_cout1 == 0 :
    #         min_cout = min_cout1
    #         min_fuse = fuse2
    #     fuse1 = numpy.append(fuse1, [[0]*len(fuse[0])], 0)
    #     fuse2, min_cout1, but = fabriq_etag(fuse1, len(fuse1), min_cout)
    # return min_fuse
fabriq_fuse()