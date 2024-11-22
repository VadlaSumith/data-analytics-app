import pandas as pd

def run_analysis():
    # Load the sample data
    data = pd.read_csv('data/sample.csv')
    
    # Perform analysis (e.g., calculate mean of a column 'value')
    mean_value = data['value'].mean()
    return {'mean': mean_value}
