import requests
import streamlit as st
import re

# Formats the Brazilian Corporate Tax ID (CNPJ)
def format_corporate_tax_id(corporate_tax_id):
    """Formats CNPJ into XX.XXX.XXX/XXXX-XX."""
    return f"{corporate_tax_id[:2]}.{corporate_tax_id[2:5]}.{corporate_tax_id[5:8]}/{corporate_tax_id[8:12]}-{corporate_tax_id[12:14]}"

# Formats the Brazilian Zip Code (CEP)
def format_zip_code(zip_code):
    """Formats CEP into XXXXX-XXX."""
    return f"{zip_code[:5]}-{zip_code[5:]}"

# Formats the Brazilian Individual Tax ID (CPF)
def format_individual_tax_id(individual_tax_id):
    """Formats CPF into XXX.XXX.XXX-XX."""
    # Ensure it only contains digits for correct formatting
    individual_tax_id = re.sub(r'\D', '', individual_tax_id)
    return f"{individual_tax_id[:3]}.{individual_tax_id[3:6]}.{individual_tax_id[6:9]}-{individual_tax_id[9:]}"

st.set_page_config(page_title="CNPJ Lookup", layout="centered", page_icon="🏢")
st.title("Brazil API CNPJ Lookup 🏢")

st.markdown("Enter a CNPJ to search for corresponding company information.")

corporate_tax_id_input = st.text_input("CNPJ:", help="Accepts CNPJ with dots, slash, and dash or only numbers.")

if st.button("Search"):
    if corporate_tax_id_input:
        # Clean the input, keeping only digits
        corporate_tax_id_clean = re.sub(r'\D', '', corporate_tax_id_input)
        
        if len(corporate_tax_id_clean) != 14:
            st.error("Invalid CNPJ. Ensure the CNPJ has 14 digits.")
        else:
            api_url = f'https://brasilapi.com.br/api/cnpj/v1/{corporate_tax_id_clean}'
            try:
                api_response = requests.get(api_url)
                
                if api_response.status_code == 200:
                    data = api_response.json()
                    st.success("Data successfully found!")

                    st.subheader("Company Information:")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("📝 **Legal Name (Razão Social):**")
                        # API fields remain in Portuguese
                        st.write(data.get("razao_social"))
                        st.write("🏷️ **Trade Name (Nome Fantasia):**")
                        st.write(data.get("nome_fantasia"))
                        st.write("🏢 **CNPJ:**")
                        st.write(format_corporate_tax_id(data.get("cnpj")))

                        st.write("💰 **Social Capital:**")
                        # Format Brazilian currency
                        st.write(f"R$ {data.get('capital_social', 0):,.2f}")
                        st.write("📅 **Opening Date:**")
                        st.write(data.get("data_inicio_atividade"))
                        st.write("📞 **Phones:**")
                        st.write(f"{data.get('ddd_telefone_1')}, {data.get('ddd_telefone_2')}")

                    with col2:
                        st.write("📍 **Address:**")
                        st.write(f"{data.get('descricao_tipo_de_logradouro')} {data.get('logradouro')}, {data.get('numero')}, {data.get('complemento')}")
                        st.write(f"{data.get('bairro')}, {data.get('municipio')} - {data.get('uf')}")
                        # Use the translated format function
                        st.write(f"**ZIP Code (CEP):** {format_zip_code(data.get('cep'))}")
                        st.write("✉️ **Email:**")
                        st.write(data.get("email"))
                        st.write("💼 **Registration Status:**")
                        st.write(data.get("descricao_situacao_cadastral"))
                        st.write("📅 **Registration Status Date:**")
                        st.write(data.get("data_situacao_cadastral"))
                        st.write("📜 **Tax Regime:**")

                        tax_regimes = data.get("regime_tributario", [])
                        tax_regime = tax_regimes[-1] if tax_regimes else None
                        # API field 'forma_de_tributacao' is left as is
                        st.write(tax_regime.get('forma_de_tributacao') if tax_regime else "N/A")

                    st.subheader("Partners:")
                    partners = data.get("qsa", [])
                    if partners:
                        for partner in partners:
                            # API fields 'nome_socio' and 'qualificacao_socio' are left as is
                            st.write(f"- Name: {partner.get('nome_socio')} ({partner.get('qualificacao_socio')})")
                            
                            tax_id = partner.get('cnpj_cpf_do_socio')
                            if tax_id and len(tax_id) == 14:
                                st.write(f"  - CNPJ: {format_corporate_tax_id(tax_id)}")
                            elif tax_id and len(tax_id) == 11:
                                # Use the translated format function
                                st.write(f"  - CPF: {format_individual_tax_id(tax_id)}")
                            
                            # API field 'faixa_etaria' is left as is
                            st.write(f"- Age Group: {partner.get('faixa_etaria')}")
                            # API field 'data_entrada_sociedade' is left as is
                            st.write(f"- Date of Entry: {partner.get('data_entrada_sociedade')}")
                            st.write("---")
                    else:
                        st.write("No partners found.")
                    
                    st.subheader("Activities")
                    st.write("**Main Activity:**")
                    # API field 'cnae_fiscal_descricao' is left as is
                    st.write(f"- {data.get('cnae_fiscal_descricao')}")

                    if data.get("cnaes_secundarios"):
                        st.write("**Secondary Activities:**")
                        for activity in data.get("cnaes_secundarios"):
                            # API field 'descricao' is left as is
                            st.write(f"- {activity.get('descricao')}")
                else:
                    st.error("CNPJ not found in the database.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the API: {e}")
    else:
        st.error("Please enter a CNPJ.")