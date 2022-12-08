import pandas
import seaborn as sns


def carrega_dataset(nome_dataset:str) -> pandas.DataFrame:
    """Carrega uma base de dados do seaborn de acordo com o nome
    do dataset.

    Args:
        nome_dataset (str): nome do dataset a ser carregado

    Returns:
        pandas.DataFrame: dataset
    """
    return sns.load_dataset(nome_dataset)



def soma(a:int, b:int) -> int:
    """_summary_

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        int: _description_
    """
    return a + b