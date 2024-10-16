import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Generate random data
data = np.random.randn(1000)
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
x_line = np.linspace(0, 10, 100)
y_line = np.sin(x_line)
sizes = [30, 20, 15, 35]
labels = ['Group A', 'Group B', 'Group C', 'Group D']
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']
data_box = [np.random.randn(100) for _ in range(4)]
data_heatmap = np.random.rand(10, 10)
x_area = np.arange(1, 6)
y1_area = np.array([1, 3, 4, 5, 2])
y2_area = np.array([2, 4, 6, 7, 4])
x_3d = np.linspace(-5, 5, 100)
y_3d = np.linspace(-5, 5, 100)
x_3d, y_3d = np.meshgrid(x_3d, y_3d)
z_3d = np.sin(np.sqrt(x_3d**2 + y_3d**2))

# 1. Histogram
plt.figure()
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.show()

# 2. Bar Plot
plt.figure()
plt.bar(categories, values, color='skyblue')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 3. Hexbin Plot
plt.figure()
x_hexbin = np.random.randn(10000)
y_hexbin = np.random.randn(10000)
plt.hexbin(x_hexbin, y_hexbin, gridsize=30, cmap='Blues')
plt.colorbar(label='Density')
plt.title('Hexbin Plot')
plt.show()

# 4. Scatter Plot
plt.figure()
plt.scatter(x_scatter, y_scatter, color='green')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 5. Line Plot
plt.figure()
plt.plot(x_line, y_line, color='red')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 6. Pie Chart
plt.figure()
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.show()

# 7. Box Plot
plt.figure()
plt.boxplot(data_box)
plt.title('Box Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 8. Heatmap (Using imshow)
plt.figure()
plt.imshow(data_heatmap, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')
plt.show()

# 9. Area Plot (Stack Plot)
plt.figure()
plt.stackplot(x_area, y1_area, y2_area, labels=['Y1', 'Y2'], colors=['skyblue', 'lightgreen'])
plt.legend(loc='upper left')
plt.title('Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# 10. 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_3d, y_3d, z_3d, cmap='viridis')
ax.set_title('3D Plot')
plt.show()
