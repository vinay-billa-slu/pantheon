
import matplotlib.pyplot as plt

protocols = ['CUBIC', 'BBR', 'Sprout']

# Average Throughput in Mbps
throughput = [8.5, 9.2, 6.0]

# Average RTT in ms
rtt = [80, 100, 120]

# 95th Percentile RTT
rtt_95th = [110, 130, 160]

# Packet Loss Rate (%)
loss = [1.5, 0.5, 3.0]

# Time-Series Data (Simulated)
time = list(range(0, 61, 10))
cubic_throughput = [1, 3, 5, 6.5, 7.5, 8, 8.5]
bbr_throughput = [2, 4.5, 6.5, 7.8, 8.8, 9.1, 9.2]
sprout_throughput = [1, 2.5, 3.5, 4.2, 5, 5.8, 6.0]

cubic_loss = [0.5, 0.8, 1.0, 1.3, 1.4, 1.5, 1.5]
bbr_loss = [0.2, 0.3, 0.4, 0.5, 0.5, 0.5, 0.5]
sprout_loss = [1.0, 2.0, 2.5, 2.8, 3.0, 3.0, 3.0]

# Plot 1: Throughput over Time
plt.figure(figsize=(8, 5))
plt.plot(time, cubic_throughput, label='CUBIC', marker='o')
plt.plot(time, bbr_throughput, label='BBR', marker='s')
plt.plot(time, sprout_throughput, label='Sprout', marker='^')
plt.title("Throughput over Time")
plt.xlabel("Time (s)")
plt.ylabel("Throughput (Mbps)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("throughput_time.png")
plt.close()

# Plot 2: Loss over Time
plt.figure(figsize=(8, 5))
plt.plot(time, cubic_loss, label='CUBIC', marker='o')
plt.plot(time, bbr_loss, label='BBR', marker='s')
plt.plot(time, sprout_loss, label='Sprout', marker='^')
plt.title("Packet Loss over Time")
plt.xlabel("Time (s)")
plt.ylabel("Loss Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("loss_time.png")
plt.close()

# Plot 3: Average RTT
plt.figure(figsize=(6, 4))
plt.bar(protocols, rtt, color='orange')
plt.title("Average RTT")
plt.ylabel("RTT (ms)")
plt.tight_layout()
plt.savefig("rtt_avg.png")
plt.close()

# Plot 4: 95th Percentile RTT
plt.figure(figsize=(6, 4))
plt.bar(protocols, rtt_95th, color='teal')
plt.title("95th Percentile RTT")
plt.ylabel("RTT (ms)")
plt.tight_layout()
plt.savefig("rtt_95th.png")
plt.close()

# Plot 5: RTT vs Throughput
plt.figure(figsize=(6, 6))
plt.scatter(rtt, throughput)
for i, protocol in enumerate(protocols):
    plt.annotate(protocol, (rtt[i], throughput[i]))
plt.title("RTT vs Throughput")
plt.xlabel("RTT (ms) → Lower is better")
plt.ylabel("Throughput (Mbps) ↑ Higher is better")
plt.grid(True)
plt.tight_layout()
plt.savefig("rtt_vs_throughput.png")
plt.close()

# Plot 6: Loss Rate
plt.figure(figsize=(6, 4))
plt.bar(protocols, loss, color='lightcoral')
plt.title("Packet Loss Rate")
plt.ylabel("Loss Rate (%)")
plt.tight_layout()
plt.savefig("loss_rate.png")
plt.close()

print("✅ Graphs generated successfully!")
