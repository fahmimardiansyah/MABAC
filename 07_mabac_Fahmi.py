data = [
    ["Kode", "C1", "C2", "C3", "C4"],
    ["D1", 90, 81, 89, 77],
    ["D2", 70, 80, 80, 85],
    ["D3", 85, 69, 78, 80],
    ["D4", 95, 80, 83, 80],
    ["D5", 82, 75, 85, 82],
    ["D6", 76, 85, 80, 87],
    ["D7", 72, 80, 73, 78],
    ["D8", 68, 72, 79, 86]
]

# Bobot
bobot = [
    ["C1", "C2", "C3", "C4"],
    [25, 30, 25, 20]
]

def print_table(matrix):
    widths = [max(map(len, map(str, col))) for col in zip(*matrix)]
    for row in matrix:
        print("  ".join((str(val).ljust(width) for val, width in zip(row, widths))))

# Tahap 1: Pembentukan matriks keputusan (X)
print("Tahap 1: Pembentukan matriks keputusan (X)")
print_table(data)
print()

# Tahap 2: Normalisasi matriks keputusan (X)
norm_data = [data[0]]
cols = list(zip(*data[1:]))  # Mengubah hasil zip menjadi list agar bisa diakses menggunakan indeks
mins = [min(col) for col in cols[1:]]
maxs = [max(col) for col in cols[1:]]
for row in data[1:]:
    norm_data.append([row[0]] + [(row[i] - mins[i-1]) / (maxs[i-1] - mins[i-1]) for i in range(1, len(row))])

print("Tahap 2: Matriks Keputusan (X) Setelah Normalisasi:")
print_table(norm_data)
print()

# Tahap 3: Perhitungan elemen matriks tertimbang (V)
weighted_matrix = [data[0]]
for row in norm_data[1:]:
    weighted_matrix.append([row[0]] + [row[i] * bobot[1][i-1] + bobot[1][i-1] for i in range(1, len(row))])

print("Tahap 3: Perhitungan Elemen Matriks Tertimbang (V):")
print_table(weighted_matrix)
print()

# Tahap 4: Matriks Area Perkiraan Batas (G)
def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

G = ["G"] + [pow(product([row[i] for row in weighted_matrix[1:]]), 1/8) for i in range(1, len(weighted_matrix[0]))]

print("Tahap 4: Matriks Area Perkiraan Batas (G):")
print_table([G])
print()

# Tahap 5: Perhitungan matriks jarak elemen alternatif dari batas perkiraan daerah (Q)
Q = [["Alternatif"] + weighted_matrix[0][1:]]
for row in weighted_matrix[1:]:
    Q.append([row[0]] + [row[i] - G[i] for i in range(1, len(row))])

print("Tahap 5: Matriks Jarak (Q):")
print_table(Q)
print()

# Tahap 6: Perangkingan alternatif
ranking_scores = {row[0]: sum(row[1:]) for row in Q[1:]}
sorted_ranking = sorted(ranking_scores.items(), key=lambda x: x[1])

print("Tahap 6: Perangkingan Alternatif")
for alt, score in sorted_ranking:
    print(f"{alt}: {score}")

print("Peringkat Alternatif:")
for rank, (alt, score) in enumerate(sorted_ranking, start=1):
    print(f"{rank}. {alt}: {score}")
