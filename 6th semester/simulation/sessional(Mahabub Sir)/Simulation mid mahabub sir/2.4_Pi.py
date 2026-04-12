import random
import math

def simulate_pi_table(num_points=20):
    print(f"{'Point':<8} {'R1 (x)':<10} {'R2 (y)':<10} {'sqrt(1-R1²)':<15} {'Result':<8}")
    print("-" * 55)
    
    hits = 0
    
    for i in range(1, num_points + 1):
        # Generate random numbers between 0 and 1
        r1 = random.random()
        r2 = random.random()
        
        # Calculate the boundary value: sqrt(1 - R1^2)
        boundary = math.sqrt(1 - r1**2)
        
        # Determine if it's "In" or "Out"
        # Point is inside if R2 <= boundary
        if r2 <= boundary:
            result = "In"
            hits += 1
        else:
            result = "Out"
            
        # Print the row formatted like the table in the image
        print(f"{i:<8} {r1:<10.2f} {r2:<10.2f} {boundary:<15.4f} {result:<8}")

    # Final Calculation
    pi_estimate = (hits / num_points) * 4
    
    print("-" * 55)
    print(f"Total Points (N): {num_points}")
    print(f"Points Inside (M): {hits}")
    print(f"Value of Pi ~ (4 * {hits}/{num_points}) = {pi_estimate:.3f}")

# Run simulation with 20 points (similar to the book's sample size)
simulate_pi_table(20)
