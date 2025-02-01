import streamlit as st
from Get_Trading_Data import *

chave = obter_chave(
    r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Automação\Banco_e_Visualizador_De_Ativos\CHAVE.txt"
)


def obter_ativos_cadastrados() -> list[str]:
    """
    Descrição:
        Obtém ativos já cadastrados a partir do configuration.txt
    """

    return [
        "",
        "Adicionar Ativo",
    ]


def cadastrar_novo_ativo():
    """
    Descrição:
        A partir do desejo do usuário, disponibiliza a interface
        de cadastro de um novo ativo.
    """

    st.header(
        "Cadastrando Novo Ativo"
    )

    nome_dado_pelo_usuario = st.text_input(
        label="Insira o possível símbolo do ativo"
    )

    if nome_dado_pelo_usuario != "":
        pass

        # try:
        #     resultados_de_busca_de_semelhantes = buscar_ativos_semelhantes(
        #         nome_dado_pelo_usuario,
        #         chave
        #     )
        #
        #     st.write(
        #         resultados_de_busca_de_semelhantes
        #     )
        #
        #     if len(
        #             resultados_de_busca_de_semelhantes
        #     ) > 0:
        #
        #         nome_das_colunas = (
        #             "Código",
        #             "Nome",
        #             "Tipo do Ativo",
        #             "Região",
        #             "Abertura",
        #             "Fechamento",
        #             "Fuso Horário",
        #             "Moeda"
        #         )
        #
        #         colunas_do_ativo_encontrado = st.columns(
        #             (
        #                 1, 3, 3
        #             )
        #         )
        #
        #         primeiro = True
        #         for ativo_encontrado in resultados_de_busca_de_semelhantes:
        #             for key, col, nome_coluna in zip(
        #                 ativo_encontrado.keys(),
        #                 colunas_do_ativo_encontrado,
        #                 nome_das_colunas
        #             ):
        #                 with col:
        #                     if primeiro:
        #                         st.subheader(
        #                             nome_coluna
        #                         )
        #
        #                     st.write(
        #                         ativo_encontrado[
        #                             key
        #                         ]
        #                     )
        #             primeiro = False
        #
        #     else:
        #         st.write(
        #             "Não há ativos semelhantes à este nome."
        #         )
        #
        # except Exception as error:
        #     st.error(
        #         f"Obtive {error}"
        #     )
