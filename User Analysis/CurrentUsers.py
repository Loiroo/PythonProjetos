def currentusers():
    caminho = str(pathlib.Path(__file__).parent.resolve())
    data_inicial_obj = datetime.strptime(data_inicial.get(), '%Y-%m-%d') - timedelta(days=7)
    data_final_obj = datetime.strptime(data_final.get(), '%Y-%m-%d') - timedelta(days=7)
    data_inicial = data_inicial_obj.strftime("%Y-%m-%d")
    data_final = data_final_obj.strftime("%Y-%m-%d")
    cadastro_current= pd.read_excel(caminho + '\\dados.xlsx')
    venda_current = pd.read_excel(caminho + '\\dados.xlsx', sheet_name=1)
    unir_current = pd.merge(cadastro_current, venda_current, on= 'Identificador', how='outer')
    currentusers1 = unir_current[unir_current['Data da Venda'].between(data_inicial, data_final)]
    currentusers2 = unir_current[unir_current['Data da Venda'].between(data_inicial.get(), data_final.get())]
    ids1 = list(currentusers1['Identificador'])
    ids2 = list(currentusers2['Identificador'])
    currentusers_full = set(ids1).intersection(ids2)
    return (str(len(currentusers_full)))