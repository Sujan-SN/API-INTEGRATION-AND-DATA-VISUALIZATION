import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Bangalore coordinates
url = "https://api.open-meteo.com/v1/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m,relativehumidity_2m"

response = requests.get(url)
data = response.json()

# Extract data
times = data['hourly']['time'][:10]
temps = data['hourly']['temperature_2m'][:10]
humidity = data['hourly']['relativehumidity_2m'][:10]

# Plot
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))

plt.plot(times, temps, marker='o', label="Temperature (°C)")
plt.plot(times, humidity, marker='s', label="Humidity (%)")

plt.xticks(rotation=45)
plt.title("Weather Data (Bangalore)")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()

plt.tight_layout()
plt.show()
