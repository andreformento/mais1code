let saldoAtual = 10
function sacarDinheiro(quantidade, operacaoDeSaque, saqueComTaxa) {
  if (saldoAtual >= quantidade) {
    operacaoDeSaque(quantidade)
    return "voce ainda tem " + saldoAtual
  } else {
    saqueComTaxa(quantidade)
    return "voce nao tem saldo suficiente, mas sacou com taxa e o saldo é " + saldoAtual
  }
}
sacarDinheiro(
    30,
    (qtd) => { saldoAtual = saldoAtual - qtd },
    (qtd) => { saldoAtual = saldoAtual - (qtd * 1.1) }
)
