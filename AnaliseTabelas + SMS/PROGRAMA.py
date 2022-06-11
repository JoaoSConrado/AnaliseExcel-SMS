# PANDAS    -> PYTHON COM EXCEL
# OPENPYXL  -> PYTHON COM EXCEL
# TWILIO    -> PYTHON COM SMS

from twilio.rest import Client
import pandas as pd

# TWILIO
account_sid = "AC1f5df706014efc1c6126d85f75856450"
auth_token = "a6d3f605bad0a727aa772d39c28b1ecd"
client = Client(account_sid, auth_token)

lista_meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO']

# VERIFICAÇÃO E LEITURA DAS PLANILHAS
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']
                                     > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']
                                   > 55000, 'Vendas'].values[0]
        print(
            f'No Mês {mes} alguém bateu a meta. Vendedor: {vendedor}, vendas {vendas}'
        )
        message = client.messages.create(
            to="+5511930763154",
            from_="+18486006634",
            body=f'NO MÊS: {mes}, O VENDEDOR(A) {vendedor} BATEU A META!!! COM UM TOTAL DE R$ {vendas} REAIS')
        print(message.sid)
