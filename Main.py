from typing import List
def parition(data, low, high) -> List[int]:
    i = (low-1)
    pivot = data[high]
    for j in range(low, high):
        if data[j] < pivot:
            i = i+1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return (i+1)

def quick_sort(data, low, high) -> List[int]:
    # Write code here
    if low < high:
        pi = parition(data, low, high)
        quick_sort(data, low, pi-1)
        quick_sort(data, pi+1, high)
    return data


input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(quick_sort(data, 0, len(data)-1))
