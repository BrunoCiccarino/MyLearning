object Aula02 {
  def main(args: Array[String]): Unit = {
    def functionRecebeAny(v: Any) = println("O valor recebido foi: " + v)
    functionRecebeAny("78634.d9")
    functionRecebeAny(888)
    val aByte: Byte = 38
    functionRecebeAny(aByte)
  }
}
