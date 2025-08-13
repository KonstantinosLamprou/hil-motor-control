import matplotlib.pyplot as plt

from motor_model import VirtualMotor
from pid_controller import create_pid_controller


# 1. Systeme initialisieren
motor = VirtualMotor()
pid = create_pid_controller()
dt = 0.01  # Zeitschritt [s]

# 2. Logging-Variablen
time_log = []
rpm_log = []
voltage_log = []
setpoint_log = []

# 3. Simulations-Loop
for step in range(3000):
    # Sollwert-Änderung nach 15 Sekunden
    if step == 1500:
        pid.setpoint = 500
        pid._integral = 0
    # Regelung
    voltage = pid(motor.y) # PID-Regler berechnet die Stellgröße
    motor.update(voltage, dt) # Motor-Modell wird aktualisiert
    
    # Daten speichern
    time_log.append(step * dt)
    rpm_log.append(motor.y)
    voltage_log.append(voltage)
    setpoint_log.append(pid.setpoint)
    
    # Debug-Ausgabe nur alle 1s
    if step > 0 and step % int(1/dt) == 0:
        print(f"t={step*dt:.1f}s | RPM={motor.y:.1f} | Voltage={voltage:.2f}V | Error={pid.setpoint-motor.y:.1f}")

# # 4. Ergebnisse plotten (leicht verbessert für Lesbarkeit)
# plt.figure(figsize=(12, 7))
# plt.plot(time_log, rpm_log, label="Drehzahl [RPM]", linewidth=2, color='blue')
# plt.plot(time_log, setpoint_log, 'r--', label="Sollwert [RPM]", linewidth=2)

# # Spannung auf einer zweiten y-Achse für bessere Übersicht
# ax2 = plt.gca().twinx()
# ax2.plot(time_log, voltage_log, label="Stellspannung [V]", linestyle='-.', color='green', alpha=0.8)
# ax2.set_ylabel("Stellspannung [V]")
# ax2.set_ylim(0, 11)

# # Haupt-Achsenbeschriftungen
# plt.gca().set_xlabel("Zeit [s]")
# plt.gca().set_ylabel("Drehzahl [RPM]")
# plt.title("Stabile PID-Regelung (Manuelle Implementierung)")
# plt.grid(True)

# # Legenden von beiden Achsen kombinieren
# lines, labels = plt.gca().get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(lines + lines2, labels + labels2, loc='center right')

# plt.show() # Zeigt den Plot an

# Plot mit korrigierter Legende
plt.figure(figsize=(12, 7))

# Hauptplot (Drehzahl & Sollwert)
plt.plot(time_log, rpm_log, label="Drehzahl [RPM]", linewidth=2, color='blue')
plt.plot(time_log, setpoint_log, 'r--', label="Sollwert [RPM]", linewidth=2)
plt.xlabel("Zeit [s]")
plt.ylabel("Drehzahl [RPM]")
plt.grid(True)

# Zweite Y-Achse für Spannung (OHNE label im plot-Befehl)
ax2 = plt.gca().twinx()
ax2.plot(time_log, voltage_log, linestyle='-.', color='green', alpha=0.8)  # Label entfernt
ax2.set_ylabel("Stellspannung [V]", color='green')  # Farbe angepasst
ax2.tick_params(axis='y', colors='green')  # Skala in Grün
ax2.set_ylim(0, 11)

# Manuelle Legende (explizite Steuerung)
from matplotlib.lines import Line2D  # Für benutzerdefinierte Legenden-Einträge
legend_elements = [
    Line2D([0], [0], color='blue', lw=2, label='Drehzahl [RPM]'),
    Line2D([0], [0], linestyle='--', color='red', lw=2, label='Sollwert [RPM]'),
    Line2D([0], [0], linestyle='-.', color='green', alpha=0.8, lw=2, label='Stellspannung [V]')
]
plt.legend(handles=legend_elements, loc='center right')

plt.title("PID-Regelung: Virtueller Motor (optimiert)")
plt.tight_layout()
plt.show()
