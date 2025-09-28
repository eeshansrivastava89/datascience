# ☕ Blind Coffee Taste Test Analysis

A comprehensive statistical analysis of a blind coffee taste test experiment featuring 8 participants rating 5 popular coffee brands at different temperatures.

## 📋 Project Overview

This project presents a complete statistical analysis of a blind coffee taste test conducted with **8 participants** who rated **5 coffee brands** (Starbucks, McDonald's, Krispy Kreme, 7-Eleven, and Macrina) served at both **hot and cold temperatures**.

### 🎯 Research Questions

The analysis addresses several key questions:
- Which coffee brands perform best in blind taste tests?
- How does temperature affect taste preferences?
- Can people accurately identify coffee brands without knowing what they're drinking?
- What are the individual differences in tasting abilities and preferences?
- How do price and quality relate in the coffee market?

## 📊 Analysis Structure

The project is organized into four comprehensive segments:

### 1️⃣ **Taste Preferences & Statistical Winners**
- Summary statistics with 95% confidence intervals
- Temperature effect analysis and interaction plots
- Identification of consensus favorites vs controversial choices

### 2️⃣ **Brand Recognition & Confusion Patterns**
- Brand identification accuracy rates
- Confusion matrices showing misidentification patterns
- Analysis of which brands are most/least recognizable

### 3️⃣ **Price-Value Analysis & Market Positioning**
- Value frontier analysis (price vs quality relationship)
- Sweet spot identification for best value coffees
- Market positioning insights

### 4️⃣ **Individual Differences & Rater Psychology**
- **Accuracy Leaderboard**: Who's the best brand detective?
- **Drama Analysis**: Who has the most extreme reactions?
- **Generosity Index**: Who gives the highest ratings?
- **Wildcard Detection**: Most unpredictable tasters
- **Overall MVP**: The ultimate coffee tasting champion
- **Hall of Fame**: Fun superlatives and personality insights

## 📁 Project Structure

```
tastingExperiment/
├── BlindCoffee_FullAnalysis_Seg1to4.ipynb  # Main analysis notebook
├── TasteLearn_CopyES.xlsx                   # Raw experiment data
└── README.md                                # This file
```

## 🔬 Methodology

### Experimental Design
- **Participants**: 8 coffee tasters
- **Brands**: 5 popular coffee chains (Starbucks, McDonald's, Krispy Kreme, 7-Eleven, Macrina)
- **Conditions**: Hot (brewed) and Cold (iced latte) temperatures
- **Measurement**: Taste ratings and brand identification guesses
- **Design**: Blind taste test (participants didn't know which brand they were tasting)

### Statistical Methods Used
- **Descriptive Statistics**: Means, standard deviations, confidence intervals
- **ANOVA**: Analysis of variance for comparing groups
- **t-tests**: Pairwise comparisons between conditions
- **Chi-square tests**: Brand recognition accuracy analysis
- **Correlation Analysis**: Price-quality relationships
- **Visualization**: Interactive plots, heatmaps, error bars

### Key Statistical Features
- 95% confidence intervals for all estimates
- Multiple comparison corrections where appropriate
- Effect size calculations
- Power analysis considerations
- Robust statistical visualizations with uncertainty quantification

## 🔧 Technical Requirements

### Dependencies
```python
- Python 3.x
- pandas
- numpy
- scipy
- statsmodels
- seaborn
- matplotlib
```

### Running the Analysis
1. Ensure all dependencies are installed
2. Place the Excel data file (`TasteLearn_CopyES.xlsx`) in the same directory
3. Open and run the Jupyter notebook (`BlindCoffee_FullAnalysis_Seg1to4.ipynb`)

## 📈 Key Findings Summary

*Note: Run the notebook to see detailed statistical results, but here are some general insights the analysis reveals:*

- **Temperature Effects**: Significant differences in how brands perform at hot vs cold temperatures
- **Brand Recognition**: Varying levels of brand identifiability, with some brands being more distinctive than others
- **Individual Differences**: Substantial variation in tasting abilities, rating generosity, and preference patterns
- **Price-Quality Relationships**: Analysis of whether expensive coffee actually tastes better
- **Consensus vs Controversy**: Some brands generate agreement while others divide opinions

## 🎨 Visualizations

The notebook includes numerous high-quality visualizations:
- Bar charts with confidence interval error bars
- Interaction plots showing temperature effects
- Heatmaps for confusion matrices
- Scatter plots for price-value analysis
- Individual difference profiles
- Statistical test result summaries

## 📚 Educational Value

This project serves as an excellent example of:
- **Experimental design** in sensory testing
- **Statistical analysis** with real-world data
- **Data visualization** best practices
- **Scientific communication** through clear reporting
- **Individual differences** analysis in psychology/sensory science

## 🏆 Awards & Superlatives

The analysis includes a fun "Hall of Fame" section identifying:
- The most accurate brand identifier
- The most generous/critical taster
- The most controversial opinion holder
- The most consistent/inconsistent rater
- And many more entertaining insights!

## 📄 License

This project is for educational and research purposes. The data represents actual taste test results conducted with willing participants.

## 🤝 Contributing

This analysis can be extended in several ways:
- Additional statistical tests
- More sophisticated modeling approaches
- Extended visualizations
- Comparison with other sensory testing datasets
- Replication studies with different brands or participants

## 📞 Contact

Generated on September 28, 2025 as part of a comprehensive data science analysis project.

---

*"May your cups always be full and your ratings accurate!" ☕*