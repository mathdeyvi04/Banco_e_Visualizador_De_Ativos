import requests as re
import streamlit as st
from pandas import DataFrame
from pprint import pprint

st.session_state[
    "Quantas Vezes Usamos API"
] = 0

NOME_DO_ARQUIVO_DE_CHAVES = r'C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\CHAVE.txt'


def obter_chave(
        nome_do_arquivo_que_contem_chave: str
) -> list[list[str] | int]:
    """
    Descrição:
        Obtém chaves da API do usuário a partir de um arquivo .txt
        que a contém.

        Utilizamos inúmeras chaves para contornar o acesso limitado à API.

        Utilizamos
    """

    with open(
            nome_do_arquivo_que_contem_chave,
            "r"
    ) as arq:
        lista_de_chaves = arq.readlines()

        for index in range(
                0,
                len(
                    lista_de_chaves
                )
        ):
            lista_de_chaves[
                index
            ] = lista_de_chaves[
                index
            ].replace(
                "\n",
                ""
            )

    return [
        lista_de_chaves,
        0
    ]


st.session_state[
    "chaves"
] = obter_chave(
    NOME_DO_ARQUIVO_DE_CHAVES
)


def buscar_ativos_semelhantes(
        chute_do_nome_do_ativo: str,
        chave: list[list[str] | int]
) -> list[dict[str, str]]:
    """
    Descrição:
        Obtém lista de possíveis ativos a
        partir do chute do usuário.
    """

    resultados = {
        "bestMatches": [
            # Para não abusar da API
            {
                "1. symbol": f"AW {i}",
                "2. name": "A&W Revenue Royalties Income Fund",
                "3. type": "Equity",
                "4. region": "Toronto",
                "5. marketOpen": "09:30",
                "6. marketClose": "16:00",
                "7. timezone": "UTC-05",
                "8. currency": "CAD",
                "9. matchScore": "0.6800"
            } for i in range(0, 10)
        ]
    }

    # resultados = re.get(
    #     f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={chute_do_nome_do_ativo}&apikey={chave[0][chave[1]]}"
    # ).json()

    if "Quantas Vezes Usamos API" not in st.session_state:
        st.session_state[
            "Quantas Vezes Usamos API"
        ] = 0

    st.session_state[
        "Quantas Vezes Usamos API"
    ] += 1

    st.info(f"Hop vim: {st.session_state['Quantas Vezes Usamos API']}.")

    if "Information" in resultados:
        # Chegamos no limite desta chave.

        chave[1] += 1

        st.warning(
            f"Trocando para nova chave, total de usos: {st.session_state['Quantas Vezes Usamos API']}."
        )

        return buscar_ativos_semelhantes(
            chute_do_nome_do_ativo,
            chave
        ) if len(chave[0]) != chave[1] else st.error(
            f"Atingiu-se o limite de todas as chaves. {resultados}"
        )

    return resultados["bestMatches"]

