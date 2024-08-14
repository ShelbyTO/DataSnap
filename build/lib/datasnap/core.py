import pandas as pd
import re

def data_overview(df):
    overview = {
        'Shape': df.shape,
        'Missing Values': df.isna().sum().sum(),
        'Columns': list(df.columns),
        'Data Types': {col: str(df[col].dtype) for col in df.columns},
        'Unique Values': df.nunique().to_dict(),
        'Missing Values per Column': {col: (df[col].isna().sum(), round(df[col].isna().mean() * 100, 2)) for col in df.columns}
    }
    return overview

def check_column_names(df):
    rename_mapping = {}
    recommendations = []

    for col in df.columns:
        suggestion = None
        reason = None
        if re.search(r'[^a-zA-Z0-9_]', col):
            suggestion = re.sub(r'[^a-zA-Z0-9_]', '_', col).lower()
            reason = 'Use underscores and avoid special characters.'
        elif re.search(r'[A-Z]', col):
            suggestion = re.sub(r'([a-z])([A-Z])', r'\1_\2', col).lower()
            reason = 'Use lowercase letters only.'

        if suggestion:
            rename_mapping[col] = suggestion

    if rename_mapping:
        recommendation_lines = []
        for col, suggestion in rename_mapping.items():
            reason = 'Use underscores and avoid special characters.' if re.search(r'[^a-zA-Z0-9_]', col) else 'Use lowercase letters only.'
            recommendation_lines.append(f"- {col}: {reason} Consider renaming to `{suggestion}`.")
        recommendations.append("Consider renaming columns to follow good coding practices: " + " ".join(recommendation_lines))

        rename_code = " ".join([f"df.rename(columns={{'{k}': '{v}'}}, inplace=True)" for k, v in rename_mapping.items()])
        recommendations.append(f"To apply these changes, use the following code: {rename_code}")

    return recommendations

def generate_report(df):
    overview = data_overview(df)
    column_recommendations = check_column_names(df)
    return overview, column_recommendations
