from logic.file_reader import xlsx_to_pd, csvs_to_pd, unify_df
from logic.query_data import ValidCertificadora
from logic.output_file import export_xlsx
import streamlit as st
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

def generate_report(df_xlsx, df_csvs):
    """
    Generate the report based on the data.
    
    Args:
    df_xlsx: DataFrame from the Excel file.
    df_csvs: DataFrame from the CSV file.
    
    Returns:
    A list of tuples with DataFrames and sheet names, and the total of rows.
    """
    valid_certificadora = ValidCertificadora(df_xlsx, df_csvs)
    df_large = valid_certificadora.scan_data('large')
    df_small = valid_certificadora.scan_data('small')
    
    total = len(df_large) + len(df_small)
    
    output_list = [(df_large, 'Escopo Maior'), (df_small, 'Escopo Menor')]
    return output_list, str(total)
    
    

def main():
    col1, col2 = st.columns(2)
    with col1:
        xlsx_file = st.file_uploader("Selecione o arquivo XLSX (Valid)", type=['xlsx'])
    with col2:
        csv_files = st.file_uploader("Selecione o arquivo CSV (Prática)", type=['csv'], accept_multiple_files=True)
    
    if xlsx_file and csv_files:
        try:
            df_xlsx = xlsx_to_pd(xlsx_file)
            print("df_xlsx: ", len(df_xlsx))
            df_csvs = csvs_to_pd(csv_files)
            print("df_csvs: ", len(df_csvs))
            df_csv = unify_df(df_csvs)
            print("df_csv: ", len(df_csv))
        except Exception as e:
            st.error(f"Erro ao carregar os arquivos. Erro: {e}")
            
        
        if st.button("Gerar Relatório"):
            with st.spinner("Gerando Relatório..."):
                report, total = generate_report(df_xlsx, df_csv)
            st.success("Relatório gerado com sucesso!")
            
            file_name = f"report-{today}--{total}.xlsx"
            st.divider()
            st.download_button(label="Baixar Relatório", data=export_xlsx(report, file_name), file_name=file_name)
            