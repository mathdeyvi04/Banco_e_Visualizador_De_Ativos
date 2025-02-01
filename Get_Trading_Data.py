import requests as re
from pprint import pprint
import streamlit as st

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


