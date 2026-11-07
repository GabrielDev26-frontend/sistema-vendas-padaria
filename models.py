"""Modelos de dados (SQLAlchemy) e configuração do banco SQLite.

Stack conforme definido na Experiência Prática 2 (seção "Seleção das
tecnologias"): SQLite em modalidade local, integrado via SQLAlchemy.
"""
from __future__ import annotations

import os
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

# Permite trocar o banco em testes (ex: sqlite:///:memory:) sem mexer no código.
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///vendas.db")

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Venda(Base):
    """Entidade Venda (Experiência Prática 2 - Modelagem simplificada dos dados)."""

    __tablename__ = "vendas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    produto: Mapped[str] = mapped_column(String(120), nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    valor: Mapped[float] = mapped_column(Float, nullable=False)
    data_venda: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)


def init_db() -> None:
    """Cria as tabelas no banco, caso ainda não existam."""
    Base.metadata.create_all(engine)
