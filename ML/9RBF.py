import math

centers = [(0,0), (0,1), (1,0), (1,1)]

weights = [-0.8, 0.9, 0.9, -0.8]
bias = 0.2

x = (1,1)
sigma = 1

output = 0

print("Radial Basis Function Network\n")

for i in range(4):

    d2 = (x[0]-centers[i][0])**2 + (x[1]-centers[i][1])**2

    H = math.exp(-d2 / (2*sigma**2))

    print(f"Hidden Neuron H{i+1}")
    print("Center :", centers[i])
    print("Distance² :", d2)
    print("Gaussian H :", round(H,3))
    print("Weight :", weights[i])
    print()

    output += H * weights[i]

output += bias

print("Bias =", bias)
print("Final Output =", round(output,4))

if output >= 0:
    print("Predicted Class = +1")
else:
    print("Predicted Class = -1")
