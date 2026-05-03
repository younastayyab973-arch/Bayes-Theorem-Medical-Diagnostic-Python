# Conditional Probability - Medical Disease Testing
# Bayes' Theorem Implementation
# By: Muhammad Tayyab | Data Science Student

# ──────────────────────────────────────────
# FUNCTION: Total Probability of Testing Positive
# ──────────────────────────────────────────
def total_probability(p_disease, p_pos_given_disease, p_pos_given_healthy):
    p_healthy = 1 - p_disease
    return (p_pos_given_disease * p_disease) + (p_pos_given_healthy * p_healthy)

# ──────────────────────────────────────────
# FUNCTION: Bayes' Theorem
# ──────────────────────────────────────────
def bayes_theorem(p_disease, p_pos_given_disease, p_total_positive):
    return (p_pos_given_disease * p_disease) / p_total_positive

# ──────────────────────────────────────────
# GIVEN DATA
# ──────────────────────────────────────────
p_disease        = 0.02   # 2% population has disease
p_healthy        = 0.98   # 98% are healthy
p_pos_disease    = 0.95   # Test correctly detects disease 95%
p_pos_healthy    = 0.04   # False alarm rate 4%

print("=" * 55)
print("   MEDICAL DIAGNOSTIC SYSTEM — BAYES' THEOREM")
print("=" * 55)

# ──────────────────────────────────────────
# Q1: Probability of disease given positive test
# ──────────────────────────────────────────
p_positive = total_probability(p_disease, p_pos_disease, p_pos_healthy)
p_disease_given_pos = bayes_theorem(p_disease, p_pos_disease, p_positive)
p_false_alarm = 1 - p_disease_given_pos

print("\n FIRST TEST RESULTS")
print(f"  Total P(Positive)         : {p_positive:.4f}")
print(f"  P(Disease | Positive)     : {p_disease_given_pos:.4f} = {p_disease_given_pos*100:.2f}%")

# ──────────────────────────────────────────
# Q2: False alarm probability
# ──────────────────────────────────────────
print(f"\n  FALSE ALARM ANALYSIS")
print(f"  P(Healthy | Positive)     : {p_false_alarm:.4f} = {p_false_alarm*100:.2f}%")
print(f"  → {p_false_alarm*100:.2f}% of positive results are FALSE ALARMS!")

# ──────────────────────────────────────────
# Q3: Updated probability after second test
# ──────────────────────────────────────────
p_pos2_disease  = 0.90   # Second test: 90% accuracy
p_pos2_healthy  = 0.05   # Second test: 5% false positive

# Q1 answer becomes new prior
new_prior = p_disease_given_pos

p_positive2 = total_probability(new_prior, p_pos2_disease, p_pos2_healthy)
p_final = bayes_theorem(new_prior, p_pos2_disease, p_positive2)

print(f"\n SECOND TEST RESULTS (Updated Prior = {new_prior*100:.2f}%)")
print(f"  Total P(Positive2)        : {p_positive2:.4f}")
print(f"  P(Disease | Both Positive): {p_final:.4f} = {p_final*100:.2f}%")

# ──────────────────────────────────────────
# SUMMARY TABLE
# ──────────────────────────────────────────
print("\n" + "=" * 55)
print("   PROBABILITY PROGRESSION SUMMARY")
print("=" * 55)

stages = [
    ("Before any test (Prior)",     p_disease),
    ("After 1st positive test",     p_disease_given_pos),
    ("After 2nd positive test",     p_final)
]

for stage, prob in stages:
    bar = "█" * int(prob * 50)
    print(f"  {stage:<30} {prob*100:6.2f}%  {bar}")

print("=" * 55)
print("\n✅ Conclusion:")
print(f"  A single positive test only gives {p_disease_given_pos*100:.1f}% confidence.")
print(f"  Two positive tests raise confidence to {p_final*100:.1f}%.")
print("  This is WHY doctors always recommend a second test!")