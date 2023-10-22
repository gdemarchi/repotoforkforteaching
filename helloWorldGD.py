# could you write a very fancy hello world script in python, just to showcase some more cool python/numpy/scipy
# features in one short silly script    


import numpy as np

# Define the message to display
message = "Hello, World! Did you know that the brown fox jumps over the lazy dog?"

# Convert the message to a NumPy array of characters
chars = np.array(list(message))

# Create a mask for the vowels in the message
vowelA = np.isin(chars, list("Aa"))
consonantB = np.isin(chars, list("Bb"))
vowelE = np.isin(chars, list("Ee"))
vowelI = np.isin(chars, list("Ii"))
vowelO = np.isin(chars, list("Oo"))


# Replace the vowels with asterisks
chars[vowelA] = "4"
chars[consonantB] = "8"
chars[vowelE] = "3"
chars[vowelI] = "1"
chars[vowelO] = "0"

# Print the modified message
print("".join(chars))



