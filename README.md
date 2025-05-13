
# Procura Mapas - Grand Line Adventures

O **Procura Mapas** é um projeto desenvolvido para ajudar os jogadores do jogo **Grand Line Adventures** a encontrar mapas e pistas dentro do jogo, facilitando a busca por tesouros e outros objetivos. O sistema permite que os jogadores registrem mapas, visualizem os registros e filtrem por diferentes categorias, como "lado" e "terreno".

## Funcionalidades

- **Login de Usuário**: Protege o acesso às funções de cadastro de mapas.
- **Cadastro de Mapas**: Permite adicionar novos mapas, incluindo imagens e descrições.
- **Visualização de Mapas**: Exibe uma lista de mapas cadastrados, com filtros para lado e terreno.
- **Armazenamento Local**: Utiliza um banco de dados SQLite para armazenar as informações dos mapas.

## Tecnologias Utilizadas

- **Streamlit**: Framework utilizado para criar a interface web.
- **SQLite**: Banco de dados para armazenar as informações dos mapas.
- **Pillow**: Biblioteca para manipulação de imagens (usada para carregar as imagens dos mapas).

## Funcionalidades

### Login
A aplicação requer que o usuário faça login para cadastrar novos mapas. Após o login, o usuário pode visualizar e adicionar novos mapas.

### Adicionar Mapas
Após o login, os jogadores podem adicionar mapas à base de dados. Para cada mapa, é necessário fornecer:
- Nome do mapa
- Descrição do mapa
- Imagem do mapa (grande)
- Imagem miniatura
- Lado do mapa (ex: direito, esquerdo)
- Tipo de terreno (ex: areia, pedra, terra)

### Visualizar Mapas
O usuário pode visualizar todos os mapas cadastrados e aplicar filtros, como o lado (direito ou esquerdo) e o tipo de terreno (areia, pedra, terra).

## Como Rodar o Projeto

### Requisitos

- **Python 3.x**
- **Streamlit**: `pip install streamlit`
- **SQLite** (já incluso no Python)

### Passos para Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Pedroxbr16/procura-mapa.git
   cd procura-mapa
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo Streamlit:
   ```bash
   streamlit run app.py
   ```

4. O app estará disponível em `http://localhost:8501` ou no link fornecido pelo **Streamlit Sharing**.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto! Para isso, basta seguir os seguintes passos:

1. Fork este repositório.
2. Crie uma nova branch (`git checkout -b minha-nova-feature`).
3. Faça suas alterações e commit (`git commit -am 'Adicionando nova feature'`).
4. Envie suas alterações (`git push origin minha-nova-feature`).
5. Abra um Pull Request.



---

**Procura Mapas** é um projeto open-source e gratuito para ajudar a comunidade de **Grand Line Adventures** a tornar suas aventuras mais emocionantes!

---

### Notas

Este projeto ainda está em desenvolvimento e mais funcionalidades serão implementadas com o tempo, como a possibilidade de exportar dados de mapas e integração com plataformas de chat para compartilhar mapas com outros jogadores.
