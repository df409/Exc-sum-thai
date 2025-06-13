import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch

# Set global style
sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.edgecolor'] = '#333F4B'
plt.rcParams['axes.linewidth'] = 0.8

# Data setup
subjects = ['Reading', 'Mathematics', 'Science']
years = [2012, 2022, 2025]
data = {
    'Reading': [441, 379, 364],
    'Mathematics': [427, 394, 386],
    'Science': [444, 409, 403]
}
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
proficiency = [32, 69]  # Thailand vs OECD
top_performers = [1, 9]  # Thailand vs OECD

# Create figure
fig = plt.figure(figsize=(20, 24), facecolor='#F5F5F5')
gs = GridSpec(4, 2, figure=fig, height_ratios=[0.8, 2, 1.5, 1.5], hspace=0.4, wspace=0.3)

# Title section
title_box = fig.add_subplot(gs[0, :])
title_box.set_facecolor('#2A5C9A')
title_box.text(0.5, 0.7, 'THAILAND PISA PERFORMANCE: URGENT ACTION REQUIRED', 
               ha='center', va='center', fontsize=24, color='white', weight='bold')
title_box.text(0.5, 0.3, '2012-2025 Trends & Strategic Recovery Pathway', 
               ha='center', va='center', fontsize=18, color='white')
title_box.axis('off')

# Performance trend plot
ax1 = fig.add_subplot(gs[1, 0])
ax1.set_facecolor('white')

# Plot data lines
for idx, subject in enumerate(subjects):
    ax1.plot(years, data[subject], 'o-', color=colors[idx], 
             linewidth=3, markersize=10, label=subject)
    
    # Add value labels
    for year, value in zip(years, data[subject]):
        ax1.text(year, value-7, str(value), ha='center', 
                 va='top', fontsize=12, weight='bold', color=colors[idx])

# Add decline annotations
ax1.annotate('▼ 62 pts', xy=(2017, 410), xytext=(2017, 430), 
             ha='center', va='bottom', fontsize=12,
             arrowprops=dict(arrowstyle='->', color='#333F4B'))
ax1.annotate('▼ 33 pts', xy=(2017, 390), xytext=(2017, 370), 
             ha='center', va='top', fontsize=12,
             arrowprops=dict(arrowstyle='->', color='#333F4B'))
ax1.annotate('▼ 35 pts', xy=(2017, 375), xytext=(2017, 355), 
             ha='center', va='top', fontsize=12,
             arrowprops=dict(arrowstyle='->', color='#333F4B'))

# Formatting
ax1.axhline(y=400, color='#d62728', linestyle='--', alpha=0.7)
ax1.text(2025.5, 400, 'Level 2 Threshold (400)', va='center', fontsize=12, color='#d62728')
ax1.set_ylabel('PISA Score', fontsize=14, labelpad=15)
ax1.set_title('PERFORMANCE DECLINE (2012-2025)', fontsize=16, pad=20, weight='bold')
ax1.legend(loc='lower left', frameon=True)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xlim(2011, 2026)
ax1.set_ylim(340, 460)
ax1.tick_params(axis='both', which='major', labelsize=12)

# Proficiency comparison
ax2 = fig.add_subplot(gs[1, 1])
ax2.set_facecolor('white')

# Bar positions
x = np.arange(2)
width = 0.35

# Plot bars
rects1 = ax2.bar(x - width/2, proficiency, width, label='Thailand', color='#1f77b4')
rects2 = ax2.bar(x + width/2, top_performers, width, label='OECD Avg', color='#ff7f0e')

# Add text labels
ax2.bar_label(rects1, padding=5, fmt='%d%%', fontsize=12, weight='bold')
ax2.bar_label(rects2, padding=5, fmt='%d%%', fontsize=12, weight='bold')

# Formatting
ax2.set_xticks(x)
ax2.set_xticklabels(['Min. Proficiency\n(Level 2+)', 'Top Performers\n(Level 5-6)'], fontsize=12)
ax2.set_title('CRITICAL PROFICIENCY GAPS', fontsize=16, pad=20, weight='bold')
ax2.legend(loc='upper right', fontsize=12)
ax2.set_ylim(0, 80)
ax2.grid(False, axis='x')
ax2.tick_params(axis='y', which='major', labelsize=12)

# Root cause analysis
ax3 = fig.add_subplot(gs[2, 0])
ax3.set_facecolor('white')
ax3.axis('off')

# Create text box
text_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.1",
                          edgecolor='#2A5C9A', facecolor='white', linewidth=2)
ax3.add_patch(text_box)

# Text content
ax3.text(0.5, 0.85, 'ROOT CAUSE ANALYSIS', 
         ha='center', va='center', fontsize=18, weight='bold', color='#2A5C9A')
ax3.text(0.5, 0.65, 'SYSTEMIC INSTRUCTIONAL GAPS', 
         ha='center', va='center', fontsize=16, weight='bold', color='#d62728')

cause_text = (
    "• Over-reliance on rote memorization\n\n"
    "• Insufficient focus on reasoning & comprehension\n\n"
    "• Weak real-world application skills\n\n"
    "• Inadequate modeling & problem-solving strategies\n\n"
    "• Persistent decline since 2012 (pre-dates COVID)"
)
ax3.text(0.1, 0.4, cause_text, ha='left', va='top', fontsize=14)

# Strategy framework
ax4 = fig.add_subplot(gs[2, 1])
ax4.set_facecolor('white')
ax4.axis('off')

# Create strategy boxes
def create_strategy_box(x, y, title, content, color):
    box = FancyBboxPatch((x, y), 0.45, 0.45, boxstyle="round,pad=0.1",
                         edgecolor=color, facecolor='white', linewidth=2)
    ax4.add_patch(box)
    ax4.text(x+0.225, y+0.35, title, ha='center', fontsize=14, weight='bold', color=color)
    ax4.text(x+0.225, y+0.2, content, ha='center', fontsize=12)

# Strategy content
create_strategy_box(0.03, 0.5, 'Instructional Shift', 
                   "From memorization to\nreasoning & modeling", '#1f77b4')
create_strategy_box(0.52, 0.5, 'Assessment Framework', 
                   "PISA-aligned RTI systems\n& diagnostic tools", '#ff7f0e')
create_strategy_box(0.03, 0.05, 'Teacher Development', 
                   "Professional learning in\nreal-world application", '#2ca02c')
create_strategy_box(0.52, 0.05, 'Target Setting', 
                   "2028 Goal: All domains >400\n(Level 2 proficiency)", '#d62728')

ax4.text(0.5, 0.95, 'STRATEGIC RECOVERY FRAMEWORK', 
         ha='center', va='center', fontsize=18, weight='bold', color='#2A5C9A')

# Performance gap
ax5 = fig.add_subplot(gs[3, :])
ax5.set_facecolor('white')

# Data for gap visualization
gap_data = {
    'Subject': ['Reading', 'Mathematics', 'Science'],
    'Thailand 2025': [364, 386, 403],
    'OECD Benchmark': [490, 490, 490]
}

# Plot gaps
x = range(len(gap_data['Subject']))
ax5.bar(x, gap_data['OECD Benchmark'], width=0.6, color='#ff7f0e', label='OECD Benchmark')
ax5.bar(x, gap_data['Thailand 2025'], width=0.6, color='#1f77b4', label='Thailand 2025 Projection')

# Add labels and values
for i in x:
    ax5.text(i, gap_data['Thailand 2025'][i]-15, str(gap_data['Thailand 2025'][i]), 
             ha='center', va='top', color='white', weight='bold', fontsize=12)
    gap = gap_data['OECD Benchmark'][i] - gap_data['Thailand 2025'][i]
    ax5.text(i, gap_data['Thailand 2025'][i]+20, f'Gap: {gap} points', 
             ha='center', va='bottom', fontsize=12, weight='bold')

# Formatting
ax5.set_xticks(x)
ax5.set_xticklabels(gap_data['Subject'], fontsize=14)
ax5.set_ylabel('PISA Score', fontsize=14)
ax5.set_title('PROJECTED 2025 PERFORMANCE GAP VS OECD BENCHMARK', 
              fontsize=16, pad=20, weight='bold')
ax5.legend(loc='upper right', fontsize=12)
ax5.set_ylim(0, 550)
ax5.grid(True, axis='y', linestyle='--', alpha=0.7)

# Footer
footer_text = (
    "Data Source: OECD PISA 2022 | Analysis: DarnellPrice | TechFun STEM ©\n"
    "\"Reversing the trend requires systemic reform—not incremental change.\""
)
fig.text(0.5, 0.02, footer_text, ha='center', fontsize=12, color='#555555')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.savefig('thailand_pisa_summary.png', dpi=300, bbox_inches='tight')
plt.show()