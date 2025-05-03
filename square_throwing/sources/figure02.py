import matplotlib.pyplot as plt
import numpy as np
import figure01

# Objective: Estimate the probability that a square intersects the x-axis
# Figure 2: Simulation of 
# fY,Θ(y, θ) = y / π*(l^2) , ∀(y, θ) ∈ [0, 2*l] × [0,π/2]
# fY,Θ(y, θ) = 0, otherwise.
#
# The square is centered at M=(0,Y) and rotated by angle θ.
# The square is assumed to be length of l=1.
# The square intersects the x-axis if the distance from M to the x-axis is less than or equal to l*sqrt(2)*cos(θ).

edge = 1 # l

def simulate_square_throwing(T, edge=1):
    """
    Simulate the square throwing process and return q_n values.
    """
    def generate_Y():
        """
        Generate a random Y value distributed in [0, 2*edge] and PDF is fY,Θ(y, θ) = y / π*(l^2) , ∀(y, θ) ∈ [0, 2*l] × [0,π/2].
        """
        X = np.random.uniform(0, 2 * edge)
        Y = np.random.uniform(0, 2 * edge)
        if Y > X:
            return Y
        else:
            return generate_Y()

    # Simulate the square throwing process
    print(f"Simulating Results")
    q_n_values = []
    for N in T:
        count = 0
        for _ in range(N):
            Y= generate_Y()
            theta = np.random.uniform(0, np.pi / 2)
            count += figure01.intersects_x_axis(Y, theta)
        q_n = count / N
        q_n_values.append(q_n)
        print(f"Simulated {N} throws: q_n = {q_n:.4f}")
    print("-" * 20)

    return q_n_values

def main():
    T = [1, 5, 10, 50, 100, 500, 1000, 5000,
         10000, 50000, 100000, 500000, 1000000]

    plt.figure(figsize=(10, 5))

    # Simulate the square throwing process and draw plots
    for i in range(1, 3):
        q_n_values = simulate_square_throwing(T, edge)
        figure01.draw_plot(T, q_n_values, i)
        converge_value = q_n_values[-1]
        plt.axhline(y=converge_value, color="r", linestyle='--', label='E[$q_n$] ≈{:.3f}'.format(converge_value))
    
    print(f"E[qn]≈ {converge_value}")

    plt.suptitle('Simulation of Square Throwing Probability_Fig02', fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
