import math
from rich import print


def euclidean_distance(vec1: list, vec2: list) -> float:
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same dimension")

    sum_squares = sum((x - y) ** 2 for x, y in zip(vec1, vec2))
    return math.sqrt(sum_squares)


def nearest_neighbor_search(query_vector: list, dataset: list[list]) -> tuple:
    if not dataset:
        raise ValueError("Dataset cannot be empty")
    best_match = None
    best_distance = float("inf")

    for vector in dataset:
        if len(vector) != len(query_vector):
            raise ValueError("All vectors must have the same dimension")

        distance = euclidean_distance(query_vector, vector)
        if distance < best_distance:
            best_distance = distance
            best_match = vector

    return best_match, best_distance


dataset = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21],
    [22, 23, 24],
    [25, 26, 27],
    [28, 29, 30],
    [31, 32, 33],
    [34, 35, 36],
    [37, 38, 39],
    [40, 41, 42],
    [43, 44, 45],
    [46, 47, 48],
    [49, 50, 51],
    [52, 53, 54],
    [55, 56, 57],
    [58, 59, 60],
    [61, 62, 63],
    [64, 65, 66],
    [67, 68, 69],
    [70, 71, 72],
    [73, 74, 75],
    [76, 77, 78],
    [79, 80, 81],
    [82, 83, 84],
    [85, 86, 87],
    [88, 89, 90],
    [91, 92, 93],
    [94, 95, 96],
    [97, 98, 99],
    [100, 101, 102],
    [103, 104, 105],
    [106, 107, 108],
    [109, 110, 111],
    [112, 113, 114],
    [115, 116, 117],
    [118, 119, 120],
    [121, 122, 123],
    [124, 125, 126],
    [127, 128, 129],
    [130, 131, 132],
    [133, 134, 135],
    [136, 137, 138],
    [139, 140, 141],
    [142, 143, 144],
    [145, 146, 147],
    [148, 149, 150],
    [151, 152, 153],
    [154, 155, 156],
    [157, 158, 159],
    [160, 161, 162],
    [163, 164, 165],
]

query_vector = [8, 11, 14]

best_match, best_distance = nearest_neighbor_search(query_vector, dataset)

print("Query Vector:", query_vector)
print("Best Match:", best_match)
print("Distance:", best_distance)
