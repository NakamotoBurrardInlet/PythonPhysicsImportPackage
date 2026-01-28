import numpy as np
from typing import Union, Dict, Optional
from .constants import PhysicsConstants as pc

class DynamicsEvaluator:
    """
    A high-computational suite for Classical and Celestial Dynamics.
    Handles force vectors, gravitational fields, and energy transitions.
    """

    @staticmethod
    def calculate_centripetal_force(mass: float, velocity: float, radius: float) -> float:
        """
        Calculates the force required to maintain circular motion.
        Formula: F = (m * v^2) / r
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive non-zero value.")
        return (mass * (velocity**2)) / radius

    @staticmethod
    def gravitational_attraction(m1: float, m2: float, distance: float) -> float:
        """
        Newton's Law of Universal Gravitation.
        Formula: F = G * (m1 * m2) / r^2
        """
        if distance <= 0:
            raise ValueError("Distance between centers of mass must be positive.")
        return pc.G * (m1 * m2) / (distance**2)

    @staticmethod
    def escape_velocity(mass_of_body: float, radius: float) -> float:
        """
        Calculates the velocity required to escape a gravitational well.
        Formula: v_e = sqrt(2GM / r)
        """
        return np.sqrt((2 * pc.G * mass_of_body) / radius)

    @staticmethod
    def work_done(force: Union[float, np.ndarray], 
                  displacement: Union[float, np.ndarray], 
                  theta: float = 0.0) -> float:
        """
        Calculates Work: W = F * d * cos(theta).
        Supports both scalar magnitudes and vector dot products.
        """
        if isinstance(force, np.ndarray) and isinstance(displacement, np.ndarray):
            return np.dot(force, displacement)
        
        # Convert degrees to radians for scalar calculation
        rad = np.radians(theta)
        return float(force * displacement * np.cos(rad))

    @staticmethod
    def kinetic_energy(mass: float, velocity: float) -> float:
        """Calculates Translational Kinetic Energy: Ek = 0.5 * m * v^2"""
        return 0.5 * mass * (velocity**2)

    @staticmethod
    def power_output(work: float, time: float) -> float:
        """Calculates Power: P = W / t (Watts)"""
        if time <= 0:
            raise ZeroDivisionError("Time interval must be greater than zero.")
        return work / time