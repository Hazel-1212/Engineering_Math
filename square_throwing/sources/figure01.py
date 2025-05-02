import matplotlib.pyplot as plt
import numpy as np

# Objective : Estimate the probability that a square intersects the x-axis
# Figure 1 : Simulation of 
# fY,Θ(y, θ) = 1 / π*l , ∀(y, θ) ∈ [0, 2*l] × [0,π/2]
# fY,Θ(y, θ) = 0, otherwise.
 
edge = 1

def intersects_x_axis(Y, theta):
    """
    Given center M=(0,Y) and angle theta, determine whether
    the square intersects the x-axis.
    """
    sub_theta = theta 
    if theta > np.pi / 4:
        sub_theta = np.pi / 2 - theta
    return Y <= edge * np.sqrt(2) * np.cos(sub_theta) /2

def simulate_square_throwing(T, edge=1):
    """
    Simulate the square throwing process and return q_n values.
    """
        
    q_n_values = []

    print(f"Simulating Results")

    for N in T:
        count = 0
        for _ in range(N):
            Y= np.random.uniform(0, 2 * edge)
            theta = np.random.uniform(0, np.pi / 2)
            count += intersects_x_axis(Y, theta)
        q_n = count / N
        q_n_values.append(q_n)
        print(f"Simulated {N} throws: q_n = {q_n:.4f}")

    print("-" * 20)
    return q_n_values

def draw_plot(T, q_n_values, i):
    """
    Draw a subplot for the given simulation results.
    """
    ax = plt.subplot(1, 2, i)
    ax.plot(T, q_n_values, marker='o', linestyle='-', color='b')
    ax.set_xscale('log')
    ax.set_ylim(0, 1)
    ax.set_xlabel('n (Number of Throws)')
    ax.set_ylabel('$q_n$ ')
    ax.set_title(f'{i} round',fontdict={'fontsize': 10})
    ax.grid(True)

def main():
    T = [1, 5, 10, 50, 100, 500, 1000, 5000,
         10000, 50000, 100000, 500000, 1000000]

    plt.figure(figsize=(10, 5))

    for i in range(1, 3):
        q_n_values = simulate_square_throwing(T, edge)
        draw_plot(T, q_n_values, i)
        converge_value = np.floor(q_n_values[-1] * 1000) / 1000
        #plt.axhline(y=converge_value, color='r', linestyle='--', label=f'Converged Value: {converge_value}')
        plt.axhline(y=0.318, color="r", linestyle='--', label='E[$q_n$]: 0.318')

    
    print(f"The result gets close to {converge_value} as n gets large.")

    plt.suptitle('Simulation of Square Throwing Probability_Fig01', fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit suptitle
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()