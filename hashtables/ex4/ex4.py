def has_negatives(a):
    number_set = {}
    result = []
    for num in a:
        if -num in number_set:
            result.append(abs(num))
        else:
            number_set[num] = True
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
