import requests
import os

# Defina suas variáveis de ambiente
username = 'jcmarques'
domain = 'jcmarques'
token = os.getenv('PA_API_TOKEN')

# URL correta para o endpoint de recarregamento
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'

# Solicitação POST para recarregar o web app
response = requests.post(url, headers={'Authorization': f'Token {token}'})

# Verifique a resposta
if response.status_code == 200:
    print("Web app recarregado com sucesso!")
else:
    print(f"Erro ao recarregar o web app: {response.status_code}")
    print(response.text)
