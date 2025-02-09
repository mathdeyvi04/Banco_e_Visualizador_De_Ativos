# Objetivos

* Auxiliar um investidor nas suas decisões de comprar/vender ativos.

> Para tal, o sistema deve registrar periodicamente a cotação atual de
ativos da B3 e também avisar, via e-mail, caso haja oportunidade de
negociação.

# Necessidades 

* Interface Web
* Ativos Desejados pelo Usuário
* Parâmetros de Túnel de Preço Alteráveis pelo Usuário
* Periodicidade de Checagem
* Armazenamento dos Valores Checados
* Pela Interface, Visualização dos Valores Armazenados de um Determinado Ativo

# Conclusão

* Cadastramento de Ativos Desejados

<div align="center">
<img src="https://github.com/user-attachments/assets/e260a419-68ee-4ee2-82b1-aa39b38733a6" width="1000"/>
</div>

* Visualização de Valores Obtidos Dos Ativos

> Infelizmente, ainda não pega os valores com uma determinada periodicidade, devido à limitação da API paga.
> Apenas obtém os valores diários do ativo.

> Apesar da ideia de dispor informações cadastradas do ativo e permitir alteração delas, não foi possível tal realização
> devido à limitação da API.

<div align="center">
<img src="https://github.com/user-attachments/assets/9e96fa2e-b97c-4242-b632-9abaefb38b87" width="1000"/>
</div>


## Pontos Explicados

* Por que não usar web scrapping?
    * Utilizamos a API limitada e gratuita pela simplicidade extrema.