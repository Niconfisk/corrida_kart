# Sistema de Gestão de Corridas de Kart 🏎️

Bem-vindo ao **Sistema de Gestão de Corridas de Kart**, um projeto desenvolvido com o framework **Django** para gerenciar pilotos e corridas. Este sistema permite realizar operações completas de CRUD (Create, Read, Update, Delete) tanto para os pilotos quanto para as corridas.

## 🚀 Funcionalidades

- Gerenciamento de **Pilotos**:
    - Adicionar, listar, editar e excluir pilotos.
    - Informações do piloto: Nome, Idade, Equipe.
- Gerenciamento de **Corridas**:
    - Adicionar, listar, editar e excluir corridas.
    - Informações da corrida: Nome, Data, e Pilotos participantes.
- Página inicial com navegação intuitiva.

---

## 🛠️ Tecnologias Utilizadas

- **Python** (v3.12)
- **Django** (v5.1)
- Banco de dados SQLite (padrão do Django)

---

## 📂 Estrutura do Projeto

```
corrida_kart/
├── corrida/                # Aplicação principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── templates/          # Templates HTML
│   │   ├── piloto/         # Templates relacionados aos pilotos
│   │   ├── corrida/        # Templates relacionados às corridas
│   │   └── pagina_inicial.html  # Página inicial do sistema
│   ├── admin.py            # Registro no Django Admin
│   ├── models.py           # Definição dos modelos Piloto e Corrida
│   ├── views.py            # Views para as funcionalidades de CRUD
│   └── urls.py             # Rotas da aplicação
├── corrida_kart/           # Configurações do projeto Django
│   ├── settings.py         # Configurações globais
│   ├── urls.py             # Rotas do projeto
│   └── wsgi.py             # Arquivo WSGI para deploy
└── manage.py               # Utilitário de gerenciamento do Django
```

---

## ⚙️ Instalação e Configuração

### Pré-requisitos

Certifique-se de ter o **Python 3.12+** instalado em sua máquina.

### Passo a passo

1. Clone este repositório:
    
    ```bash
    git clone https://github.com/Niconfisk/corrida_kart.git
    ```
    
2. Acesse o diretório do projeto:
    
    ```bash
    cd corrida_kart
    ```
    
3. Crie um ambiente virtual:
    
    ```bash
    python -m venv .venv
    ```
    
4. Ative o ambiente virtual:
    - No Windows:
        
        ```bash
        .venv\Scripts\activate
        ```
        
    - No Linux/Mac:
        
        ```bash
        source .venv/bin/activate
        ```
        
5. Instale as dependências:
    
    ```bash
    pip install -r requirements.txt
    ```
    
6. Realize as migrações do banco de dados:
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    
7. Crie um superusuário para acessar o Django Admin:
    
    ```bash
    python manage.py createsuperuser
    ```
    
8. Inicie o servidor:
    
    ```bash
    python manage.py runserver
    ```
    
9. Acesse o sistema no navegador:
    - Página inicial: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    - Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 👤 Autor

Desenvolvido por [Niconfisk](https://github.com/Niconfisk).
