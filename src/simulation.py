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
        print(f"\nSollwert geändert auf 500 RPM bei t={step*dt:.1f}s\n")
    
    # Regelung
    voltage = pid(motor.y)
    rpm = motor.update(voltage, dt)
    
    # Daten speichern
    time_log.append(step * dt)
    rpm_log.append(rpm)
    voltage_log.append(voltage)
    setpoint_log.append(pid.setpoint)
    
    # Debug-Ausgabe nur alle 1s
    if step % int(1/dt) == 0:
        print(f"t={step*dt:.1f}s | RPM={rpm:.1f} | Voltage={voltage:.2f}V | Error={pid.setpoint-rpm:.1f}")

# 4. Ergebnisse plotten
plt.figure(figsize=(10, 5))
plt.plot(time_log, rpm_log, label="Drehzahl [RPM]")
plt.plot(time_log, voltage_log, label="Stellspannung [V]")
plt.plot(time_log, setpoint_log, 'r--', label="Sollwert [RPM]")
plt.xlabel("Zeit [s]")
plt.title("PID-Regelung mit Sollwertänderung")
plt.legend()
plt.grid()
plt.show()
