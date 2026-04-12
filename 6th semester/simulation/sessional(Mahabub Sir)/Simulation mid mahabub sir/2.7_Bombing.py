import numpy as np

def simulate_bombing():
    print("--- Bombing Simulation Configuration ---")
    
    # 1. Get user inputs
    try:
        width = float(input("Enter depot width (X-direction) in meters: "))
        height = float(input("Enter depot height (Y-direction) in meters: "))
        
        sigma_x = float(input("Enter standard deviation for X (e.g., 500): "))
        sigma_y = float(input("Enter standard deviation for Y (e.g., 300): "))
        
        num_bombs = int(input("Enter number of bombs to drop (e.g., 10000): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # 2. Define target boundaries
    # Since the bombers aim at the center (0,0), the limits are +/- half the dimension
    x_limit = width / 2
    y_limit = height / 2
    
    # 3. Generate Random Strikes
    # np.random.normal(mean, std_dev, size)
    strikes_x = np.random.normal(0, sigma_x, num_bombs)
    strikes_y = np.random.normal(0, sigma_y, num_bombs)
    
    # 4. Analysis: Determine Hits
    hits_mask = (np.abs(strikes_x) <= x_limit) & (np.abs(strikes_y) <= y_limit)
    num_hits = np.sum(hits_mask)
    hit_percentage = (num_hits / num_bombs) * 100
    
    # 5. Output Results
    print("\n" + "="*30)
    print(f"SIMULATION RESULTS")
    print("="*30)
    print(f"Target Area:      {width}m x {height}m")
    print(f"Standard Deviation (σ):     X={sigma_x}, Y={sigma_y}")
    print(f"Bombs Dropped:    {num_bombs}")
    print("-" * 30)
    print(f"Total Hits:       {num_hits}")
    print(f"Total Misses:     {num_bombs - num_hits}")
    print(f"Hit Percentage:   {hit_percentage:.2f}%")
    print("="*30)

# Run the interactive simulation
if __name__ == "__main__":
    simulate_bombing()
