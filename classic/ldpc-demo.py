import numpy as np

#---------------- parametre ----------------#

NBR_BIT = 8 #taille du message que l'on envoie

#---------------- utils ----------------#

def mod2(x) :
    return x % 2

def bitflip(b) :
    return mod2(b+1)

#---------------- encode ----------------#

def get_H(): # 4×12 LDPC parity-check matrix H = [A | I]
    A = np.array([
        [1,0,1,0,0,1,0,0],
        [0,1,1,0,1,0,0,0],
        [1,0,0,1,0,0,1,0],
        [0,0,1,0,1,0,0,1]
    ], dtype=int) # choisis manuellement avec une faible densité

    I = np.eye(4, dtype=int)

    return np.concatenate([A, I], axis=1)

def get_G(): # Matrice generatrice G = [I | A^T] A est tq H = [A | I]
    H = get_H()
    A = H[:, :8]
    A_T = A.T
    I_k = np.eye(8, dtype=int)
    G = np.concatenate([I_k, A_T], axis=1)
    return G

def encode(message) :
    G = get_G()
    encoded_message = mod2(message @ G)
    return encoded_message

#---------------- decode ----------------#

def syndrome(message_received):
    H = get_H()
    return mod2(H @ message_received)

def find_error(syndrome):
    H = get_H()
    for j in range(H.shape[1]):
        if np.array_equal(H[:, j], syndrome):
            return j
    return None

#---------------- main ----------------#

message = np.array([1,0,1,1,0,0,1,0])
print("message  :", message)

#on encode notre message pour le rendre plus robuste
encoded_message = encode(message)
print("encodé   :",encoded_message)

# Ajout d'un bruit simple aléatoirement (1 bit d'erreur)
message_received = np.copy(encoded_message)
noise_pos = np.random.randint(0, NBR_BIT)
message_received[noise_pos] = bitflip(encoded_message[noise_pos])  
print("Reçu     :", message_received)

# On cherche ou est l erreur
s = syndrome(message_received)
pos = find_error(s)

# Correction
message_received[pos] = bitflip(message_received[pos])  
print("corrigé  :", message_received)
