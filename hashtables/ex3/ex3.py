def intersection(arrays):
    num_counts = {}
    for array in arrays:
        for num in array:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1
    return [num for num in num_counts.keys() if num_counts[num] == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
