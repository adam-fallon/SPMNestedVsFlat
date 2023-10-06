import subprocess
import time
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.chart import BarChart, Reference

# Initialize
cmd1 = "cd Flat && swift build"
cmd2 = "cd Nested && swift build"
clean = "rm -rf Flat/.build && rm -rf Nested/.build"
iterations = 5
time_cmd1 = []
time_cmd2 = []

# Execute commands and time them
for _ in range(iterations):
    subprocess.run(clean, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    start_time = time.time()
    subprocess.run(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end_time = time.time()
    time_cmd1.append(end_time - start_time)
    
    start_time = time.time()
    subprocess.run(cmd2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end_time = time.time()
    time_cmd2.append(end_time - start_time)

# Create an Excel workbook and add data
wb = Workbook()
ws = wb.active
ws.append(["Iteration", "Flat", "Nested"])

for i, (t1, t2) in enumerate(zip(time_cmd1, time_cmd2), 1):
    ws.append([i, t1, t2])

# Create a bar chart
chart = BarChart()
chart.type = "col"
chart.title = "Execution Times for Commands"
chart.y_axis.title = "Time (s)"
chart.x_axis.title = "Iterations"

data = Reference(ws, min_col=2, min_row=1, max_row=iterations+1, max_col=3)
categories = Reference(ws, min_col=1, min_row=2, max_row=iterations+1)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)

# Set colors
chart.series[0].graphicalProperties.solidFill = "0000FF"  # Blue for cmd1
chart.series[1].graphicalProperties.solidFill = "FF0000"  # Red for cmd2

ws.add_chart(chart, "E5")

# Save workbook
wb.save("cmd_execution_times.xlsx")
