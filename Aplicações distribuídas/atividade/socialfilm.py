#!bin/python
from flask import Flask,jsonify,abort
from flask import make_response, request
import acesso_omdb


app = Flask(__name__)

reviews = [
    {
        'film_id': 'tt0076759',
        'user_id': 'marcos',
        'comment': 'gostei'
    },
    {
        'film_id': 'tt0076759',
        'user_id': 'lucio',
        'comment': 'achei legal'
    },
    {
        'film_id': 'tt1211837',
        'user_id': 'lucio',
        'comment': 'estranho'
    }
]

notas = [
    {
        'film_id': 'tt0076759',
        'user_id': 'marcos',
        'stars': 4
    },
    {
        'film_id': 'tt0076759',
        'user_id': 'lucio',
        'stars': 5
    },
    {
        'film_id': 'tt1211837',
        'user_id': 'lucio',
        'stars': 2
    }
]

'''
Primeira coisa:
    certifique-se que o arquivo atividade_hoje.py 
    e o arq
    uivo acesso_omdb.py estao na mesma pasta
    se nao, nao vai rodar
'''


'''
Você consegue abrir a pagina que geramos abaixo?

Mesmo dando problema com a firewall, voce deve conseguir vê-la em http://localhost:5000
'''
@app.route('/')
def index():
        return "Hello, World!"
'''
Vou deixar essa rota pronta pra vocês, para vocês poderem debugar mais facil

Ela imprime tudo que esta guardado no servidor
'''
@app.route('/socialfilm/all/', methods=['GET'])
def tudo():
    return jsonify({'reviews':reviews,'notas':notas})


'''
Ler reviews existentes
    ao acessar a URL /socialfilm/reviews/id_filme/id_usuario com o metodo GET,
    podemos ler a review do usuario para aquele filme
    
    Você pode percorrer o objeto "reviews" com um for. Se acontecer
    de algum elemento lá dentro ter film_id igual à passada na url
    e user_id igual ao passado na url, retorne o comentario.

    Caso contrario, retorne ("comentario nao encontrado",404)
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['GET'])
'''
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['GET'])
def get_review(film_id,user_id):
        cont = 0
        for review in reviews:
                filme = review.values()
                if film_id == review['film_id'] and user_id == review['user_id']:
                        cont += 1
                        comentario = review['comment']
                        return jsonify({'comentario':comentario})
        if cont == 0:
                return jsonify({'comentario nao encontrado':None}),404

'''
Adicionar um comentario:
    ao acessar a URL /socialfilm/reviews/id_filme/id_usuario com o metodo PUT, 
    podemos adicionar (ou trocar) a review do usuario.

    A (nova) review vem num objeto que vem no body do request

    Cuidado! Se o usuário já fez review daquele filme, troque, nao adicione outra

    Você pode percorrer o objeto "reviews" com um for. Se acontecer
    de algum elemento lá dentro ter film_id igual à passada na url
    e user_id igual ao passado na url, mude o comentario. 
    (isso é, mantenha o dicionário e altere apenas a chave "comment")

    Caso contrario, adicione.

    Retorne o objeto da review adicionada
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['PUT'])
'''
@app.route('/socialfilm/reviews/<film_id>/<user_id>', methods=['PUT'])
def put_review(film_id,user_id):
        comentario = request.json.get('comment','')
        for review in reviews :
                conteudo = review.values()
                if film_id == review['film_id'] and user_id == review['user_id']:
                        review['comment'] = comentario
                        return jsonify({'review alterada':review})

        novo = {
        'film_id': film_id,
        'user_id': user_id,
        'comment': comentario
        }
        reviews.append(novo)
        return jsonify({'review alterada': novo})
'''
Va ao arquivo acesso_omdb.py e crie a funcao existe_id

Depois, altere a funcao de adicionar reviews para dar um erro quando voce tentou fazer
uma review de um filme que nao existe no banco de dados

Para acessar a funcao, basta usar acesso_omdb.existe_id(sua_id)

Pergunta interessante: o retorno de existe_id está sendo 'True' (uma string)
ou True (um booleano)?
'''
#feito
'''
quando acessarmos a url /socialfilm/reviews/all_films/<user_id> com o metodo GET,
devemos receber todas as reviews feitas pelo usuario
'''
@app.route('/socialfilm/reviews/all_films/<user_id>', methods=['GET'])
def all_reviews(user_id):
  return 'ola3'

'''
Vamos adicionar o nome do filme na resposta anterior.

Antes de mais nada, va no acesso_omdb e defina a função pega_nome

Entao, use a função para adicionar um campo name no dicionario de cada filme 
retornado pela funcao anterior

Tome cuidado: nao queremos alternar os dados locais. 
Verifique que o vetor reviews nao esta recebendo esses nomes

Voce talvez queira aprender a copiar dicionarios em python
'''

'''
Agora, façamos a parte das estrelas:
    /socialfilm/stars/film_id/user_id deve poder receber GET (para lermos quantas 
    estrelas um usuário deu a um filme) e PUT (para um usuario alterar suas estrelas,
    ou avaliar um filme que nao avaliou ainda)

    No caso do PUT, envie no body um dicionario {"stars":num}, onde numero vai de 0 a 5.
    Retorne um erro 400 se o numero nao for válido ou se "stars" nao estiver definido
'''
@app.route('/socialfilm/stars/<film_id>/<user_id>', methods=['GET'])
def retorna_estrelas(film_id,user_id):
    return 'estrelas'

@app.route('/socialfilm/stars/<film_id>/<user_id>', methods=['PUT'])
def add_estrelas(film_id,user_id):
    return 'mais estrelas'

'''
Para vermos a média de estrelas de um filme, podemos acessar a URL
/socialfilm/stars/film_id/average com GET.

O retorno é um json: {"average_stars": num} onde num é a media
do numero de estrelas que os usuários deram para o filme,
ou 'nao avaliado' se nenhum usuário avaliou o filme ainda
'''
@app.route('/socialfilm/stars/<film_id>/average', methods=['GET'])
def retorna_media(film_id):
    return '12'

'''
Vamos implementar uma funcao de busca. Ela recebe uma string,
faz a busca no omdb, e nos retorna o nome e ano dos 10 primeiros 
filmes que batem com a busca (ou menos, se nao houver 10 filmes)

Ou seja: quando o usuário acessar /socialfilm/search (veja exemplo no Postman)
ele cria uma busca, que dispara uma funcao busca_filmes no acesso_omdb.

Essa funcao busca_filmes, no acesso_omdb, retorna uma lista de 10 filmes.

A nossa URL /socialfilm/search deve retornar a mesma lista, mas para
cada filme, apenas um dicionario com 'nome' e 'ano' do filme.

Note que já fizemos algo muito parecido na atividade do OMDB
'''

@app.route('/socialfilm/search', methods=['GET'])
def busca_filme():
        termo_busca = request.args.get('buscar', None)
        return termo_busca

'''
Trate erro da funcao de busca: se por acaso ela nao contiver o termo da busca, retorne
'busca mal formada' e o codigo 400
'''

'''
Adicione review a nossa funcao de busca.

Cada filme, além dos campos 'nome' e 'ano' deverá conter um campo 'review'.
Se temos uma review para o filme no sistema, colocamos (qualquer uma das reviews) no campo

Caso contrario, colocamos 'review indisponivel'
'''

'''
Adicione a media de estrelas a nossa funcao de buscas.

Cada filme, além dos campos 'nome', 'ano' e 'review' deverá conter um campo 'estrelas'.
Se temos avaliaçoes para o filme no sistema, colocamos a media no campo

Caso contrario, colocamos 'ainda nao foi avaliado'
'''

'''
DESAFIO

Ao acessarmos a URL /socialfilm/bestof/<int:ano>
devemos receber (usando o mesmo formato da busca por ID)
o melhor filme do ano (segundo as nossas stars)

Note que isso implica que teremos que descobrir o ano de alguns dos filmes que tiveram review.

Teste, em particular, o ano 1977 e o ano 2016
'''
@app.route('/socialfilm/bestof/<int:ano>', methods=['GET'])
def soma_url(ano):
        return '1977'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
