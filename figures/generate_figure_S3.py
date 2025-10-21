#!/usr/bin/env python3
"""
Génération Figure S3: API Calculation Flowchart
Brouillon avec boxes et flèches (haute déf Visio/draw.io après acceptation)

Author: Tommy Lepesteur
License: MIT
Version: 1.0 (draft)
Date: October 2025
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('white')

# Titre
fig.suptitle('Figure S3. Arrest Potency Index (API) Calculation Workflow\n(Draft - Professional flowchart upon acceptance)', 
             fontsize=16, fontweight='bold', y=0.96)

def draw_box(ax, x, y, width, height, text, color='lightblue', text_size=10, bold=False):
    """Dessiner une box avec texte"""
    box = FancyBboxPatch((x-width/2, y-height/2), width, height,
                         boxstyle="round,pad=0.1",
                         facecolor=color, edgecolor='black', linewidth=2)
    ax.add_patch(box)
    
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', 
            fontsize=text_size, fontweight=weight, wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, label=''):
    """Dessiner une flèche entre deux points"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=30,
                           linewidth=2, color='black')
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.3, mid_y, label, fontsize=8, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# === INPUTS (top) ===
draw_box(ax, 3, 9, 2, 0.8, 'K_d\n(dissociation constant)\nnM', '#FFE5CC', 9, bold=True)
draw_box(ax, 5.5, 9, 2, 0.8, 'k_off\n(dissociation rate)\nmin⁻¹', '#FFE5CC', 9, bold=True)
draw_box(ax, 8, 9, 2, 0.8, 't_onset\n(time to 50% effect)\nmin', '#FFE5CC', 9, bold=True)
draw_box(ax, 10.5, 9, 2, 0.8, 'EC₅₀\n(effective conc.)\nnM', '#FFE5CC', 9, bold=True)

# === INTERMEDIATE CALCULATIONS ===
draw_box(ax, 4.25, 7.5, 2.5, 0.7, 'τ_residence = 1/k_off\n(residence time, min)', '#D4E6F1', 9)
draw_arrow(ax, 5.5, 8.6, 4.25, 7.9)

draw_box(ax, 3, 6.5, 2.5, 0.7, '1/K_d\n(affinity term)\nnM⁻¹', '#D4E6F1', 9)
draw_arrow(ax, 3, 8.6, 3, 6.9)

draw_box(ax, 9.25, 6.5, 2.5, 0.7, 't_onset × EC₅₀\n(response term)\nmin·nM', '#D4E6F1', 9)
draw_arrow(ax, 8, 8.6, 8.5, 6.9)
draw_arrow(ax, 10.5, 8.6, 9.7, 6.9)

# === NUMERATOR ===
draw_box(ax, 3.5, 5, 3, 0.8, 'Numerator =\n(1/K_d) × τ_residence', '#A9DFBF', 10, bold=True)
draw_arrow(ax, 3, 6.1, 3.5, 5.4)
draw_arrow(ax, 4.25, 7.1, 3.8, 5.4)

# === DENOMINATOR ===
draw_box(ax, 9.5, 5, 3, 0.8, 'Denominator =\nt_onset × EC₅₀', '#F9E79F', 10, bold=True)
draw_arrow(ax, 9.25, 6.1, 9.5, 5.4)

# === API ABSOLUTE ===
draw_box(ax, 6.5, 3.5, 4, 1, 'API_absolute =\nNumerator / Denominator\n(units: nM⁻²)', '#AED6F1', 11, bold=True)
draw_arrow(ax, 3.5, 4.6, 5.5, 4)
draw_arrow(ax, 9.5, 4.6, 7.5, 4)

# === NORMALIZATION ===
draw_box(ax, 11, 3.5, 2, 0.7, 'Salvinorin A\nAPI_ref = 6.95 nM⁻²', '#FADBD8', 9)

# === API RELATIVE ===
draw_box(ax, 6.5, 2, 4, 1, 'API_relative =\nAPI_absolute / API_salvinorin_A\n(dimensionless)', '#85C1E2', 11, bold=True)
draw_arrow(ax, 6.5, 3, 6.5, 2.5)
draw_arrow(ax, 11, 3.15, 8.5, 2.5, 'normalize')

# === MONTE CARLO ===
draw_box(ax, 2, 0.8, 3, 0.8, 'Monte Carlo\nUncertainty\nQuantification\n(10,000 iterations)', '#F5B7B1', 9)
draw_arrow(ax, 3, 1.5, 4.5, 1.5)

# === OUTPUT FINAL ===
draw_box(ax, 6.5, 0.8, 3, 0.8, 'API ± 95% CI\n+ Confidence Grade', '#76D7C4', 11, bold=True)
draw_arrow(ax, 6.5, 1.5, 6.5, 1.3)

# === LEGEND ===
legend_x, legend_y = 11.5, 7
ax.text(legend_x, legend_y + 0.5, 'Legend:', fontsize=10, fontweight='bold')
ax.text(legend_x, legend_y, '• Orange: Inputs (literature)', fontsize=8)
ax.text(legend_x, legend_y - 0.4, '• Light blue: Intermediate', fontsize=8)
ax.text(legend_x, legend_y - 0.8, '• Green: Numerator', fontsize=8)
ax.text(legend_x, legend_y - 1.2, '• Yellow: Denominator', fontsize=8)
ax.text(legend_x, legend_y - 1.6, '• Blue: API values', fontsize=8)
ax.text(legend_x, legend_y - 2.0, '• Pink: Reference / MC', fontsize=8)
ax.text(legend_x, legend_y - 2.4, '• Teal: Final output', fontsize=8)

# Note bas de page
fig.text(0.5, 0.02, 
         'Note: Draft flowchart using matplotlib. Professional version (Visio/draw.io) upon manuscript acceptance.',
         ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 0.94])

# Sauvegarder
output_path = 'Figure_S3_API_Flowchart_draft.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"✅ Figure S3 draft sauvegardée : {output_path}")
print(f"   Résolution : 300 dpi")
print(f"   Dimensions : 14 × 10 pouces")
print(f"   Note : Flowchart basique. Version professionnelle après acceptation.")

plt.close()

