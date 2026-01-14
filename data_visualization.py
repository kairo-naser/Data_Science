import matplotlib.pyplot as plt # Import the plotting library

# --- 1. THE BASIC PLOT HIERARCHY ---
# Matplotlib plots are comprised of a hierarchy of objects.
# The 'Figure' is the whole window/container.
# Within the Figure, we add 'Axes' (the actual plot area).

# Create a figure object
fig = plt.figure()

# add_axes() defines the position and size of the plot [left, bottom, width, height]
# These are fractions (0 to 1) of the figure size.
# [0, 0, 1, 1] means the plot starts at the bottom-left and fills the whole figure.
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 

# --- 2. TYPES OF PLOTS ---

# A. LINE PLOTS
# Useful for showing trends over time.
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
ax.plot(x, y)

# B. SCATTER PLOTS
# Useful for showing the relationship between two variables.
ax.scatter(x, y, color='red')

# C. BAR CHARTS
# Useful for comparing quantities of different categories.
names = ['Category A', 'Category B', 'Category C']
values = [19, 50, 29]
# Note: Usually you'd create a new figure or clear the old one for a new chart
fig_bar = plt.figure()
ax_bar = fig_bar.add_axes([0.1, 0.1, 0.8, 0.8])
ax_bar.bar(names, values)

# --- 3. CUSTOMIZATION ---
# Almost every aspect of a Matplotlib plot can be customized.
ax_bar.set_title('My Bar Chart')      # Adding a title
ax_bar.set_xlabel('Names')           # Labeling the x-axis
ax_bar.set_ylabel('Values')          # Labeling the y-axis

# --- 4. SUBPLOTS (Multiple plots in one figure) ---
# add_subplot(rows, columns, plot_number)
fig_sub = plt.figure()

# Add a subplot in a 2x2 grid, at position 1 (top left)
ax1 = fig_sub.add_subplot(2, 2, 1)
ax1.plot([1, 2], [1, 2])

# Add a subplot in a 2x2 grid, at position 4 (bottom right)
ax4 = fig_sub.add_subplot(2, 2, 4)
ax4.bar(['X', 'Y'], [5, 10])

# --- 5. CLEANING UP ---
# You can delete specific axes if needed.
# fig_sub.delaxes(ax1)

# Display the plots
plt.show()