import pandas as pd
from datasnap.core import generate_report

def test_generate_report():
    df = pd.DataFrame({
        'Order ID': [1, 2],
        'Order Date': ['2024-01-01', '2024-01-02'],
        'CustomerName': ['John Doe', 'Jane Doe'],
        'State': ['NY', 'CA'],
        'City': ['New York', 'Los Angeles'],
        'Day': [1, 2],
        'Month': [1, 1],
        'Year': [2024, 2024]
    })
    overview, recommendations = generate_report(df)
    assert overview['Shape'] == (2, 8)
    assert 'Consider renaming columns to follow good coding practices' in recommendations[0]
