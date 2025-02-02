import requests as re
import streamlit as st


def obter_chave(
        nome_do_arquivo_que_contem_chave: str
) -> list[list[str] | int]:
    """
    Descrição:
        Obtém chaves da API do usuário a partir de um arquivo .txt
        que a contém.

        Foi feito desta maneira para contar o acesso limitado à API.

        Isso é feito para medidas de segurança.

    """

    with open(
            nome_do_arquivo_que_contem_chave,
            "r"
    ) as arq:
        lista_de_chaves = arq.readlines()

        lista_de_chaves[0] = lista_de_chaves[0].replace("\n", "")

    return [
        lista_de_chaves,
        0
    ]


chaves = obter_chave(
    r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\Banco_e_Visualizador_De_Ativos\CHAVE.txt"
)


def buscar_ativos_semelhantes(
        chute_do_nome_do_ativo: str,
        chave: list[list[str] | int]
) -> list:
    """
    Descrição:
        Obtém lista de possíveis ativos a
        partir do chute do usuário.
    """
    st.write(f"Vendo chaves: {chave}")
    resultados = re.get(
        f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={chute_do_nome_do_ativo}&apikey={chave[0][chave[1]]}"
    ).json()

    if "Information" in resultados:
        # Chegamos no limite desta chave.

        chave[1] += 1

        return buscar_ativos_semelhantes(
            chute_do_nome_do_ativo,
            chave
        ) if len(chave[0]) != chave[1] else st.error(
            f"Atingiu-se o limite de todas as chaves. {resultados}"
        )

    return resultados["bestMatches"]
