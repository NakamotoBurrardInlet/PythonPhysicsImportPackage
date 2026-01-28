import numpy as np

class MotionEvaluator:
    @staticmethod
    def calculate_displacement(u: float, t: float, a: float) -> float:
        """Calculates s = ut + 0.5at^2"""
        return (u * t) + (0.5 * a * (t**2))

    @staticmethod
    def final_velocity(u: float, a: float, t: float) -> float:
        """Calculates v = u + at"""
        return u + (a * t)

    @staticmethod
    def lorentz_factor(v: float) -> float:
        """Calculates the relativistic gamma factor."""
        from .constants import PhysicsConstants as pc
        if v >= pc.C:
            raise ValueError("Velocity cannot exceed the speed of light.")
        return 1 / np.sqrt(1 - (v**2 / pc.C**2))