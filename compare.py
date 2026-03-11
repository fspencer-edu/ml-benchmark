import json

mac_file = "artifacts-mac/results.json"
pc_file = "artifacts-pc/results.json"

with open(mac_file) as f:
    mac = json.load(f)

with open(pc_file) as f:
    pc = json.load(f)

print("\n=== Benchmark Comparison ===\n")

print(f"Mac machine: {mac['machine']}")
print(f"Architecture: {mac['arch']}")
print(f"CPU cores: {mac['cpu_count']}")
print(f"Training time: {mac['train_seconds']} seconds")
print(f"Accuracy: {mac['accuracy']}\n")

print(f"PC machine: {pc['machine']}")
print(f"Architecture: {pc['arch']}")
print(f"CPU cores: {pc['cpu_count']}")
print(f"Training time: {pc['train_seconds']} seconds")
print(f"Accuracy: {pc['accuracy']}\n")

speedup = mac["train_seconds"] / pc["train_seconds"]

print("=== Performance Difference ===\n")
print(f"Speedup (PC vs Mac): {speedup:.2f}x faster")

time_diff = mac["train_seconds"] - pc["train_seconds"]
print(f"Time saved: {time_diff:.4f} seconds")

acc_diff = abs(mac["accuracy"] - pc["accuracy"])
print(f"Accuracy difference: {acc_diff:.6f}")

print("\nSummary")
print("-" * 40)
print(f"{'Metric':<15}{'Mac':<12}{'PC'}")
print("-" * 40)
print(f"{'CPU Cores':<15}{mac['cpu_count']:<12}{pc['cpu_count']}")
print(f"{'Train Time':<15}{mac['train_seconds']:<12}{pc['train_seconds']}")
print(f"{'Accuracy':<15}{mac['accuracy']:<12}{pc['accuracy']}")