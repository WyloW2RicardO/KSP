# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:04:24 2022

@author: HP TG01
"""
## CONSTRUCT
import numpy
import math
import matplotlib.pyplot

def position(liste, but, deb = 0) :
    for i in range(deb, len(liste)) :
        if liste[i] >= but :
            return i
    return False

def surface_baes(diametre) :
    return math.pi * math.pow(diametre / 2, 2)

def surface_cylindre(diametre, hauteur) :
    return math.pi * diametre * hauteur

def surface_conne(diametre, hauteur) :
    return math.pi * diametre * hauteur / 2

def sheriq_cartesien(ligne, biais = 0) :
    return [0,
            (biais + ligne[norm]) * math.cos(math.radians(ligne[the])) * math.cos(math.radians(ligne[phi])),
            (biais + ligne[norm]) * math.cos(math.radians(ligne[the])) * math.sin(math.radians(ligne[phi])),
            (biais + ligne[norm]) * math.sin(math.radians(ligne[the]))]

def add_force(force1, force2) :
    force = numpy.add(sheriq_cartesien(force1), sheriq_cartesien(force2))
    return[0,
           math.sqrt(math.pow(force[1], 2) + math.pow(force[2], 2) + math.pow(force[3], 2)),
           math.degrees(math.atan2(force[2],force[1])),
           0]

def regretion(X, Y, d = 2) :
    P = numpy.polyfit(X, Y, d)
    return P[0], P[1], P[2]

def trac(nom, X, x_nom, Y, y_nom):
    matplotlib.pyplot.plot(X, Y)
    matplotlib.pyplot.title(nom)
    matplotlib.pyplot.xlabel(x_nom)
    matplotlib.pyplot.ylabel(y_nom)
    matplotlib.pyplot.show()

## PHYSIQUE
G = 6.674e-11  # Constante gravitationnelle m3⋅kg−1⋅s−2
R = 8.31446261815324  # Constante de gaz kg⋅m2.s−2⋅K−1⋅mol−1
base = 71

def PA_atm(nombre) : return nombre / 101325
def celcus_kelvin(nombre) : return nombre + 273.15

def escap(N, altitud):  # m.s-1
    return math.sqrt(2 * G * planet[N][masse] / (planet[N][rayon] + altitud))

def vites_ms(distance, temp) : return distance / temp


## PARTIE
#masse(kg), rayon(m), day(s), temp(k), masse_moyen_mol(kg.mol-1), pression_pa(kg⋅m −1⋅s −2), atm_limit(m)
planet = [[5.2915158e22, 6e+5, 21600, celcus_kelvin(15), 0.0289644, 101325, 7e4, 'kerbin']]
masse=0
rayon=1
time=2
temp=3
mol=4
press=5
atmL=6

temperature = [[[0,planet[0][temp]],[11e3,celcus_kelvin(-56.5)],[20.1e3,celcus_kelvin(-56.5)],[32.2e3,celcus_kelvin(-44.5)],[47.3,celcus_kelvin(-2.5)],[52.4e3,celcus_kelvin(-2.5)],[61.6e3,celcus_kelvin(-20.5)],[80e3,celcus_kelvin(-92.5)]]]


#masse(kg), cout, haut(m), diam(m), nom
chut = [[ 75, 150, 0    , 0  , 'mk12-r'],
        [100, 422, 0.631, 0.6, 'mk16']]
cout=-4
haut=-3
diam=-2
nom=-1

stack = [[ 10, 150, 0.625, 0.6, 'td-06'],
         [ 40, 200, 0    , 1.3, 'td-12'],
         [160, 300, 1    , 2.5, 'td-25'],
         [360, 375, 1    , 3.8, 'td-37']]
radial = [[ 25, 600, 0, 0, 'tt-38'],
          [ 50, 700, 0, 0, 'tt-70'],
          [400, 770, 0, 0, 'hdm']]
coupling = [stack, radial]

#masse(kg), what, cout, haut(m), diam(m), nom
baterie = [[5, 100, 80, 0, 0, 'z-100']]
what = 1

#masse(kg), what_d, cout, haut(m), diam(m), nom
bodys =[[ 50, 1.7/60, 300, 1, 0.6, 'staysputnick']]
whatD = 1

#masse(kg), what, whatD, coefT, surf(m), cout, haut(m), diam(m), nom
pods = [[800, 100, 0.2, 0.1, 0, 635, 1.1, 1.3, 'mk1']]
whatD_pods = 2
coefT = 3
surf = 4
pods[0][surf] = surface_conne(pods[0][diam], pods[0][haut])

control = [[50, 0.3, 600, 0.628, 0.6, 'SAS']]

antenne = [[5, 20, 300, 0, 0, '16']]

#masse(kg), ergol(u), oxidizer(u), multipl, cout, haut(m), diam(m), nom
tanks = [[  25  ,   18,   22, 0,  52  , 0.625, 0.6, 'oscar-b'],
         [  62.5,   45,   55, 8,  54.1, 0.5  , 1.3, 'fl'],
         [ 500  ,  360,  440, 8, 351.5, 1    , 2.5, 'x200'],
         [2250  , 1620, 1980, 3, 347.5, 2.665, 3.8, 's3']]
ergol   =  1
oxidizer=  2
multipl =  3

#masse(kg), ergolD(u), oxidizerD(u), solidD(u), ergolD(u.s-1), oxidizerD(u.s-1), solidD(u.s-1), pousse_asl(kg.m.s-2), pousse_vac(kg.m.s-2), isp_asl(s), isp_vac(s), typ, cout, haut(m), diam(m), nom
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
solid    =  3
ergolD   =  4
oxidizerD=  5
solidD   =  6
aslP     =  7
vacP     =  8
aslI     =  9
vacI     = 10
typ      = 11


def GRAVIT(N, altitud):  # m.s-2
    return G * planet[N][masse] / math.pow(planet[N][rayon] + altitud, 2)

def TEMPER(N, altitud) :
    for i in range(len(temperature[N])) :
        if temperature[N][i][0] <= altitud :
            a = (temperature[N][i][1] - temperature[N][i-1][1]) / (temperature[N][i][0] - temperature[N][i-1][0])
            b = temperature[N][i][1] - a * altitud
            return a * altitud + b
    return temperature[N][-1][1]

def HE(N):
    return R * planet[N][temp] / planet[N][mol] / GRAVIT(N, 0)

def PRESSION(N, altitud):  # pa
    if altitud >= planet[N][atmL] : return 0
    return planet[N][press] * math.exp(-altitud / HE(N))

def densiter(N, altitud) : #masse volumique kg.m-3
    return PRESSION(N, altitud) * planet[0][mol] / TEMPER(N, altitud) / R

def vites_orbital(N, R, axe_grand_demi) :
    return math.sqrt(G * planet[N][masse] * (2 / R - 1 / axe_grand_demi))

vites_k = vites_ms(2 * math.pi * planet[0][rayon], planet[0][time])

def ergol_k(nombre)   : return nombre * 5
def oxidizer_k(nombre): return nombre * 5
def solid_k(nombre)   : return nombre * 2810 / 375
def ergol_c(nombre)    : return nombre * 0.8
def oxidizer_c(nombre) : return nombre * 0.18
def solid_c(nombre)    : return nombre * 225 / 375


## ETAGE
#masse, tanksNB, reactNB, coefT, surf, cout, haut, diam, react
tanksNB = 1
reactNB = 2

def fuel(etage, mod = 'kg') :
    R = int(etage[nom])
    T = int(etage[diam])
    if mod != 'kg' :
        return etage[tanksNB] * (ergol_c(tanks[T][ergol]) + oxidizer_c(tanks[T][oxidizer])) + etage[reactNB] * (solid_c(reacteurs[R][solid]) + ergol_c(reacteurs[R][ergol]) + oxidizer_c(reacteurs[R][oxidizer]))
    return     etage[tanksNB] * (ergol_k(tanks[T][ergol]) + oxidizer_k(tanks[T][oxidizer])) + etage[reactNB] * (solid_k(reacteurs[R][solid]) + ergol_c(reacteurs[R][ergol]) + oxidizer_c(reacteurs[R][oxidizer]))

def fuel_d(etage) :
    R = int(etage[nom])
    return etage[reactNB] * (ergol_k(reacteurs[R][ergolD]) + oxidizer_k(reacteurs[R][oxidizerD]) + solid_k(reacteurs[R][solidD]))

def ISP(N, etage, altitud = 0):  # s
    #print('etage',etage)
    R = int(etage[nom])
    return etage[reactNB] * (reacteurs[R][vacI] + PA_atm(PRESSION(N, altitud)) * (reacteurs[R][aslI] - reacteurs[R][vacI]))

def POUSSE(N, etage, altitud = 0):
    return etage[reactNB] * ISP(N, etage, altitud) * GRAVIT(N, altitud) * fuel_d(etage)

def RPP(N, fuse, altitud = 0):  # >1
    kg = sum(fuse[:,masse])
    return POUSSE(N, fuse[-1], altitud) / (kg * GRAVIT(N, altitud))

def a_GRAVIT(N, fuse, altitud = 0) :
    return GRAVIT(N, altitud) * (RPP(N, fuse, altitud) - 1)

def vites_delta(N, fuse, etag, altitud = 0) :
    return ISP(N, fuse[etag], altitud) * GRAVIT(N, altitud) * math.log((fuse[:etag,masse] + fuel(fuse[etag])) / fuse[:etag,masse])


## TRAJECTOIRE
#trajet : time, norm, phi, the
time_t = 0
norm = 1
phi  = 2
the  = 3

objectif = 8e4
but_dv =  escap(0, objectif)
def eulair(fuse, etag, mod=3, step=1, coord=[], trajet=[], prev=[], vites=[], masseE=0) :
    "mode 1 jusqua la sortie orbital"
    "mode 3 jusqua la mise en orbite"
    #print('prev', prev)
    if masseE == 0 :
        "tout ses sont en coordoné geocentrique sherique"
        vites1 = [[0, 0, 0, 0]]
        trajet1= [[0, 0, 0, 0]]
        coord1 = [[0, planet[0][rayon], 0, 0]]
        prev1  = numpy.copy(coord1)
        masseE1= fuel(fuse[etag])
    else :
        vites1 = numpy.copy(vites)
        trajet1= numpy.copy(trajet)
        coord1 = numpy.copy(coord)
        prev1  = numpy.copy(prev)
        masseE1= numpy.copy(masseE)
    if mod == 3 :
        coord1, prev1, trajet1, vites1, masseE1 = eulair(fuse, etag, 1, step, coord1, prev1, trajet1, vites1, masseE1)
    S = sum(fuse[: etag, surf])         # surface totalde la fuser
    CT= sum(fuse[: etag, coefT])        # coefitien de la forme de la fuser
    fuelD = fuel_d(fuse[etag])          # debi de la fuser
    masseF= sum(fuse[: etag, masse])    # masse total de la fuser
    i0 = trajet1[- 1][0]
    while trajet1[-1][norm] >= 0 :      # tanque la fuser ne secrase pas
        stepi = step *(i0 + 1)
        trajet1= numpy.append(trajet1,[[stepi,
                                        abs(coord1[-1][norm]) - planet[0][rayon],
                                        0,
                                        0]], 0)
        if mod > 1 : trajet1[-1][phi] = 90  # des qu'il sort de l'atmospher
        elif trajet1[-1][norm] > 1e4 : trajet1[-1][phi] = 70
        elif trajet1[-1][norm] > 1e3 : trajet1[-1][phi] = 45
        propuls = [stepi, 0, 0, 0]
        if mod % 2 == 0 :
            if (mod == 0                                                                    # periode de decolage
                and (max(trajet1[:, norm]) >= objectif                              # si la fuser est sorti de l'atmospher
                     or trajet1[-1-(len(trajet1)>1)][norm] > trajet1[-1][norm])) :          # si la fuse monte
                return coord1, prev1, trajet1, vites1, masseE1
            #print(coord1[-1][phi], '> 0', coord1[-1][phi] > 0)
            if (mod == 2                                                                    # periode orbital
                and coord1[-1][phi] < 0                                                     # si la boucle est boucle
                and min(trajet1[position(trajet1[:,norm], objectif):,norm]) >= objectif) :  # si on reste inferieur a l'objectif
                return coord1, prev1, trajet1, vites1, masseE1
        else :
            prev1, coord2, trajet2, vites2, masseE2 = eulair(fuse, etag, mod-1, step, coord1, prev1, trajet1, vites1, masseE1)
            print('prev1', prev1[len(coord1) :])
            prev_max = max(prev1[:, norm]) - planet[0][rayon]
            prev_min = min(prev1[len(coord1) :, norm]) - planet[0][rayon]
            prev_time= position(prev1[:, norm], objectif + planet[0][rayon], len(coord1))
            print('prev_max', prev_max)
            print('prev_min', prev_min)
            print('prev_time', prev_time)
            #print('prev', prev1)
            #print('trajet', trajet1)
            if mod == 1 and prev_max >= objectif  :
                return coord1, prev1, trajet1, vites1, masseE1
            elif (mod == 3
                and stepi < prev_time                               # atendre l'apoger
                and reacteurs[int(fuse[etag][nom])][typ] == 0) :    # si revoir liquide
                pass
            else:
                if masseE1 <= 0 or (mod == 3 and prev_min >= objectif) :
                    return coord1, prev1, trajet1, vites1, masseE1
                masseE1 -= step * fuelD
                propuls = [stepi,
                           0,
                           coord1[-1][phi] + trajet1[-1][phi],
                           0]
                if prev_time is False or stepi >= prev_time :
                    propuls[1] = POUSSE(0, fuse[etag])/(masseE1 + masseF)
        train = [stepi,
                 densiter(0, trajet1[-1][norm]) * vites1[-1][norm] * S * CT / (masseE1 + masseF),
                 180 - vites1[-1][phi],
                 0]
        gravit = [stepi,
                  GRAVIT(0, trajet1[-1][norm]),
                  180 + coord1[-1][phi],
                  0]
        acceler= add_force(add_force(propuls, train),gravit)
        vites1 = numpy.append(vites1, [add_force(vites1[-1], acceler)]   , 0)
        # vites1[-1][phi] = coord1[-1][phi] + trajet1[-1][phi]
        coord1 = numpy.append(coord1, [add_force(coord1[-1], vites1[-1])], 0)
        coord1[-1][time_t] = stepi 
        if mod % 2 == 1 :
            print('mod    ', mod)
            #print('masseE ', masseE1)
            print('trajet ', trajet1[-1])
            #print('train  ', train)
            #print('propuls', propuls)
            #print('gravit ', gravit)
            print('acceler', acceler)
            print('vites  ', vites1[-1])
            print('coord  ', coord1[-1])
        i0 += 1
    return coord1, prev1, trajet1, vites1, masseE1

def eulair_etag(fuse, mod=3, step=1) :
    coord, prev, trajet, vites, masseE = eulair(fuse, len(fuse) - 1, mod, step)
    for etag in [len(fuse) - i for i in range(2, len(fuse))] :
        coord, prev, trajet, vites, masseE = eulair(fuse, etag, mod, step, trajet, coord, prev, trajet, vites)
    return coord, prev, trajet, vites, masseE

def trac_plan(coord,prev):
    T = [sheriq_cartesien([0,planet[0][norm],i,0]) for i in range(360)]
    C = [sheriq_cartesien(coord[i]) for i in range(len(coord))]
    P = [sheriq_cartesien(prev[i]) for i in range(len(coord))]
    trac('vol', C, 'x', P, 'y')
    pass


## FUSEE
coefT_coif = 0.01
coefT_ratio = 0.01
coefT_culo = 0.01

def essence(fuse, etag, R, T, min_cout, but, altitud=0) :
    print(fuse)
    print("typ",reacteurs[R][typ])
    if reacteurs[R][typ] == 1 : # si c'est un reacteur combustible solide
        fuse[etag][cout] += fuel(fuse[etag], 'c')
        if (a_GRAVIT(0, fuse, altitud) > 1                                              # si les reacteurs de l'etage son asser puissan pour décoler
            and but_dv <= sum([vites_delta(0, fuse, etag) for i in range(len(fuse))])   # si le detaV theorique est sufisant
            and (sum(fuse[:,cout]) < min_cout or min_cout == 0)) :                      # si on est inferieur au min cout
            print("a_gravit",a_GRAVIT(0, fuse))
            print("DV", sum([vites_delta(0, fuse, etag) for i in range(len(fuse))]))
            coord, prev, trajet, vites, masseE = eulair_etag(fuse)
            #print('trajet',trajet)
            trac_plan(coord,prev)
            but = True
    else :
        fuse[etag][tanksNB] = 0
        #print("a_gravit",a_GRAVIT(0, fuse))
        print("a_gravit",a_GRAVIT(0, fuse))
        print("sum(fuse[:,cout]) < min_cout",sum(fuse[:,cout]),min_cout)
        while (a_GRAVIT(0, fuse, altitud) > 1
               and not(but)                                             # arret si notre objectif est atein
               and (sum(fuse[:,cout]) < min_cout or min_cout == 0)) :   # si on est inferieur au min cout
            fuse[etag][tanksNB] += 1
            print("fuse[etag][tanksNB]", fuse[etag][tanksNB])
            fuse[etag][masse]+= tanks[T][masse]
            fuse[etag][cout] += tanks[T][cout] + fuel(fuse[etag], 'c')
            haut_tanks = fuse[etag][tanksNB] * tanks[T][haut]
            fuse[etag][haut] += haut_tanks / fuse[etag][reactNB]
            fuse[etag][coefT]+= coefT_ratio * haut_tanks / fuse[etag][diam]
            fuse[etag][surf] += surface_cylindre(tanks[T][diam], haut_tanks)
            print("DV", sum([vites_delta(0, fuse[i], 0) for i in range(len(fuse))]))
            if (but_dv <= sum([vites_delta(0, fuse, etag) for i in range(len(fuse))])   # si le detaV theorique est sufisant
                and (sum(fuse[:,cout]) < min_cout or min_cout == 0)) :                  # si on est inferieur au min cout
                but = True
    return fuse, but

def fabriq_etag(fuse, min_cout, etag = -1) :
    fuse1 = numpy.copy(fuse)
    but = False
    # print(fuse1)
    while (fuse1[etag][nom] < len(reacteurs)                        # se limiter au reactuer donné
           and not(but)                                             # arret si notre objectif est atein
           and (sum(fuse1[:,cout]) < min_cout or min_cout == 0)) :  # si on est inferieur au min cout
        fuse1[etag][nom] += 1
        #print("nom", fuse1[etag][nom])
        # typ_i = reacteurs[react][typ]
        R = int(fuse1[etag][nom])
        T = int(reacteurs[R][diam])
        fuse1[etag][reactNB] = fuse1[etag-1][reactNB]
        while (fuse1[etag][reactNB] < 10                                # limite le nombre de reacteurs latereaux
               and not(but)                                             # arret si notre objectif est atein
               and (sum(fuse1[:,cout]) < min_cout or min_cout == 0)) :  # si on est inferieur au min cout
            fuse1[etag][reactNB] += 1
            if fuse1[etag][reactNB] == 2 and fuse1[etag-1][nom] == -1 : # si il est apres le pods
                fuse1[etag][reactNB] += 1
            colonNW = fuse1[etag][reactNB] - fuse1[etag-1][reactNB] # le nombre de nouvel colone
            #colonOD = fuse1[etag][reactNB] - colonNW
            #print("reactNB",fuse1[etag][reactNB])
            if fuse1[etag][reactNB] == 2 :
                "pour une question déquilibre evidant quand il y a que 2 reacteur nous les meterons sur le coté"
                fuse1[etag][masse]=(coupling[1][T][masse]+ reacteurs[R][masse])* 2
                fuse1[etag][cout] =(coupling[1][T][cout] + reacteurs[R][cout]) * 2
            else :
                fuse1[etag][masse]= coupling[0][T][masse]+ reacteurs[R][masse]+ (fuse1[etag][reactNB] - 1) * (coupling[1][T][masse]+ reacteurs[R][masse])
                fuse1[etag][cout] = coupling[0][T][cout] + reacteurs[R][cout] + (fuse1[etag][reactNB] - 1) * (coupling[1][T][cout] + reacteurs[R][cout])
                fuse1[etag][haut] = coupling[0][T][haut] + reacteurs[R][haut]
            if fuse1[etag - 1][reactNB] < 2 and fuse1[etag][reactNB] >= 2 : # si c'est les premier reacteur latereaux
                fuse1[etag][diam] = coupling[0][T][diam] * 2
            if reacteurs[int(fuse1[etag - 1][nom])][diam] < reacteurs[R][diam] : # si le reacteurs devien plus gros
                if fuse1[etag][reactNB] >= 2 : a = 2
                else : a = 1
                fuse1[etag][diam] +=(reacteurs[R][diam] - reacteurs[int(fuse1[etag - 1][nom])][diam]) * a / 2
            haut_sum = sum(fuse[:,haut])
            if fuse1[etag][reactNB] >= 2 and reacteurs[R][haut] > haut_sum : # si les reacteurs lateraux sont plus grand
                fuse1[etag][haut] += reacteurs[R][haut] - haut_sum
            fuse1[etag][coefT]= fuse1[etag][reactNB] * coefT_ratio * fuse1[etag][haut] / reacteurs[R][diam]   + colonNW * coefT_coif
            fuse1[etag][surf] = fuse1[etag][reactNB] * surface_cylindre(reacteurs[R][diam], fuse1[etag][haut])+ colonNW * surface_baes(reacteurs[R][diam])
            if (fuse1[etag][i] == fuse1[-1][i] for i in range(len(fuse1[-1]))) : # si c'est le dernier etage
                fuse1[etag][coefT]+= fuse1[etag][reactNB] * coefT_culo
                fuse1[etag][surf] += fuse1[etag][reactNB] * surface_baes(reacteurs[R][diam])
                fuse1, but  = essence(fuse1, etag, R, T, min_cout, but)
            else : fuse1,but= essence(fuse1, etag, R, T, min_cout, but, planet[0][atmL])
    return fuse1

fuse = [[pods[0][masse]+chut[0][masse], 0, 1, pods[0][coefT], pods[0][surf], pods[0][cout]+chut[0][cout], pods[0][haut]+chut[0][haut], pods[0][diam], -1]]
def fabriq_fuse(fuse) :
    min_cout = 0
    min_etage = []
    # print(numpy.append([[1,2,3]],[[4,5,6]],0))
    fuse1 = numpy.append(fuse, [[0]*len(fuse[0])], 0)
    fuse1[-1][nom] = -1
    fuse2 = fabriq_etag(fuse1, min_cout)
    sum_cout = sum(fuse2[:,cout])
    if min_cout > sum_cout or min_cout == 0 :
        min_cout = sum_cout
        min_etage = fuse2[-1]
    print(sum_cout)
    return min_etage
fuse = numpy.append(fuse, [fabriq_fuse(fuse)], 0)
print(numpy.array(fuse))