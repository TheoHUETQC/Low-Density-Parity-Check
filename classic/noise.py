import numpy as np
from utils import mod2

#---------------- 1 bitflip ----------------#
"""Ajout d'un bruit simple aléatoirement (1 bit d'erreur)"""
def simplest_noise(message) : 
    bits = message.copy()
    noise_pos = np.random.randint(0, message.size)
    bits[noise_pos] = mod2(bits[noise_pos]+1) 
    return bits

#---------------- Binary Symmetric Channel ----------------#
"""Chaque bit transmis a une probabilité p d etre inversé (0→1, 1→0)"""
def simulate_bsc(message, p = 0.1) :
    p_flip = np.random.rand(message.size) < p # proba p de faire un flip
    return mod2(message + p_flip)

#---------------- Additive White Gaussian Noise ----------------#
""" ajoute un bruit sur chaque bit avec une loi normal de parametre sigma """
def simulate_awgn(message, sigma = 1) :
    bits = message.copy()
    bits = ( -2 * message) + 1 # 0 → +1, 1 → −1
    noise = np.random.normal(0, sigma**2, message.size) # bruit gaussien
    bits = bits + noise
    return np.multiply(bits < 0, 1) # si notre nouveau "bit" est > 0 → 0 et si < 0 → 1

#---------------- Binary Erasure Channel ----------------#
"""Chaque bit transmis a une probabilité e d'etre effacé"""
def simulate_bec(message, e = 0.2) :
    bits = message.copy()
    p_flip = np.random.rand(message.size) < e # proba e d'etre effacé
    bits[p_flip] = -1 # correspond a un bit effacé
    return bits
