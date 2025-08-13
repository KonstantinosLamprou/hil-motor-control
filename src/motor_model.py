class VirtualMotor:
    def __init__(self):
        self.T = 0.5 # Zeitkonstante [s] (Motorträgheit)
        self.y = 0.0   # Aktuelle Drehzahl [RPM]
        
    def update(self, u, dt):
        """Simuliert die Motor-Dynamik (PT1-Verhalten)."""
        self.y += (u - self.y) / self.T * dt  # PT1-Differentialgleichung
        return min(self.y, 1200)  