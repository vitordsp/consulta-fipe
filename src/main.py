import pandas as pd
# import matplotlib.pyplot as plt
import sys
from datetime import datetime
from pyfipe.core import ConsultaFipe
from pyfipe.tabelas import consulta_tabela_referencia, consulta_tabela_marcas, consulta_tabela_modelos

MESES = [
    'janeiro',
    'fevereiro',
    'março',
    'abril',
    'maio',
    'junho',
    'julho',
    'agosto',
    'setembro',
    'outubro',
    'novembro',
    'dezembro'
]

def safe_stop():
    sys.exit()
    pass

def gerar_data(hoje=datetime.now()) -> str:
    """Monta string com data no formato string_mes/ano
    Se nenhuma data for providenciada, utiliza o dia atual"""

    mes = hoje.month - 1
    ano = hoje.year

    return MESES[mes] + '/' + str(ano)

def tela_consulta_codigo():
    # TODO: implementar consulta por codigo fipe
    raise NotImplementedError

def tela_consulta_historico():
    # TODO: implementar consulta de historico por codigo
    raise NotImplementedError

def tela_listar_marcas_iniciais():
    """Imprime a lista de marcas por incial para a data atual na tela"""

    for i in range(1):
        try:
            tipo = int(input("Qual tipo de veiculo deseja listar?\n[1] Carros\n[2] Motocicletas\n\nSua entrada:"))
            inicial = input("Qual a inicial da marca de veiculo?")
        except ValueError:
            continue
    marcas = consulta_tabela_marcas(mes=gerar_data(), tipo_veiculo='moto' if tipo == 2 else 'carro')
    filtered_marcas = marcas[marcas['marca'].str.startswith(inicial)]
    print(filtered_marcas)

def tela_listar_modelos():
    # TODO: implementar listagem de modelos
    raise NotImplementedError

def plot_consulta():
    # TODO: implementar grafico de consulta
    raise NotImplementedError

def main():
    """Tela inicial"""

    try:
        print("\nSeja bem vindo a consulta FIPE\n\n")
        while True:
            entrada = input(
"""
O que voce gostaria de fazer?

[1] Listar as marcas de veiculo
[2] Listar os modelos de veiculo
[3] Consultar por codigo FIPE
[4] Consultar historico

[0] Sair do programa
""")
            try:
                entrada = int(entrada)
            except ValueError:
                print ("\n\nPor favor insira um numero")
            pass

            match entrada:
                case 0:
                    print("\n\nbyebye\n\n")
                    safe_stop()
                case 1:
                    tela_listar_marcas_iniciais()
                case 2:
                    tela_listar_modelos()
                case 3:
                    tela_consulta_codigo()
                case 4:
                    tela_consulta_historico()
    except KeyboardInterrupt:
        safe_stop()
    except NotImplementedError:
        print("\n\nOoops! Parece que algo nao foi implementado rsrs...\n")
        input("Pressione ENTER para sair...")
    except Exception as e:
        print("Ocorreu um erro:\n\n{}".format(e))
        safe_stop()


if __name__ == '__main__':
    main()
