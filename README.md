# klchat

#### Plataforma de venda online, com interação em tempo real entre cliente e vendendor.

#
**Links**
api: https://klchat.herokuapp.com
[Documentação Projeto](https://andersonvaler.github.io/documentation-capstone/)

#
### End-Points

1. Signup
    - Cliente
    - Lojista
2. Login
3. Enderecos
4. Carrinho
5. Produto
6. Categoria
7. Vendas
8. Status

---
* ### Signup

Cadastro de cliente podendo ser Pessoa Fisica, Pessoa Juridica é Lojista (quem vai fornecer os produtos na plataforma).

**Clientes CPF**

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/signup`   |`Post`  |	`200 - 400`	|

**Body** - `json`
~~~
{
	"tipo_usuario": "cliente",
	"nome": "bruno",
	"email": "bruno@bruno.com",
	"senha": "bruno",
	"cpf": "29170528055",
	"telefone": "33111111111"
}
~~~
**Response** - `json`
~~~
{
	"nome": "bruno",
	"email": "bruno@bruno.com",
	"telefone": "33111111111",
	"endereco_id": null,
	"carrinho_id": 12,
	"cpf": "29170528055"
}
~~~
**Clientes CNPJ**

**Body** - `json`
~~~
{
	"tipo_usuario": "cliente",
	"nome": "Alfaiateria",
	"email": "alfaiate@luxo.com",
	"senha": "bruno",
	"cnpj": "92795487000164",
	"telefone": "33111111111"
}
~~~

**Response** - `json`
~~~
{
	"nome": "Alfaiateria",
	"email": "alfaiate@luxo.com",
	"telefone": "33111111111",
	"endereco_id": null,
	"carrinho_id": 12,
	"cnpj": "92795487000164"
}
~~~

**Lojista**

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/signup`   |`Post`  |	`200 - 400`	|


**Body** - `json`
~~~
{
	"tipo_usuario": "lojista",
	"nome": "ca",
	"email": "caaa@gmail.com",
	"senha": "1234",
	"cnpj": "38019816000130",
	"telefone": "11112111111"
}
~~~

**Response** - `json`
~~~
{
	"id": 16,
	"nome": "ca",
	"email": "caaa@gmail.com",
	"cnpj": "38019816000130",
	"telefone": "11112111111",
	"endereco_id": null
}
~~~

---

* ### Login
Gera um token de acesso.

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/login`   |`Post`	  |	`200 - 400`	|

**Body** - `json`
~~~
{
	"email": "bruno@bruno.com",
	"senha": "bruno"
}
~~~
**Response** - `json`
~~~
{
  	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjcxNjU4NiwianRpIjoiMWNmZDYwNGItNDk5ZC00MzgwLTk2YWEtNTgxMjdmNmY0OTFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImJydW5vQGJydW5vLmNvbSIsIm5iZiI6MTYyNjcxNjU4Nn0.y3kzn5DZOeh1b2rvEs2uHVf72uj0ZJ39ooNaaGWnr8U"
}
~~~
---

* ### Enderecos
Cadastrar um endereço serve para Cliente e Lojista.

- Cadastro de endereço

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/perfil`   |`Post`|	`200 - 400`	|


*Authorization*
~~~
Bearer:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjcxNjU4NiwianRpIjoiMWNmZDYwNGItNDk5ZC00MzgwLTk2YWEtNTgxMjdmNmY0OTFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImJydW5vQGJydW5vLmNvbSIsIm5iZiI6MTYyNjcxNjU4Nn0.y3kzn5DZOeh1b2rvEs2uHVf72uj0ZJ39ooNaaGWnr8U
~~~

**Body** - `json`

~~~
{
	"logradouro": "Rua das palmeiras",
	"numero": 100,
	"bairro": "Teste",
	"cidade": "Briocholandia",
	"estado": "RS",
	"cep": "35000000"
}
~~~

**Response** - `json`

~~~
{
	"endereco": "cadastrado"
}
~~~

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/perfil` |`Get` | `200 - 400` |

**Response** - `json`

~~~
{
	"id": 11,
	"logradouro": "Rua Das Palmeiras",
	"numero": "100",
	"complemento": null,
	"bairro": "Teste",
	"cidade": "Briocholandia",
	"estado": "RS",
	"cep": "35000000"
}
~~~

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/perfil`| `Put`| `200 - 400` |

**Body** - `json`

~~~
{
  	"logradouro": "",
	"numero": 6,
	"bairro": "",
	"cidade": "",
	"estado": "",
	"cep": ""
}
~~~

**Response** - `json`

~~~
{
	"endereco": "Atualizado"
}
~~~
---

* ### Carinho
Gerenciamento de produtos de um carrinho.

- Finalizar o Carrinho

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/finalizar-carrinho`   |`Get`	  |	`200 - 400`	|

*Authorization*
~~~
Bearer:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjcxNjU4NiwianRpIjoiMWNmZDYwNGItNDk5ZC00MzgwLTk2YWEtNTgxMjdmNmY0OTFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImJydW5vQGJydW5vLmNvbSIsIm5iZiI6MTYyNjcxNjU4Nn0.y3kzn5DZOeh1b2rvEs2uHVf72uj0ZJ39ooNaaGWnr8U
~~~

**Response** - `json`

~~~
{
  "id": 15,
  "valor_total": 0.0,
  "nota_fiscal": null,
  "cupom_id": 0,
  "data_venda": "Tue, 20 Jul 2021 00:00:00 GMT",
  "status_id": 2,
  "endereco_entrega_id": 13,
  "carrinho_id": 73
}
~~~
- Esvaziar o carrinho

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/carrinho`   |`Delete`	  |	`204 - 400`	|

**Response** - `status`
~~~
200
~~~
- Deleta um produto do carrinho


|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/carrinho/id`   |`Delete`	  |	`200 - 400`	|

**Response** - `status`
~~~
200
~~~

- Deleta um produto do carrinho

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/carrinho/id`   |`Patch`	  |	`200 - 400`	|

**Response** - `status`
~~~
200
~~~

- Inserir produto no carrinho

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/carrinho`   |`Post`	  |	`200 - 400`	|

**Body** - `json`

~~~
{
	"produto_id": 1
}
~~~

**Response** - `json`

~~~
{
  "msg": "Produto inserido"
}
~~~

- Ver produtos do carrinho

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/carrinho`   |`Get`	  |	`200 - 400`	|

**Response** - `json`

~~~
{
  "carrinho_id": 73,
  "produtos": []
}

{
  "carrinho_id": 73,
  "produtos": [
    {
      "id": 1,
      "descricao": "Mesinha",
      "marca": "Granejeira",
      "quantidade": 1.0,
      "valor_unitario": 0.0,
      "lojista_id": 1
    }
  ]
}
~~~

---

* ### Produto
Cadastro de produto associado ao lojista.

- Buscar produto

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/produto`   |`Post`	  |	`200 - 400`	|

*Obs: `?` concatenar rota com parametros.*
Ex: `/produto?lojista_id=3`

*Obs: `&` concatenar entre um parametros e outro.*
Ex: `/produto?marca=Philips&lojista_id=3`

**Body** - `Param`
~~~
	marca=Phillips
	descricao=led
	modelo=40
	valor_max=100
	valor_min=1000
	lojista_id=3
~~~

**Response** - `json`

~~~
[
  {
    "id": 6,
    "modelo": "tv_40_led",
    "descricao": "Tv led 40 polegadas",
    "marca": "Philips",
    "qtd_estoque": 10.0,
    "valor_unitario": 1200.0,
    "categoria_id": 1,
    "lojista_id": 3
  },
  {
    "id": 7,
    "modelo": "tv_50_led",
    "descricao": "Tv led 50 polegadas",
    "marca": "Philips",
    "qtd_estoque": 10.0,
    "valor_unitario": 1200.0,
    "categoria_id": 1,
    "lojista_id": 3
  }
]
~~~

- Cadastrar produto

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/produto/id`   |`Post`	  |	`200 - 400`	|

**Body** - `json`

~~~
~~~

**Response** - `json`

~~~
~~~


- Editar produto

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/produto/id`   |`Post`	  |	`200 - 400`	|

**Body** - `json`

~~~
{
	"descricao": "Nova descricao"
}
~~~

**Response** - `json`

~~~
{

}
~~~
---

* ### Vendas
Gera um o inicio de uma venda e altera o status o status do carrinho para finalizado.

- Ver vendas



|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/vendas-andamento`   |`Get`	  |	`200 - 400`	|

*Authorization*
~~~
Bearer:
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjcxNjU4NiwianRpIjoiMWNmZDYwNGItNDk5ZC00MzgwLTk2YWEtNTgxMjdmNmY0OTFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImJydW5vQGJydW5vLmNvbSIsIm5iZiI6MTYyNjcxNjU4Nn0.y3kzn5DZOeh1b2rvEs2uHVf72uj0ZJ39ooNaaGWnr8U
~~~

**Response** - `json`

~~~
~~~

- Ver vendas

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/vendas/id`   |`Get`	  |	`200 - 400`	|

**Response** - `json`

~~~
~~~

- Cancelar venda

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/vendas/id/cancelar`   |`get`	  |	`200 - 400`	|


**Response** - `json`

~~~
~~~

- Despachar produto

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/vendas/id/despachar`   |`get`	  |	`200 - 400`	|


**Response** - `json`

~~~
~~~

- Aprovar venda

|url       | metodo   | status  |
|:---------: |:---------: |:---------:|
|`/vendas/id/aprovar`   |`get`	  |	`200 - 400`	|


**Response** - `json`

~~~
~~~
