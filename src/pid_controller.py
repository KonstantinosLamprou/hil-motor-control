from simple_pid import PID

def create_pid_controller():
    """Initialisiert den PID-Regler mit Standardwerten."""
    pid = PID(Kp=3.0, Ki=1.5, Kd=0.5, setpoint=1000) 
    pid.output_limits = (0, 10)  # Stellgröße (0-10V)
    return pid
