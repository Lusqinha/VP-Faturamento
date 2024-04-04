import pandas as pd

class ValidCertificadora:
    """
    Class to filter data based on 'Valid Certificadora' report.
    
    Initialize args:
    xlsx_df: DataFrame from the Excel file.
    csv_df: DataFrame from the CSV file.
    """
    def __init__(self, xlsx_df:pd.DataFrame, csv_df:pd.DataFrame):
        self.xlsx = xlsx_df
        self.csv = csv_df
       
    def data_normalize(self):
        """
        Normalize the data to remove the '.0' suffix from the TICKET column.
        
        Returns:
        None
        """
        self.csv['TICKET'] = self.csv['TICKET'].astype(str).str.removesuffix('.0')
        self.xlsx['Solicitação'] = self.xlsx['Solicitação'].astype(str)
        self.xlsx['Titular'] = self.xlsx['Titular'].astype(str)
    
    def scan_data(self, scope:str):
        """
        Scan the data and return a DataFrame with the filtered data.
        
        Args:
        scope: 'large' or 'small'.
        """
        output_df = pd.DataFrame()
        scope_fnc = self.large_scope if scope == 'large' else self.small_scope
        
        self.data_normalize()
        
        for ticket, cliente in zip(self.xlsx['Solicitação'], self.xlsx['Titular']):
            
            check_ticket = self.csv[self.csv['TICKET'] == ticket]
            check_cliente = self.csv[self.csv['CLIENTE'] == cliente]
            
            item = scope_fnc(check_ticket, check_cliente, cliente)
            print("item: ", item)
            output_df = pd.concat([output_df, item])
        
        return output_df
                
    def large_scope(self, check_ticket, check_cliente, cliente):
        """
        Check if the ticket or the client is in the CSV file.
        
        Args:
        check_ticket: DataFrame with the ticket data.
        check_cliente: DataFrame with the client data.
        cliente: client name.
        
        Returns:
        DataFrame with the filtered data.
        """
        if len(check_ticket) == 0 or len(check_cliente) == 0:
            item = self.xlsx[self.xlsx['Titular'] == cliente]
            return item
        
        return None
                
    def small_scope(self, check_ticket, check_cliente, cliente):
        """
        Check if the ticket and the client are in the CSV file.
        
        Args:
        check_ticket: DataFrame with the ticket data.
        check_cliente: DataFrame with the client data.
        cliente: client name.
        
        Returns:
        DataFrame with the filtered data.
        """
        if len(check_ticket) == 0 and len(check_cliente) == 0:
            item = self.xlsx[self.xlsx['Titular'] == cliente]
            return item

        return None
                