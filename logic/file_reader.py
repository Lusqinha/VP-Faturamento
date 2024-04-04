import pandas as pd

def xlsx_to_pd(xlsx_file):
    """
    Read an Excel file and return a DataFrame.
    
    Args:
    xlsx_file: path to the Excel file.
    
    Returns:
    DataFrame with the data from the Excel file.
    """
    df = pd.read_excel(xlsx_file)
    print("xlsx_to_pd: ", len(df))
    
    return df

def csv_to_pd(csv_file):
    """
    Read a CSV file and return a DataFrame.
    
    Args:
    csv_file: path to the CSV file.
    
    Returns:
    DataFrame with the data from the CSV file.
    """
    df = pd.read_csv(csv_file, encoding_errors='ignore', sep=';')
    print("csv_to_pd: ", len(df))
    return df

def unify_df(dfs:list[pd.DataFrame]):
    """
    Unify a list of DataFrames into a single DataFrame.
    
    Args:
    dfs: list of DataFrames.
    
    Returns:
    DataFrame with the unified data.
    """
    out_df:pd.DataFrame = pd.DataFrame()
    for df in dfs:
        out_df = pd.concat([out_df, df])
        
    print("unify_df: ", len(out_df))
    return out_df

def csvs_to_pd(csv_files:list[str]):
    """
    Read a list of CSV files and return a list of DataFrames.
    
    Args:
    csv_files: list of paths to CSV files.
    
    Returns:
    list of DataFrames with the data from the CSV files.
    """
    dfs = []
    for csv_file in csv_files:
        dfs.append(csv_to_pd(csv_file))
        
    return dfs