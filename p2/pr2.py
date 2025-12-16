import math

print("=" * 70)
print("Практична робота 2: Варіант 6")
print("=" * 70)

# ============================================================================
# ЗАВДАННЯ 1: Відстань прямої видимості
# ============================================================================
print("\n" + "=" * 70)
print("ЗАВДАННЯ 1: Відстань прямої видимості")
print("=" * 70)

# Вхідні дані
r0 = 39.07  # км
k = 3.33    # h1 = k * h2

print(f"\nВхідні дані:")
print(f"r₀ = {r0} км")
print(f"h₁ = {k} × h₂")

# Формула відстані прямої видимості: r₀ = 3.57 × √(h₁ + h₂)
# r₀ = 3.57 × √(k×h₂ + h₂) = 3.57 × √(h₂(k + 1))
# r₀² = 3.57² × h₂ × (k + 1)
# h₂ = r₀² / (3.57² × (k + 1))

print(f"\nРішення:")
print(f"Формула відстані прямої видимості: r₀ = 3.57 × √(h₁ + h₂)")
print(f"Оскільки h₁ = {k} × h₂, то:")
print(f"r₀ = 3.57 × √({k} × h₂ + h₂) = 3.57 × √(h₂ × ({k} + 1))")
print(f"r₀² = 3.57² × h₂ × ({k} + 1)")
print(f"h₂ = r₀² / (3.57² × ({k} + 1))")

h2 = r0**2 / (3.57**2 * (k + 1))
h1 = k * h2

print(f"\nОбчислення:")
print(f"h₂ = {r0}² / (3.57² × ({k} + 1))")
print(f"h₂ = {r0**2:.2f} / ({3.57**2:.2f} × {k + 1:.2f})")
print(f"h₂ = {r0**2:.2f} / {3.57**2 * (k + 1):.2f}")
print(f"h₂ = {h2:.2f} м")
print(f"\nh₁ = {k} × h₂ = {k} × {h2:.2f} = {h1:.2f} м")

# Перевірка
r0_check = 3.57 * math.sqrt(h1 + h2)
print(f"\nПеревірка:")
print(f"r₀ = 3.57 × √({h1:.2f} + {h2:.2f}) = 3.57 × √{h1 + h2:.2f} = {r0_check:.2f} км ≈ {r0} км ✓")

print(f"\n{'='*70}")
print(f"ВІДПОВІДЬ ЗАВДАННЯ 1:")
print(f"h₁ = {h1:.2f} м")
print(f"h₂ = {h2:.2f} м")
print(f"{'='*70}")

# ============================================================================
# ЗАВДАННЯ 2: Поширення радіохвиль
# ============================================================================
print("\n\n" + "=" * 70)
print("ЗАВДАННЯ 2: Поширення радіохвиль над плоскою поверхнею Землі")
print("=" * 70)

# Вхідні дані
P1 = 10      # Вт
lambda_m = 5 # м
h1_z2 = 45   # м
h2_z2 = 45   # м
r = 6        # км
Phi = 176    # градуси
R_mod = 0.98 # модуль коефіцієнта відбиття
D1 = 100
D2 = 100

print(f"\nВхідні дані:")
print(f"P₁ = {P1} Вт")
print(f"λ = {lambda_m} м")
print(f"h₁ = {h1_z2} м")
print(f"h₂ = {h2_z2} м")
print(f"r = {r} км")
print(f"Ф = {Phi}°")
print(f"|R| = {R_mod}")
print(f"D₁ = D₂ = {D1}")

# Крок 1: Перевірка можливості застосування формули Введенського
print(f"\n{'='*70}")
print(f"1. Перевірка можливості застосування формули Введенського")
print(f"{'='*70}")

r_vved_min = (18 * lambda_m) / (h1_z2 + h2_z2)
print(f"Умова: r ≥ 18λ/(h₁ + h₂)")
print(f"18λ/(h₁ + h₂) = 18 × {lambda_m} / ({h1_z2} + {h2_z2}) = {18 * lambda_m} / {h1_z2 + h2_z2} = {r_vved_min:.3f} км")
print(f"r = {r} км")

if r >= r_vved_min:
    print(f"✓ {r} ≥ {r_vved_min:.3f} - формула Введенського ЗАСТОСОВУЄТЬСЯ")
    use_vvedensky = True
else:
    print(f"✗ {r} < {r_vved_min:.3f} - формула Введенського НЕ ЗАСТОСОВУЄТЬСЯ")
    use_vvedensky = False

# Крок 2: Перевірка можливості застосування спрощеної формули
print(f"\n{'='*70}")
print(f"2. Перевірка можливості застосування спрощеної формули")
print(f"{'='*70}")

print(f"Умови: 0.95 < |R| < 1 та 175° < Ф < 180°")
print(f"|R| = {R_mod}: ", end="")
if 0.95 < R_mod < 1:
    print(f"✓ 0.95 < {R_mod} < 1")
    cond1 = True
else:
    print(f"✗ умова не виконується")
    cond1 = False

print(f"Ф = {Phi}°: ", end="")
if 175 < Phi < 180:
    print(f"✓ 175° < {Phi}° < 180°")
    cond2 = True
else:
    print(f"✗ умова не виконується")
    cond2 = False

use_simplified = cond1 and cond2

if use_simplified:
    print(f"\n✓ Обидві умови виконуються - використовуємо СПРОЩЕНУ формулу")
else:
    print(f"\n✗ Умови не виконуються - використовуємо ПОВНУ інтерференційну формулу")

# Крок 3: Обчислення множника ослаблення
print(f"\n{'='*70}")
print(f"3. Обчислення множника ослаблення F")
print(f"{'='*70}")

if use_vvedensky:
    print(f"Використовуємо формулу Введенського:")
    print(f"F = 4h₁h₂/(λr)")
    
    F = (4 * h1_z2 * h2_z2) / (lambda_m * r)
    
    print(f"F = (4 × {h1_z2} × {h2_z2}) / ({lambda_m} × {r})")
    print(f"F = {4 * h1_z2 * h2_z2} / {lambda_m * r}")
    print(f"F = {F:.4f}")
    
elif use_simplified:
    print(f"Використовуємо спрощену інтерференційну формулу:")
    print(f"F = 2|sin(2πh₁h₂/(λr))|")
    
    arg = (2 * math.pi * h1_z2 * h2_z2) / (lambda_m * r * 1000)  # r в метрах
    F = 2 * abs(math.sin(arg))
    
    print(f"Аргумент: 2πh₁h₂/(λr) = 2π × {h1_z2} × {h2_z2} / ({lambda_m} × {r*1000})")
    print(f"         = {arg:.4f} рад")
    print(f"F = 2 × |sin({arg:.4f})| = {F:.4f}")
    
else:
    print(f"Використовуємо повну інтерференційну формулу:")
    print(f"F = √(1 + R² + 2R×cos(Δφ))")
    
    # Різниця ходу променів
    delta_r = (2 * h1_z2 * h2_z2) / (r * 1000)  # в метрах
    print(f"\nРізниця ходу: Δr = 2h₁h₂/r = 2 × {h1_z2} × {h2_z2} / {r*1000} = {delta_r:.4f} м")
    
    # Різниця фаз
    delta_phi_rad = (2 * math.pi * delta_r) / lambda_m + math.radians(180 - Phi)
    print(f"Різниця фаз: Δφ = 2πΔr/λ + (180° - Ф)")
    print(f"           = 2π × {delta_r:.4f} / {lambda_m} + {180 - Phi}°")
    print(f"           = {delta_phi_rad:.4f} рад")
    
    F_squared = 1 + R_mod**2 + 2 * R_mod * math.cos(delta_phi_rad)
    F = math.sqrt(F_squared)
    
    print(f"\nF = √(1 + {R_mod}² + 2 × {R_mod} × cos({delta_phi_rad:.4f}))")
    print(f"F = √(1 + {R_mod**2:.4f} + {2 * R_mod * math.cos(delta_phi_rad):.4f})")
    print(f"F = √{F_squared:.4f}")
    print(f"F = {F:.4f}")

# Переведення F в дБ
F_dB = 20 * math.log10(F)
print(f"\nF (дБ) = 20 × lg(F) = 20 × lg({F:.4f}) = {F_dB:.2f} дБ")

# Крок 4: Обчислення напруженості поля
print(f"\n{'='*70}")
print(f"4. Обчислення напруженості електричного поля")
print(f"{'='*70}")

print(f"Формула: E = 173 × √(P₁ × D₁) / r × F")

E = 173 * math.sqrt(P1 * D1) / r * F

print(f"E = 173 × √({P1} × {D1}) / {r} × {F:.4f}")
print(f"E = 173 × √{P1 * D1} / {r} × {F:.4f}")
print(f"E = 173 × {math.sqrt(P1 * D1):.2f} / {r} × {F:.4f}")
print(f"E = {173 * math.sqrt(P1 * D1) / r:.2f} × {F:.4f}")
print(f"E = {E:.4f} мВ/м")

# Переведення в дБ (відносно 1 мкВ/м)
E_mkV = E * 1000  # переводимо в мкВ/м
E_dB = 20 * math.log10(E_mkV)
print(f"E = {E_mkV:.2f} мкВ/м")
print(f"E (дБ) = 20 × lg({E_mkV:.2f}) = {E_dB:.2f} дБ(мкВ/м)")

# Крок 5: Обчислення втрат
print(f"\n{'='*70}")
print(f"5. Обчислення втрат при поширенні")
print(f"{'='*70}")

# Основні втрати (втрати у вільному просторі)
L_osn = (4 * math.pi * r * 1000 / lambda_m)**2 / F**2
L_osn_dB = 20 * math.log10(4 * math.pi * r * 1000 / lambda_m) - F_dB

print(f"Основні втрати L_осн = (4πr/λ)² / F²")
print(f"L_осн = (4π × {r*1000} / {lambda_m})² / {F:.4f}²")
print(f"L_осн = ({4 * math.pi * r * 1000 / lambda_m:.2f})² / {F**2:.4f}")
print(f"L_осн = {L_osn:.2f}")
print(f"L_осн (дБ) = 20lg(4πr/λ) - F(дБ) = {20 * math.log10(4 * math.pi * r * 1000 / lambda_m):.2f} - {F_dB:.2f} = {L_osn_dB:.2f} дБ")

# Загальні втрати
L_zag = L_osn / (D1 * D2)
D1_dB = 10 * math.log10(D1)
D2_dB = 10 * math.log10(D2)
L_zag_dB = L_osn_dB - D1_dB - D2_dB

print(f"\nЗагальні втрати L_заг = L_осн / (D₁ × D₂)")
print(f"L_заг = {L_osn:.2f} / ({D1} × {D2})")
print(f"L_заг = {L_osn:.2f} / {D1 * D2}")
print(f"L_заг = {L_zag:.6f}")
print(f"L_заг (дБ) = L_осн(дБ) - D₁(дБ) - D₂(дБ)")
print(f"         = {L_osn_dB:.2f} - {D1_dB:.2f} - {D2_dB:.2f}")
print(f"         = {L_zag_dB:.2f} дБ")

# Крок 6: Відстань до першого максимуму та мінімуму
print(f"\n{'='*70}")
print(f"6. Відстань до першого максимуму та мінімуму")
print(f"{'='*70}")

r_max1 = (4 * h1_z2 * h2_z2) / lambda_m / 1000  # в км
r_min1 = (2 * h1_z2 * h2_z2) / lambda_m / 1000  # в км

print(f"Перший максимум (з боку великих відстаней):")
print(f"r_max1 = 4h₁h₂/λ = 4 × {h1_z2} × {h2_z2} / {lambda_m} = {4 * h1_z2 * h2_z2} / {lambda_m} = {r_max1:.3f} км")

print(f"\nПерший мінімум (з боку великих відстаней):")
print(f"r_min1 = 2h₁h₂/λ = 2 × {h1_z2} × {h2_z2} / {lambda_m} = {2 * h1_z2 * h2_z2} / {lambda_m} = {r_min1:.3f} км")

# Відстань, при якій F = 1
r_F1 = (math.pi * h1_z2 * h2_z2) / (6 * lambda_m) / 1000  # в км
print(f"\nВідстань, при якій F = 1:")
print(f"r(F=1) = πh₁h₂/(6λ) = π × {h1_z2} × {h2_z2} / (6 × {lambda_m})")
print(f"       = {math.pi * h1_z2 * h2_z2} / {6 * lambda_m}")
print(f"       = {r_F1:.3f} км")

# Підсумкова таблиця результатів
print(f"\n\n{'='*70}")
print(f"ПІДСУМКОВІ РЕЗУЛЬТАТИ ЗАВДАННЯ 2")
print(f"{'='*70}")
print(f"{'Параметр':<40} {'Значення':<30}")
print(f"{'-'*70}")
print(f"{'Множник ослаблення F':<40} {F:.4f} ({F_dB:.2f} дБ)")
print(f"{'Напруженість поля E':<40} {E:.4f} мВ/м ({E_dB:.2f} дБ(мкВ/м))")
print(f"{'Основні втрати L_осн':<40} {L_osn:.2f} ({L_osn_dB:.2f} дБ)")
print(f"{'Загальні втрати L_заг':<40} {L_zag:.6f} ({L_zag_dB:.2f} дБ)")
print(f"{'Відстань до 1-го максимуму':<40} {r_max1:.3f} км")
print(f"{'Відстань до 1-го мінімуму':<40} {r_min1:.3f} км")
print(f"{'Відстань при F=1':<40} {r_F1:.3f} км")
print(f"{'='*70}")

print(f"\n✓ Розрахунки завершено!")
