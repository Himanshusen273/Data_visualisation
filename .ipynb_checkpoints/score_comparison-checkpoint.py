# import matplotlib
# matplotlib.use('Agg')  # For non-GUI environments

import matplotlib.pyplot as plt

# Styling
plt.style.use('dark_background')

# Data
years = [2015, 2016, 2017, 2018, 2019, 2020]
kohli = [700, 850, 750, 900, 880, 670]
devilliers = [600, 780, 720, 810, 790, 620]
gayle = [500, 690, 640, 730, 710, 580]

# Plot
plt.plot(years, kohli, 'ro--', linewidth=2, label='virat_runs')
plt.plot(years, devilliers, 'g>-.', linewidth=2, label='devilliers_runs')
plt.plot(years, gayle, 'yD:', linewidth=2, label='gayle_runs')

plt.xlabel('years', fontstyle='italic', fontsize=12)
plt.ylabel('scores', fontstyle='oblique', fontsize=12)
plt.title('Score--comparison', fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)
plt.show()
# Layout fix and Save

# plt.savefig('score_plot.png', dpi=300)


# from PIL import Image
# img = Image.open('score_plot.png')
# img.show()
