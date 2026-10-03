import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="WT INVESTORS V2.0", page_icon="💰")
st.title("💰 WT INVESTORS V2.0 - Tony")
st.write("*** APP DA BOLSA DO TONY ***")

def buscar_preco(moeda):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={moeda}&vs_currencies=usd"
        with urllib.request.urlopen(url, timeout=10) as resposta:
            dados = json.loads(resposta.read().decode())
            return dados[moeda]['usd']
    except:
        return 0

st.write("A tentar conectar...")

bitcoin = buscar_preco("bitcoin")
ethereum = buscar_preco("ethereum")

col1, col2 = st.columns(2)
with col1:
    st.metric("Bitcoin BTC", f"${bitcoin}")
with col2:
    st.metric("Ethereum ETH", f"${ethereum}")

if bitcoin > 0:
    st.success(f"Conectado! BTC: ${bitcoin}")
else:
    st.error("Erro ao buscar preços. Tenta recarregar.")

st.write("---")
st.write("Feito por Wiltony em Matola")
