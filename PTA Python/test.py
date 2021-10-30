import numpy as np

arr = np.random.randint(0, 10, (10, 10))
print(arr)
s = 3
flt = np.array(
    [
        [1, 1, 1,],
        [0, 0, 0,],
        [-1, -1, -1]
    ]
)
def convolution(data, flt):
    img_new = []
    m, n = data.shape
    for i in range(m - s + 1):
        line = []
        for j in range(n - s + 1):
            a = data[i: i + s, j: j + s]
            ans = np.sum(np.multiply(a, flt))
            line.append(ans)
        img_new.append(line)
    img_new = np.array(img_new)
    return img_new

print(convolution(arr, flt))