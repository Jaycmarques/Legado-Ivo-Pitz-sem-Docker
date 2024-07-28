import subprocess
import requests

# Atualiza o repositório
subprocess.run(['git', 'pull', 'origin', 'main'])

# Recarrega o web app
username = 'jcmarques'
token = '19009bba6d7cfd7d1e6c362e3f69f6165dfab307'
domain_name = 'jcmarques.pythonanywhere.com'

response = requests.post(
    f'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/',
    headers={'Authorization': f'Token {token}'}
)

if response.status_code == 200:
    print('Web app recarregado com sucesso!')
else:
    print(f'Erro ao recarregar o web app: {response.status_code}')
    print(response.content)
