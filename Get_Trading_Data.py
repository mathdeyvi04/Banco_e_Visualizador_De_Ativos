import requests as re
import json as js
import plotly.express as px

try:
    # Um erro pode ocorrer ao executar essas coisas
    # sem ser do jeito que eles querem.
    import streamlit as st
except:
    pass
from pandas import DataFrame
from matplotlib import pyplot as pp
from pprint import pprint
from os import listdir, remove
from os.path import exists

try:
    st.session_state[
        "Quantas Vezes Usamos API"
    ] = 0
except:
    pass

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


def obter_ativos_cadastrados() -> list[str]:
    """
    Descrição:
        Obtém ativos já cadastrados a partir do configuration.txt
    """

    resultado = [
        "",
        "Adicionar Ativo"
    ]

    for arquivo_ou_pasta_disponivel in listdir(
            r"C:\Users\deyvi\Downloads"
    ):
        if arquivo_ou_pasta_disponivel.startswith(
                "ativo="
        ):
            # Temos um ativo salvo.
            resultado.append(
                arquivo_ou_pasta_disponivel.replace(
                    "ativo=",
                    ""
                ).replace(
                    ".txt",
                    ""
                )
            )

    return resultado


try:
    st.session_state[
        "chaves"
    ] = obter_chave(
        NOME_DO_ARQUIVO_DE_CHAVES
    )
except:
    pass


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

    try:
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
    except:
        pass

    return resultados["bestMatches"]


def obter_dados_de_ativo(
        codigo: str,
        chave: list[list[str] | int],
        deseja_saida: bool = False,
        teste: bool = True
) -> None | DataFrame:
    """
    Descrição:
        Função responsável por buscar os dados do ativo.

        Com o intuito de mais acurácia financeira, devemos ficar
        aplicando esta função várias vezes
    """

    def tratando_dados(
            resultado_: dict
    ) -> dict:
        """
        Descrição:
            Função responsável por separar os dados obtidos do ativo
            corretamente
        """

        instantes = list(resultado_.keys())[::-1]

        colunas = (
            "open",
            "high",
            "low",
            "close",
            "volume"
        )

        corrigido = {
            "inicio": instantes[0],
            "final": instantes[-1],
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "volume": []
        }

        for instante in instantes:
            for i, coluna in enumerate(colunas):
                corrigido[
                    coluna
                ].append(
                    float(
                        resultado_[
                            instante
                        ][
                            f"{i + 1}. {coluna}"
                        ]
                    )
                )

        return corrigido

    resultado = {} if teste else re.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={chave[0][chave[1]]}"
    ).json()

    if "Information" in resultado:
        chave[-1] += 1

        st.warning(
            f"Trocando para nova chave."
        )

        return obter_dados_de_ativo(
            codigo,
            chave
        ) if len(chave[0]) != chave[1] else st.error(
            f"Atingiu-se o limite de todas as chaves. {resultados}"
        )

    caminho_do_ativo = rf"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\Banco_e_Visualizador_De_Ativos\Dados\{codigo}.json"

    if exists(
            caminho_do_ativo
    ) and len(
        # Garante que em um ambiente de teste não apagaremos o arquivo.
        resultado
    ):
        remove(
            caminho_do_ativo
        )

    if resultado:
        with open(
                caminho_do_ativo,
                "x"
        ) as base:
            base.write(
                f"{resultado['Time Series (5min)']}".replace(
                    "'",
                    '"'
                )
            )

    if deseja_saida:
        with open(
                caminho_do_ativo,
                "r"
        ) as base:
            resultado_baixado = js.loads(
                base.read()
            )

        return DataFrame(
            tratando_dados(
                resultado_baixado
            )
        )


def plotando(
        info: DataFrame,
        opcoes: list[str]
) -> None:
    """
    Descrição:
        Plotará um gráfico muito lindo com as opções selecionadas.
    """

    plotly_figure = px.line(
        data_frame=info[opcoes],
        title=f"Apresentando Valores para {info['inicio'][0]}-{info['final'][99]}",
        labels={
            "value": "Valor",
            "index": "Instantes"
        }
    )

    st.plotly_chart(
        plotly_figure
    )
