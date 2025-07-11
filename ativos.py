//para rodar os geradores sera necessario instalar o PIP via cmd

import utils
from datetime import datetime
import csv
 
# Definindo o nome do arquivo CSV
data_atual = datetime.now().strftime("%d%m20%y")
nome_arquivo_clientes = f"BASE_CLIENTES_{data_atual}.csv"
nome_arquivo_telefones = f"BASE_TELEFONES_{data_atual}.csv"
nome_arquivo_operacoes = f"BASE_OPERACOES_{data_atual}.csv"
nome_arquivo_exclusao = f"EXCLUSAO_CLIENTES{data_atual}.csv"
nome_arquivo_acordos_pagamento = f"ACORDOS_PAGAMENTOS{data_atual}.csv"
 
# Cabeçalhos dos arquivos
cabecalho_clientes = ['NDG', 'Nome', 'Tipo_Pessoa', 'CPF_CNPJ', 'Data_Nascimento', 'Email']
cabecalho_telefones = ['NDG', 'TIPO_TELEFONE', 'DDD', 'NUMERO', 'CPF_CNPJ']
cabecalho_operacoes = ['ID_OPERACAO', 'NDG', 'NOME', 'VALOR_ATUALIZADO', 'VALOR_OFERTA', 'DATA_VENCIMENTO','ORIGEM','CPF_CNPJ']
cabecalho_exclusao = ['NDG', 'CPF_CNPJ']
cabecalho_acordos_pagamento = ['ndg','num_acordo','num_parcela','num_boleto','valor_pago','cpf_cnpj','data_pagamento']
 
# Lista para armazenar os dados compartilhados
dados_compartilhados = []
 
# Gerando dados para o arquivo de clientes
dados_clientes = []
for i in range(1, 101):  # Gerando 9 registros
    NDG = utils.gerar_numero_aleatorio_16()
    Nome = utils.gerar_nome_sobrenome()
    Tipo_Pessoa = utils.gerar_indicador_1_2()
    CPF_CNPJ = utils.gerar_cpf()
    Data_Nascimento = utils.gerar_data_nascimento()
    Email = utils.gerar_email()
 
    # Adiciona o registro à lista de clientes
    dados_clientes.append([NDG, Nome, Tipo_Pessoa, CPF_CNPJ, Data_Nascimento, Email])
   
    # Adiciona os dados compartilhados (NDG e CPF_CNPJ) à lista
    dados_compartilhados.append({'NDG': NDG, 'CPF_CNPJ': CPF_CNPJ})
 
# Gerando dados para o arquivo de telefones usando os dados compartilhados
dados_telefones = []
for registro in dados_compartilhados:
    NDG = registro['NDG']
    CPF_CNPJ = registro['CPF_CNPJ']
    TIPO_TELEFONE = utils.gerar_indicador_1_2()
    DDD = utils.gerar_numero_aleatorio_2()
    NUMERO = utils.gerar_telefone_sem_119()
 
    # Adiciona o registro à lista de telefones
    dados_telefones.append([NDG, TIPO_TELEFONE, DDD, NUMERO, CPF_CNPJ])
   
 
# Gerando dados para o arquivo de operacoes usando os dados compartilhados
dados_operacoes = []
for registro in dados_compartilhados:
    ID_OPERACAO = utils.gerar_id_operacao()
    NDG = registro['NDG']
    NOME = utils.gerar_nome_empresa()
    VALOR_ATUALIZADO = utils.gerar_valor_RS_sem_centavos_ponto()
    VALOR_OFERTA = utils.gerar_valor_RS_com_centavos_ponto()
    DATA_VENCIMENTO = utils.gerar_data_vencimento_ativos()
    ORIGEM = utils.gerar_origem_divida()
    CPF_CNPJ = registro['CPF_CNPJ']
 
    # Adiciona o registro à lista de telefones
    dados_operacoes.append([ID_OPERACAO, NDG, NOME, VALOR_ATUALIZADO, VALOR_OFERTA, DATA_VENCIMENTO, ORIGEM, CPF_CNPJ])
   
 
# Gerando dados para o arquivo de exclusoes usando os dados compartilhados
    dados_exclusao = []
for registro in dados_compartilhados:
    NDG = registro['NDG']
    CPF_CNPJ = registro['CPF_CNPJ']
 
    # Adiciona o registro à lista de clientes
    dados_exclusao.append([NDG, CPF_CNPJ])
 
# Gerando dados para o arquivo de acordos e pagamentos usando os dados compartilhados
dados_acordos_pagamento = []
for registro in dados_compartilhados:
    NDG = registro['NDG']
    NUM_ACORDO = utils.gerar_numero_aleatorio_10()
    CPF_CNPJ = registro['CPF_CNPJ']
    NUM_PARCELA = utils.gerar_indicador_1_2()
    NUM_BOLETO = utils.gerar_numero_aleatorio_15()
    VALOR_PAGO = utils.gerar_valor_RS_com_centavos_ponto()
    DATA_PAGAMENTO = utils.gerar_data_pagamento()
    # Adiciona o registro à lista de telefones
    dados_acordos_pagamento.append([NDG, NUM_ACORDO, NUM_PARCELA, NUM_BOLETO, VALOR_PAGO, CPF_CNPJ, DATA_PAGAMENTO])
 
# Escrevendo os dados no arquivo de clientes
with open(nome_arquivo_clientes, mode='w', newline='', encoding='utf-8') as arquivo_clientes:
    escritor_clientes = csv.writer(arquivo_clientes, delimiter=';')
    escritor_clientes.writerow(cabecalho_clientes)
    escritor_clientes.writerows(dados_clientes)
 
with open(nome_arquivo_telefones, mode='w', newline='', encoding='utf-8') as arquivo_telefones:
    escritor_telefones = csv.writer(arquivo_telefones, delimiter=';')
    escritor_telefones.writerow(cabecalho_telefones)
    escritor_telefones.writerows(dados_telefones)
   
with open(nome_arquivo_operacoes, mode='w', newline='', encoding='utf-8') as arquivo_operacoes:
    escritor_operacoes = csv.writer(arquivo_operacoes, delimiter=';')
    escritor_operacoes.writerow(cabecalho_operacoes)
    escritor_operacoes.writerows(dados_operacoes)
 
with open(nome_arquivo_exclusao, mode='w', newline='', encoding='utf-8') as arquivo_exclusao:
    escritor_exclusao = csv.writer(arquivo_exclusao, delimiter=';')
    escritor_exclusao.writerow(cabecalho_exclusao)
    escritor_exclusao.writerows(dados_exclusao)
 
with open(nome_arquivo_acordos_pagamento, mode='w', newline='', encoding='utf-8') as acordos_pagamento:
    escritor_acordos_pagamento = csv.writer(acordos_pagamento, delimiter=';')
    escritor_acordos_pagamento.writerow(cabecalho_acordos_pagamento)
    escritor_acordos_pagamento.writerows(dados_acordos_pagamento)
 
print(f"Dados gerados e salvos em {nome_arquivo_clientes},{nome_arquivo_telefones} e {nome_arquivo_telefones} com sucesso!")