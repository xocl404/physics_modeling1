import numpy
import matplotlib.pyplot
m = float(input("Введите массу тела (кг): "))
R = float(input("Введите радиус кольца (м): "))
a = float(input("Введите угловой размер дуги (рад): "))
u = float(input("Введите коэффициент трения: "))
g = 9.81
friction_force = u * m * g  # Сила трения
theta = a / 2  # Максимальный угол дуги
v_critical = numpy.sqrt(2 * g * R * (1 - numpy.cos(theta)))  # Критическая скорость
print(f"{v_critical:.2f} м/с")
# Движение после отрыва
t_flight = 2 * v_critical * numpy.sin(theta) / g  # Время полета
t = numpy.linspace(0, t_flight, num=100)  # Дискретные моменты времени
# Позиции тела в момент времени t
x = v_critical * numpy.cos(theta) * t  # Горизонтальная координата
y = v_critical * numpy.sin(theta) * t - 0.5 * g * t**2  # Вертикальная координата
# Строим траекторию
matplotlib.pyplot.figure(figsize=(8, 6))
matplotlib.pyplot.plot(x, y, label='Траектория тела', color='b')
matplotlib.pyplot.title("Траектория тела после отрыва от дуги")
matplotlib.pyplot.xlabel("Горизонтальная координата, м")
matplotlib.pyplot.ylabel("Вертикальная координата, м")
matplotlib.pyplot.axhline(0, color='black', lw=1)
matplotlib.pyplot.legend()
matplotlib.pyplot.grid()
matplotlib.pyplot.show()
