import numpy
import matplotlib.pyplot as plt
import math

N = 11
F = 520 * 10 ** 6
lambd = 299792458 / F
print("λ = " + str(lambd) + " (m) = " + str(lambd * 100) + " (cm)")

d = 0.25 * lambd
print("dcp = " + str(d) + " (m) = " + str(d * 100) + " (cm)")

k = (2 * numpy.pi) / lambd
print("k = " + str(k) + " (rad/m)")

F1E = [1]
FC = [1]
FE = [1]
steps = [0]

SGP1 = 0
SGP2 = 0
fS1 = 0
fS2 = 0

max_x_FC = []
max_y_FC = []
max_x_FE = []
max_y_FE = []

min_x_FC = []
min_y_FC = []
min_x_FE = []
min_y_FE = []

print("\nРозрахунок ДН...")

for teta in numpy.arange(0.01, numpy.pi / 2, 0.00001):
    mn1 = abs((numpy.cos(numpy.pi/2 * numpy.sin(teta)) / numpy.cos(teta)))
    
    mn2 = abs(numpy.sin((N * k * d * (1 - numpy.cos(teta)) / 2)) / 
              (N * numpy.sin((k * d * (1 - numpy.cos(teta))) / 2)))
    
    mn3 = mn1 * mn2

    F1E.append(mn1)
    FC.append(mn2)
    FE.append(mn3)

    if 0.707 < mn2 < 0.708:
        SGP1 = 2 * math.degrees(teta)
        fS1 = mn2

    if 0.707 < mn3 < 0.708:
        SGP2 = 2 * math.degrees(teta)
        fS2 = mn3

    steps.append(math.degrees(teta))

print("Пошук максимумів і нулів...")

for i in range(1, len(FC) - 1):
    if FC[i] > FC[i - 1] and FC[i] > FC[i + 1]:
        max_x_FC.append(steps[i])
        max_y_FC.append(FC[i])
    if FE[i] > FE[i - 1] and FE[i] > FE[i + 1]:
        max_x_FE.append(steps[i])
        max_y_FE.append(FE[i])

for i in range(1, len(FC) - 1):
    if FC[i] < FC[i - 1] and FC[i] < FC[i + 1]:
        min_x_FC.append(steps[i])
        min_y_FC.append(FC[i])
    if FE[i] < FE[i - 1] and FE[i] < FE[i + 1]:
        min_x_FE.append(steps[i])
        min_y_FE.append(FE[i])

print("\n" + "="*50)
print("РЕЗУЛЬТАТИ РОЗРАХУНКІВ")
print("="*50)
print(f"Частота: {F/1e6:.0f} МГц")
print(f"Число елементів: {N}")
print(f"Довжина хвилі: {lambd*100:.2f} см")
print(f"Середня відстань між елементами: {d*100:.2f} см")
print(f"\nШирина головного пелюстка в площині H = {round(SGP1, 2)}°")
print(f"Ширина головного пелюстка в площині E = {round(SGP2, 2)}°")
print("="*50)

len_value = [len(max_x_FC), len(max_x_FE), len(min_x_FC), len(min_x_FE)]
print("\nТабл. 1 - Аналіз ДН директорної антени в площині H і E")
print("-" * 58)
print("| № |θ min H|θ min E|θ max H|FH(θ) |θ max E|FE(θ) |")
print("-" * 58)

for i in range(0, max(len_value)):
    v1 = f" {i + 1}"
    v2 = f"{min_x_FC[i]:6.2f}" if i < len(min_x_FC) else "   -  "
    v3 = f"{min_x_FE[i]:6.2f}" if i < len(min_x_FE) else "   -  "
    v4 = f"{max_x_FC[i]:6.2f}" if i < len(max_x_FC) else "   -  "
    h4 = f"{max_y_FC[i]:6.3f}" if i < len(max_y_FC) else "   -  "
    v5 = f"{max_x_FE[i]:6.2f}" if i < len(max_x_FE) else "   -  "
    h5 = f"{max_y_FE[i]:6.3f}" if i < len(max_y_FE) else "   -  "
    print(f"|{v1:^3}|{v2}|{v3}|{v4}|{h4}|{v5}|{h5}|")

print("-" * 58)

print("\nПобудова графіка...")

fig, ax = plt.subplots(figsize=(20/2.54, 12/2.54))

ax.plot(steps, F1E, linewidth=0.7, label="$ F_{1E}(θ) $")
ax.plot(steps, FC, linewidth=0.7, label="$ F_{H}(θ) $")
ax.plot(steps, FE, linewidth=0.7, label="$ F_{E}(θ) $")

ax.plot(SGP1/2, fS1, 'ro', markersize=4, label="ШГП в площині H")
ax.plot(SGP2/2, fS2, 'go', markersize=4, label="ШГП в площині E")

plt.annotate(f'({fS1:.3f}, {SGP1/2:.2f}°)',
             xy=(SGP1 / 2, fS1),
             xytext=((SGP1/2)+3, fS1+0.05),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=6)

plt.annotate(f'({fS2:.3f}, {SGP2/2:.2f}°)',
             xy=(SGP2 / 2, fS2),
             xytext=((SGP2/2)-13, fS2+0.05),
             arrowprops=dict(arrowstyle='->', color='black'), fontsize=6)

ax.plot([0, SGP1/2], [fS2, fS2], 'r--', linewidth=0.5)
ax.plot([SGP2/2, SGP2/2], [0, fS2], 'r--', linewidth=0.5)
ax.plot([SGP1/2, SGP1/2], [0, fS1], 'r--', linewidth=0.5)

ax.plot(max_x_FC, max_y_FC, "o", markersize=4, color="black", label="$ θ_{max} $ FH")
ax.plot(max_x_FE, max_y_FE, "o", markersize=4, color="grey", label="$ θ_{max} $ FE")
ax.plot(min_x_FC, min_y_FC, "o", markersize=4, color="blue", label="$ θ_{min} $ FH і FE")

ax.set_xlabel('θ°', fontsize=10)
ax.set_ylabel('|FH(θ°)|, |FE(θ°)|, |F1E(θ°)|', fontsize=10)
plt.xticks(numpy.arange(0, 100, 2), fontsize=7)
plt.yticks(numpy.arange(0, 1.2, 0.1), fontsize=7)
plt.ylim(-0.01, 1.01)
plt.xlim(0, 90.5)

plt.legend(loc="upper right", fontsize=7)
plt.grid(which='both', linestyle='--', linewidth=0.2, color='gray')

filename = f"lab2/DN_directional_antenna_N{N}_F{F//1e6}MHz.jpg"
fig.savefig(filename, dpi=600)
print(f"\nГрафік збережено: {filename}")

plt.show()

print("\n=== РОЗРАХУНОК ЗАВЕРШЕНО ===")
