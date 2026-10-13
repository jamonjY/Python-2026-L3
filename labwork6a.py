import matplotlib.pyplot as plt
import math
x = [i/10 for i in range(-50, 51)]
y = [2*i + math.sin(i)**2 + 3 for i in x]
plt.plot(x,y)
plt.grid(True)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("hello, po!")
plt.savefig("po.pdf")




