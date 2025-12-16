import math

# Вхідні дані (Варіант 6)
h1 = 5  # м
h2 = 40  # м
Hpr = 14  # м (висота нерівності)
f = 450  # МГц
r = 18  # км

print("=" * 60)
print("Практична робота 3: Облік кривизни Землі")
print("Варіант 6")
print("=" * 60)
print(f"\nВхідні дані:")
print(f"h₁ = {h1} м")
print(f"h₂ = {h2} м")
print(f"Hпр = {Hpr} м")
print(f"f = {f} МГц")
print(f"r = {r} км")

# Константи
R3 = 6370  # км - радіус Землі
c = 3e8  # м/с - швидкість світла

# 1. Обчислення відстані прямої видимості
r0 = 3.57 * math.sqrt(h1 + h2)
print(f"\n{'='*60}")
print(f"1. Відстань прямої видимості:")
print(f"r₀ = 3.57 × √(h₁ + h₂) = 3.57 × √({h1} + {h2})")
print(f"r₀ = {r0:.2f} км")

# Визначення зони
print(f"\n{'='*60}")
print(f"2. Визначення зони:")
print(f"r = {r} км")
print(f"0.2×r₀ = {0.2*r0:.2f} км")
print(f"0.8×r₀ = {0.8*r0:.2f} км")
print(f"1.2×r₀ = {1.2*r0:.2f} км")

if r < 0.2 * r0:
    zone = "плоскої поверхні"
    formula_type = 1
elif r < 0.8 * r0:
    zone = "освітленості"
    formula_type = 2
elif r < 1.2 * r0:
    zone = "півтіні"
    formula_type = 2
else:
    zone = "тіні"
    formula_type = 2

print(f"Зона: {zone}")

# 3. Розрахунок r1 і r2
print(f"\n{'='*60}")
print(f"3. Розрахунок r₁ і r₂:")

if formula_type == 1:
    # Для зони плоскої поверхні
    print(f"Використовуємо формули для плоскої поверхні:")
    r1 = (h2 * r) / (h1 + h2)
    r2 = (h1 * r) / (h1 + h2)
    print(f"r₁ = h₂×r/(h₁+h₂) = {h2}×{r}/({h1}+{h2}) = {r1:.3f} км")
    print(f"r₂ = h₁×r/(h₁+h₂) = {h1}×{r}/({h1}+{h2}) = {r2:.3f} км")
else:
    # Для інших зон з урахуванням кривизни
    print(f"Використовуємо формули з урахуванням кривизни Землі:")
    # Використовуємо простіші формули
    r1 = (h2 * r) / (h1 + h2)
    r2 = (h1 * r) / (h1 + h2)
    
    print(f"r₁ = h₂×r/(h₁+h₂) = {h2}×{r}/({h1}+{h2}) = {r1:.3f} км")
    print(f"r₂ = h₁×r/(h₁+h₂) = {h1}×{r}/({h1}+{h2}) = {r2:.3f} км")

# 4. Наведені висоти
print(f"\n{'='*60}")
print(f"4. Наведені висоти:")
h1_prim = h1 - r1**2 / 12.8
h2_prim = h2 - r2**2 / 12.8

print(f"h₁' = h₁ - r₁²/12.8")
print(f"h₁' = {h1} - {r1:.3f}²/12.8 = {h1} - {r1**2/12.8:.3f}")
print(f"h₁' = {h1_prim:.3f} м")
print()
print(f"h₂' = h₂ - r₂²/12.8")
print(f"h₂' = {h2} - {r2:.3f}²/12.8 = {h2} - {r2**2/12.8:.3f}")
print(f"h₂' = {h2_prim:.3f} м")

# 5. Кут ковзання
print(f"\n{'='*60}")
print(f"5. Кут ковзання:")
gamma_rad = abs(h1_prim) / (r1 * 1000)  # радіани, використовуємо модуль
gamma_deg = math.degrees(gamma_rad)
gamma_mrad = gamma_rad * 1000  # мілірадіани

print(f"γ = |h₁'|/(r₁ × 10³)")
print(f"γ = |{h1_prim:.3f}|/({r1:.3f} × 10³)")
print(f"γ = {gamma_rad:.6f} рад")
print(f"γ = {gamma_mrad:.3f} мрад")
print(f"γ = {gamma_deg:.4f}°")

# 6. Критерій Релея
print(f"\n{'='*60}")
print(f"6. Критерій Релея:")

# Довжина хвілі
lambda_m = c / (f * 1e6)  # переводимо МГц в Гц
print(f"λ = c/f = {c}/{f}×10⁶ = {lambda_m:.4f} м")

# Критерій Релея: Δh < λ/(8×sin(γ))
rayleigh_limit = lambda_m / (8 * math.sin(gamma_rad))
print(f"\nКритерій Релея: Δh < λ/(8×sin(γ))")
print(f"λ/(8×sin(γ)) = {lambda_m:.4f}/(8×sin({gamma_rad:.6f}))")
print(f"λ/(8×sin(γ)) = {rayleigh_limit:.3f} м")
print(f"\nΔh (Hпр) = {Hpr} м")

if Hpr < rayleigh_limit:
    print(f"\n✓ {Hpr} < {rayleigh_limit:.3f}")
    print("Критерій Релея ВИКОНУЄТЬСЯ")
    print("Поверхня ГЛАДКА")
else:
    print(f"\n✗ {Hpr} ≥ {rayleigh_limit:.3f}")
    print("Критерій Релея НЕ ВИКОНУЄТЬСЯ")
    print("Поверхня ШОРСТКА")

# 7. Коефіцієнт розбіжності
print(f"\n{'='*60}")
print(f"7. Коефіцієнт розбіжності:")

numerator = 2 * r1 * r2
denominator = R3 * (r1 + r2) * math.sin(gamma_rad)
D = 1 / (1 + numerator / denominator)

print(f"D = 1 / (1 + 2×r₁×r₂/(R₃×(r₁+r₂)×sin(γ)))")
print(f"D = 1 / (1 + 2×{r1:.3f}×{r2:.3f}/({R3}×({r1:.3f}+{r2:.3f})×sin({gamma_rad:.6f})))")
print(f"D = 1 / (1 + {numerator:.3f}/{denominator:.3f})")
print(f"D = 1 / (1 + {numerator/denominator:.6f})")
print(f"D = {D:.6f}")

print(f"\n{'='*60}")
print("РЕЗУЛЬТАТИ:")
print(f"{'='*60}")
print(f"h₁' = {h1_prim:.3f} м")
print(f"h₂' = {h2_prim:.3f} м")
print(f"γ = {gamma_rad:.6f} рад = {gamma_mrad:.3f} мрад = {gamma_deg:.4f}°")
print(f"Критерій Релея: {'ВИКОНУЄТЬСЯ (поверхня ГЛАДКА)' if Hpr < rayleigh_limit else 'НЕ ВИКОНУЄТЬСЯ (поверхня ШОРСТКА)'}")
print(f"D = {D:.6f}")
print(f"{'='*60}")
