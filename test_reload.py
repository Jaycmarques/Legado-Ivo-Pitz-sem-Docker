import requests

# Defina suas variáveis de ambiente
username = 'jcmarques'  # Substitua pelo seu nome de usuário real
token = '19009bba6d7cfd7d1e6c362e3f69f6165dfab307'  # Substitua pelo seu token real

# URL correta para o endpoint de informações de CPU
url = f'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'

# Solicitação GET para obter informações sobre a CPU
response = requests.get(
    url,
    headers={'Authorization': f'Token {token}'}
)

if response.status_code == 200:
    print('Informações sobre a quota de CPU:')
    print(response.content)
else:
    print(f'Código de status inesperado {response.status_code}: {response.content!r}')
