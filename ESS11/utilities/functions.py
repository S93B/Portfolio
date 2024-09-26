import numpy as np

def check_matching_indices(*dataframes):
    """
    :param dataframes: Variable number of pandas DataFrame objects to be checked.
    :return: Boolean value indicating whether all provided DataFrames have matching indices.
    """
    return all(df.index.equals(dataframes[0].index) for df in dataframes)


def replace_missing_with_sentinels(df, sentinel_list, columns):
    """
    Replaces rows in specified columns with NaN if the row index is in sentinel_list.

    Parameters:
        df (pd.DataFrame): DataFrame in which replacement is to be done.
        sentinel_list (list): List of row indices where replacement should occur.
        columns (list): List of columns in which to perform the replacement.

    Returns:
        pd.DataFrame: DataFrame with replacements done.
    """
    for col in columns:
        df.loc[sentinel_list, col] = np.nan
    return df
