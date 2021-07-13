"""Week I Assignment
Simulate the trajectory of a robot approximated using a unicycle model given the
following start states, dt, velocity commands and timesteps
State = (x, y, theta);
Velocity = (v, w) 
1. Start=(0, 0, 0); dt=0.1; vel=(1, 0.5); timesteps: 25
2. Start=(0, 0, 1.57); dt=0.2; vel=(0.5, 1); timesteps: 10
3. Start(0, 0, 0.77); dt=0.05; vel=(5, 4); timestep: 50
Upload the completed python file and the figures of the three sub parts in classroom
"""
import numpy as np
import matplotlib.pyplot as plt
import math

class Unicycle:
    def __init__(self, x: float, y: float, theta: float, dt: float):
        self.x = x
        self.y = y
        self.theta = theta
        self.dt = dt

        # Store the points of the trajectory to plot
        self.x_points = [self.x]
        self.y_points = [self.y]

    def step(self, v: float, w: float, n: int):
        
        self.v = v
        self.w = w
        self.n = n
        t = 0.0
        while(t <= (n * self.dt)):
            t = t + 0.1
            vx = v * math.cos(self.theta + (w * t))
            vy = v * math.sin(self.theta + (w * t))

            xf = self.x + (vx * t)
            yf = self.y + (vy * t)
            thetaf = self.theta + (w * t)

            self.x_points.append(xf)
            self.y_points.append(yf)

            if(t == (n * self.dt)):
                return xf, yf, thetaf

            """"
        Write the Kinematics model here
                Expectation:
            1. Given v, w and the current state self.x, self.y, self.theta
                and control commands (v, w) for n timesteps, i.e. n * dt seconds,
                return the final pose (x, y, theta) after this time.
            2. Append all intermediate points into the self.x_points, self.y_points list
                for plotting the trajectory.
        Args:
            v (float): linear velocity
            w (float): angular velocity
            n (int)  : timesteps
        Return:
            x, y, theta (float): final pose 
        """

    def plot(self, v: float, w: float):
        """Function that plots the intermeditate trajectory of the Robot"""
        plt.title(f"Unicycle Model: {v}, {w}")
        plt.xlabel("X-Coordinates")
        plt.ylabel("Y-Coordinates")
        plt.plot(self.x_points, self.y_points, color="red", alpha=0.75)
        plt.grid()
        plt.show()

        # If you want to view the plot uncomment plt.show() and comment out plt.savefig()
        # If you want to save the file, uncomment plt.savefig() and comment out plt.show()
        # plt.savefig(f"Unicycle_{v}_{w}.png")

if __name__ == "__main__":
    print("Unicycle Model Assignment")

xi = float(input("Enter intial x coordinate"))
yi = float(input("Enter intial y coordinate"))
thetai = float(input("Enter intial theta"))
dti = float(input("Enter time dt"))
vel = float(input("Enter linear velocity"))
angv = float(input("Enter angular velocity"))
timestp = float(input("Enter timesteps"))


ob1 = Unicycle(xi, yi, thetai, dti)
ob1.step(vel, angv, timestp)
ob1.plot(vel, angv)

