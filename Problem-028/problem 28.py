spiral = 3
current_num = 1
total_sum = 1
corners = 0

while spiral <= 1001:
    corners += 1
    current_num += spiral - 1
    total_sum += current_num
    if corners == 4:
        spiral += 2
        corners = 0

print(total_sum)