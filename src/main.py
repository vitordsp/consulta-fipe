import pandas as pd
import matplotlib.pyplot as plt
import sys
import datetime
from pyfipe.core import ConsultaFipe
from pyfipe.tabelas import consulta_tabela_referencia, consulta_tabela_marcas, consulta_tabela_modelos


def safe_stop():
    sys.exit()
    pass

def consulta_codigo():
    # TODO: implementar consulta por codigo fipe
    raise NotImplementedError

def listar_marcas():
    # TODO: implementar listagem de marcas
    raise NotImplementedError

def listar_modelos():
    # TODO: implementar listagem de modelos
    raise NotImplementedError

def plot_consulta():
    # TODO: implementar grafico de consulta
    raise NotImplementedError

def main():
    # TODO: implementar loop
    try:
        pass
    except KeyboardInterrupt:
        safe_stop()
        pass


if __name__ == '__main__':
    main()
