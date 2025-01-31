import requests as re
from pprint import pprint


def obter_chave(
        nome_do_arquivo_que_contem_chave: str
) -> str:
    """
    Descrição:
        Obtém chave da API do usuário a partir de um arquivo .txt
        que a contém.

        Isso é feito para medidas de segurança.
    """

    chave = "None"

    with open(
            nome_do_arquivo_que_contem_chave,
            "r"
    ) as arq:
        chave = arq.read()

    return chave


def buscar_ativos_semelhantes(
        chute_do_nome_do_ativo: str,
        chave: str
) -> list:
    """
    Descrição:
        Obtém lista de possíveis ativos a
        partir do chute do usuário.
    """

    return re.get(
        f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={chute_do_nome_do_ativo}&apikey={chave}"
    ).json()["bestMatches"]
