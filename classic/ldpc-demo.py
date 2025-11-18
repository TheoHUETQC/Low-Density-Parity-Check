import numpy as np
from utils import mod2
from noise import simplest_noise

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

print("One exemple step by step :")

# Generate a message of 8 random bits
message = np.random.randint(2, size=8)
print("message   :", message)

# We encode our message to make it more robust
encoded_message = encode(message)
print("encoded   :",encoded_message)

# Noise is applied
message_received = simplest_noise(encoded_message)
print("Received  :", message_received)

# We are looking for the error
s = syndrome(message_received)
pos = find_error(s)

# Correction
message_received[pos] = mod2(message_received[pos]+1)  
print("corrected :", message_received)

# Final message
print("final     :", message_received[:8])

# Testing the method on N messages
N = 1000
result = []
for i in range(N) :
    message = np.random.randint(2, size=8)
    message_received = simplest_noise(encode(message))
    s = syndrome(message_received)
    pos = find_error(s)
    message_received[pos] = mod2(message_received[pos]+1) 
    result.append(np.array_equal(message, message_received[:8]))

print("Testing the method on N messages :",np.sum(result),"/",N,"are corrected correctly")
