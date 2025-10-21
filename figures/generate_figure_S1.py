#!/usr/bin/env python3
"""
Génération Figure S1: Structures moléculaires avec highlights pharmacophores
Brouillon basse-fidélité mais propre (haute déf sera créée avec ChemDraw après acceptation)

Author: Tommy Lepesteur
License: MIT
Version: 1.0 (draft)
Date: October 2025
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# Configuration
fig, axes = plt.subplots(3, 2, figsize=(12, 16))
fig.suptitle('Figure S1. Molecular Structures with Pharmacophore Highlights\n(Draft - High-fidelity ChemDraw version upon acceptance)', 
             fontsize=16, fontweight='bold', y=0.995)

compounds = [
    {
        'name': 'Salvinorin A',
        'formula': 'C23H28O8',
        'mw': '432.47',
        'logp': '2.73',
        'api': '1.00',
        'features': ['Rigid tricyclic core', 'C2-acetyl (KOR binding)', '3 rotatable bonds'],
        'color': '#2E86AB'
    },
    {
        'name': 'Paclitaxel',
        'formula': 'C47H51NO14',
        'mw': '853.91',
        'logp': '3.2',
        'api': '0.44',
        'features': ['Taxane rigid core', 'β-tubulin K_d 0.9 nM', '15 rotatable bonds'],
        'color': '#A23B72'
    },
    {
        'name': 'Rapamycin',
        'formula': 'C51H79NO13',
        'mw': '914.18',
        'logp': '4.3',
        'api': '0.12',
        'features': ['31-membered macrocycle', 'mTORC1 K_i 0.1 nM', 'Slow onset reduces API'],
        'color': '#F18F01'
    },
    {
        'name': 'Capsaicin',
        'formula': 'C18H27NO3',
        'mw': '305.41',
        'logp': '3.0',
        'api': '0.024',
        'features': ['Flexible chain (4 rotatable bonds)', 'TRPV1 EC50 700 nM', 'Lower API'],
        'color': '#C73E1D'
    },
    {
        'name': 'Tetrodotoxin',
        'formula': 'C11H17N3O8',
        'mw': '319.27',
        'logp': '-4.3',
        'api': '4.0',
        'features': ['Rigid polycyclic cage', 'Nav IC50 5-15 nM', 'Highest API'],
        'color': '#6A4C93'
    },
    {
        'name': 'Resveratrol',
        'formula': 'C14H12O3',
        'mw': '228.25',
        'logp': '3.1',
        'api': '0.00003',
        'features': ['Minimal rigidity (2 rot bonds)', 'Rapid metabolism', 'Negligible API'],
        'color': '#1A535C'
    }
]

for idx, (ax, compound) in enumerate(zip(axes.flat, compounds)):
    # Fond blanc
    ax.set_facecolor('white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Cadre principal
    fancy_box = FancyBboxPatch((0.5, 0.5), 9, 9, 
                               boxstyle="round,pad=0.1", 
                               edgecolor=compound['color'], 
                               facecolor='white', 
                               linewidth=3)
    ax.add_patch(fancy_box)
    
    # Titre composé
    ax.text(5, 9, compound['name'], 
            fontsize=14, fontweight='bold', 
            ha='center', va='top',
            color=compound['color'])
    
    # Zone structure moléculaire simulée (placeholder)
    # En production: Remplacer par vraies structures 2D from ChemDraw
    structure_box = Rectangle((1.5, 4.5), 7, 3.5, 
                              facecolor='#F0F0F0', 
                              edgecolor='gray', 
                              linewidth=1)
    ax.add_patch(structure_box)
    
    ax.text(5, 6.25, f"[Structure 2D]\n{compound['formula']}", 
            fontsize=10, ha='center', va='center',
            style='italic', color='gray')
    
    # Highlights pharmacophores (zones colorées simulées)
    # Rouge = rigid core, Bleu = H-bond, Vert = lipophile
    if 'rigid' in ' '.join(compound['features']).lower():
        rigid_patch = patches.Circle((3, 6), 0.6, color='red', alpha=0.3)
        ax.add_patch(rigid_patch)
        ax.text(3, 5.2, 'Rigid', fontsize=7, ha='center', color='red', fontweight='bold')
    
    if 'acetyl' in ' '.join(compound['features']).lower() or 'hydroxyl' in ' '.join(compound['features']).lower():
        hbond_patch = patches.Circle((7, 6), 0.6, color='blue', alpha=0.3)
        ax.add_patch(hbond_patch)
        ax.text(7, 5.2, 'H-bond', fontsize=7, ha='center', color='blue', fontweight='bold')
    
    # Propriétés physicochimiques
    props_y = 3.8
    ax.text(1.2, props_y, f"MW: {compound['mw']} g/mol", fontsize=9)
    ax.text(1.2, props_y - 0.5, f"logP: {compound['logp']}", fontsize=9)
    ax.text(1.2, props_y - 1.0, f"API: {compound['api']}", fontsize=9, fontweight='bold', color=compound['color'])
    
    # Caractéristiques clés
    features_y = 2.2
    for i, feature in enumerate(compound['features']):
        ax.text(1.2, features_y - i*0.4, f"• {feature}", fontsize=8, wrap=True)

# Légende globale
fig.text(0.5, 0.02, 
         'Color coding: Red = rigid core | Blue = H-bond donors/acceptors | Green = lipophilic regions\n' +
         'API = Arrest Potency Index (relative to Salvinorin A = 1.00)\n' +
         'Note: Placeholder structures. High-resolution ChemDraw versions upon manuscript acceptance.',
         ha='center', fontsize=9, style='italic', color='gray')

plt.tight_layout(rect=[0, 0.03, 1, 0.99])

# Sauvegarder
output_path = 'Figure_S1_Molecular_Structures_draft.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"✅ Figure S1 draft sauvegardée : {output_path}")
print(f"   Résolution : 300 dpi")
print(f"   Dimensions : 12 × 16 pouces")
print(f"   Note : Structures placeholder. ChemDraw haute-déf après acceptation.")

plt.close()

