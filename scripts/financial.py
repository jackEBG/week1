import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
#pypfopt.efficient frontier inport EfficientFrontier
#pypfopt
#inport risk nodels
#Pypfopt
#import expected returns

class FinancialAnalyzer:
 
#load from csv file

 file_path = (r'C:\Users\Admin.DESKTOP-M4R2VLU\Documents\week1L\data\raw_analyst_ratings.csv')
 df = pd.read_csv(file_path)
 
# Calculate text lengths for the 'headline' column
 df['headline_length'] = df['headline'].apply(len)

# Obtain basic statistics
 length_stats = df['headline_length'].describe()

# Convert stats to plain numbers
 min_length = length_stats['min']
 max_length = length_stats['max']
 mean_length = length_stats['mean']
 std_length = length_stats['std']
 count_length = length_stats['count']

# Print statistics as plain numbers
 print(f"Count: {int(count_length)}")
 print(f"Mean: {mean_length:.2f}")
 print(f"Standard Deviation: {std_length:.2f}")
 print(f"Min Length: {int(min_length)}")
 print(f"Max Length: {int(max_length)}")

  