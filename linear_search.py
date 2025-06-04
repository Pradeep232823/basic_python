def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return f"{target} found at index {i}"
    return "not found"

data=[34,24,64,4,2,64,6]
print(linear_search(data, 64))