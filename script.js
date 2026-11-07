function mostrarTela(tela) {
    const venda = document.getElementById('venda');

    if (venda) {
        venda.hidden = tela !== 'venda';
    }
}

function validarVenda(produto, quantidade, valor) {
    return !!produto && quantidade >= 1 && valor > 0;
}

function salvarVenda() {
    const produto = document.getElementById('produto').value.trim();
    const quantidade = Number(document.getElementById('quantidade').value);
    const valor = Number(document.getElementById('valor').value);

    if (!validarVenda(produto, quantidade, valor)) {
        alert('Preencha todos os campos corretamente.');
        return false;
    }

    alert('Venda registrada com sucesso!');
    return true;
}

if (typeof module !== 'undefined') {
    module.exports = {
        mostrarTela,
        validarVenda,
        salvarVenda
    };
}
