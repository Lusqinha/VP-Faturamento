from screens import valid_certificadora
import streamlit as st


st.set_page_config(page_title="Relatório de Faturamento", page_icon="📊", layout="wide", initial_sidebar_state="collapsed")

def main():
    with st.sidebar:
        
        st.title("Gerar Relatório")
        
        selected_enterprise = st.selectbox("Selecione a empresa", ["Valid Certificadora"], index=0)

    match selected_enterprise:
        case "Valid Certificadora":
            valid_certificadora.main()
        case _:
            st.write("Selecione uma empresa")
                

if __name__ == "__main__":
    main()