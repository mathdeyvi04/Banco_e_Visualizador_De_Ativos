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

ativos_cadastrados = obter_ativos_cadastrados()

combobox_ativo = st.sidebar.selectbox(
    "Selecione o Ativo",
    ativos_cadastrados
)


if combobox_ativo != "":

    if combobox_ativo.startswith(
        "Adici"
    ):
        # Vamos adicionar um novo ativo.
        cadastrar_novo_ativo()

    # Temos garantia que outro ativo não cadastrado não será aceito.
    else:
        # Então vamos apresentar um ativo já existente.
        pass
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
