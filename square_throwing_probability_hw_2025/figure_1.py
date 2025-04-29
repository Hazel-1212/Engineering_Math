# Objective : Generate a plot of the probability of a square intersecting the x-axis
# Figure 1 : Simulation of 
# fY,Θ(y, θ) = 
# 1 / πl , ∀(y, θ) ∈ [0, 2l] × [0,2/π]
# 0, otherwise.

import numpy as np
import matplotlib.pyplot as plt

# Parameters
side_length = 1.0
T = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000,
                   50000, 100000, 500000, 1000000]

def intersects_x_axis(Y, theta, side=1.0):
    """
    Given center M=(0,Y) and angle theta, determine whether
    square intersects x-axis.
    """
    half_diag = (side / np.sqrt(2))
    
    # Square corners in local coordinates (before rotation)
    corners = np.array([
        [ half_diag,  half_diag],
        [ half_diag, -half_diag],
        [-half_diag, -half_diag],
        [-half_diag,  half_diag]
    ])
    
    # Rotation matrix for angle theta
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    # Rotate and shift to get global coordinates
    rotated = corners @ R.T + np.array([0, Y])
    
    # Check if any corner has y-coordinate ≤ 0
    return np.any(rotated[:, 1] <= 0)



fig=plt.figure(figsize=(20, 10))
plt.title('Simulation of Square Throwing Probability')
for i in range(1, 5):
# For storing q_n values
    q_n_values = []

    for N in T:
        a_k = []
        for _ in range(N):
            Y = np.random.uniform(0, 2 * side_length)
            theta = np.random.uniform(0, np.pi / 2)
            a_k.append(1 if intersects_x_axis(Y, theta) else 0)
        q_n = np.mean(a_k)
        q_n_values.append(q_n)

# Plot using semilogx
    ax = fig.add_subplot(2,2,i)
    ax.semilogx(T, q_n_values, marker='o')
    ax.set_xlabel('n (log scale)')
    ax.set_ylabel('$q_n$')
    ax.set_title('Figure 1-1 : The First Round')

plt.grid(True)
plt.show()
