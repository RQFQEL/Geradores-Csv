//Requisitos para executar seu código:
//Tenha o Python instalado (versão 3.x recomendada).
//Você pode verificar com: python --version

import csv
import random
from datetime import datetime, timedelta
from itertools import cycle
from collections import deque
 
# gerador de indicador 1 e 2----------------------------------------------------------------------------------------------------------------------------
# Insumos indicadores
tipos = ["1"]
 
# Função para gerar indicador aleatorio
def gerar_indicador_1_2():
    tipo = random.choice(tipos)
    return f"{tipo}"
 
# gerador de tipo divida---------------------------------------------------------------------------------------------------------------------------
# Insumos tipo divida
tiposDivida = ['Credito', 'Multa']
 
# Função para gerar cidade aleatório
def gerar_tipos_divida():
    tipoDivida = random.choice(tiposDivida)
    return f"{tipoDivida}"
 
 
# gerador de cidade-------------------------------------------------------------------------------------------------------------------------------
dados_uf_cidade = {
    "SP": ["São Paulo", "Campinas", "Santos", "Sorocaba"],
    "RJ": ["Rio de Janeiro", "Niterói", "Petrópolis", "Volta Redonda"],
    "MG": ["Belo Horizonte", "Uberlândia", "Juiz de Fora", "Contagem"],
    "BA": ["Salvador", "Feira de Santana", "Vitória da Conquista", "Ilhéus"]
}
 
# Função para gerar uma UF
def gerar_uf():
    return random.choice(list(dados_uf_cidade.keys()))
 
# Função para gerar uma cidade correspondente à UF
def gerar_cidade(uf):
    return random.choice(dados_uf_cidade[uf])
 
# gerador de bairro-------------------------------------------------------------------------------------------------------------------------------
# Insumos bairro
bairros = ['Vila gomes', 'Bonfa', 'Ibirapuera', 'Vila lobos']
 
# Função para gerar bairro aleatório
def gerar_bairro():
    bairro = random.choice(bairros)
    return f"{bairro}"
 
# gerador de nome empresa---------------------------------------------------------------------------------------------------------------------------
empresa = ["Petrobras", "Vale", "Ambev", "Natura", "Embraer", "Itau", "Bradesco",
 "Renner", "Riachuelo", "Gerdau", "Suzano", "Votorantim", "Marfrig",
 "Magalu", "Positivo", "Unimed", "Cielo", "Carrefour", "Vivara"]
 
# Função para gerar logradouro aleatório
def gerar_nome_empresa():
    empresas = random.choice(empresa)
    return f"{empresas}"
 
# gerador de complemento-------------------------------------------------------------------------------------------------------------------------------
# Insumos complemento
complementos = ["Casa", "Office", "AP"]
 
# Função para gerar logradouro aleatório
def gerar_complemento():
    complemento = random.choice(complementos)
    return f"{complemento}"
 
# gerador de logradouro----------------------------------------------------------------------------------------------------------------------------
# Insumos logradouro
ruas = ["Rua", "Avenida", "Rod"]
adjetivos = ["Floresta", "Cruz", "Sol", "Catarina", "Santos", "Lima", "Jardim"]
 
# Função para gerar logradouro aleatório
def gerar_logradouro():
    rua = random.choice(ruas)
    adj = random.choice(adjetivos)
    return f"{rua} {adj}"
 
# gerador de cnpj valido -------------------------------------------------------------------------------------------------------------------------------
def calcula_digito(cnpj, multiplicadores):
    soma = sum(int(a) * b for a, b in zip(cnpj, multiplicadores))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)
 
def gerar_cnpj():
    # Definir os primeiros 8 dígitos (podemos fixar UF/Setor se necessário)
    cnpj = [random.randint(0, 9) for _ in range(8)]
   
    # Fixar os últimos 4 números antes dos dígitos verificadores
    cnpj.extend([0, 0, 0, 1])  # Exemplo padrão
   
    # Calcular o primeiro dígito verificador
    multiplicadores_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = calcula_digito(cnpj, multiplicadores_1)
    cnpj.append(int(primeiro_digito))
   
    # Calcular o segundo dígito verificador
    multiplicadores_2 = [6] + multiplicadores_1
    segundo_digito = calcula_digito(cnpj, multiplicadores_2)
    cnpj.append(int(segundo_digito))
   
    # Retornar o CNPJ formatado
    return "{}{}{}{}{}".format(
        ''.join(map(str, cnpj[:2])),
        ''.join(map(str, cnpj[2:5])),
        ''.join(map(str, cnpj[5:8])),
        ''.join(map(str, cnpj[8:12])),
        ''.join(map(str, cnpj[12:]))
    )
 
# gerador indicador cpf e cnpj valido--------------------------------------------------------------------------------------------------------------------------------
def gerar_cpf_cnpj():
    if random.choice(["cpf", "cnpj"]) == "cpf":
        return gerar_cpf()
    else:
        return gerar_cnpj()
 
# gerador cpf valido--------------------------------------------------------------------------------------------------------------------------------
def gerar_cpf():
   # Gera os 9 primeiros dígitos
   cpf = [random.randint(0, 9) for _ in range(9)]
   # Primeiro dígito verificador
   soma = sum(cpf[i] * (10 - i) for i in range(9))
   digito1 = (soma * 10) % 11
   digito1 = digito1 if digito1 < 10 else 0
   cpf.append(digito1)
   # Segundo dígito verificador
   soma = sum(cpf[i] * (11 - i) for i in range(10))
   digito2 = (soma * 10) % 11
   digito2 = digito2 if digito2 < 10 else 0
   cpf.append(digito2)
   # Retorna o CPF como string
   return ''.join(map(str, cpf))
 
# gerador de 6 numeros-----------------------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_6(tamanho_maximo=6):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
# gerador de 10 numeros-----------------------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_10(tamanho_maximo=10):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
# gerador de 15 numeros-----------------------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_15(tamanho_maximo=15):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
 
# gerador de 16 numeros-----------------------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_16(tamanho_maximo=16):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
 
# gerador de 12 numeros---------------------------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_12(tamanho_maximo=12):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho aleatório entre 1 e 12
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
# gerador de valor-divida sem decimais-----------------------------------------------------------------------------------------------------------------------
def gerar_valor_RS_sem_centavos_virgula():
    # Gera um valor aleatório entre 10 e 99, com duas casas decimais
    valor = random.randint(10, 99)  # Gera um valor inteiro entre 10 e 99
    return f'{valor},00'
 
# gerador de valor-divida decimais-----------------------------------------------------------------------------------------------------------------------
def gerar_valor_RS_com_centavos_virgula():
    # Gera um valor aleatório entre 0 e 99, com duas casas decimais
    valor = round(random.uniform(99, 999), 2)
    return f'{valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
 
# gerador de valor-divida sem decimais-----------------------------------------------------------------------------------------------------------------------
def gerar_valor_RS_sem_centavos_ponto():
    # Gera um valor aleatório entre 10 e 99, com duas casas decimais
    valor = random.randint(10, 99)  # Gera um valor inteiro entre 10 e 99
    return f'{valor}.00'
 
# gerador de valor-divida com decimais-----------------------------------------------------------------------------------------------------------------------
def gerar_valor_RS_com_centavos_ponto():
    # Gera um valor aleatório entre 0 e 99, com duas casas decimais
    valor = round(random.uniform(9, 99), 2)
    return f'{valor:,.2f}'.replace('.', 'X').replace('.', '.').replace('X', '.')
 
# gerador de data de vencimento-----------------------------------------------------------------------------------------------------------------
#def gerar_data_vencimento():
 #   # Data atual do sistema
  #  data_atual = datetime.now()
   
    # Adiciona 3 meses e 1 dia para garantir que seja maior que 3 meses
   # data_vencimento = data_atual - relativedelta(months=3) + timedelta(days=1)
   
    #return data_vencimento.strftime('%d/%m/%Y')
 
# Insumos datas random
datas = ["10/04/2023", "17/05/2021", "27/02/2020", "24/11/2021", "19/11/2019"]
 
# Função para gerar nome aleatório
def gerar_data_vencimento_listadatas():
    data_carga = random.choice(datas)
    return f"{data_carga}"
 
# gerador de data de vencimento para carga ativos-----------------------------------------------------------------------------------------------------------------
datas_ativos = ["2023-04-11", "2021-05-21", "2020-02-24", "2021-11-02", "2019-11-07"]
 
# Função para gerar nome aleatório
def gerar_data_vencimento_ativos():
    data_ativos = random.choice(datas_ativos)
    return f"{data_ativos}"
 
# gerador aleatorio dois numeros----------------------------------------------------------------------------------------------------------------
def gerar_numero_aleatorio_2(tamanho_maximo=2):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define tamanho
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return numero_aleatorio
 
# gerador telefone com 11 e 9------------------------------------------------------------------------------------------------------------------------------
def gerar_telefone_11_8(tamanho_maximo=8):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho aleatório entre 1 e 8
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return f'110{numero_aleatorio}'
 
# gerador telefone sem------------------------------------------------------------------------------------------------------------------------------
def gerar_telefone_sem_119(tamanho_maximo=8):
    tamanho = random.randint(tamanho_maximo, tamanho_maximo)  # Define um tamanho aleatório entre 1 e 8
    numero_aleatorio = ''.join(random.choices('0123456789', k=tamanho))  # Gera o número aleatório
    return f'{numero_aleatorio}'
 
# gerador de email------------------------------------------------------------------------------------------------------------------------------
 
# Listas de nomes, sobrenomes e domínios
nomes = ["Joao", "Maria", "Ana", "Carlos", "Bruno", "Fernanda", "Paula", "Roberto", "Julia", "Ricardo"]
sobrenomes = ["Silva", "Oliveira", "Santos", "Pereira", "Costa", "Martins", "Araujo", "Souza", "Gomes", "Barbosa"]
dominios = ["spcbrasil.com.br", "email.com", "teste.org", "site.net", "dominio.com.br"]
 
def gerar_email():
    # Seleciona nome, sobrenome e domínio aleatoriamente
    nome = random.choice(nomes).lower()
    dominio = random.choice(dominios)
   
    # Gera um número aleatório para evitar duplicidade
    numero = random.randint(1, 999)
   
    # Formata o e-mail
    email = f"{nome}.{numero}@{dominio}"
   
    return email
 
# gerador de cep--------------------------------------------------------------------------------------------------------------------------------
def gerar_cep():
    # Gera os cinco primeiros dígitos (de 10000 a 99999) para representar a região
    prefixo = random.randint(10000, 99999)
   
    # Gera os três últimos dígitos (de 000 a 999) para representar o setor de entrega
    sufixo = random.randint(000, 999)
   
    # Formata o CEP com zeros à esquerda, se necessário, para garantir que o sufixo tenha três dígitos
    cep = f"{prefixo}{sufixo:03}"
   
    return cep
 
# gerador de nome e sobrenome----------------------------------------------------------------------------------------------------------------------------
# Insumos nome e sobrenome
nome = ["Rafael", "Gabriel", "Guilherme", "Julia", "Ana", "Leo", "Luana", "Janaina", "Laura", "Iara", "Giuliano", "Vanderlei", "Larissa", "Paulo"]
sobrenome = ["Silva", "Cruz", "Pires", "Rocha", "Santos", "Lima", "Figueira"]
 
# Função para gerar nome aleatório
def gerar_nome_sobrenome():
    nomes = random.choice(nome)
    sobrenomes = random.choice(sobrenome)
    return f"{nomes} {sobrenomes}"
 
 
# gerador de data nascimento----------------------------------------------------------------------------------------------------------------------------
def gerar_data_nascimento(min_idade=18, max_idade=80):
    # Data atual
    hoje = datetime.today()
    # Calcular os limites de data de nascimento
    inicio = hoje - timedelta(days=max_idade * 365)
    fim = hoje - timedelta(days=min_idade * 365)
    # Gerar uma data aleatória dentro do intervalo
    data_aleatoria = inicio + timedelta(days=random.randint(0, (fim - inicio).days))
    # Retornar a data formatada (padrão DD/MM/AAAA)
    return data_aleatoria.strftime("%Y-%m-%d")
 
# gerador de data vencimento----------------------------------------------------------------------------------------------------------------------------
def gerar_data_vencimento(min_idade=0, max_idade=7):
    # Data atual
    hoje = datetime.today()
    # Calcular os limites de data de vencimento
    inicio = hoje - timedelta(days=max_idade * 365)
    fim = hoje - timedelta(days=min_idade * 365)
    # Gerar uma data aleatória dentro do intervalo
    data_aleatoria = inicio + timedelta(days=random.randint(0, (fim - inicio).days))
    # Retornar a data formatada
    return data_aleatoria.strftime("%d/%m/%Y")
 
# gerador de data vencimento----------------------------------------------------------------------------------------------------------------------------
def gerar_data_pagamento(min_idade=0, max_idade=1):
    # Data atual
    hoje = datetime.today()
    # Calcular os limites de data
    inicio = hoje - timedelta(days=max_idade * 365)
    fim = hoje - timedelta(days=min_idade * 365)
    # Gerar uma data aleatória dentro do intervalo
    data_aleatoria = inicio + timedelta(days=random.randint(0, (fim - inicio).days))
    # Retornar a data formatada
    return data_aleatoria.strftime("%Y-%m-%d")
 
# gerador de origem da divida-----------------------------------------------------------------------------------------------------------------------------
# Insumos Origem
origem = ["Caixa Economica Federal","Banco Do Brasil","NUbank","Magazine Luiza Cartao"]
 
# Função para gerar nome aleatório
def gerar_origem_divida():
    origens = random.choice(origem)
    return f"{origens}"
 
 
# gerador de id operacao--------------------------------------------------------------------------------------------------------------------------------------------
 
def gerar_id_operacao():
     ids_gerados = set()
     while True:
          id__operacao = random.randint(10**9, 10**10 - 1)
          if id__operacao not in ids_gerados:
              ids_gerados.add(id__operacao)
              return id__operacao
         
 
# gerador de contrato identico---------------------------------------------------------------------------------------------------------------------------------------------
 
contratoAut = ["CalValidaAut11022025"]
 
# Função para gerar logradouro aleatório
def gerar_contrato_identico():
    cotratoUnico = random.choice(contratoAut)
    return f"{cotratoUnico}"