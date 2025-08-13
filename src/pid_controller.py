import time

class PID:
    """Eine manuelle Implementierung eines PID-Reglers mit Anti-Windup."""
    def __init__(self, Kp, Ki, Kd, setpoint, sample_time, output_limits):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.sample_time = sample_time
        self.output_min, self.output_max = output_limits
        
        self._integral = 0
        self._previous_error = 0

    def __call__(self, pv):
        """Berechnet die Stellgröße."""
        error = self.setpoint - pv
        
        # P-Anteil
        p_term = self.Kp * error
        
        # I-Anteil (wird später mit Anti-Windup berechnet)
        i_term = self._integral + self.Ki * error * self.sample_time
        
        # D-Anteil
        derivative = (error - self._previous_error) / self.sample_time
        d_term = self.Kd * derivative
        
        # Vorläufige Stellgröße berechnen, um Sättigung zu prüfen
        output = p_term + i_term + d_term

        # WICHTIG: Anti-Windup Logik
        # Das Integral wird nur dann aktualisiert, wenn der Regler NICHT am Anschlag ist.
        # Dies verhindert das "Aufschaukeln" des I-Anteils.
        if self.output_min < output < self.output_max:
            self._integral = i_term
        
        # Finale Stellgröße mit dem (ggf. unveränderten) Integral neu berechnen
        output = p_term + self._integral + d_term

        # Ausgang begrenzen (Clamping)
        clamped_output = max(self.output_min, min(self.output_max, output))
        
        # Zustand für nächsten Schritt speichern
        self._previous_error = error
        
        return clamped_output

    @property
    def setpoint(self):
        return self._setpoint

    @setpoint.setter
    def setpoint(self, new_setpoint):
        self._setpoint = new_setpoint

def create_pid_controller():
    """Initialisiert den manuellen PID-Regler."""
    return PID(
        Kp=0.005, 
        Ki=0.01, 
        Kd=0.0, 
        setpoint=1000, 
        sample_time=0.01, 
        output_limits=(0, 10)
    )