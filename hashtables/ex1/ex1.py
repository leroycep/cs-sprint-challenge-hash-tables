def get_indices_of_item_weights(weights, length, limit):
    num_indices = {}
    for (idx, weight) in enumerate(weights):
        complement = limit - weight
        if complement in num_indices:
            complement_idx = num_indices[complement]
            return (idx, complement_idx)
        else: # complement not in num_indices
            num_indices[weight] = idx
    return None
