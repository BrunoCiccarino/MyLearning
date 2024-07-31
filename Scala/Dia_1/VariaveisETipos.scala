import scala.io.StdIn.readLine

/*
* Código de exemplo de como declaro variaveis e quais são os tipos primitivos do scala.
* Também exemplifiquei como funciona a entrada de dados, para a entrada de dados é necessário a importação da biblioteca scala.io.StdIn.readLine
* Usar val ao invez de var é uma boa prática, assim como declarar o tipo da variavel ou do valor antes de atribuir o valor
* No scala variaveis são ideais quando são temporarias ou quando acumulam valores em loops
* Também podemos declarar valores e variaveis igual no python, sem declarar o tipo na variavel ou valor, igual no exemplo abaixo:
* val s = "String"
*/
object VariaveisETipos {

  def main(args: Array[String]): Unit = { // Unit significa void
    var X: Int = 23 // Uma váriavel mutável
    val nOme: String = "Bruno" // Uma valor que é imutável
    val atSymbol: Char = '@'
    val hEllo: String = "Hello"
    val wOrld: String = "World"
    val cOncat = hEllo + " " + wOrld // Exemplo de concatenação

    println(s"$cOncat")
    println(s"Olá, $nOme")
    var data = readLine("Digite sua data de nascimento: ").toString // Aqui eu uso a função readLine e faço um casting para string no toString
    println(s"Você nasceu no dia/mes/ano: $data")
  }
}
