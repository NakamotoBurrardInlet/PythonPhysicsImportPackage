from .dynamics import DynamicsEvaluator
from .kinematics import MotionEvaluator
from .constants import PhysicsConstants

class PhysEvalEngine:
    def __init__(self):
        self.kinematics = MotionEvaluator()
        self.dynamics = DynamicsEvaluator()  # New Power Link
        
    def orbital_analysis(self, planet_mass, satellite_mass, distance):
        force = self.dynamics.gravitational_attraction(planet_mass, satellite_mass, distance)
        v_escape = self.dynamics.escape_velocity(planet_mass, distance)
        return {"force_n": force, "escape_v_ms": v_escape}
    

    def evaluate_force(self, mass: float, acceleration: float) -> dict:
        """Newtons Second Law: F = ma"""
        force = mass * acceleration
        return {
            "magnitude": force,
            "unit": "Newtons",
            "relativistic_mass": None
        }

    def evaluate_energy_equivalence(self, mass: float) -> float:
        """Einstein's Mass-Energy Equivalence: E = mc^2"""
        return mass * (PhysicsConstants.C ** 2)