const divisivelPorDois = (num, num2) => {
    if(num % num2 === 0){
        return "O número é par";
    }
    return "O numero é impar";
}
console.log(divisivelPorDois(2,2))