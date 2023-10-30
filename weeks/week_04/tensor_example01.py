import torch

# numpy dau buoi re rach, pytorch can het

low = 0
high = 10

# Define
x = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
y = torch.tensor([[2], [3], [1], [0]])

# 5 x 3
x2 = torch.tensor(torch.randint(low, high, size=(5, 3)))
# 3 x 5
y2 = torch.tensor(torch.randint(low, high, size=(3, 5)))

# Multiply
# Output: Tensor: [[11], [35]] 2x1
# print(torch.matmul(x, y))
# Output: Tensor: [[11], [35]]
# print(x@y)

# Output: Tensor: 5x5
# print(torch.matmul(x2, y2))
# Output: Tensor: 5x5
# print(x2@y2)

# Concatenate
# torch.randn(row, col)
x = torch.randn(2, 3, 2)
z = torch.cat([x, x], axis=1)

print("x: ", x)
print("z: ", z)