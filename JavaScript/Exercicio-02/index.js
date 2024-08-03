
const vidaPersonagem = (dano, saude) => {
    if (dano - saude === 0){
        return 1;
    }
    return 0;
}

console.log(vidaPersonagem(100, 100));