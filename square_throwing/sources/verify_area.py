# This file verifies the area of the region W(y, θ) in the square throwing problem.
from scipy.integrate import dblquad
from math import sin, cos, pi, sqrt

edge = 1  # l = 1

def W(y, theta):
    # Like area() function in figure03.py
    Yb = y - edge * sqrt(2) * sin(theta) / 2
    Yc = y - edge * sqrt(2) * cos(theta) / 2

    sub_theta = theta
    if theta > pi / 4:
        sub_theta = pi / 2 - theta

    if Yb < 0 and Yc < 0:
        area = (abs(Yb) + abs(Yc)) * edge * sin(sub_theta + pi/4) / 2
    elif Yb < 0 or Yc < 0:
        area = (y - edge * sqrt(2) * cos(sub_theta) / 2)**2 / (2 * sin(sub_theta + pi/4) * cos(sub_theta + pi/4))
    else:
        area = 0.0
    return area

def integrand(theta, y):
    pdf = y / (pi * edge**2) # PDF of Y,Θ(y, θ)
    return W(y, theta) * pdf

# Integration bounds
y_lower, y_upper = 0, 2 * edge
theta_lower, theta_upper = 0, pi / 2

# Double integration
expected_W, error = dblquad(integrand, y_lower, y_upper,
                            lambda y: theta_lower, lambda y: theta_upper)

print(f"E[W] ≈ {expected_W:.6f}")
print(f"Estimated error: {error:.2e}")
