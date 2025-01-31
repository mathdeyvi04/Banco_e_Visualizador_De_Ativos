# Código desenvolvido por Matheus Deyvisson.
# Descrição:
#   Construção da Interface Web que disporá todas as configurações
#   e formas de visualização dos dados salvos.
from Back_Web import *

ATIVOS_CADASTRADOS = obter_ativos_cadastrados()

# Barra Lateral
st.sidebar.title(
    "Configurações"
)

combobox_ativo = st.sidebar.selectbox(
    "Selecione, ou Digite, o Ativo",
    obter_ativos_cadastrados()
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
        Permita-me apresentar-lhe algo 🚀!
    </div>
    """,
    unsafe_allow_html=True
)
