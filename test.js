const assert = require('assert');
const { validarVenda } = require('./script.js');

assert.strictEqual(validarVenda('Pão', 2, 10), true);
assert.strictEqual(validarVenda('', 2, 10), false);
assert.strictEqual(validarVenda('Pão', 0, 10), false);
assert.strictEqual(validarVenda('Pão', 2, 0), false);

console.log('Todos os testes passaram!');
