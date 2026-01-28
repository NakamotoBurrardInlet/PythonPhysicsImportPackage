import numpy as np
from phys_eval_sol import PhysEvalEngine, PhysicsConstants

def run_master_evaluation():
    # 1. Initialization of the AI-Driven Engine
    # The engine acts as the central neuron, connecting all sub-modules.
    engine = PhysEvalEngine()
    
    print(f"{'='*60}")
    print(f"PHYS_EVAL_SOL: ADVANCED COMPUTATIONAL REPORT")
    print(f"{'='*60}\n")

    # --- DOMAIN 1: RELATIVISTIC KINEMATICS ---
    # Calculating the 'Lorentz Factor' (Gamma) for a particle at high velocity.
    velocity_percent = 0.95
    v = velocity_percent * PhysicsConstants.C
    
    gamma = engine.kinematics.lorentz_factor(v)
    energy = engine.evaluate_energy_equivalence(1.0) * gamma # Relativistic Energy

    print(f" [KINEMATICS & RELATIVITY]")
    print(f" > Target Velocity: {velocity_percent*100}% of C")
    print(f" > Lorentz Factor (γ): {gamma:.6f}")
    print(f" > Total Relativistic Energy (E=γmc²): {energy:.2e} Joules\n")

    # --- DOMAIN 2: CELESTIAL DYNAMICS ---
    # Simulating a satellite in Low Earth Orbit (LEO)
    earth_mass = 5.972e24  # kg
    earth_radius = 6.371e6 # m
    altitude = 400000      # 400km altitude
    total_r = earth_radius + altitude

    v_escape = engine.dynamics.escape_velocity(earth_mass, total_r)
    g_force = engine.dynamics.gravitational_attraction(earth_mass, 1000.0, total_r)

    print(f" [CELESTIAL DYNAMICS - LEO SIMULATION]")
    print(f" > Current Radius: {total_r/1000:.2f} km from center")
    print(f" > Gravitational Pull (1k kg satellite): {g_force:.2f} N")
    print(f" > Required Escape Velocity: {v_escape:.2f} m/s\n")

    # --- DOMAIN 3: VECTORIZED WORK & ENERGY ---
    # Using NumPy arrays to calculate work done by a variable force vector
    force_vector = np.array([10, 25, 0])      # Force in 3D space
    displacement_vector = np.array([5, 2, 0]) # Movement in 3D space
    
    work = engine.dynamics.work_done(force_vector, displacement_vector)
    
    print(f" [MECHANICAL POWER]")
    print(f" > Force Vector: {force_vector} N")
    print(f" > Displacement: {displacement_vector} m")
    print(f" > Net Work Performed: {work:.2f} Joules")
    print(f"\n{'='*60}")

if __name__ == "__main__":
    run_master_evaluation()