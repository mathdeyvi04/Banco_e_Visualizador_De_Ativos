from Get_Trading_Data import *


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


def selecionar_atributos_do_ativo(
        opcao_escolhida: str | None
) -> None:
    """
    Descrição:
        Dispõe os atributos necessários para que a aplicação busque
        esse ativo.
    """

    # Seria ótimo ter o preço atual do ativo, em apresentação aqui.

    st.write(
        f"Exibindo Atributos Para: _{opcao_escolhida}_."
    )
    st.divider()

    def parametros_de_tunel() -> tuple[str, list]:
        st.subheader(
            f"Parâmetros de Túnel"
        )

        classificao: str = st.radio(
            label="Classificação do Túnel",
            options=(
                "Estático",
                "Síncrono"
            ),
            captions=(
                "Nos quais os limites são estáticos e previamente fixados antes da sessão de negociação.",
                "Sincronizados com o valor de referência do preço do ativo ou derivativo em tempo real, durante a sessão de negociação.",
            ),
            index=False
        )

        cols = st.columns(
            (1, 5, 10)
        )

        tabela_de_ref = []
        with cols[1]:
            if classificao.startswith(
                    "E"
            ):
                tabela_de_ref.append(
                    st.number_input(
                        label="Limite Superior",
                        step=1,
                        help="Este valor servirá como limite fixo."
                    )
                )
                tabela_de_ref.append(
                    st.number_input(
                        label="Limite Inferior",
                        step=1,
                        help="Este valor servirá como limite fixo."
                    )
                )

            if classificao.startswith(
                    "S"
            ):
                referencia = st.radio(
                    label="Referência Para Túnel",
                    options=(
                        "Último preço atualizado",
                        "Preço da última operação",
                        "Preço de fechamento"
                    ),
                    captions=(
                        "",
                        "",
                        ""
                    ),
                    index=False
                )

                tabela_de_ref.append(
                    st.number_input(
                        label="Porcentagem do Valor Para Limite Superior",
                    )
                )

                tabela_de_ref.append(
                    st.number_input(
                        label="Porcentagem do Valor Para Limite Inferior",
                    )
                )

                tabela_de_ref.append(
                    referencia
                )

        return classificao, tabela_de_ref

    clasf, tab_ref = parametros_de_tunel()

    st.divider()

    def periodicidade():
        cols = st.columns(
            (1, 2)
        )

        with cols[0]:
            interv = st.selectbox(
                "Insira a Periodicidade de Checagem",
                options=(
                    "1 min",
                    "5 min",
                    "10 min"
                ),
                placeholder="Escolha"
            )

        return interv

    interv_ = periodicidade()

    st.divider()

    def pegar_dict_do_ativo(
            codigo_ativo: str
    ) -> dict:

        for ativo_encontrado in st.session_state[
            "Resultados_De_Busca_De_Semelhantes"
        ]:
            if ativo_encontrado[
                "1. symbol"
            ] == codigo_ativo:
                return ativo_encontrado

    def fechar() -> None:

        st.session_state["Novo_Ativo_Sendo_Cadastrado"] = False
        st.session_state.pop(
            "Resultados_De_Busca_De_Semelhantes"
        )

    st.download_button(
        # LIMITAÇÃO:
        # Não Consegui Fazer DownLoad do Arquivo
        # da forma correta, humilhante diga-se de passagem.
        "Finalizar Cadastro de Ativo",
        f"{pegar_dict_do_ativo(opcao_escolhida)};{clasf};{tab_ref};{interv_}",
        f"ativo={opcao_escolhida}.txt",
        on_click=fechar
    )


def cadastrar_novo_ativo():
    """
    Descrição:
        A partir do desejo do usuário, disponibiliza a interface
        de cadastro de um novo ativo.
    """
    st.divider()
    st.subheader(
        "Buscando Novo Ativo"
    )

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
