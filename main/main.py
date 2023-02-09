import pandas as pd
import streamlit as st

def converter_porcentagem(lista):
  lista = [imposto / 100 for imposto in lista]
  return lista

def calcular_imposto(faturamento, imposto):
  imposto = faturamento * imposto
  return imposto

st.title(':blue[Calculadora de Impostos] :calendar:')

st.markdown(
    '#### Insira abaixo as alíquotas dos impostos :point_down: :point_down:')

faturamento = st.number_input('**Digite o faturamento:**')

enquadramento = st.radio(
    '**Marque seu enquadramento tributário:**',
    ('MEI', 'Simples Nacional', 'Lucro Presumido', 'Lucro Real'),
    horizontal=True, index=False
)

col1, col2 = st.columns(2)

with col1:
    iss = st.number_input('**ISS: %**', min_value=0.00)
    cofins = st.number_input('**COFINS: %**', min_value=0.00)


with col2:
    pis = st.number_input('**PIS: %**', min_value=0.00)
    ir = st.number_input('**IR: %**', min_value=0.00)


calcular = st.button('Calcular', type='primary')

if calcular == True:
  impostos = [iss, pis, cofins, ir]
  impostos_convertidos = converter_porcentagem(impostos)

  valor_iss = 'R$ ' + format(round(calcular_imposto(faturamento, impostos_convertidos[0])),',')
  valor_pis = 'R$ ' + format(round(calcular_imposto(faturamento, impostos_convertidos[1])), ',')
  valor_cofins = 'R$ ' + format(round(calcular_imposto(faturamento, impostos_convertidos[2])), ',')
  valor_ir = 'R$ ' + format(round(calcular_imposto(faturamento, impostos_convertidos[3])), ',')

  dados = {'ISS': [valor_iss],
        'PIS': [valor_pis],
        'COFINS': [valor_cofins],
        'IR': [valor_ir]}

  df = pd.DataFrame(dados)

  st.header('Tabela Dados')
  st.dataframe((df), width=800)





