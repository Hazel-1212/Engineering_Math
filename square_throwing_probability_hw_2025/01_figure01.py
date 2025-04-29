import matplotlib.pyplot as plt
import numpy as np

# Objective : Generate a plot of the probability of a square intersecting the x-axis
# Figure 1 : Simulation of 
# fY,Θ(y, θ) = 1 / π*l , ∀(y, θ) ∈ [0, 2l] × [0,2/π]
# fY,Θ(y, θ) = 0, otherwise.

edge=1

def intersects_x_axis(Y, theta):
    """
    Given center M=(0,Y) and angle theta, determine whether
    square intersects x-axis.
    """
    if theta>np.pi/4:
        theta = np.pi/2 - theta
    if Y<=edge*np.sqrt(2)*np.cos(theta):
        return True
    else:
        return False
    
def simulate_square_throwing(T, edge=1):
    """
    Simulate the square throwing process and return the probability of intersection with the x-axis.
    """
    q_n_values = []
    
    for N in T:
        a_k = []
        for _ in range(N):
            Y = np.random.uniform(0, 2 * edge)
            theta = np.random.uniform(0, np.pi / 2)
            a_k.append(1 if intersects_x_axis(Y, theta) else 0)
        q_n = np.mean(a_k)
        q_n_values.append(q_n)
    
    return q_n_values

def draw_plot(fig, T, q_n_values, i):
    """
    Draw the plot for the given T and q_n_values.
    """
    ax = fig.add_subplot(2, 2, i)
    ax.set_ylim(0,1)
    ax.plot(T, q_n_values, marker='o', linestyle='-', color='b')
    ax.set_xscale('log')
    ax.set_xlabel('N (Number of Throws)')
    ax.set_ylabel('q_n (Probability)')
    ax.set_title(f'{i} round')
    ax.grid(True)
        
def main():
    # n values for simulation
    T = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000,
         50000, 100000, 500000, 1000000]
    
    fig = plt.figure(figsize=(20, 10))
    plt.title('Simulation of Square Throwing Probability', fontsize=16)
    
    for i in range(1, 5):
        q_n_values = simulate_square_throwing(T, edge)
        draw_plot(fig, T, q_n_values, i)
        converge_value=np.floor(q_n_values[12]*1000)/1000 # Convergence value to 3 decimal places
    
    print("The result gets close to {} as n gets large".format(converge_value))
    plt.tight_layout()
    plt.show()
    plt.savefig('figure_01.png', dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    main()
    