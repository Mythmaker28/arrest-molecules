#!/usr/bin/env python3
"""
Génération Figure S2: Oscillatory Advantage (version Python alternative au script R)
Brouillon 3 panneaux (moléculaire/cellulaire/clinique)

Author: Tommy Lepesteur
License: MIT
Version: 1.0 (draft)
Date: October 2025
"""

import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(3, 1, figsize=(10, 14))
fig.suptitle('Figure S2. Oscillatory Advantage Across Biological Scales\n(Draft - R/ggplot2 high-quality version upon acceptance)', 
             fontsize=16, fontweight='bold')

# ==================================================================
# PANEL A: Molecular Scale (mTOR Activity)
# ==================================================================
ax = axes[0]
time_h = np.linspace(0, 48, 200)

# Control: constant 100%
control_mtor = np.ones_like(time_h) * 100

# Continuous rapamycin: sustained suppression ~20%
continuous_mtor = 20 + 5 * np.sin(time_h / 4)

# Oscillatory rapamycin: 24h on/off cycles
oscillatory_mtor = np.where(
    (time_h % 48) < 24,
    20 + 5 * np.sin(time_h / 4),  # Suppressed during ON
    85 + 10 * np.sin(time_h / 3)   # Recovery during OFF
)

ax.plot(time_h, control_mtor, 'k-', linewidth=2, label='Control')
ax.plot(time_h, continuous_mtor, 'r--', linewidth=2, label='Continuous rapamycin')
ax.plot(time_h, oscillatory_mtor, 'b-', linewidth=2.5, label='Oscillatory rapamycin (24h cycle)')

ax.axhline(100, linestyle=':', color='gray', alpha=0.5, linewidth=1)
ax.text(40, 105, 'Basal activity', fontsize=9, color='gray')

ax.set_xlabel('Time (hours)', fontsize=12, fontweight='bold')
ax.set_ylabel('mTOR Activity (% of baseline)', fontsize=12, fontweight='bold')
ax.set_title('A. Molecular Scale: mTOR Activity', fontsize=13, fontweight='bold', loc='left')
ax.set_ylim(0, 120)
ax.set_xlim(0, 48)
ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)

# ==================================================================
# PANEL B: Cellular Scale (Cumulative Population Doublings)
# ==================================================================
ax = axes[1]
days = np.linspace(0, 60, 100)

# Control: Hayflick limit ~50 CPD
control_cpd = 50 * (1 - np.exp(-days / 20))

# Continuous rapamycin: growth suppression, ~46 CPD
continuous_cpd = 46 * (1 - np.exp(-days / 25))

# Oscillatory rapamycin (48h cycle): enhanced lifespan ~62 CPD (+24%)
oscillatory_cpd = 62 * (1 - np.exp(-days / 22))

ax.plot(days, control_cpd, 'k-', linewidth=2, label='Control')
ax.plot(days, continuous_cpd, 'r--', linewidth=2, label='Continuous rapamycin')
ax.plot(days, oscillatory_cpd, 'b-', linewidth=2.5, label='Oscillatory rapamycin (48h cycle)')

# Annotation +24%
ax.annotate('', xy=(55, 62), xytext=(55, 46),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
ax.text(58, 54, '+24%', fontsize=11, color='blue', fontweight='bold')

ax.set_xlabel('Time (days)', fontsize=12, fontweight='bold')
ax.set_ylabel('Cumulative Population Doublings (CPD)', fontsize=12, fontweight='bold')
ax.set_title('B. Cellular Scale: Replicative Lifespan', fontsize=13, fontweight='bold', loc='left')
ax.set_ylim(0, 70)
ax.set_xlim(0, 60)
ax.legend(loc='lower right', fontsize=10, framealpha=0.9)
ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)

# ==================================================================
# PANEL C: Clinical Scale (Progression-Free Survival)
# ==================================================================
ax = axes[2]
months = np.linspace(0, 24, 100)

# Continuous therapy: median TTP = 5.5 months
continuous_surv = np.exp(-months / 5.5)

# Adaptive oscillatory therapy: median TTP = 10.2 months
adaptive_surv = np.exp(-months / 10.2)

ax.plot(months, continuous_surv, 'r--', linewidth=2, label='Continuous docetaxel')
ax.plot(months, adaptive_surv, 'b-', linewidth=2.5, label='Adaptive oscillatory docetaxel')

# Median TTP markers
ax.axhline(0.5, linestyle=':', color='gray', alpha=0.5, linewidth=1)
ax.text(20, 0.52, 'Median TTP', fontsize=9, color='gray')

ax.axvline(5.5, ymax=0.5, linestyle=':', color='red', alpha=0.5, linewidth=1)
ax.axvline(10.2, ymax=0.5, linestyle=':', color='blue', alpha=0.5, linewidth=1)

ax.text(5.5, -0.07, '5.5 mo', fontsize=10, color='red', ha='center', fontweight='bold')
ax.text(10.2, -0.07, '10.2 mo', fontsize=10, color='blue', ha='center', fontweight='bold')

ax.set_xlabel('Time (months)', fontsize=12, fontweight='bold')
ax.set_ylabel('Progression-Free Fraction', fontsize=12, fontweight='bold')
ax.set_title('C. Clinical Scale: Progression-Free Survival', fontsize=13, fontweight='bold', loc='left')
ax.set_ylim(0, 1.05)
ax.set_xlim(0, 24)
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)

# ==================================================================
# Note bas de page
# ==================================================================
fig.text(0.5, 0.01, 
         'Source: Simulated data based on literature values (see v6.txt references)\n' +
         'Draft Python/matplotlib version. High-quality R/ggplot2 version upon manuscript acceptance.',
         ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.02, 1, 0.98])

# Sauvegarder
output_path = 'Figure_S2_Oscillatory_Advantage_draft.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"✅ Figure S2 draft sauvegardée : {output_path}")
print(f"   Résolution : 300 dpi")
print(f"   Dimensions : 10 × 14 pouces")
print(f"   Note : Version Python. Script R disponible dans Data_Package_FAIR2/")

# Aussi en TIFF pour compatibilité journal
output_tiff = 'Figure_S2_Oscillatory_Advantage_draft.tiff'
plt.savefig(output_tiff, dpi=300, bbox_inches='tight', facecolor='white', format='tiff')
print(f"✅ Version TIFF sauvegardée : {output_tiff}")

plt.close()

