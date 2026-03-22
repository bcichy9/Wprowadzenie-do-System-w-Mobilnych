import numpy as np
import time
import matplotlib.pyplot as plt

S = 5
LAMBDA = 2.0
N = 10
SIGMA = 3
QUEUE_SIZE = 20


channels = [0] * S
queue = []
wait_times = []
served = 0

arrival_times = []
service_times = []

time_series_rho = []
time_series_q = []
time_series_w = []

time_pointer = 0


current_time = 0
for _ in range(100):
    inter_arrival = np.random.exponential(1 / LAMBDA)
    current_time += inter_arrival
    arrival_times.append(current_time)

    t = int(np.random.normal(N, SIGMA))
    while t <= 0:
        t = int(np.random.normal(N, SIGMA))
    service_times.append(t)


plt.ion()
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

line_rho, = ax1.plot([], [])
ax1.set_title("Intensywność ruchu (ρ)")

line_q, = ax2.plot([], [])
ax2.set_title("Długość kolejki (Q)")

line_w, = ax3.plot([], [])
ax3.set_title("Średni czas oczekiwania (W)")


t = 0

while True:


    for i in range(S):
        if channels[i] > 0:
            channels[i] -= 1


    while time_pointer < len(arrival_times) and arrival_times[time_pointer] <= t:
        queue.append({
            "service": service_times[time_pointer],
            "wait": 0
        })
        time_pointer += 1


    if time_pointer >= len(arrival_times):
        new_arrival = arrival_times[-1] + np.random.exponential(1 / LAMBDA)
        arrival_times.append(new_arrival)

        t_service = int(np.random.normal(N, SIGMA))
        while t_service <= 0:
            t_service = int(np.random.normal(N, SIGMA))

        service_times.append(t_service)


    for i in range(S):
        if channels[i] == 0 and queue:
            client = queue.pop(0)
            channels[i] = client["service"]
            wait_times.append(client["wait"])
            served += 1


    for client in queue:
        client["wait"] += 1


    if len(queue) > QUEUE_SIZE:
        queue = queue[:QUEUE_SIZE]


    busy_channels = sum(1 for c in channels if c > 0)
    rho = busy_channels / S
    Q = len(queue)
    W = np.mean(wait_times) if wait_times else 0

    time_series_rho.append(rho)
    time_series_q.append(Q)
    time_series_w.append(W)

    line_rho.set_data(range(len(time_series_rho)), time_series_rho)
    line_q.set_data(range(len(time_series_q)), time_series_q)
    line_w.set_data(range(len(time_series_w)), time_series_w)

    for ax in [ax1, ax2, ax3]:
        ax.relim()
        ax.autoscale_view()

    plt.pause(0.01)


    print(f"Czas: {t}s | Kanały: {busy_channels}/{S} | Kolejka: {Q} | Obsłużono: {served}")

    time.sleep(0.1)
    t += 1