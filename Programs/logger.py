import matplotlib.pyplot as plt
import numpy as np

# параметры ракеты и взлёта
TIME_1 = 200  # время работы первой ступени
TIME_2 = 100  # время работы первой ступени
M0_1 = 90_000  # взлётная масса
M0_2 = 19_000  # масса без 1 ступени
F_1T = 374_000 * 4  # в первой ступени было 4 двигателя
F_2T = 374_000  # вторая ступень
K_1 = 325  # скороть расхода массы первой ступени
K_2 = 81.25  # скороть расхода массы второй ступени
B_1 = -0.001  # скорость повортота ракеты на 1 ступени рад/с
B_2 = -0.024  # скорость повортота ракеты на 2 ступени
C_F = 0.8  # (с потолка) коэф сопростивления(надо обЪем)
S = 2_712 ** (2 / 3)  # площадь лобового сопротивления(примерное, пусть ракета просто цилиндр)

# всякие константы
DT = 0.1  # отрезок времяни равное 0.01 с
ANG_0 = np.pi / 2
ANG_1 = ANG_0 + TIME_1 * B_1
G = 9.81
M_A = 0.029
R = 8.31
T = 300
P_0 = 101_300
GAZ_P = M_A / (R * T)

x_values = [0]
y_values = [0]
vx_values = [0]
vy_values = [0]
ax_values = [0]
ay_values = [-9.81]

x = 0
y = 0
vx = 0
vy = 0
ax = 0
ay = 0

for i in range(int(TIME_1 // DT)):  # рассчитываем n секунд шагов первой ступени
    t = i * DT
    rho = (GAZ_P * P_0) * np.exp((-G * y * GAZ_P))
    f_cx = C_F * S * (rho * (vx_values[-1] ** 2) * 0.5)
    f_cy = C_F * S * (rho * (vy_values[-1] ** 2) * 0.5)
    ax = ((F_1T) * np.cos(ANG_0 + B_1 * t) - f_cx)/(M0_1 - K_1 * t)
    ay = ((F_1T) * np.sin(ANG_0 + B_1 * t) - f_cy)/(M0_1 - K_1 * t) - G
    vx = vx_values[-1] + ax * DT
    vy = vy_values[-1] + ay * DT
    x = x_values[-1] + vx * DT
    y = y_values[-1] + vy * DT
    ax_values.append(ax)
    ay_values.append(ay)
    vx_values.append(vx)
    vy_values.append(vy)
    x_values.append(x)
    y_values.append(y)

for i in range(int(TIME_2 // DT)):  # рассчитываем n секунд шагов второй ступени
    t = i * DT
    rho = (GAZ_P * P_0) * np.exp((-G * y * GAZ_P))
    f_cx = C_F * S * (rho * (vx_values[-1] ** 2) * 0.5)
    f_cy = C_F * S * (rho * (vy_values[-1] ** 2) * 0.5)
    ax = ((F_2T) * np.cos(ANG_1 + B_2 * t) - f_cx)/(M0_2 - K_2 * t)
    ay = ((F_2T) * np.sin(ANG_1 + B_2 * t) - f_cy)/(M0_2 - K_2 * t) - G
    vx = vx_values[-1] + ax * DT
    vy = vy_values[-1] + ay * DT
    x = x_values[-1] + vx * DT
    y = y_values[-1] + vy * DT
    ax_values.append(ax)
    ay_values.append(ay)
    vx_values.append(vx)
    vy_values.append(vy)
    x_values.append(x)
    y_values.append(y)

velocity = [((vx_values[i]) ** 2 + vy_values[i] ** 2) ** 0.5 for i in range(len(vx_values))]

# print([((vx_values[::10][i]) ** 2 + vy_values[::10][i] ** 2) ** 0.5 for i in range(TIME_1 + TIME_2)])
# print(y_values[::100])
# plt.plot(range(0, TIME_1+TIME_2), vx_values[::int(DT ** -1)])
plt.xlabel("Время, с")
plt.ylabel("Скорость, м/с")
# plt.plot(range(0, TIME_1+TIME_2), vy_values[::int(DT ** -1)])
# plt.plot(range(0, TIME_1 + 1), velocity[::int(DT ** -1)][:TIME_1 + 1])
plt.plot(range(0, TIME_2), velocity[::int(DT ** -1)][TIME_1:TIME_1+TIME_2])
plt.show()

