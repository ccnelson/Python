import matplotlib.pyplot as plt

plt.autoscale(enable=True, axis=u'both', tight=False)
plt.subplot(2, 1, 1)
plt.plot([0, 1, 2, 3, 4, 5])
plt.ylabel('avg. scores')
plt.subplot(2, 1, 2)
plt.plot([9, 7, 6, 4, 2, 1, 2, 3])
plt.ylabel('standard deviation')
plt.xlabel('generation')
plt.show()

