import random
import matplotlib.pyplot as plt

def run_random_walk():
    print("--- Random Walk Simulation Parameters ---")
    
    # 1. User Inputs
    try:
        # Initial Position
        start_x = float(input("Enter initial X position: "))
        start_y = float(input("Enter initial Y position: "))
        
        # Step Size
        step_size = float(input("Enter step size: "))
        
        # Probabilities
        p_forward = float(input("Enter probability for Forward (e.g., 0.5): "))
        p_left = float(input("Enter probability for Left (e.g., 0.3): "))
        p_right = float(input("Enter probability for Right (e.g., 0.1): "))
        p_backward = float(input("Enter probability for Backward (e.g., 0.1): "))
        
        # Total Steps
        total_steps = int(input("Enter total number of steps: "))

        # Validation: Probabilities must sum to 1
        total_p = p_forward + p_left + p_right + p_backward
        if not (0.99 <= total_p <= 1.01): # Allowing for minor float rounding
            print(f"\nWarning: Probabilities sum to {total_p}. They should sum to 1.0.")
            print("Normalizing probabilities automatically...")
            p_forward /= total_p
            p_left /= total_p
            p_right /= total_p
            p_backward /= total_p

    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # 2. Setup Simulation
    directions = ['Forward', 'Left', 'Right', 'Backward']
    probabilities = [p_forward, p_left, p_right, p_backward]
    
    current_x, current_y = start_x, start_y
    path_x = [current_x]
    path_y = [current_y]

    # 3. Simulation Loop
    for i in range(total_steps):
        # Choose direction based on weighted probabilities
        move = random.choices(directions, weights=probabilities, k=1)[0]
        
        if move == 'Forward':
            current_y += step_size
        elif move == 'Backward':
            current_y -= step_size
        elif move == 'Left':
            current_x -= step_size
        elif move == 'Right':
            current_x += step_size
            
        path_x.append(current_x)
        path_y.append(current_y)

    # 4. Display Results
    print("\n" + "="*30)
    print(f"SIMULATION COMPLETE")
    print("="*30)
    print(f"Final Position: ({current_x}, {current_y})")
    print(f"Total Displacement: {((current_x-start_x)**2 + (current_y-start_y)**2)**0.5:.2f} units")

    # 5. Plotting (Recreating Fig 2.5)
    plt.figure(figsize=(8, 10))
    plt.plot(path_x, path_y, marker='o', markersize=3, linestyle='-', color='black', alpha=0.7)
    plt.scatter(start_x, start_y, color='green', label='Start', zorder=5)
    plt.scatter(current_x, current_y, color='red', label='End', zorder=5)
    
    plt.title(f"Random Walk Trace ({total_steps} steps)")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_random_walk()
