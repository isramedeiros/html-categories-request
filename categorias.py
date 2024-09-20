import requests
from bs4 import BeautifulSoup

# URL da página
url = 'https://www.poder360.com.br/poder-hoje/?3'

# Fazendo a requisição da página
response = requests.get(url)
html_content = response.content

# Parsing do HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Definindo a data correta
target_date = '20.set.2024'

# Encontrando os posts
posts = []
collecting = False

# Buscando todos os elementos de lista (<li>) que contêm os posts
for element in soup.find_all(['strong', 'li']):
    # Verificando se encontramos o título que marca o início da data desejada
    if element.name == 'strong' and target_date in element.text:
        collecting = True  # Iniciar a coleta
    # Verificando se encontramos a data que marca o final da coleta
    elif element.name == 'strong' and '19.set.2024' in element.text:
        collecting = False  # Parar a coleta
    elif collecting and element.name == 'li':
        post_link = element.find('a', href=True)
        if post_link and 'https://www.poder360.com.br/' in post_link['href']:
            category = post_link['href'].split('/')[3]
            post_text = post_link.text.strip()
            post_url = post_link['href']  # Obtendo o link original
            posts.append({'post': post_text, 'category': category, 'url': post_url})

# Exibindo os posts, categorias e links originais
for post in posts:
    print(f"{post['post']} | {post['category']} | {post['url']}")
