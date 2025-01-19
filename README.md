# FlaskApp - Gerenciador de Cursos e Mais

Este é um aplicativo web desenvolvido em Flask que inclui funcionalidades como gerenciar cursos, exibir filmes populares, listar frutas favoritas e muito mais. O projeto utiliza um banco de dados SQLite para armazenar informações e apresenta uma interface interativa para os usuários.

## Funcionalidades

### Gestão de Cursos:
- Listar cursos com paginação.
- Adicionar, editar e remover cursos.
- Atributos dos cursos: Nome, Descrição e Carga Horária (CH).

### Listagem de Filmes:
- Filtrar filmes por categorias, como "Mais Populares", "Kids", "2010", "Drama", e "Tom Cruise".
- Exibir informações detalhadas dos filmes, incluindo título, descrição e nota média.

### Registro de Frutas:
- Adicionar e listar frutas favoritas.

### Diário do Professor:
- Registrar alunos e suas respectivas notas.
- Exibir registros com interface expansível.

## Configuração

### Pré-requisitos
- Python 3.7 ou superior.
- Biblioteca Flask.
- Biblioteca Flask-SQLAlchemy.

### Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual e instale as dependências:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```

3. Configure o banco de dados:

    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    ```

4. Execute o aplicativo:

    ```bash
    python app.py
    ```

## Estrutura do Projeto

- **app.py**: Arquivo principal que define as rotas e funcionalidades.
- **templates/**: Contém os arquivos HTML para renderização.
- **static/**: Arquivos estáticos como CSS e JS.
- **cursos.sqlite3**: Banco de dados SQLite para armazenar informações.

## Rotas Principais

- **/**: Página inicial com a lista de frutas.
- **/sobre**: Registro de alunos e notas.
- **/filmes/<categoria>**: Exibe filmes por categoria.
- **/cursos**: Lista os cursos disponíveis.
- **/cria_curso**: Formulário para adicionar um novo curso.
- **/<id>/atualiza_curso**: Atualiza as informações de um curso.
- **/<id>/remove_curso**: Remove um curso do banco de dados.

## Tecnologias Utilizadas

- **Backend**: Flask, Flask-SQLAlchemy.
- **Frontend**: Bootstrap.
- **Banco de Dados**: SQLite.
- **API Externa**: The Movie Database (TMDb) para informações de filmes.

## Contribuição
Sinta-se à vontade para enviar pull requests ou reportar problemas no repositório.

## Licença
Este projeto é licenciado sob a MIT License.
