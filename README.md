<h1>Desenvolvimento API Python Magic The Gathering!<h1>

URL Heroku: [https://api-python-mtg.herokuapp.com/docs ](https://api-python-mtg.herokuapp.com/docs)

# **Endpoints Cartas - Necessita primeiro a criação da lista cartas** Post: /api/v1/cartas -> {

“id”:int -> gerado automaticamente

“nome”: String

“idioma”: String

“foil”: Boolean

“preco”:Decimal

“cont\_cartas”: int

(número de cartas como uma característica) “listaCartaId”:int -> ID lista Cartas

}

Get: /api/v1/cartas -> Necessita do id da lista de cartas

Get-id: /api/v1/cartas -> Numero de id da carta

Delete: /api/v1/cartas -> Numero de id da carta

Put: /api/v1/cartas -> Numero de id da carta e o id da lista de cartas


# **Endpoints Lista Cartas** Post: /api/v1/lista-cartas -> {

“id”: int -> gerado automaticamente “nome”:string

}

Get: /api/v1/lista-cartas -> Lista todas a lista de cartas

Get-id: /api/v1/cartas -> Numero de id da lista carta Delete: /api/v1/cartas -> Numero de id da lista carta Put: /api/v1/cartas -> Numero de id da lista de cartas
