import requests
import os

# Defina suas variáveis de ambiente
username = 'jcmarques'
domain_name = 'jcmarques.pythonanywhere.com'  # Nome completo do domínio
host = 'www.pythonanywhere.com'  # ou 'eu.pythonanywhere.com' se estiver na UE

# Obtenha o token da variável de ambiente
token = os.getenv('PA_API_TOKEN')

if not token:
    raise ValueError("A variável de ambiente PA_API_TOKEN não está definida.")

# URL correta para o endpoint de recarregamento
url = f'https://{host}/api/v0/user/{username}/webapps/{domain_name}/reload/'

# Solicitação POST para recarregar o web app
response = requests.post(
    url,
    headers={'Authorization': f'Token {token}'}
)

# Verifique a resposta
if response.status_code == 200:
    print("Web app recarregado com sucesso!")
else:
    print(f"Erro ao recarregar o web app: {response.status_code}")
    print("Resposta do servidor:", response.text)
