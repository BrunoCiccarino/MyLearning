function verificaNumero(numero) {
    if (numero < 0){
        return "O numero é negativo";
    } else if (numero > 0){
        return "O numero é positivo";
    }
    return "O numero é o zero";
}
console.log(verificaNumero(0));