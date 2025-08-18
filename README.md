# hil-motor-control
Hardware-in-the-Loop Simulation of a PID-controlled DC motor using Python

Overview
This project simulates a PID controller for a virtual DC motor. The implementation includes:

A virtual motor model with PT1 behavior (first-order lag system)

A manually implemented PID controller with anti-windup protection

A simulation environment with logging and visualization capabilities

Components
1. Virtual Motor Model (motor_model.py)
The VirtualMotor class simulates a DC motor with:

Time constant T = 0.5s (motor inertia)

Gain K = 120 RPM/V (10V input → 1200 RPM)

PT1 transfer function behavior

Methods:

update(u, dt): Updates motor speed based on input voltage and timestep

2. PID Controller (pid_controller.py)
The PID class implements a complete PID controller with:

Proportional, Integral, and Derivative terms

Anti-windup protection

Output clamping

Configurable sample time

Key Features:

Anti-windup prevents integral term accumulation when output is saturated

Configurable output limits (0-10V by default)

Settable target (setpoint)

3. Main Simulation (main.py)
The simulation:

Initializes motor and PID controller

Runs a 30-second simulation (3000 steps at 0.01s timestep)

Changes setpoint from 1000 RPM to 500 RPM at 15 seconds

Logs and visualizes results

Configuration
PID Parameters
Default values (can be modified in create_pid_controller()):

python
Kp = 0.08  # Proportional gain
Ki = 0.02  # Integral gain
Kd = 0.00  # Derivative gain (disabled by default)
Motor Parameters
python
T = 0.5    # Time constant [s]
K = 120    # Gain [RPM/V]
Usage
Run main.py to execute the simulation

The script will:

Simulate motor control for 30 seconds

Print status updates every second

Generate a plot showing:

Actual RPM (blue)

Setpoint RPM (red dashed)

Control voltage (green dotted)

Visualization
The plot shows:

Left Y-axis: Motor speed in RPM

Right Y-axis: Control voltage in Volts

X-axis: Time in seconds

Example output shows:

Initial convergence to 1000 RPM

Transient response when setpoint changes to 500 RPM

Control voltage adjustments

Customization
To experiment with different settings:

Adjust PID gains in create_pid_controller()

Modify motor parameters in VirtualMotor class

Change simulation duration or timestep in main loop

Adjust setpoint change timing (currently at 15 seconds)

Requirements
Python 3.x

Matplotlib (for visualization)

(Optional) Jupyter Notebook for interactive experimentation

Files
motor_model.py - Virtual motor implementation

pid_controller.py - PID controller implementation

main.py - Simulation and visualization

Notes
The current implementation uses a manual PID implementation for educational purposes

Anti-windup is implemented by only updating the integral term when the output isn't saturated

The derivative term is disabled by default (Kd=0) but can be enabled for experimentation
