import sys

import dns.resolver

resolver = dns.resolver.Resolver()

try:
    alvo = sys.argv[1].strip()
    wordlist = sys.argv[2].strip()
except:
    print('Por favor, passe argumentos posicionais.')
    print('Usage: python3 dnsbrute.py {dominio_alvo} {nome_wordlist}')
    sys.exit()

subdominios = []
try:
    with open(wordlist, 'r') as arq:
        subdominios = arq.readlines()
        for num in range(len(subdominios)):
            subdominios[num] = subdominios[num].strip()

except Exception as e:
    print('Erro ao abrir "wordlist.txt" -', e)


def testar_subdominio(subdominio):
    print('Testando subdomínio -', subdominio)
    try:
        resultados = resolver.resolve(f'{subdominio}.{alvo}', 'A')
        for resultado in resultados:
            print('>>>', resultado)

    except Exception as e:
        print('Erro:', e)
    finally:

        print()


for subdominio in subdominios:
    testar_subdominio(subdominio)