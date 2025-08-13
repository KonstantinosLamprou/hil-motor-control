class VirtualMotor:
    def __init__(self):
        self.T = 0.5    # Zeitkonstante [s] (Motorträgheit)
        self.K = 120    # Verstärkung [RPM/V] → 10V = 1200 RPM
        self.y = 0.0    # Aktuelle Drehzahl [RPM]

    def update(self, u, dt):
        """Simuliert die Motor-Dynamik (PT1-Verhalten) mit Verstärkung."""
        target_rpm = self.K * u  # Umrechnung Spannung → Ziel-RPM
        self.y += (target_rpm - self.y) / self.T * dt
        return min(self.y, self.K * 10)  # Begrenzung auf 10V → 1200 RPM
