import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# No need for special font for English; comment out Chinese font settings
# plt.rcParams['font.sans-serif'] = ['SimHei']  # For Windows
# plt.rcParams['font.sans-serif'] = ['Heiti TC']  # For macOS, uncomment if needed
plt.rcParams['axes.unicode_minus'] = False

# Data for Chart 1: Grouped Bar Chart
indicators = ['Guess Entropy (bits)', 'Information Gain (bits)', 'Average Guess Attempts', 'Worst Guess Attempts', 'Number of Valid Feedback Results']
classic_feedback = [2.9, 2.8, 6.0, 9.0, 15]
positional_feedback = [3.0, 4.5, 4.0, 6.0, 75]

x = np.arange(len(indicators))  # Label locations
width = 0.3  # Width of the bars

fig1, ax1 = plt.subplots(figsize=(6, 4), dpi=150)  # Reduced size
bars1 = ax1.bar(x - width/2, classic_feedback, width, label='Classic Feedback', color='#1f77b4')
bars2 = ax1.bar(x + width/2, positional_feedback, width, label='Positional Feedback', color='#ff7f0e')

# Add labels, title, and custom x-axis tick labels
ax1.set_ylabel('Value', fontsize=9)
ax1.set_title('Entropy Maximization Strategy: Classic Feedback vs Positional Feedback Core Metrics Comparison', fontsize=8, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(indicators, fontsize=7, rotation=10, ha='right')
ax1.set_ylim(0, 80)  # As per spec, up to 80
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=5)

for bar in bars2:
    height = bar.get_height()
    ax1.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=5)

# Legend
ax1.legend(loc='upper left', shadow=True, fancybox=True)

# Save and show
plt.savefig('core_metrics_comparison.png')
plt.show()

# Data for Chart 2: Scatter Plot
classic_x, classic_y = 2.9, 2.8
positional_x, positional_y = 3.0, 4.5

fig2, ax2 = plt.subplots(figsize=(10, 5), dpi=150)  # Reduced size
ax2.scatter(classic_x, classic_y, s=250, color='#1f77b4', edgecolor='black', linewidth=1.5, label='Classic Feedback')
ax2.scatter(positional_x, positional_y, s=250, color='#ff7f0e', edgecolor='black', linewidth=1.5, label='Positional Feedback')

# Annotations
ax2.annotate(f'({classic_x}, {classic_y})', (classic_x, classic_y), xytext=(-20, -20),
             textcoords='offset points', ha='left', va='bottom', fontsize=7)
ax2.annotate(f'({positional_x}, {positional_y})', (positional_x, positional_y), xytext=(-20, -20),
             textcoords='offset points', ha='left', va='bottom', fontsize=7)

# Labels and title
ax2.set_xlabel('Guess Entropy (bits)', fontsize=7)
ax2.set_ylabel('Information Gain (bits)', fontsize=7)
ax2.set_title('Entropy and Information Gain Correlation Comparison', fontsize=9, fontweight='bold')
ax2.set_xlim(0, 4)
ax2.set_xticks(np.arange(0, 4.5, 0.5))
ax2.set_ylim(0, 5)
ax2.set_yticks(np.arange(0, 6, 1))
ax2.grid(linestyle='--', alpha=0.7)

# Legend
ax2.legend(loc='center right')

# Save and show
plt.savefig('entropy_ig_correlation.png')
plt.show()