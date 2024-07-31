# Um exercicio que eu fiz para o Livro Entendendo Algoritmos - Um Guia Ilustrado Para Programadores e Outros Curiosos 

x = 'Lucas'
nomes = ["Aaron", "Abigail", "Adam", "Adrian", "Aiden", "Alan", "Albert", "Alec", "Alexa", "Alexander", "Alexandra", "Alice", "Alicia", "Allan", "Amanda", "Amber", "Amy", "Andrea", "Andrew", "Angela", "Anita", "Ann", "Anna", "Anne", "Anthony", "April", "Arthur", "Ashley", "Aubrey", "Austin", "Barbara", "Barry", "Beatrice", "Benjamin", "Benny", "Bernard", "Beth", "Betty", "Beverly", "Bill", "Billy", "Blake", "Bob", "Bobby", "Brad", "Bradley", "Brandon", "Brenda", "Brent", "Brett", "Brian", "Brianna", "Brittany", "Bruce", "Bryan", "Caleb", "Cameron", "Carl", "Carla", "Carlos", "Carmen", "Carol", "Caroline", "Carolyn", "Cassandra", "Catherine", "Cathy", "Cecilia", "Cedric", "Chad", "Charles", "Charlie", "Charlotte", "Cheryl", "Chloe", "Chris", "Christina", "Christine", "Christopher", "Cindy", "Claire", "Clara", "Clarence", "Claude", "Claudia", "Clayton", "Clifford", "Clint", "Clinton", "Clyde", "Cody", "Colin", "Connie", "Connor", "Constance", "Corey", "Courtney", "Craig", "Crystal", "Curtis", "Cynthia", "Daisy", "Dana", "Daniel", "Danielle", "Danny", "Darlene", "Darrell", "Darren", "Dave", "David", "Dawn", "Dean", "Deanna", "Debbie", "Deborah", "Debra", "Denise", "Dennis", "Derek", "Derrick", "Diana", "Diane", "Dianne", "Dolores", "Dominic", "Don", "Donna", "Doris", "Dorothy", "Doug", "Douglas", "Duane", "Dustin", "Dwayne", "Dylan", "Earl", "Ed", "Eddie", "Edgar", "Edith", "Edmund", "Edward", "Edwin", "Elaine", "Eleanor", "Elena", "Eli", "Elias", "Elijah", "Elizabeth", "Ella", "Ellen", "Ellie", "Elmer", "Elsa", "Emily", "Emma", "Enrique", "Eric", "Erica", "Erik", "Erin", "Ernest", "Esther", "Ethan", "Eugene", "Eva", "Evan", "Evelyn", "Everett", "Faith", "Faye", "Felicia", "Felix", "Fiona", "Florence", "Floyd", "Frances", "Francis", "Frank", "Franklin", "Fred", "Frederick", "Gabriel", "Gail", "Gary", "Gavin", "Gene", "Geoffrey", "George", "Georgia", "Gerald", "Geraldine", "Gilbert", "Gina", "Glenn", "Gloria", "Grace", "Graham", "Greg", "Gregory", "Gretchen", "Guy", "Gwen", "Hailey", "Hannah", "Harold", "Harry", "Hayden", "Hazel", "Heather", "Heidi", "Helen", "Henry", "Herbert", "Herman", "Holly", "Howard", "Hugh", "Hunter", "Ian", "Irene", "Iris", "Irma", "Isaac", "Isabel", "Isabella", "Jack", "Jackie", "Jacob", "Jacqueline", "Jake", "James", "Jamie", "Jane", "Janet", "Janice", "Jared", "Jason", "Jean", "Jeff", "Jeffrey", "Jen", "Jenna", "Jennifer", "Jenny", "Jeremy", "Jerome", "Jerry", "Jesse", "Jessica", "Jill", "Jim", "Joan", "Joanne", "Jocelyn", "Joe", "Joel", "John", "Johnny", "Jon", "Jonathan", "Jordan", "Jorge", "Jose", "Joseph", "Joshua", "Joy", "Joyce", "Juan", "Judith", "Judy", "Julia", "Julian", "Julie", "June", "Justin", "Kaitlyn", "Karen", "Karl", "Katherine", "Kathleen", "Kathryn", "Kathy", "Katie", "Kay", "Keith", "Kelly", "Ken", "Kendra", "Kenneth", "Kenny", "Kent", "Kevin", "Kim", "Kimberly", "Kirk", "Kristen", "Kristin", "Kyle", "Lance", "Larry", "Laura", "Lauren", "Laverne", "Lawrence", "Leah", "Lee", "Leon", "Leonard", "Leroy", "Leslie", "Lester", "Lewis", "Liam", "Linda", "Lindsay", "Lisa", "Lloyd", "Logan", "Lois", "Lora", "Lorraine", "Louis", "Louise", "Lucas", "Lucille", "Lucy", "Luis", "Luke", "Lydia", "Lyle"]
low = 0
high = len(nomes) - 1

"""
A busca binária é uma maneira simples e rápida de encontrar um valor dentro de um array por eliminação
algoritmo funciona dividindo o arranjo no meio repetidamente e comparando o elemento no meio com o elemento procurado.
o low que eu declarei ali em cima é o valor mínimo e o high é o valor máximo, o x é o valor que eu quero encontrar dentro do array
"""

while low < high:
    mid = low + (high - low) / 2
    int_mid = int(mid)
    
    if nomes[int_mid] == x:
        print(int_mid)
        break
    elif x < nomes[int_mid]:
        high = int_mid
    else:
        low = int_mid + 1

