import matplotlib.pyplot as plt  # подключаем библиотеку для рисования графиков
import krpc

connection = krpc.connect(name='Graphics')
vessel = connection.space_center.active_vessel

fig, ax = plt.subplots()  # создаём Рисунок и 1 график на нём ax
speed_ar = []
time_ar = []
orbit_frame = vessel.orbit.body.reference_frame


while True:
    speed_ar.append((vessel.flight(orbit_frame).speed * 60) / 1000)
    time_ar.append(vessel.met / 60)
    if vessel.metvessel.flight(orbit_frame).speed > 2500:
        break

ax.plot(time_ar, speed_ar)  # рисуем график, задавая значением по оси y
# функцию y, а значением по оси x функцию x
plt.xlabel('t, мин')
plt.ylabel('U, kм/мин')
plt.grid(color='black')  # задаём легенду осям и цвет сетки
plt.show()  # Выводим на экран
