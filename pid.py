from simple_pid import PID
import time
import matplotlib.pyplot as plt

# Setpoint and initial process value
setpoint = 5
process_value = 0.0

# Initialize the PID controller
pid = PID(1, 0, 0.1, setpoint=setpoint)

# Lists to store data for plotting
time_values = []
process_values = []
control_values = []

# Simulation parameters
duration = 25  # in seconds
interval = 0.1  # in seconds

# Run the PID controller
start_time = time.time()
while (time.time() - start_time) < duration:
    control = pid(process_value)
    process_value += control

    # Simulate the process value (for example)
    process_value -= process_value * 0.1

    # Store data for plotting
    current_time = time.time() - start_time
    time_values.append(current_time)
    process_values.append(process_value)
    control_values.append(control)

    # Wait for a bit before the next iteration
    time.sleep(interval)

# Plot the process value and control value over time
plt.figure(figsize=(10, 5))
plt.plot(time_values, process_values, label='Process Value')
plt.plot(time_values, [setpoint] * len(time_values), 'r--', label='Setpoint')
plt.xlabel('Time (s)')
plt.ylabel('Process Value')
plt.title('PID Controller Response')
plt.legend()
plt.grid(True)
plt.show()
