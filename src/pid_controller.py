from simple_pid import PID

def create_pid_controller():
    """Initialisiert den PID-Regler mit Standardwerten."""
    # Verwende sehr kleine Werte, um ein stabiles Verhalten zu testen
    pid = PID(Kp=0.1, Ki=0.01, Kd=0.001, setpoint=1000, proportional_on_measurement=False)
    pid.output_limits = (0, 10)  # Stellgröße (0-10V)
    return pid