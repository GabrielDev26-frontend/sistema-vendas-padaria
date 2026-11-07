// Única coisa que ainda precisa rodar no navegador: o toggle visual de
// alto contraste. A validação da venda agora é feita no servidor (app.py).
function alternarContraste() {
    const ativo = document.body.classList.toggle('alto-contraste');

    document.querySelectorAll('#contraste').forEach((botao) => {
        botao.setAttribute('aria-pressed', ativo);
        botao.textContent = ativo
            ? 'Desativar alto contraste'
            : 'Ativar alto contraste';
    });
}
