def ressurrectedusers():
    caminho = str(pathlib.Path(__file__).parent.resolve())
    cadastro_ressurrected = pd.read_excel(caminho + '\\dados.xlsx')
    venda_ressurected = pd.read_excel(caminho + '\\dados.xlsx', sheet_name=1)
    unir_ressurected = pd.merge(cadastro_ressurrected, venda_ressurected, on= 'Identificador', how='outer')
    data_group_nosell = unir_ressurected[unir_ressurected['Data da Venda'].between('2022-01-01', '2022-01-01')]
    group_nosell = data_group_nosell.groupby('Email')[['Quantidade de vendas','Valor total transacionado',]].sum()
    data1_group_sell = unir_ressurected[unir_ressurected['Data da Venda'].between('2022-01-01', '2022-01-01')]
    group_sell1 = data1_group_sell.groupby('Email')[['Quantidade de vendas','Valor total transacionado',]].sum()
    data2_group_sell = unir_ressurected[unir_ressurected['Data da Venda'].between('2022-01-01', '2022-01-01')]
    group_sell2 = data2_group_sell.groupby('Email')[['Quantidade de vendas','Valor total transacionado',]].sum()
    ressurected_users1 = group_sell1.merge(data_group_nosell, 'outer' , on= 'Email', indicator=True).query('_merge == "left_only"')
    ressurected_users2 = group_sell2.merge(data_group_nosell, 'outer' , on= 'Email', indicator=True).query('_merge == "left_only"')
    ressurected_usersgroup = pd.merge(ressurected_users1, ressurected_users2, on= 'Email', how='left')
    ressurected_users = ressurected_usersgroup.groupby('Email').sum()
    return(str(ressurected_users))