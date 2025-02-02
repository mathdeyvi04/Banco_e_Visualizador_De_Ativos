from Get_Trading_Data import *


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

        try:
            resultados_de_busca_de_semelhantes = buscar_ativos_semelhantes(
                nome_dado_pelo_usuario,
                chaves
            )

            st.write(
                resultados_de_busca_de_semelhantes
            )

            if len(
                resultados_de_busca_de_semelhantes
            ) > 0:

                nome_das_colunas = (
                    "Código",
                    "Nome",
                    "Tipo",
                    "Região",
                    "Abertura",
                    "Fechamento",
                    "Fuso Horário",
                    "Moeda"
                )

            else:
                st.write(
                    "Não há ativos semelhantes à este nome."
                )

        except Exception as error:
            st.error(
                f"Obtive: {error}"
            )
