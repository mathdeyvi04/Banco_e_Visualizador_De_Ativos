from Get_Trading_Data import *

CHAVE = obter_chave(
    NOME_DO_ARQUIVO_DE_CHAVES
)

# Novos ativos não estarão na pasta Dados, estarão lá.

ativos = obter_ativos_cadastrados()

for ativo in ativos:
    if ativo not in {
        "",
        "Adicionar Ativo"
    }:
        print(
            f"Concluí {ativo}"
        )
        obter_dados_de_ativo(
            ativo,
            CHAVE,
            teste=False,
            deseja_saida=False
        )



