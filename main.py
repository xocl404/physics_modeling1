import numpy
import matplotlib.pyplot

m = float(input("Введите массу тела (кг): "))
R = float(input("Введите радиус кольца (м): "))
a = float(input("Введите угловой размер дуги (рад): "))
u = float(input("Введите коэффициент трения: "))
g = 9.81  # Ускорение свободного падения
friction_force = u * m * g  # Сила трения
theta = a / 2  # Максимальный угол дуги
v_critical = numpy.sqrt(2 * g * R * (1 - numpy.cos(theta)))  # Критическая скорость
print(f"Необходимая начальная скорость: {v_critical:.2f} м/с")
# Движение на дуге
angles = numpy.linspace(0, a, num=100)  # Углы от 0 до a
x_arc = R * numpy.sin(angles)  # Горизонтальная координата на дуге
y_arc = R * (1 - numpy.cos(angles))  # Вертикальная координата на дуге
# Движение после отрыва
t_flight = 2 * v_critical * numpy.sin(theta) / g  # Время полета
t = numpy.linspace(0, t_flight, num=100)  # Дискретные моменты времени
x_flight = R * numpy.sin(a) + v_critical * numpy.cos(theta) * t  # Горизонтальная координата
y_flight = R * (1 - numpy.cos(a)) + v_critical * numpy.sin(theta) * t - 0.5 * g * t**2  # Вертикальная координата

# Построение графика
matplotlib.pyplot.figure(figsize=(10, 8))

# Траектория на дуге
matplotlib.pyplot.plot(x_arc, y_arc, label='Траектория на дуге', color='g')

# Траектория после отрыва
matplotlib.pyplot.plot(x_flight, y_flight, label='Траектория после отрыва', color='b')

matplotlib.pyplot.title("Траектория тела на дуге и после отрыва")
matplotlib.pyplot.xlabel("Горизонтальная координата, м")
matplotlib.pyplot.ylabel("Вертикальная координата, м")
matplotlib.pyplot.axhline(0, color='black', lw=1)
matplotlib.pyplot.legend()
matplotlib.pyplot.grid()
matplotlib.pyplot.show()
