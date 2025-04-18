import requests
from bs4 import BeautifulSoup

# URL do portal de licitações
url = "https://www.comprasnet.gov.br/"

# Realizando a requisição GET para obter a página
response = requests.get(url)
if response.status_code == 200:
    # Se a requisição for bem-sucedida, parse a página HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Aqui você pode buscar informações específicas
    # Exemplo: buscar por licitações abertas
    licitacoes = soup.find_all("div", class_="licitacao")  # Exemplo de classe, ajuste conforme necessário

    for licitacao in licitacoes:
        # Extrair informações relevantes de cada licitação
        titulo = licitacao.find("h3").text.strip()  # Exemplo de título, ajuste conforme a estrutura da página
        data = licitacao.find("span", class_="data").text.strip()  # Exemplo de data, ajuste conforme necessário
        print(f"Título: {titulo}\nData: {data}\n")
else:
    print(f"Erro ao acessar o site: {response.status_code}")
