# Código desenvolvido por Matheus Deyvisson.
# Descrição:
#   Construção da Interface Web que disporá todas as configurações
#   e formas de visualização dos dados salvos.
#
# Dicas de Construção:
#   Aparentemente, é como o site ficasse rodando o código
#   a cada instante, não é tão intuitivo.
#
#
from Back_Web import *

st.set_page_config(
    layout="wide"
)
ATIVOS_CADASTRADOS = obter_ativos_cadastrados()

# Barra Lateral
st.sidebar.title(
    "Configurações"
)

combobox_ativo = st.sidebar.selectbox(
    "Selecione o Ativo",
    ATIVOS_CADASTRADOS
)

if combobox_ativo != "":

    if combobox_ativo.startswith(
            "Adici"
    ):
        # Vamos adicionar um novo ativo.
        if "Novo_Ativo_Sendo_Cadastrado" not in st.session_state:
            st.session_state["Novo_Ativo_Sendo_Cadastrado"] = True

        if st.session_state["Novo_Ativo_Sendo_Cadastrado"]:
            cadastrar_novo_ativo()
        else:
            st.session_state.pop(
                "Novo_Ativo_Sendo_Cadastrado"
            )

            st.markdown(
                """
                <style>
                .big-title {
                    font-size: 40px;
                    text-align: center;
                    color: #FF4B4B;
                    font-family: 'Roboto', sans-serif;
                    margin-top: 20%;
                }
                </style>

                <div class="big-title">
                    Cadastro Concluído!<br>
                    Aguarde um tempo enquanto o sistema capta os dados do ativo.<br>
                    Tente selecionar um outro ativo.
                </div>
                """,
                unsafe_allow_html=True
            )

    # Temos garantia que outro ativo não cadastrado não será aceito.
    else:

        opcoes_de_apresentacao = st.sidebar.multiselect(
            "Selecione o que deseja ver",
            options=(
                "open",
                "high",
                "low",
                "close"
            ),
            help="Mostrará os valores correspondentes aos significados selecionados",
        )

        resultados_do_ativo = obter_dados_de_ativo(
            combobox_ativo,
            st.session_state[
                "chaves"
            ],
            True
        )

        plotando(
            resultados_do_ativo,
            opcoes_de_apresentacao
        )


        # st.write(
        #     resultado
        # )
        #
        # pp.plot(
        #     resultado["open"]
        # )
        # pp.ylim(
        #     min(resultado["open"]),
        #     max(resultado["open"])
        # )
        # pp.title(
        #     "Open"
        # )
        # pp.xlabel(
        #     "Instante"
        # )
        # pp.show()
        #
        # st.pyplot(pp)



else:

    # Título Chamativo
    st.markdown(
        """
        <style>
        .big-title {
            font-size: 40px;
            text-align: center;
            color: #FF4B4B;
            font-family: 'Roboto', sans-serif;
            margin-top: 20%;
        }
        </style>

        <div class="big-title">
            Permita-me apresentar-lhe algo 🚀!
        </div>
        """,
        unsafe_allow_html=True
    )
