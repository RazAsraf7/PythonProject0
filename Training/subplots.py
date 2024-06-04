import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10,6))
counts = [16, 17, 4, 5]
counts1 = [1,4,2,7]
# plt.barh(counts, counts1)
# plt.title('Trial')
# plt.show()
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(counts, counts1)
plt.show()