import requests

# Defina suas variáveis de ambiente
username = 'jcmarques'
domain_name = 'jcmarques.pythonanywhere.com'  # Nome completo do domínio
token = '19009bba6d7cfd7d1e6c362e3f69f6165dfab307'
host = 'www.pythonanywhere.com'  # ou 'eu.pythonanywhere.com' se estiver na UE

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
