__Modelo de dados do Python__

__Métodos especiais / Dunder methods__

Por meio dos métodos especiais é possível realizar operações básicas em objetos como iterações, coleções, representação e formatação de strings, entre outros.

__Exemplo 1.1__

Esse exemplo representa uma sequência de cartas de baralho.

Foi utilizado collections.namedtuple para fazer a representação de uma classe de objetos com seus atributos, no caso "rank" e "suit".

A classe FrenchDeck traz os métodos especiais "getitem" e "len".

O primeiro método pode ser invocado após instanciar a classe e fizer a chamada pela função len()

deck = FrenchDeck()
len(deck)

O retorno será a devolução de um número que representa a quantidade de cartas.

Para obter uma posição específica de carta no baralho basta informar o indíce

deck[0] 

deck[-1] 

deck[:4] 

deck[5::10]


