function encontraMaiorNumero(num1, num2, num3) {
    if (num1 > num2 && num1 > num3){
        return "O primeiro numero é maior";
    } else if (num3 < num2){
        return "O segundo numero é o maior";
    }
    return "O terceiro numero é o maior"
}
console.log(encontraMaiorNumero(1, 2, 3))