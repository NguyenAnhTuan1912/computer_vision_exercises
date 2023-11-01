# GPU Accelerated Computing
import torch
import time

x = torch.rand(1, 6400)
y = torch.rand(6400, 5000)

device = "cpu"

# Define a simple benchmark function
def calculateComputingTime(x, y):
  start = time.time()
  z = x @ y
  end = time.time()
  return (start, end)

# Check if computer support GPU Computing (or Computer has GPU :))
if torch.cuda.is_available():
  device = "cuda"

# Set GPU Computing
x, y = x.to(device), y.to(device)

# Start
start, end = calculateComputingTime(x, y)
# End

print("Time (GPU): ", end - start)

# Back to CPU Computing
x, y = x.cpu(), y.cpu()

# Start
start, end = calculateComputingTime(x, y)
# End

print("Time (CPU): ", end - start)