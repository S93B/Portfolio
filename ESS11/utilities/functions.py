import numpy as np
import pandas as pd
from scipy.stats import pearsonr
def check_matching_indices(*dataframes):
    """
    :param dataframes: Variable number of pandas DataFrame objects to be checked.
    :return: Boolean value indicating whether all provided DataFrames have matching indices.
    """
    return all(df.index.equals(dataframes[0].index) for df in dataframes)


def replace_missing_with_sentinels(df, sentinel_list, columns):
    """
    Replaces row values in specified columns with NaN if the values are in sentinel_list.

    Parameters:
        df (pd.DataFrame): DataFrame in which replacement is to be done.
        sentinel_list (list): List of values where replacement should occur.
        columns (list): List of columns in which to perform the replacement.

    Returns:
        pd.DataFrame: DataFrame with replacements done.
    """
    for col in columns:
        df[col] = df[col].apply(lambda x: np.nan if x in sentinel_list else x)
    return df

# Function to calculate Pearson correlation and significance values for all columns
def calculate_pearson_correlation(df):
    corr_dict = {}
    p_value_dict = {}
    columns = df.columns
    for col1 in columns:
        for col2 in columns:
            if col1 != col2: #niet met zichzelf correleren
                corr, p_value = pearsonr(df[col1], df[col2])
                round(corr,2)
                corr_dict[(col1, col2)] = corr
                p_value_dict[(col1, col2)] = p_value

    # Create DataFrame from the dictionaries
    corr_df = pd.DataFrame.from_dict(corr_dict, orient='index', columns=['Correlation'])
    p_value_df = pd.DataFrame.from_dict(p_value_dict, orient='index', columns=['P-value'])

    # Concatenate the two DataFrames
    result_df = pd.concat([corr_df, p_value_df], axis=1)
    return result_df

# TODO write documentation
def recode_educational_level(df, var, bins, levels):
    df['educational_level'] = pd.cut(df[var], bins=bins, labels=levels)
    return df