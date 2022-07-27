def newusers():
    #cadastro= pd.read_excel(r'C:\Users\xlsx')
    caminho = str(pathlib.Path(__file__).parent.resolve())
    cadastro_newusers= pd.read_excel(caminho + '\\dados.xlsx')

    #venda = pd.read_excel(r'C:\Users\xlsx', sheet_name=1)
    venda_newusers = pd.read_excel(caminho + '\\dados.xlsx', sheet_name=1)
    unir_newusers = pd.merge(cadastro_newusers, venda_newusers, on= 'Identificador', how='outer')

    #data_cadastro = unir[df_murge['Data_de_cadastro'].between('2022-01-01', '2022-01-01')]
    data_cadastro = unir_newusers[unir_newusers['Data_de_cadastro'].between(data_inicial.get(), data_final.get())]
    newusers = data_cadastro[data_cadastro['Quantidade de vendas'].notnull()]
    newusers_group = newusers.groupby('Identificador')[['Quantidade de vendas','Valor total transacionado',]].sum()
    return str(len(newusers_group))