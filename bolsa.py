import urllib.request
import json

print("=== APP DA BOLSA DO TONY ===")

def buscar_preco(moeda):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=usd"
        with urllib.request.urlopen(url, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados[moeda]['usd']
    except:
        return 0

print("A tentar conectar...")
bitcoin = buscar_preco("bitcoin")
ethereum = buscar_preco("ethereum")

if bitcoin!= 0:
    print(f"Preco Bitcoin hoje: ${bitcoin}")
    print(f"Preco Ethereum hoje: ${ethereum}")
else:
    print("\n--- MODO SEM INTERNET (treino) ---")
    print("Bitcoin simulado: $65000")
    print("Ethereum simulado: $3500")
    bitcoin = 65000

print("\n--- TUA BARRACA ---")
entrada = float(input("Quanto entrou hoje? "))
saida = float(input("Quanto gastou hoje? "))
lucro = entrada - saida
print(f"Teu lucro hoje: {lucro} MT")

if lucro == 3750:
    print("Igual ontem! Bom!")
input("\nPressiona ENTER para fechar...")