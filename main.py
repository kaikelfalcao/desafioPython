import json,requests,os,tldextract
from bs4 import BeautifulSoup

print("Bem vindo ao sistema de redirecionamento de URLs ")

rm = input("Digite seu RM:")

with open('base_tdspy.json', 'r') as arquivo:
    conteudo = json.load(arquivo)
    
    lista_de_sites = []
    
    if rm not in conteudo:
        print("\nRegistro de Matricula não encontrado. Tente novamente!")
        exit()

    for obj in conteudo[rm]:
      url = ''.join(obj) 
      lista_de_sites.append(url) 

if not os.path.exists(rm):
    os.makedirs(rm)

print("Carregando Informações")
os.chdir(rm)

for site in lista_de_sites:
    
    response = None
    try:
        response = requests.get('https://' + site)
    except requests.exceptions.ConnectionError:
        print(f"Aconteceu um erro tentando acessar {site}. ")
        option = input("Deseja pular para o proximo site ? (s/n): ")
        if option == 'n':
            exit()
        continue
    else:
        
        
        domain = tldextract.extract(site).domain
        
        if domain == "":
            nome_do_site = "gov"
        else:
            nome_do_site = domain

        
        with open(f"{nome_do_site}.html", "w", encoding="utf-8") as f:
            f.write(str(BeautifulSoup(response.text, "html.parser")))


print(f"Obrigado por Usar nosso Sistema, a matricula utilizada foi {rm}")





