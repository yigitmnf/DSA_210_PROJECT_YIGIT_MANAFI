# DSA210PROJECT

# 📊 Read the Signs: Tomorrow's Mood, Today's Data

**DSA 210 – Introduction to Data Science | Spring 2026**  
**Yigit Manafi**

---

## 🎯 Project Overview

Can we predict how we will feel tomorrow by looking at today's data? This project investigates the relationship between daily behavioral, physiological, and contextual variables and next-day mood using 398 days of personal self-tracked data.

The core idea is that our emotions are not random — they are connected to measurable factors such as sleep quality, heart rate, stress levels, physical activity, and exam schedules.



## 🔬 Hypotheses

| ID | Hypothesis |
|----|------------|
| **H₀** | There is no statistically significant relationship between next-day mood and today's variables |
| **H1a** | Mood shows temporal continuity — today's mood positively correlates with tomorrow's mood |
| **H1b** | As exam day approaches, next-day mood decreases |
| **H1c** | Higher heart rate is associated with lower next-day mood |
| **H1e** | Better sleep quality and duration are associated with higher next-day mood 

## 📊 Data Source

All data comes from personal self-tracking over **398 days** (March 2025 – April 2026):

| Source | Features |
|--------|----------|
| **Smartwatch** | Heart rate, sleep data (duration, deep/light/REM, bedtime) |
| **Samsung Notes** | Daily self-reported mood (after processing 1–5 scale, 0.5 increments) |
| **Google Calendar** | Exam dates and proximity |
**Dataset:** 398 rows × 11 features. Mood data available for 305 days.

## 🔬 Hypotheses

| ID | Hypothesis |
|----|------------|
| **H₀** | No significant relationship between next-day mood and today's variables |
| **H1a** | Mood shows temporal continuity — today's mood positively correlates with tomorrow's |
| **H1b** | As exam day approaches, next-day mood decreases |
| **H1c** | Higher heart rate → lower next-day mood |
| **H1d** | Next-day mood is higher when tomorrow is a weekend |
| **H1e** | Better sleep → higher next-day mood |

## 📈 Key Findings

| Hypothesis | Test | Statistic | p-value | α = 0.05 Decision | α = 0.10 Decision |
|------------|------|-----------|---------|-------------------|-------------------|
| **H1a** | Spearman correlation | ρ = 0.197 | **0.0008** | ✅ Reject H₀ | ✅ Reject H₀ |
| H1b (corr) | Spearman correlation | ρ = 0.058 | 0.490 | ❌ Fail to reject | ❌ Fail to reject |
| H1b (group) | Mann-Whitney U | U = 3443 | 0.074 | ❌ Fail to reject *(borderline)* | ✅ Reject H₀ *(weak evidence)* |
| H1c (avg HR) | Spearman correlation | ρ = -0.014 | 0.818 | ❌ Fail to reject | ❌ Fail to reject |
| H1c (resting) | Spearman correlation | ρ = -0.116 | 0.059 | ❌ Fail to reject *(borderline)* | ✅ Reject H₀ *(weak evidence)* |
| H1d | Mann-Whitney U | U = 9556 | 0.393 | ❌ Fail to reject | ❌ Fail to reject |
| H1e (duration) | Spearman correlation | ρ = 0.014 | 0.825 | ❌ Fail to reject | ❌ Fail to reject |
| H1e (quality) | Spearman correlation | ρ = 0.038 | 0.552 | ❌ Fail to reject | ❌ Fail to reject |


**Key insight:** Today's mood is the strongest predictor of tomorrow's mood (p < 0.001), confirming temporal continuity of emotional states. At α = 0.10, resting heart rate and exam proximity (group comparison) also show weak evidence of association with next-day mood.

## 🔧 How to Reproduce

```bash
pip install -r requirements.txt
jupyter notebook EDA_and_Hypothesis_Testing.ipynb
```



## 🔮 Next Steps

- **Machine Learning Models** — Regression and classification for mood prediction
- **Feature Importance Analysis** — Which variables matter most?|


