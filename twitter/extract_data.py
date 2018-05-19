import twitter
import json


# Função auxiliar para imprimir o resultado
def print_status(status_list):
    for status in status_list:
        print(status.user.name, ':', status.text+'\n')

with open('tokens.json') as f:
    data = json.load(f)

# Carrega a API do Twitter
api = twitter.Api(**data)

# Verifica se as credenciais estão OK
print(api.VerifyCredentials())

# Busca na timeline de um usuário
status_list = api.GetUserTimeline(screen_name='RosieDaSerenata')
print_status(status_list=status_list)

# Faz uma busca por termos
status_list = api.GetSearch(term="Operação Serenata de Amor",
                            lang='pt',
                            count=50,
                            result_type='recent')
print_status(status_list=status_list)


# Faz uma busca em twittes que estão geoferenciados
status_list = api.GetSearch(geocode=(-27.231700, -52.023781, "2km"))
print_status(status_list=status_list)

# Atualiza o status
status = api.PostUpdate('Testing python-twitter!!')
print(status.text)
