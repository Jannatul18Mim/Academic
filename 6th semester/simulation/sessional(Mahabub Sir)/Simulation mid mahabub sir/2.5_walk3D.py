import random
import matplotlib.pyplot as plt


def run_3d_random_walk():
    print("--- 3D Random Walk Simulation ---")

    # 1. User Inputs
    try:
        # Initial Positions
        x, y, z = float(input("Start X: ")), float(
            input("Start Y: ")), float(input("Start Z: "))
        start_pos = (x, y, z)

        step_size = float(input("Step size: "))
        total_steps = int(input("Number of steps: "))

        print("\nEnter probabilities (Total should be 1.0):")
        p_forward = float(input("  Forward (+Y): "))
        p_backward = float(input("  Backward (-Y): "))
        p_left = float(input("  Left (-X):     "))
        p_right = float(input("  Right (+X):    "))
        p_up = float(input("  Up (+Z):       "))
        p_down = float(input("  Down (-Z):     "))

        # Validation & Normalization
        probs = [p_forward, p_backward, p_left, p_right, p_up, p_down]
        total_p = sum(probs)
        if not (0.99 <= total_p <= 1.01):
            print(f"Normalizing probabilities (Sum was {total_p})...")
            probs = [p / total_p for p in probs]

    except ValueError:
        print("Invalid input. Please use numbers.")
        return

    # 2. Setup 3D Directions
    # Mapping: (dx, dy, dz)
    directions = ['Forward', 'Backward', 'Left', 'Right', 'Up', 'Down']
    move_map = {
        'Forward':  (0, step_size, 0),
        'Backward': (0, -step_size, 0),
        'Left':     (-step_size, 0, 0),
        'Right':    (step_size, 0, 0),
        'Up':       (0, 0, step_size),
        'Down':     (0, 0, -step_size)
    }

    path_x, path_y, path_z = [x], [y], [z]

    # 3. Simulation Loop
    for _ in range(total_steps):
        move = random.choices(directions, weights=probs, k=1)[0]
        dx, dy, dz = move_map[move]
        x += dx
        y += dy
        z += dz
        
        path_x.append(x)
        path_y.append(y)
        path_z.append(z)

        print("\n" + "="*40)
    print("         WALK SUMMARY")
    print("="*40)
    print(f"Starting Position: ({start_pos[0]}, {start_pos[1]}, {start_pos[2]})")
    print(f"Final Position:    ({x:.2f}, {y:.2f}, {z:.2f})")
    print("-" * 40)

    # 4. 3D Plotting
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot the path
    ax.plot(path_x, path_y, path_z, color='black',
            alpha=0.7, lw=1, label='Path')

    # Mark Start and End
    ax.scatter(start_pos[0], start_pos[1], start_pos[2],
               color='green', s=100, label='Start')
    ax.scatter(x, y, z, color='red', s=100, label='End')

    ax.set_title(f"3D Random Walk ({total_steps} steps)")
    ax.set_xlabel("X (Left/Right)")
    ax.set_ylabel("Y (Forward/Backward)")
    ax.set_zlabel("Z (Up/Down)")
    ax.legend()

    plt.show()

    print(f"\nFinal Position: ({x}, {y}, {z})")


if __name__ == "__main__":
    run_3d_random_walk()
