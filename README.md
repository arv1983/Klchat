# klchat

#### Plataforma de venda online, com interação em tempo real entre cliente e vendendor

### End-Points

1. Signup
    1.1 Cliente
    1.2 Lojista
2. Login
3. Enderecos
4. Carrinho
5. Produto
6. Categoria
7. Vendas
8. Status

* ### Signup

Cadastro de cliente podendo ser Pessoa Fisica, Pessoa Juridica é Lojista (quem vai fornecer os produtos na plataforma).

**Clientes CPF**
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

**Clientes CNPJ**
~~~
{
	"tipo_usuario": "cliente",
	"nome": "bruno",
	"email": "bruno@bruno.com",
	"senha": "bruno",
	"cnpj": "90860559000184",
	"telefone": "33111111111"
}
~~~

* ### Login
Gera um token de acesso.

~~~
{
	"email": "bruno@bruno.com",
	"senha": "bruno"
}
~~~

* ### Enderecos
Cadastrar um endereço.

~~~
~~~

* ### Carinho
Armazena os produtos disponiveis em estoque para gerar uma venda.

~~~
~~~


* ### Produto
Cadastro de produto associado ao lojista.

~~~
{
	"descricao": "cacetinho de chocolate",
	"marca": "padaria A",
	"modelo": "brioche MG",
	"qtd_estoque": 100,
	"lojista_id": 1,
	"valor_unitario": 10.20
}
~~~


* ### Categorias
Categorais Produtos.


~~~
~~~


* ### Vendas
Gera um o inicio de uma venda e altera o status o status do carrinho para finalizado.


~~~
~~~


* ### Status
Situações da venda e do carrinho.

~~~
~~~
