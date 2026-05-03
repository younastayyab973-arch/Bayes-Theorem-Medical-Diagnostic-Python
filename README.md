# Conditional Probability — Bayes' Theorem Medical Diagnostic System

A Python implementation of Bayes' Theorem applied to a real-world 
medical testing scenario, demonstrating how conditional probability 
updates with new evidence.

## Problem Statement
A rare disease affects 2% of the population. Given a diagnostic test 
with 95% accuracy, what is the real probability a patient has the 
disease after testing positive?

## What This Program Calculates
- P(Disease | Positive Test) using Bayes' Theorem
- False alarm probability analysis
- Updated posterior probability after a second independent test
- Visual probability progression summary

## Results
| Stage                    | Probability |
|--------------------------|-------------|
| Before any test (Prior)  | 2.00%       |
| After 1st positive test  | 32.65%      |
| After 2nd positive test  | 89.72%      |

## Concepts Applied
- Bayes' Theorem
- Conditional Probability
- Prior & Posterior Probability
- Python Functions

## How to Run
1. Make sure Python is installed
2. Run: python stats.py

## Author
Muhammad Tayyab | Data Science Student | COMSATS University Islamabad
