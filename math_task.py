import math
import matplotlib.pyplot as plt
X = []
Y = []
x = 50000.0
y = 0.0
river = 7/3.6
boat = 25/3.6
t = 0.0
a = 0
dt = 0.1
while x > 0:
    t += dt
    x -= boat * math.cos(a) * dt
    y += river * dt
    y -= boat * math.sin(a) * dt
    a = math.atan(y/x)
    X.append(x)
    Y.append(y)
    print(x, " ", y)
print(t)
plt.figure()
plt.plot(X, Y)
plt.grid()
plt.xlabel("до берега")
plt.ylabel("по реке")
plt.savefig("C:\\Users\\aatis\\OneDrive\\Рабочий стол\\shura\\sssshura.png")

