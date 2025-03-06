import math

def calculate_distance(p1, p2):
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 3)

num_points = int(input())
points = []
for _ in range(num_points):
    x, y = map(int, input().split())
    points.append((x, y))

distance_matrix = [[float('inf')] * num_points for _ in range(num_points)]
for i in range(num_points):
    for j in range(num_points):
        distance_matrix[i][j] = calculate_distance(points[i], points[j])

min_max_distance = distance_matrix[0][1]
for k in range(num_points):
    for i in range(num_points):
        for j in range(num_points):
            current_max = max(distance_matrix[i][k], distance_matrix[k][j])
            if distance_matrix[i][j] > current_max and current_max < min_max_distance:
                distance_matrix[i][j] = current_max

print(distance_matrix[0][1])