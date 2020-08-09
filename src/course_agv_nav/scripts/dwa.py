import math
import numpy as np


"""
Dynamic window approach implementation with python
Reference: The Dynamic Window Approach to Collision Avoidance
https://www.ri.cmu.edu/pub_files/pub1/fox_dieter_1997_1/fox_dieter_1997_1.pdf
"""
class DWAPlanner():
    def __init__(self):
        # robot parameter
        self.max_speed = 0.8  # [m/s]
        self.predict_time = 2  # [s]

    def plan(self, x, goal, ob):
        # x: [x(m), y(m), yaw(rad), v(m/s), w(rad/s)]
        # search space: generate allowable v & yaw
        v_min = None
        v_max = None
        w_min = None
        w_max = None

        # maximize object function: find the best v & yaw
        best_u = [0.0, 0.0]

        return best_u

    def predict_trajectory(self, x_init, v, w):
        """
        Predict trajectory: return trajectory in predict time
        """
        pass

    def check_collision(self, trajectory, ob):
        """
        Check Collision: return true if collision happens
        """
        pass

    def heading_obj_func(self, trajectory, goal):
        """
        Target heading: heading is a measure of progress towards the goal location.
        It is maximal if the robot moves directly towards the target.
        """
        pass

    def clearance_obj_func(self, trajectory, ob):
        """
        Clearance: dist is the distance to the closest obstacle on the trajectory.
        The smaller the distance to an obstacle the higher is the robot's desire to move around it.
        """
        pass

    def velocity_obj_func(self, trajectory):
        """
        Velocity: vel is the forward velocity of the robot and supports fast movements.
        """
        pass
