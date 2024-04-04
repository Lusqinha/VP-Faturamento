import pandas as pd

def export_xlsx(dfs:list[tuple[pd.DataFrame, str]], file_name:str):
    """
    Export a list of DataFrames to a single Excel file.
    
    Args:
    dfs: list of tuples with DataFrames and sheet names.
    file_name: name of the Excel file.
    
    Returns:
    file_name if the export was successful, False otherwise.
    """
    try:
        with pd.ExcelWriter(file_name, mode='w') as writer:
            for df, sheet_name in dfs:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print("export_xlsx: ", file_name)
        with open(f'./{file_name}', 'rb') as file:
            return file.read()
    except Exception as e:
        print("export_xlsx: ", e)
        return False
