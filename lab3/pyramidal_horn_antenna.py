import numpy as np
import matplotlib.pyplot as plt

lambd = 3.0
ap = 12.0
bp = 12.0

print(f"λ = {lambd} см")
print(f"ap × bp = {ap}×{bp} см")

k = 2 * np.pi / lambd
print(f"k = {k:.4f} рад/см")

theta_deg = np.linspace(-90, 90, 1801)
theta_rad = np.deg2rad(theta_deg)


def calculate_H_plane(theta, ap, lambd):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    epsilon = 1e-10

    numerator = np.cos((ap / lambd) * np.pi * sin_theta) * sin_theta * (1 + cos_theta) / 2
    denominator = 1 - ((2 * ap / lambd) * sin_theta) ** 2 + epsilon

    F = numerator / denominator
    return np.abs(F)


def calculate_E_plane(theta, bp, lambd):
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    epsilon = 1e-10

    arg = (bp / lambd) * np.pi * sin_theta + epsilon
    numerator = np.sin(arg) * (1 + cos_theta) / 2
    denominator = arg

    F = numerator / denominator
    return np.abs(F)


F_H = calculate_H_plane(theta_rad, ap, lambd)
F_E = calculate_E_plane(theta_rad, bp, lambd)

F_H_norm = F_H / np.max(F_H)
F_E_norm = F_E / np.max(F_E)


def find_beamwidth(theta_deg, F_norm, level=0.707):
    indices = np.where(F_norm >= level)[0]
    if len(indices) > 0:
        theta_left = theta_deg[indices[0]]
        theta_right = theta_deg[indices[-1]]
        width = theta_right - theta_left
        return width, theta_left, theta_right
    return None, None, None


def find_extrema(theta_deg, F_norm):
    max_indices = []
    min_indices = []

    for i in range(1, len(F_norm) - 1):
        if F_norm[i] > F_norm[i - 1] and F_norm[i] > F_norm[i + 1] and F_norm[i] > 0.01:
            max_indices.append(i)
        if F_norm[i] < F_norm[i - 1] and F_norm[i] < F_norm[i + 1] and F_norm[i] < 0.01:
            min_indices.append(i)

    max_angles = [theta_deg[i] for i in max_indices]
    max_values = [F_norm[i] for i in max_indices]
    min_angles = [theta_deg[i] for i in min_indices]
    min_values = [F_norm[i] for i in min_indices]

    return max_angles, max_values, min_angles, min_values


width_H, left_H, right_H = find_beamwidth(theta_deg, F_H_norm)
width_E, left_E, right_E = find_beamwidth(theta_deg, F_E_norm)

max_ang_H, max_val_H, min_ang_H, min_val_H = find_extrema(theta_deg, F_H_norm)
max_ang_E, max_val_E, min_ang_E, min_val_E = find_extrema(theta_deg, F_E_norm)

print("\n" + "=" * 60)
print("РЕЗУЛЬТАТИ РОЗРАХУНКІВ")
print("=" * 60)
print(f"Ширина головної пелюстки на рівні 0.707:")
print(f"  H-площина: {width_H:.2f}° (від {left_H:.2f}° до {right_H:.2f}°)")
print(f"  E-площина: {width_E:.2f}° (від {left_E:.2f}° до {right_E:.2f}°)")

print(f"\nБокові пелюстки H-площини:")
for i, (ang, val) in enumerate(zip(max_ang_H[:5], max_val_H[:5]), 1):
    print(f"  {i}. θ = {ang:.2f}°, F = {val:.3f}")

print(f"\nБокові пелюстки E-площини:")
for i, (ang, val) in enumerate(zip(max_ang_E[:5], max_val_E[:5]), 1):
    print(f"  {i}. θ = {ang:.2f}°, F = {val:.3f}")

print("=" * 60)

plt.figure(figsize=(16, 6))
plt.rcParams['font.size'] = 10

plt.subplot(1, 2, 1)
plt.plot(theta_deg, F_H_norm, 'b-', linewidth=2, label='F_H(θ)')
plt.axhline(y=0.707, color='r', linestyle='--', linewidth=1, label='Рівень 0.707')
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.plot(max_ang_H, max_val_H, 'ro', markersize=4, label='Максимуми')
plt.plot(min_ang_H, min_val_H, 'go', markersize=4, label='Нулі')
plt.grid(True, alpha=0.3)
plt.xlabel('θ, градуси', fontsize=12)
plt.ylabel('F(θ) нормована', fontsize=12)
plt.title(f'ДН у H-площині\n(λ={lambd} см, ap={ap} см)', fontsize=12, fontweight='bold')
plt.legend(fontsize=9)
plt.xlim(-90, 90)
plt.ylim(0, 1.1)

plt.subplot(1, 2, 2)
plt.plot(theta_deg, F_E_norm, 'g-', linewidth=2, label='F_E(θ)')
plt.axhline(y=0.707, color='r', linestyle='--', linewidth=1, label='Рівень 0.707')
plt.axvline(x=0, color='k', linestyle='-', linewidth=0.5)
plt.plot(max_ang_E, max_val_E, 'ro', markersize=4, label='Максимуми')
plt.plot(min_ang_E, min_val_E, 'go', markersize=4, label='Нулі')
plt.grid(True, alpha=0.3)
plt.xlabel('θ, градуси', fontsize=12)
plt.ylabel('F(θ) нормована', fontsize=12)
plt.title(f'ДН у E-площині\n(λ={lambd} см, bp={bp} см)', fontsize=12, fontweight='bold')
plt.legend(fontsize=9)
plt.xlim(-90, 90)
plt.ylim(0, 1.1)

plt.tight_layout()
filename = f"lab3/DN_pyramidal_horn_lambda{lambd}_ap{ap}_bp{bp}.jpg"
plt.savefig(filename, dpi=600)
print(f"\nГрафік збережено: {filename}")
plt.show()

print("\n=== РОЗРАХУНОК ЗАВЕРШЕНО ===")