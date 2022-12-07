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