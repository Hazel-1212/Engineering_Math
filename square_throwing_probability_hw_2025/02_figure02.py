import matplotlib.pyplot as plt
import numpy as np

# Objective: Estimate the probability that a square intersects the x-axis
edge = 1

def intersects_x_axis(Y, theta):
    """
    Given center M=(0,Y) and angle theta, determine whether
    the square intersects the x-axis.
    """
    if theta > np.pi / 4:
        theta = np.pi / 2 - theta
    return Y <= edge * np.sqrt(2) * np.cos(theta) /2

def simulate_square_throwing(T, edge=1):
    """
    Simulate the square throwing process and return q_n values.
    """
    def generate_Y():
        X = np.random.uniform(0, 2 * edge)
        Y = np.random.uniform(0, 2 * edge)
        if Y > X:
            return Y
        else:
            return generate_Y()
        
    q_n_values = []

    print(f"Simulating Results")
    
    for N in T:
        count = 0
        for _ in range(N):
            Y= generate_Y()
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
        plt.axhline(y=0.102, color='r', linestyle='--', label=f'E[$q_n$]: 0.102')
    
    print(f"The result gets close to {converge_value} as n gets large.")

    plt.suptitle('Simulation of Square Throwing Probability', fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit suptitle
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
