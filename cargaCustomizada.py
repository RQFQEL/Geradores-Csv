//para rodar os geradores sera necessario instalar o PIP via cmd

import utils
 
# Definindo o nome do arquivo CSV----------------------------------------------------------------------------------------------------------------
nome_arquivo = 'CargaCustom.csv'
 
# Especificando o cabeçalho do arquivo CSV-------------------------------------------------------------------------------------------------------
cabecalho = ['documento', 'contrato', 'valor-divida', 'data-vencimento','tipo-divida','celular','email','logradouro','numero','complemento','bairro','uf','cidade','cep']
 
# --------------------------------------------------------------------------CSV------------------------------------------------------------------------------------------
dados = []
for i in range(1, 100):  # Gerando x registros
    documento = utils.gerar_cpf()
    contrato = utils.gerar_numero_aleatorio_12()
    valordivida = utils.gerar_valor_RS_com_centavos_virgula()
    datavencimento = utils.gerar_data_vencimento()
    tipodivida = utils.gerar_tipos_divida()
    celular = utils.gerar_telefone_11_8()
    email = utils.gerar_email()
    logradouro = utils.gerar_logradouro()
    numero = utils.gerar_numero_aleatorio_2()
    complemento = utils.gerar_complemento()
    bairro = utils.gerar_bairro()
    uf = utils.gerar_uf()
    cidade = utils.gerar_cidade(uf)
    cep = utils.gerar_cep()
 
    dados.append([documento, contrato, valordivida, datavencimento, tipodivida, celular, email, logradouro, numero, complemento, bairro, uf, cidade, cep])
 
# Escrevendo os dados no arquivo CSV-------------------------------------------------------------------------------------------------------------------------------------
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = utils.csv.writer(arquivo_csv, delimiter=';')
    escritor_csv.writerow(cabecalho)  # Escrevendo o cabeçalho
    escritor_csv.writerows(dados)      # Escrevendo os dados
 
print(f'Dados gerados e salvos em {nome_arquivo} com sucesso!')