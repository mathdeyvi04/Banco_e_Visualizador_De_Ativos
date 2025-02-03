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


def selecionar_atributos_do_ativo(
        opcao_escolhida: str | None
) -> None:
    """
    Descrição:
        
    """

    st.write(opcao_escolhida)


def cadastrar_novo_ativo():
    """
    Descrição:
        A partir do desejo do usuário, disponibiliza a interface
        de cadastro de um novo ativo.
    """

    st.header(
        "Cadastrando Novo Ativo"
    )

    st.divider()

    nome_dado_pelo_usuario = st.text_input(
        label="Insira o possível símbolo do ativo",
        help="Coloque o código que você acredita que seja do ativo desejado."
    )

    if nome_dado_pelo_usuario != "":

        try:
            if "chaves" not in st.session_state:
                st.session_state[
                    "chaves"
                ] = obter_chave(
                    NOME_DO_ARQUIVO_DE_CHAVES
                )

            st.session_state[
                "Resultados_De_Busca_De_Semelhantes"
            ] = buscar_ativos_semelhantes(
                nome_dado_pelo_usuario,
                st.session_state[
                    "chaves"
                ]
            )

            if len(
                    st.session_state[
                        "Resultados_De_Busca_De_Semelhantes"
                    ]
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

                nome_das_chaves = st.session_state[
                    "Resultados_De_Busca_De_Semelhantes"
                ][0].keys()

                resultados_em_dataframe = DataFrame(
                    {
                        nome_coluna: [
                            ativo_encontrado[
                                nome_chave
                            ] for ativo_encontrado in st.session_state[
                                "Resultados_De_Busca_De_Semelhantes"
                            ]
                        ] for nome_coluna, nome_chave in zip(
                            nome_das_colunas,
                            nome_das_chaves
                        )
                    }
                ).set_index(
                    nome_das_colunas[0],
                    drop=True
                )

                col1, col2 = st.columns(
                    (
                        6, 1
                    )
                )

                with col1:

                    st.dataframe(
                        resultados_em_dataframe,
                        width=1400
                    )

                opcao_escolhida = None
                with col2:
                    st.write("")

                    opcao_escolhida = st.radio(
                        label="Opções",
                        options=[
                            ativo_encontrado["1. symbol"][:5] for ativo_encontrado in st.session_state[
                                "Resultados_De_Busca_De_Semelhantes"
                            ]
                        ],
                        captions=[
                            # Para adicionar espaço.
                            "" for _ in st.session_state[
                                "Resultados_De_Busca_De_Semelhantes"
                            ]
                        ],
                        index=None,
                    )

                if opcao_escolhida:
                    selecionar_atributos_do_ativo(
                        opcao_escolhida
                    )

            else:
                st.write(
                    "Não há ativos semelhantes à este nome."
                )

        except Exception as error:
            st.error(
                f"Obtive: {error}"
            )
