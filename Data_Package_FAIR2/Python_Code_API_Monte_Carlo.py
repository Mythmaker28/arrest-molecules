#!/usr/bin/env python3
"""
Arrest Potency Index (API) Calculator with Monte Carlo Uncertainty Quantification

Author: Tommy Mythmaker
License: MIT
Version: 1.0
Date: October 2025

This script calculates the Arrest Potency Index (API) for molecular arrest agents
as defined in "Molecular Arrest in Biological Regulation" framework.

Dependencies: numpy, pandas, matplotlib, scipy
Install: pip install numpy pandas matplotlib scipy

Usage:
    python Python_Code_API_Monte_Carlo.py --compound Rapamycin
    python Python_Code_API_Monte_Carlo.py --all
    python Python_Code_API_Monte_Carlo.py --new_compound --params K_d=0.1 tau=120 t_onset=1440 EC50=1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import argparse


def calculate_API_absolute(K_d_nM, tau_residence_min, t_onset_min, EC50_nM):
    """
    Calculate absolute API value.
    
    Parameters:
    -----------
    K_d_nM : float
        Equilibrium dissociation constant in nanomolar
    tau_residence_min : float
        Target residence time in minutes (1/k_off)
    t_onset_min : float
        Time to 50% maximal effect in minutes
    EC50_nM : float
        Half-maximal effective concentration in nanomolar
    
    Returns:
    --------
    float : API in nM^-2 units (before normalization)
    
    Formula:
    --------
    API = [(1/K_d) × τ_residence] / [t_onset × EC₅₀]
    """
    if K_d_nM <= 0 or EC50_nM <= 0 or t_onset_min <= 0 or tau_residence_min <= 0:
        raise ValueError("All parameters must be positive")
    
    numerator = (1.0 / K_d_nM) * tau_residence_min
    denominator = t_onset_min * EC50_nM
    
    API_abs = numerator / denominator
    return API_abs


def calculate_API_relative(API_absolute, reference_API=6.95):
    """
    Normalize API to salvinorin A reference standard.
    
    Parameters:
    -----------
    API_absolute : float
        Absolute API value in nM^-2
    reference_API : float, default=6.95
        Salvinorin A reference value
    
    Returns:
    --------
    float : Normalized API (dimensionless)
    """
    return API_absolute / reference_API


def monte_carlo_API_uncertainty(K_d_params, tau_params, t_onset_params, EC50_params, 
                                 n_iterations=10000, reference_API=6.95):
    """
    Perform Monte Carlo simulation for API uncertainty quantification.
    
    Parameters:
    -----------
    K_d_params : tuple (mean_nM, sd_log_space, n_studies)
        K_d distribution parameters
    tau_params : tuple (mean_min, sd_log_space, n_studies)
        Residence time distribution parameters
    t_onset_params : tuple (mean_min, sd_log_space, n_studies)
        Onset time distribution parameters
    EC50_params : tuple (mean_nM, sd_log_space, n_studies)
        EC50 distribution parameters
    n_iterations : int, default=10000
        Number of Monte Carlo iterations
    reference_API : float, default=6.95
        Normalization reference
    
    Returns:
    --------
    dict : Contains median, CI_lower, CI_upper, mean, std, all_samples
    """
    
    # Define log-normal SDs based on study quality
    def get_log_sd(n_studies):
        if n_studies >= 4:
            return 0.10  # ±25% range
        elif n_studies >= 2:
            return 0.15  # ±40% range
        else:
            return 0.20  # ±50% range
    
    # Override with provided SDs or use defaults
    sd_K_d = K_d_params[1] if len(K_d_params) > 1 else get_log_sd(K_d_params[2] if len(K_d_params) > 2 else 1)
    sd_tau = tau_params[1] if len(tau_params) > 1 else get_log_sd(tau_params[2] if len(tau_params) > 2 else 1)
    sd_onset = t_onset_params[1] if len(t_onset_params) > 1 else get_log_sd(t_onset_params[2] if len(t_onset_params) > 2 else 1)
    sd_EC50 = EC50_params[1] if len(EC50_params) > 1 else get_log_sd(EC50_params[2] if len(EC50_params) > 2 else 1)
    
    # Sample from log-normal distributions
    np.random.seed(42)  # Reproducibility
    
    K_d_samples = np.random.lognormal(np.log(K_d_params[0]), sd_K_d, n_iterations)
    tau_samples = np.random.lognormal(np.log(tau_params[0]), sd_tau, n_iterations)
    t_onset_samples = np.random.lognormal(np.log(t_onset_params[0]), sd_onset, n_iterations)
    EC50_samples = np.random.lognormal(np.log(EC50_params[0]), sd_EC50, n_iterations)
    
    # Calculate API for each iteration
    API_absolute_samples = ((1 / K_d_samples) * tau_samples) / (t_onset_samples * EC50_samples)
    API_relative_samples = API_absolute_samples / reference_API
    
    # Extract statistics
    results = {
        'median': np.median(API_relative_samples),
        'mean': np.mean(API_relative_samples),
        'std': np.std(API_relative_samples),
        'CI_lower': np.percentile(API_relative_samples, 2.5),
        'CI_upper': np.percentile(API_relative_samples, 97.5),
        'all_samples': API_relative_samples
    }
    
    return results


def assign_confidence_grade(K_d_quality, tau_quality, onset_quality, EC50_quality):
    """
    Assign overall confidence grade based on parameter quality.
    
    Quality codes:
    - 'measured' : Direct experimental measurement
    - 'estimated' : Calculated from related measurements
    - 'inferred' : Extrapolated from indirect data
    
    Returns:
    --------
    str : 'VERY HIGH', 'HIGH', 'MODERATE', or 'LOW'
    """
    quality_scores = {
        'measured': 3,
        'estimated': 2,
        'inferred': 1
    }
    
    total_score = (quality_scores.get(K_d_quality, 0) + 
                   quality_scores.get(tau_quality, 0) + 
                   quality_scores.get(onset_quality, 0) + 
                   quality_scores.get(EC50_quality, 0))
    
    if total_score >= 11:
        return 'VERY HIGH'
    elif total_score >= 9:
        return 'HIGH'
    elif total_score >= 6:
        return 'MODERATE'
    else:
        return 'LOW'


# Predefined compound database
COMPOUND_DATABASE = {
    'Salvinorin A': {
        'K_d': (1.8, 0.10, 4),  # mean, sd_log, n_studies
        'tau': (25, 0.15, 2),
        't_onset': (1, 0.10, 3),
        'EC50': (2, 0.12, 3),
        'quality': ('measured', 'estimated', 'measured', 'measured')
    },
    'Rapamycin': {
        'K_d': (0.1, 0.08, 5),
        'tau': (120, 0.20, 1),  # Estimated, higher uncertainty
        't_onset': (1440, 0.15, 2),
        'EC50': (1, 0.10, 4),
        'quality': ('measured', 'estimated', 'estimated', 'measured')
    },
    'Paclitaxel': {
        'K_d': (0.9, 0.10, 3),
        'tau': (720, 0.15, 2),
        't_onset': (360, 0.20, 2),  # Variable onset time
        'EC50': (10, 0.12, 3),
        'quality': ('measured', 'estimated', 'estimated', 'measured')
    },
    'Capsaicin': {
        'K_d': (700, 0.15, 3),
        'tau': (45, 0.20, 1),
        't_onset': (5, 0.10, 4),
        'EC50': (700, 0.25, 3),  # High EC50 variability (400-1000 nM)
        'quality': ('measured', 'estimated', 'measured', 'measured')
    },
    'Tetrodotoxin': {
        'K_d': (10, 0.12, 5),
        'tau': (360, 0.20, 2),  # Variable across Nav subtypes
        't_onset': (3, 0.10, 3),
        'EC50': (10, 0.10, 4),
        'quality': ('measured', 'estimated', 'measured', 'measured')
    },
    'Resveratrol': {
        'K_d': (50000, 0.30, 2),  # Contested, high uncertainty
        'tau': (1, 0.50, 1),  # Very rapid dissociation, poorly characterized
        't_onset': (720, 0.30, 1),
        'EC50': (50000, 0.40, 2),
        'quality': ('estimated', 'inferred', 'estimated', 'estimated')
    }
}


def analyze_compound(compound_name, n_iterations=10000, plot=True):
    """
    Full analysis pipeline for a single compound.
    
    Parameters:
    -----------
    compound_name : str
        Name of compound (must be in COMPOUND_DATABASE)
    n_iterations : int
        Monte Carlo iterations
    plot : bool
        Generate diagnostic plots
    
    Returns:
    --------
    dict : Results including API, CI, confidence grade
    """
    
    if compound_name not in COMPOUND_DATABASE:
        raise ValueError(f"Compound '{compound_name}' not in database. Available: {list(COMPOUND_DATABASE.keys())}")
    
    data = COMPOUND_DATABASE[compound_name]
    
    # Calculate point estimate
    API_abs = calculate_API_absolute(
        K_d_nM=data['K_d'][0],
        tau_residence_min=data['tau'][0],
        t_onset_min=data['t_onset'][0],
        EC50_nM=data['EC50'][0]
    )
    API_rel = calculate_API_relative(API_abs)
    
    # Monte Carlo uncertainty
    mc_results = monte_carlo_API_uncertainty(
        K_d_params=data['K_d'],
        tau_params=data['tau'],
        t_onset_params=data['t_onset'],
        EC50_params=data['EC50'],
        n_iterations=n_iterations
    )
    
    # Confidence grading
    confidence = assign_confidence_grade(*data['quality'])
    
    # Compile results
    results = {
        'compound': compound_name,
        'API_absolute': API_abs,
        'API_relative_point': API_rel,
        'API_relative_median': mc_results['median'],
        'CI_lower': mc_results['CI_lower'],
        'CI_upper': mc_results['CI_upper'],
        'confidence': confidence,
        'samples': mc_results['all_samples']
    }
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"  COMPOUND: {compound_name}")
    print(f"{'='*60}")
    print(f"  Point estimate API (relative): {API_rel:.5f}")
    print(f"  Median API (Monte Carlo):      {mc_results['median']:.5f}")
    print(f"  95% Confidence Interval:       [{mc_results['CI_lower']:.5f}, {mc_results['CI_upper']:.5f}]")
    print(f"  Confidence grade:              {confidence}")
    print(f"  Uncertainty range:             ±{((mc_results['CI_upper']-mc_results['CI_lower'])/2 / mc_results['median'] * 100):.1f}%")
    print(f"{'='*60}\n")
    
    # Optional plotting
    if plot:
        plot_API_distribution(results)
    
    return results


def plot_API_distribution(results):
    """
    Generate diagnostic plots for API distribution.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Histogram
    axes[0].hist(results['samples'], bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='black')
    axes[0].axvline(results['API_relative_median'], color='red', linestyle='--', linewidth=2, label=f'Median: {results["API_relative_median"]:.4f}')
    axes[0].axvline(results['CI_lower'], color='orange', linestyle=':', linewidth=1.5, label=f'95% CI')
    axes[0].axvline(results['CI_upper'], color='orange', linestyle=':', linewidth=1.5)
    axes[0].set_xlabel('API (relative to Salvinorin A)', fontsize=12)
    axes[0].set_ylabel('Probability Density', fontsize=12)
    axes[0].set_title(f'{results["compound"]} - API Distribution', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].grid(alpha=0.3)
    
    # Q-Q plot
    stats.probplot(results['samples'], dist="norm", plot=axes[1])
    axes[1].set_title(f'Q-Q Plot (Normality Check)', fontsize=14, fontweight='bold')
    axes[1].grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'API_Distribution_{results["compound"].replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
    print(f"  → Plot saved: API_Distribution_{results['compound'].replace(' ', '_')}.png")
    plt.close()


def compare_all_compounds(plot_comparison=True):
    """
    Calculate API for all compounds and generate comparison plot.
    """
    results_all = []
    
    for compound_name in COMPOUND_DATABASE.keys():
        result = analyze_compound(compound_name, n_iterations=10000, plot=False)
        results_all.append(result)
    
    # Create summary dataframe
    df_summary = pd.DataFrame({
        'Compound': [r['compound'] for r in results_all],
        'API': [r['API_relative_median'] for r in results_all],
        'CI_Lower': [r['CI_lower'] for r in results_all],
        'CI_Upper': [r['CI_upper'] for r in results_all],
        'Confidence': [r['confidence'] for r in results_all]
    })
    
    # Sort by API
    df_summary = df_summary.sort_values('API', ascending=False).reset_index(drop=True)
    
    print("\n" + "="*80)
    print("  COMPARATIVE API ANALYSIS - ALL COMPOUNDS")
    print("="*80)
    print(df_summary.to_string(index=False))
    print("="*80 + "\n")
    
    # Save to CSV
    df_summary.to_csv('API_Comparison_All_Compounds.csv', index=False)
    print("  → Summary saved: API_Comparison_All_Compounds.csv\n")
    
    # Comparison plot
    if plot_comparison:
        plot_API_comparison(df_summary)
    
    return df_summary


def plot_API_comparison(df_summary):
    """
    Generate comparative bar plot with error bars.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Color by confidence
    colors = []
    for conf in df_summary['Confidence']:
        if conf == 'VERY HIGH':
            colors.append('darkgreen')
        elif conf == 'HIGH':
            colors.append('green')
        elif conf == 'MODERATE':
            colors.append('orange')
        else:
            colors.append('red')
    
    # Bar plot with error bars
    x_pos = np.arange(len(df_summary))
    bars = ax.bar(x_pos, df_summary['API'], color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    
    # Error bars (asymmetric)
    yerr_lower = df_summary['API'] - df_summary['CI_Lower']
    yerr_upper = df_summary['CI_Upper'] - df_summary['API']
    ax.errorbar(x_pos, df_summary['API'], yerr=[yerr_lower, yerr_upper], 
                fmt='none', ecolor='black', capsize=5, capthick=2)
    
    # Formatting
    ax.set_xticks(x_pos)
    ax.set_xticklabels(df_summary['Compound'], rotation=45, ha='right', fontsize=11)
    ax.set_ylabel('Arrest Potency Index (API)\n[relative to Salvinorin A = 1.0]', fontsize=12, fontweight='bold')
    ax.set_title('Comparative Arrest Potency with 95% Confidence Intervals', fontsize=14, fontweight='bold')
    ax.set_yscale('log')  # Log scale due to 5 orders of magnitude range
    ax.grid(axis='y', alpha=0.3, which='both')
    
    # Reference line for salvinorin A
    ax.axhline(y=1.0, color='blue', linestyle='--', linewidth=2, alpha=0.5, label='Salvinorin A reference')
    
    # Legend for confidence colors
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='darkgreen', label='Very High Confidence'),
        Patch(facecolor='green', label='High Confidence'),
        Patch(facecolor='orange', label='Moderate Confidence'),
        Patch(facecolor='red', label='Low Confidence')
    ]
    ax.legend(handles=legend_elements, loc='upper right', framealpha=0.9)
    
    plt.tight_layout()
    plt.savefig('API_Comparison_All_Compounds.png', dpi=300, bbox_inches='tight')
    print("  → Comparison plot saved: API_Comparison_All_Compounds.png\n")
    plt.close()


def calculate_new_compound(K_d, tau, t_onset, EC50, compound_name="New Compound", n_iterations=10000):
    """
    Calculate API for a user-specified novel compound.
    
    Parameters:
    -----------
    K_d : float
        Dissociation constant in nM
    tau : float
        Residence time in minutes
    t_onset : float
        Onset time in minutes
    EC50 : float
        EC50 in nM
    compound_name : str
        Name for labeling
    
    Returns:
    --------
    dict : API results with uncertainty
    """
    # Assume moderate uncertainty (1 study equivalent)
    params_K_d = (K_d, 0.20, 1)
    params_tau = (tau, 0.20, 1)
    params_onset = (t_onset, 0.15, 1)
    params_EC50 = (EC50, 0.20, 1)
    
    API_abs = calculate_API_absolute(K_d, tau, t_onset, EC50)
    API_rel = calculate_API_relative(API_abs)
    
    mc_results = monte_carlo_API_uncertainty(
        params_K_d, params_tau, params_onset, params_EC50, n_iterations
    )
    
    print(f"\n{'='*60}")
    print(f"  NEW COMPOUND: {compound_name}")
    print(f"{'='*60}")
    print(f"  Input parameters:")
    print(f"    K_d = {K_d} nM")
    print(f"    τ_residence = {tau} min")
    print(f"    t_onset = {t_onset} min")
    print(f"    EC₅₀ = {EC50} nM")
    print(f"\n  Calculated API:")
    print(f"    Absolute: {API_abs:.2e} nM^-2")
    print(f"    Relative: {API_rel:.5f}")
    print(f"    95% CI: [{mc_results['CI_lower']:.5f}, {mc_results['CI_upper']:.5f}]")
    print(f"\n  Interpretation:")
    if API_rel > 2.0:
        print(f"    → EXCEPTIONALLY POTENT (API > 2.0)")
        print(f"    → Suitable for: Acute interventions, procedural anesthesia")
    elif API_rel >= 1.0:
        print(f"    → HIGH POTENCY (API 1.0-2.0)")
        print(f"    → Suitable for: Psychiatric reset, rapid analgesia")
    elif API_rel >= 0.3:
        print(f"    → MODERATE POTENCY (API 0.3-1.0)")
        print(f"    → Suitable for: Chemotherapy, chronic pain")
    elif API_rel >= 0.1:
        print(f"    → LOWER POTENCY (API 0.1-0.3)")
        print(f"    → Suitable for: Immunosuppression, metabolic modulation")
    else:
        print(f"    → MINIMAL ARREST (API < 0.1)")
        print(f"    → Clinical utility uncertain; investigate PK barriers")
    print(f"{'='*60}\n")
    
    return mc_results


# Command-line interface
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calculate Arrest Potency Index (API) with uncertainty quantification',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python Python_Code_API_Monte_Carlo.py --compound "Salvinorin A"
  python Python_Code_API_Monte_Carlo.py --all
  python Python_Code_API_Monte_Carlo.py --new_compound --name "Novel KOR Agonist" --K_d 5 --tau 8 --t_onset 0.5 --EC50 3
        """
    )
    
    parser.add_argument('--compound', type=str, help='Compound name from database')
    parser.add_argument('--all', action='store_true', help='Analyze all compounds')
    parser.add_argument('--new_compound', action='store_true', help='Calculate API for novel compound')
    parser.add_argument('--name', type=str, default='New Compound', help='Name for new compound')
    parser.add_argument('--K_d', type=float, help='K_d in nM')
    parser.add_argument('--tau', type=float, help='Residence time in min')
    parser.add_argument('--t_onset', type=float, help='Onset time in min')
    parser.add_argument('--EC50', type=float, help='EC50 in nM')
    parser.add_argument('--iterations', type=int, default=10000, help='Monte Carlo iterations (default 10000)')
    parser.add_argument('--no_plot', action='store_true', help='Suppress plots')
    
    args = parser.parse_args()
    
    # Execute based on arguments
    if args.all:
        compare_all_compounds(plot_comparison=not args.no_plot)
    
    elif args.new_compound:
        if not all([args.K_d, args.tau, args.t_onset, args.EC50]):
            parser.error("--new_compound requires --K_d, --tau, --t_onset, --EC50")
        calculate_new_compound(args.K_d, args.tau, args.t_onset, args.EC50, 
                              compound_name=args.name, n_iterations=args.iterations)
    
    elif args.compound:
        analyze_compound(args.compound, n_iterations=args.iterations, plot=not args.no_plot)
    
    else:
        parser.print_help()
        print("\n  → Run with --all to analyze all compounds")
        print("  → Run with --compound 'Salvinorin A' for single compound")
        print("  → Run with --new_compound for novel compound calculation\n")


# Example usage (when imported as module):
"""
import Python_Code_API_Monte_Carlo as api_calc

# Single compound
results = api_calc.analyze_compound('Rapamycin', n_iterations=10000)

# All compounds
summary = api_calc.compare_all_compounds()

# Novel compound
api_calc.calculate_new_compound(K_d=5, tau=10, t_onset=2, EC50=8, compound_name="Experimental-KOR-001")
"""

