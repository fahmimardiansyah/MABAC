data = [
    ["Kode", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    ["A1", 1.10, 3.12, 3.89, 4.20, 2.21, 1.03, 3.00, 5.00],
    ["A2", 3.05, 3.98, 2.96, 3.02, 4.10, 2.99, 1.10, 4.03],
    ["A3", 1.90, 4.95, 3.01, 2.90, 4.95, 4.06, 5.00, 1.10],
    ["A4", 2.85, 3.87, 3.12, 1.05, 2.93, 4.89, 3.30, 4.90],
    ["A5", 4.77, 3.00, 4.87, 3.01, 1.97, 3.99, 2.04, 4.00]
]

# Bobot
bobot = [
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"],
    [0.178, 0.284, 0.207, 0.100, 0.057, 0.064, 0.044, 0.066]
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

G = ["G"] + [pow(product([row[i] for row in weighted_matrix[1:]]), 1/5) for i in range(1, len(weighted_matrix[0]))]

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
