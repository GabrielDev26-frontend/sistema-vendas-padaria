function mostrarTela(tela) {
    document.getElementById('venda').hidden = tela !== 'venda';
}

function salvarVenda() {
    const produto = document.getElementById('produto').value.trim();
    const quantidade = Number(document.getElementById('quantidade').value);
    const valor = Number(document.getElementById('valor').value);

    if (!produto || quantidade < 1 || valor <= 0) {
        return false;
    }

    return true;
}
