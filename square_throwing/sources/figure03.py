import figure01
import numpy as np
import matplotlib.pyplot as plt

edge=1  # Length of the square

def simulate_square_throwing(T, edge=1):
    """
    Simulate the square throwing process and return w_n values.
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

    def area(Y, theta):
        """
        Calculate the area of the square below the x-axis.
        """

        Yb = Y - edge * np.sqrt(2) * np.sin(theta) / 2 # Y coordinate of the B point of the square
        Yc = Y - edge * np.sqrt(2) * np.cos(theta) / 2 # Y coordinate of the C point of the square

        sub_theta =  theta # Angle between the BD line and the x-axis
        if theta > np.pi / 4:
            sub_theta = np.pi / 2 - theta # Because the area below the x-axis is symmetric.
        
        if Yb < 0 and Yc < 0: # If both Yb and Yc are below the x-axis, the area is a trapezoid.
            area = ( abs(Yb) + abs(Yc) )* edge * np.sin(sub_theta + np.pi/4) / 2

        elif Yb < 0 or Yc < 0:  # If one of Yb or Yc is below the x-axis, the area is a triangle.
            area = pow((Y - edge * np.sqrt(2) * np.cos(sub_theta) / 2),2) / (2*np.sin( sub_theta + np.pi/4 ) * np.cos(sub_theta + np.pi/4))
        
        #print(f"Y: {Y}, theta: {theta}, area: {area}")
        return area
    
    w_n_values = []
    for N in T:
        count = 0
        for _ in range(N):
            Y= generate_Y()
            theta = np.random.uniform(0, np.pi / 2)
            if figure01.intersects_x_axis(Y, theta):
                count += area(Y, theta)  # Count the area of the square below the x-axis

        w_n = count / N
        w_n_values.append(w_n)

    return w_n_values

def draw_plot(T, w_n_values, i):
    """
    Draw a subplot for the given simulation results.
    """
    ax = plt.subplot(1, 2, i)
    ax.plot(T, w_n_values, marker='o', linestyle='-', color='b')
    ax.set_xscale('log')
    if i == 1:
        ax.set_ylim(0, 0.5)
    else:
        ax.set_ylim(0, 0.02)
    ax.set_xlabel('n (Number of Throws)')
    ax.set_ylabel('$w_n$ ')

    if i==1:
        ax.set_title(f'Original Image',fontdict={'fontsize': 10})
    elif i == 2:
        ax.set_title(f'Enlarged Image',fontdict={'fontsize': 10}) # Enlarged Image

    ax.grid(True)


def main():
    T = [1, 5, 10, 50, 100, 500, 1000, 5000,
         10000, 50000, 100000, 500000, 1000000]

    plt.figure(figsize=(10, 5))

    # Simulate the square throwing process and draw plots
    for i in range(1, 3):
        if i == 1:
            w_n_values = simulate_square_throwing(T, edge)
            draw_plot(T, w_n_values, i)
            converge_value = w_n_values[-1]
            plt.axhline(y=converge_value, color='r', linestyle='--', label=f'E[W] ≈ {converge_value}')  
        else:
            draw_plot(T, w_n_values, i)
            plt.axhline(y=converge_value, color='r', linestyle='--', label=f'E[W] ≈ {converge_value}')
        
    # Print the results
    print("Simulated Results")
    data = [(T[i], w_n_values[i]) for i in range(len(T))]

    for i in range(len(data)):
        print(f"Simulated {data[i][0]} throws: w_n = {data[i][1]:.4f}")
    
    print("-" * 20)
    print("Conclusion :")
    print("E[W] ≈ {:^.4f}.".format(converge_value))

    plt.suptitle('Estimation of Intersection Area', fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])  
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
    

