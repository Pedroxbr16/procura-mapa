import os
import sqlite3
import streamlit as st
from PIL import Image
import time

# Definindo credenciais de login diretamente no código
USERNAME = "luluisland"  # Substitua pelo seu nome de usuário
PASSWORD = "KenayRespeitaOTimeDoBoss"    # Substitua pela sua senha

# Função para login
def login():
    st.title("Tela de Login")
    user = st.text_input("Usuário")
    pwd = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if user == USERNAME and pwd == PASSWORD:
            st.success("Login bem-sucedido!")
            # Armazenar a hora do login e gerar um token
            st.session_state["logged_in"] = True
            st.session_state["login_time"] = time.time()
            return True
        else:
            st.error("Usuário ou senha incorretos.")
            return False
    return False

# Banco de dados SQLite
conn = sqlite3.connect("mapas.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mapas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    descricao TEXT,
    imagem_path TEXT,
    imagem_miniatura_path TEXT,
    lado TEXT,
    terreno TEXT
)''')
conn.commit()

# Diretório para salvar as imagens
IMAGES_DIR = "mapas_salvos"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Função para adicionar mapa
def adicionar_mapa():
    st.header("Cadastro de Mapa")
    
    nome = st.text_input("Nome do Mapa")
    descricao = st.text_area("Descrição do Mapa")
    imagem = st.file_uploader("Envie a Imagem do Mapa (Grande)", type=["jpg", "jpeg", "png"])
    imagem_miniatura = st.file_uploader("Envie a Imagem de Miniatura", type=["jpg", "jpeg", "png"])
    lado = st.radio("Lado", ("Direito", "Esquerdo"))
    terreno = st.selectbox("Terreno", ("Areia", "Terra", "Areia Escura", "Pedra"))

    if st.button("Cadastrar"):
        if nome and imagem and imagem_miniatura:
            caminho = os.path.join(IMAGES_DIR, imagem.name)
            caminho_miniatura = os.path.join(IMAGES_DIR, imagem_miniatura.name)
            with open(caminho, "wb") as f:
                f.write(imagem.read())
            with open(caminho_miniatura, "wb") as f:
                f.write(imagem_miniatura.read())
            
            cursor.execute("INSERT INTO mapas (nome, descricao, imagem_path, imagem_miniatura_path, lado, terreno) VALUES (?, ?, ?, ?, ?, ?)", 
                           (nome, descricao, caminho, caminho_miniatura, lado, terreno))
            conn.commit()
            st.success(f"Mapa '{nome}' cadastrado com sucesso!")
        else:
            st.warning("Preencha todos os campos e envie as duas imagens.")

# Função para buscar e mostrar os mapas
def visualizar_mapas():
    st.header("Visualização de Mapas")

    # Filtros
    lado_filtro = st.sidebar.selectbox("Filtrar por Lado", ["Todos", "Direito", "Esquerdo"])
    terreno_filtro = st.sidebar.selectbox("Filtrar por Terreno", ["Todos", "Areia", "Terra", "Areia Escura", "Pedra"])
    
    query = "SELECT nome, descricao, imagem_path, imagem_miniatura_path, lado, terreno FROM mapas WHERE 1=1"
    params = []
    
    if lado_filtro != "Todos":
        query += " AND lado = ?"
        params.append(lado_filtro)
    if terreno_filtro != "Todos":
        query += " AND terreno = ?"
        params.append(terreno_filtro)

    cursor.execute(query, params)
    resultados = cursor.fetchall()

    # Variável para armazenar o mapa clicado
    mapa_selecionado = None

    # Exibir miniaturas na sidebar
    for nome, descricao, caminho, caminho_miniatura, lado, terreno in resultados:
        if st.sidebar.button(nome):
            mapa_selecionado = (nome, descricao, caminho, caminho_miniatura, lado, terreno)
        
        # Exibir miniatura na sidebar
        st.sidebar.image(Image.open(caminho_miniatura), width=100, use_column_width=True, caption=nome)
    
    # Verificar se uma miniatura foi selecionada
    if mapa_selecionado:
        nome, descricao, caminho, caminho_miniatura, lado, terreno = mapa_selecionado
        st.image(Image.open(caminho), width=600)
        st.subheader(nome)
        st.caption(descricao)
        st.write(f"Lado: {lado}")
        st.write(f"Terreno: {terreno}")
        st.markdown("---")

# Função principal para controlar a navegação
def main():
    # Verificar se o usuário está logado
    if "logged_in" in st.session_state and st.session_state["logged_in"]:
        # Se o usuário estiver logado, mostrar o menu com a opção "Adicionar Mapa"
        st.sidebar.title("Menu de Navegação")
        escolha = st.sidebar.radio("Escolha uma opção", ("Visualizar Mapas", "Adicionar Mapa"))

        if escolha == "Adicionar Mapa":
            adicionar_mapa()
        
        elif escolha == "Visualizar Mapas":
            visualizar_mapas()

    else:
        # Se não estiver logado, permitir o login e mostrar "Visualizar Mapas"
        st.sidebar.title("Menu de Navegação")
        escolha = st.sidebar.radio("Escolha uma opção", ("Login", "Visualizar Mapas"))
        
        if escolha == "Login":
            if login():
                st.sidebar.success("Você está logado!")
                # Após o login, permitir a navegação para "Adicionar Mapa" e "Visualizar Mapas"
                escolha = st.sidebar.radio("Escolha uma opção", ("Adicionar Mapa", "Visualizar Mapas"))
            else:
                st.stop()
        
        elif escolha == "Visualizar Mapas":
            visualizar_mapas()


# Rodar a aplicação
if __name__ == "__main__":
    main()
