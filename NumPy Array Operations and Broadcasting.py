import numpy as np

a = np.arange(1, 11)

print("Array:", a)

print("Slicing:", a[2:7])

print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

# Broadcasting
a = a + 5

print("After Broadcasting:", a)
