# Bluetape

## Desafio Técnico
Criação de um código em Python para para checagem de lista de palavras-chave em diversas páginas web. 

## Principais tecnologias

- Selenium
- Beautiful Soup
- Pandas

## Instalação

Para instalar as bibliotecas e dependências necessárias, basta utilizar o seguinte comando: 
#### pip install -r requirements.txt

Após isso basta executar o arquivo principal, __ init __.py

## Descrição

A aplicação busca os parametros de busca no arquivo params.xlsx e a partir disso faz uma busca das palavras coletadas de forma automatizada nos sites descritos. Toda aplicação roda sem visualização do navegador, se preferir, você pode ativar essa funcionalidade removendo a linha: 

```sh
options.add_argument("--headless")
```
O código acima se encontra no arquivo Config.py na pasta modules. Após remover o seguinte código, apenas execute novamente a aplicação. 

A saída da aplicação é um arquivo .xlsx, chamado "__Results__", que contém uma lista ordenada das palavras e sites, por ordem de recorrência.  

#### Contato e Duvidas 
Em caso de dúvidas acerca do desenvolvimeneto, aplicaçã ou outros assuntos, estou aberto para contato.

__Linkedin:__ https://www.linkedin.com/in/samuel-bernardes-lopes-santos/
__Email:__ sbernardes467@gmail.com
__Github__: https://github.com/samuel-bernardes

## Considerações finais

Por fim gostaria de agradecer a oportunidade de participar desse desafio, e a viabilidade de apreender um pouco mais sobre novas tecnologias e padrões de projeto. Obrigado e espero poder continuar entregando, e contribuindo com a Bluetape.
