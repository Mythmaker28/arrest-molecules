#!/usr/bin/env Rscript
# =============================================================================
# Oscillatory Advantage Figure S2 - Molecular Arrest Framework
# 
# Author: Tommy Lepesteur
# License: MIT
# Version: 1.0
# Date: October 2025
#
# Description:
# Generates 3-panel figure illustrating oscillatory advantage across scales:
#   Panel A: Molecular (mTOR activity over 48h)
#   Panel B: Cellular (cumulative population doublings)
#   Panel C: Clinical (survival curves for adaptive therapy)
#
# Requirements:
#   install.packages(c("ggplot2", "dplyr", "patchwork", "jsonlite"))
#
# Usage:
#   Rscript R_Code_Figures_S2.R
#   Output: figures/Figure_S2_Oscillatory_Advantage.png (300 dpi)
# =============================================================================

# Load required libraries
suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
  library(patchwork)
  library(jsonlite)
})

# Create output directory
if (!dir.exists("figures")) {
  dir.create("figures", recursive = TRUE)
}

# =============================================================================
# Panel A: Molecular Scale (mTOR Activity Over 48h)
# =============================================================================

generate_panel_A <- function() {
  # Time points (hours)
  time <- seq(0, 48, by = 0.5)
  
  # Control: constant 100% activity
  control <- data.frame(
    Time_h = time,
    mTOR_Activity = rep(100, length(time)),
    Condition = "Control"
  )
  
  # Continuous rapamycin: sustained suppression to ~20%
  continuous <- data.frame(
    Time_h = time,
    mTOR_Activity = 20 + 5 * sin(time / 4), # slight oscillation around 20%
    Condition = "Continuous rapamycin"
  )
  
  # Oscillatory rapamycin: 24h on/off cycle
  oscillatory_activity <- ifelse(
    time %% 48 < 24,
    20 + 5 * sin(time / 4),  # suppressed during ON phase
    85 + 10 * sin(time / 3)  # recovery during OFF phase
  )
  oscillatory <- data.frame(
    Time_h = time,
    mTOR_Activity = oscillatory_activity,
    Condition = "Oscillatory rapamycin (24h cycle)"
  )
  
  # Combine data
  data_A <- rbind(control, continuous, oscillatory)
  
  # Plot
  p_A <- ggplot(data_A, aes(x = Time_h, y = mTOR_Activity, color = Condition, linetype = Condition)) +
    geom_line(size = 1.2) +
    scale_color_manual(values = c("Control" = "black", 
                                   "Continuous rapamycin" = "red", 
                                   "Oscillatory rapamycin (24h cycle)" = "blue")) +
    scale_linetype_manual(values = c("Control" = "solid", 
                                      "Continuous rapamycin" = "dashed", 
                                      "Oscillatory rapamycin (24h cycle)" = "solid")) +
    labs(
      title = "A. Molecular Scale: mTOR Activity",
      x = "Time (hours)",
      y = "mTOR Activity (% of baseline)",
      color = NULL,
      linetype = NULL
    ) +
    theme_classic(base_size = 12) +
    theme(
      legend.position = "bottom",
      legend.text = element_text(size = 10),
      plot.title = element_text(face = "bold")
    ) +
    ylim(0, 120) +
    geom_hline(yintercept = 100, linetype = "dotted", color = "gray50", alpha = 0.5) +
    annotate("text", x = 40, y = 105, label = "Basal activity", size = 3, color = "gray50")
  
  return(p_A)
}

# =============================================================================
# Panel B: Cellular Scale (Cumulative Population Doublings)
# =============================================================================

generate_panel_B <- function() {
  # Time points (days)
  days <- seq(0, 60, by = 2)
  
  # Control: standard Hayflick limit (~50 CPD)
  control_cpd <- 50 * (1 - exp(-days / 20))
  
  # Continuous rapamycin: growth suppression, reduced final CPD (~46)
  continuous_cpd <- 46 * (1 - exp(-days / 25))
  
  # Oscillatory rapamycin (48h cycle): enhanced lifespan (~62 CPD, +24%)
  oscillatory_cpd <- 62 * (1 - exp(-days / 22))
  
  data_B <- data.frame(
    Days = rep(days, 3),
    CPD = c(control_cpd, continuous_cpd, oscillatory_cpd),
    Condition = rep(c("Control", "Continuous rapamycin", "Oscillatory rapamycin (48h cycle)"), each = length(days))
  )
  
  # Plot
  p_B <- ggplot(data_B, aes(x = Days, y = CPD, color = Condition, linetype = Condition)) +
    geom_line(size = 1.2) +
    scale_color_manual(values = c("Control" = "black", 
                                   "Continuous rapamycin" = "red", 
                                   "Oscillatory rapamycin (48h cycle)" = "blue")) +
    scale_linetype_manual(values = c("Control" = "solid", 
                                      "Continuous rapamycin" = "dashed", 
                                      "Oscillatory rapamycin (48h cycle)" = "solid")) +
    labs(
      title = "B. Cellular Scale: Replicative Lifespan",
      x = "Time (days)",
      y = "Cumulative Population Doublings (CPD)",
      color = NULL,
      linetype = NULL
    ) +
    theme_classic(base_size = 12) +
    theme(
      legend.position = "bottom",
      legend.text = element_text(size = 10),
      plot.title = element_text(face = "bold")
    ) +
    ylim(0, 70) +
    annotate("segment", x = 55, xend = 55, y = 46, yend = 62, 
             arrow = arrow(length = unit(0.3, "cm"), ends = "both"), 
             color = "blue", size = 0.8) +
    annotate("text", x = 58, y = 54, label = "+24%", size = 4, color = "blue", fontface = "bold")
  
  return(p_B)
}

# =============================================================================
# Panel C: Clinical Scale (Survival - Adaptive Therapy)
# =============================================================================

generate_panel_C <- function() {
  # Time points (months)
  months <- seq(0, 24, by = 0.5)
  
  # Standard continuous therapy: median TTP = 5.5 months
  continuous_surv <- exp(-months / 5.5)
  
  # Adaptive oscillatory therapy: median TTP = 10.2 months (Gatenby 2017)
  adaptive_surv <- exp(-months / 10.2)
  
  data_C <- data.frame(
    Months = rep(months, 2),
    Survival_Fraction = c(continuous_surv, adaptive_surv),
    Treatment = rep(c("Continuous docetaxel", "Adaptive oscillatory docetaxel"), each = length(months))
  )
  
  # Plot
  p_C <- ggplot(data_C, aes(x = Months, y = Survival_Fraction, color = Treatment, linetype = Treatment)) +
    geom_line(size = 1.2) +
    scale_color_manual(values = c("Continuous docetaxel" = "red", 
                                   "Adaptive oscillatory docetaxel" = "blue")) +
    scale_linetype_manual(values = c("Continuous docetaxel" = "dashed", 
                                      "Adaptive oscillatory docetaxel" = "solid")) +
    labs(
      title = "C. Clinical Scale: Progression-Free Survival",
      x = "Time (months)",
      y = "Progression-Free Fraction",
      color = NULL,
      linetype = NULL
    ) +
    theme_classic(base_size = 12) +
    theme(
      legend.position = "bottom",
      legend.text = element_text(size = 10),
      plot.title = element_text(face = "bold")
    ) +
    ylim(0, 1) +
    scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
    geom_hline(yintercept = 0.5, linetype = "dotted", color = "gray50", alpha = 0.5) +
    annotate("text", x = 20, y = 0.55, label = "Median TTP", size = 3, color = "gray50") +
    geom_segment(aes(x = 5.5, xend = 5.5, y = 0, yend = 0.5), linetype = "dotted", color = "red", size = 0.5) +
    geom_segment(aes(x = 10.2, xend = 10.2, y = 0, yend = 0.5), linetype = "dotted", color = "blue", size = 0.5) +
    annotate("text", x = 5.5, y = -0.05, label = "5.5 mo", size = 3, color = "red") +
    annotate("text", x = 10.2, y = -0.05, label = "10.2 mo", size = 3, color = "blue")
  
  return(p_C)
}

# =============================================================================
# Main Execution
# =============================================================================

cat("Génération de la Figure S2 : Oscillatory Advantage...\n")

# Generate panels
panel_A <- generate_panel_A()
panel_B <- generate_panel_B()
panel_C <- generate_panel_C()

# Combine panels using patchwork
figure_S2 <- panel_A / panel_B / panel_C +
  plot_layout(guides = "collect") +
  plot_annotation(
    title = "Figure S2. Oscillatory Advantage Across Biological Scales",
    caption = "Source: Molecular Arrest Framework (Lepesteur 2025)\nData: Simulated based on literature values (see v6.txt references)",
    theme = theme(
      plot.title = element_text(size = 16, face = "bold", hjust = 0.5),
      plot.caption = element_text(size = 8, hjust = 0)
    )
  )

# Save figure
output_path <- "figures/Figure_S2_Oscillatory_Advantage.png"
ggsave(
  filename = output_path,
  plot = figure_S2,
  width = 10,
  height = 14,
  dpi = 300,
  units = "in",
  bg = "white"
)

cat(paste0("✓ Figure sauvegardée : ", output_path, "\n"))
cat("  Dimensions : 10 × 14 pouces\n")
cat("  Résolution : 300 dpi\n")
cat("  Format : PNG\n")

# Also save as TIFF for journal submission (if requested)
output_tiff <- "figures/Figure_S2_Oscillatory_Advantage.tiff"
ggsave(
  filename = output_tiff,
  plot = figure_S2,
  width = 10,
  height = 14,
  dpi = 300,
  units = "in",
  bg = "white",
  compression = "lzw"
)

cat(paste0("✓ Version TIFF sauvegardée : ", output_tiff, "\n"))
cat("\nGénération terminée avec succès !\n")

# Optional: Export data as JSON for external use
export_data <- list(
  panel_A = list(
    description = "mTOR activity over 48h",
    conditions = c("Control", "Continuous rapamycin", "Oscillatory rapamycin"),
    time_range_h = c(0, 48),
    activity_range_pct = c(0, 120)
  ),
  panel_B = list(
    description = "Cellular lifespan (CPD)",
    conditions = c("Control", "Continuous rapamycin", "Oscillatory rapamycin"),
    time_range_days = c(0, 60),
    cpd_values = c(control = 50, continuous = 46, oscillatory = 62),
    improvement_pct = 24
  ),
  panel_C = list(
    description = "Clinical progression-free survival",
    treatments = c("Continuous docetaxel", "Adaptive oscillatory docetaxel"),
    median_ttp_months = c(continuous = 5.5, adaptive = 10.2),
    reference = "Gatenby et al. 2017, PMID:29138419"
  ),
  metadata = list(
    version = "1.0",
    date = format(Sys.Date(), "%Y-%m-%d"),
    author = "Tommy Lepesteur",
    license = "MIT"
  )
)

json_output <- "figures/Figure_S2_data.json"
write_json(export_data, json_output, pretty = TRUE)
cat(paste0("✓ Métadonnées exportées : ", json_output, "\n"))

