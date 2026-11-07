# Sistema de Vendas – Padaria 2 Corações

## Sobre o projeto
Sistema simples para registrar vendas da Padaria 2 Corações. Reescrito em
Python para alinhar o código com a stack definida na Experiência Prática 2
do projeto (a versão anterior deste repositório era em HTML/CSS/JavaScript
puro, sem backend nem banco de dados).

## Tecnologias
- Python 3.12
- Flask (interface web)
- SQLAlchemy 2.x + SQLite (persistência dos dados)
- Pytest + pytest-cov (testes automatizados)

## Funcionalidades
- Menu inicial com acesso às funções principais.
- Registro de venda (produto, quantidade, valor), com validação no servidor.
- Tela de confirmação com os dados da venda registrada.
- Alternar alto contraste, para acessibilidade.
- "Produtos" e "Consultar Vendas" ainda em desenvolvimento (fora do escopo
  do MVP atual, assim como no protótipo original).

## Como rodar localmente
```bash
pip install -r requirements.txt
python app.py
```
Acesse http://127.0.0.1:5000 no navegador. O banco `vendas.db` é criado
automaticamente na primeira execução.

## Como rodar os testes
```bash
pytest --cov=. --cov-report=term-missing
```

## Deploy (Render)
A versão anterior usava GitHub Pages, que só serve arquivos estáticos e
**não roda Flask**. Esta versão já vem pronta para o Render (arquivos
`Procfile` e `render.yaml`):

1. Crie uma conta em https://render.com (dá pra entrar com a conta do GitHub).
2. "New +" → "Web Service" → selecione o repositório `sistema-vendas-padaria`.
3. O Render detecta o `render.yaml` automaticamente (build e start command
   já configurados). Plano "Free" é suficiente.
4. Clique em "Create Web Service" e aguarde o build.

O plano free "dorme" depois de um tempo sem acesso — a primeira requisição
depois disso demora uns 30-50s pra responder, o que é normal.

## Status
Em desenvolvimento.

## Autor
Gabriel Souza
