"""Sistema de Vendas - Padaria 2 Corações.

Reescrita em Python (Flask + SQLAlchemy + SQLite) do protótipo original em
HTML/CSS/JavaScript puro, para alinhar o código com a stack definida na
Experiência Prática 2 (Python, Flask, SQLAlchemy, SQLite, Pytest).

Fluxo das 3 telas (igual ao planejado no protótipo):
  Tela 1 (menu)      -> GET  /
  Tela 2 (registro)  -> GET/POST /venda
  Tela 3 (resultado) -> GET  /resultado/<id>
"""
from __future__ import annotations

from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for

from models import Session, Venda, init_db


def validar_venda(produto, quantidade, valor) -> bool:
    """Valida os dados de uma venda antes de salvar.

    Mesmas regras do protótipo original (função `validarVenda` em
    script.js), agora validadas no servidor:
    - produto não pode ser vazio
    - quantidade deve ser maior ou igual a 1
    - valor deve ser maior que 0
    """
    try:
        quantidade_num = float(quantidade)
        valor_num = float(valor)
    except (TypeError, ValueError):
        return False

    produto_preenchido = bool(produto and str(produto).strip())
    return produto_preenchido and quantidade_num >= 1 and valor_num > 0


def create_app() -> Flask:
    app = Flask(__name__)
    init_db()

    @app.get("/")
    def menu():
        return render_template("index.html")

    @app.route("/venda", methods=["GET", "POST"])
    def venda():
        erro = None

        if request.method == "POST":
            produto = request.form.get("produto", "")
            quantidade = request.form.get("quantidade", "")
            valor = request.form.get("valor", "")

            if not validar_venda(produto, quantidade, valor):
                erro = "Preencha todos os campos corretamente."
            else:
                nova_venda = Venda(
                    produto=produto.strip(),
                    quantidade=int(float(quantidade)),
                    valor=float(valor),
                    data_venda=datetime.now(),
                )
                with Session() as session:
                    session.add(nova_venda)
                    session.commit()
                    session.refresh(nova_venda)
                return redirect(url_for("resultado", venda_id=nova_venda.id))

        return render_template("venda.html", erro=erro)

    @app.get("/resultado/<int:venda_id>")
    def resultado(venda_id: int):
        with Session() as session:
            venda_registrada = session.get(Venda, venda_id)

        if venda_registrada is None:
            return redirect(url_for("menu"))

        return render_template("resultado.html", venda=venda_registrada)

    @app.get("/produtos")
    def produtos():
        return render_template("em_desenvolvimento.html", area="Produtos")

    @app.get("/vendas")
    def consultar_vendas():
        return render_template("em_desenvolvimento.html", area="Consultar Vendas")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
