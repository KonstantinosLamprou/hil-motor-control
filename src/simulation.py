import time
import matplotlib.pyplot as plt
from motor_model import VirtualMotor
from pid_controller import create_pid_controller

# 1. Systeme initialisieren
motor = VirtualMotor()
pid = create_pid_controller()
dt = 0.01  # Zeitschritt [s]

# 2. Logging-Variablen (JETZT MIT setpoint_log)
time_log = []      # Zeitpunkte
rpm_log = []       # Tatsächliche Drehzahl
voltage_log = []   # Stellspannung
setpoint_log = []  # Neu: Sollwertverlauf

# 3. Simulations-Loop
for step in range(3000):
    # ---- Sollwert-Änderung nach 15 Sekunden ----
    if step == 1500:
        pid.setpoint = 500
        print(f"\nSollwert geändert auf 500 RPM bei t={step*dt:.1f}s\n")
    
    # ---- Regelung ----
    voltage = pid(motor.y)
    rpm = motor.update(voltage, dt)
    print(f"Step {step}: RPM={rpm:.1f}, Voltage={voltage:.2f}, Error={pid.setpoint-rpm:.1f}")
    
    # ---- Daten speichern ----
    time_log.append(step * dt)
    rpm_log.append(rpm)
    voltage_log.append(voltage)
    setpoint_log.append(pid.setpoint)  # Funktioniert jetzt!
    
    # ---- Debug-Ausgabe ----
    if step % 100 == 0:
        print(f"t={step*dt:.1f}s | RPM={rpm:.1f} | Voltage={voltage:.2f}V")

# 4. Ergebnisse plotten (MIT Sollwert)
plt.figure(figsize=(10, 5))
plt.plot(time_log, rpm_log, label="Drehzahl [RPM]")
plt.plot(time_log, voltage_log, label="Stellspannung [V]")
plt.plot(time_log, setpoint_log, 'r--', label="Sollwert [RPM]")  # Sollwert-Linie
plt.xlabel("Zeit [s]")
plt.title("PID-Regelung mit Sollwertänderung")
plt.legend()
plt.grid()
plt.show()