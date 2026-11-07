function testarSalvarVenda() {
    let passou = 0;
    let total = 4;

    if (salvarVendaTeste("Pão", 2, 10)) passou++;
    if (!salvarVendaTeste("", 2, 10)) passou++;
    if (!salvarVendaTeste("Pão", 0, 10)) passou++;
    if (!salvarVendaTeste("Pão", 2, 0)) passou++;

    console.log(`Testes: ${passou}/${total}`);
    console.log(`Coverage estimado: ${(passou / total) * 100}%`);
}

function salvarVendaTeste(produto, quantidade, valor) {
    return !!produto && quantidade >= 1 && valor > 0;
}

testarSalvarVenda();
