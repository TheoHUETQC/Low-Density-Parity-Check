# Low-Density-Parity-Check

A Minimal Classical Simulation (maybe more later)

This project is a small, hands-on introduction to **Low-Density Parity-Check (LDPC)** codes, one of the most elegant and powerful error-correcting code families in classical information theory.

The goal is simple:
- take a small binary message (e.g. 8 bits),
- encode it using an LDPC scheme,
- send it through a noisy channel,
- and try to recover the original message using a basic LDPC decoding algorithm.

---

## 🧩 What is an LDPC Code?

An LDPC code adds *parity-check bits* to your data bits in such a way that certain groups of bits must always have **even parity**.  
Each parity check only involves a *few* bits (that’s the “low-density” part).  
If some bits flip due to noise, we can use these parity constraints to detect and often correct the errors.

Mathematically, an LDPC code is defined by a **parity-check matrix** $`H`$:

$`
H \cdot c^T = 0 \pmod{2}
`$

- each **row** of $`H`$ represents one parity-check equation,  
- each **column** corresponds to one bit of the codeword,  
- and a `1` in position $`H_{ij}`$ means that bit *j* participates in parity check *i*.

---

## ⚙️ What This Project Does

1. **Defines** a small, sparse parity-check matrix $`H`$  
2. **Derives** the generator matrix $`G`$ to encode messages  
3. **Simulates** a noisy channel (like a Binary Symmetric Channel)  
4. **Attempts** to decode and correct errors using a simple belief propagation or min-sum method  
5. **Evaluates** the error-correction performance

---

## 🎓 Why This Project

This is a *classical* approach, it’s meant to be a stepping stone toward exploring LDPC ideas in other contexts (like classical computing systems or even quantum LDPC codes later on).

It’s not optimized for performance or large-scale simulation.  
It’s a conceptual and educational exercise: **LDPC from scratch, with NumPy and curiosity.**

---

## 🧠 Requirements

- Python 3.8
- NumPy

---

## 🚀 How to Run

```bash
python classic/ldpc-demo.py
```

---

## References
- http://dspace.univ-bouira.dz:8080/jspui/bitstream/123456789/2163/1/mémoire.pdf
