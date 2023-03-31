from flask import Flask, request, jsonify,render_template,Response
import openai
import json


API_KEY = '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'
openai.api_key = API_KEY
model = 'text-davinci-003'

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("MENTORMUN.html")


@app.route("/obtenerinfo_mentormun")
def obtenerinfo():
    return render_template("Obtener-info.html")


@app.route("/pp_mentormun")
def pp_mentormun():
    return render_template("PapelPosicion.html")


# La clase MentorMUN y sus métodos se mantienen igual que en el código original, pero se omiten aquí por brevedad



# Añade rutas similares para las otras funciones de la clase MentorMUN aquí
#Opción Obtener Info de tu Pais y la Comisión.
@app.route('/obtenerinfo_mentormun', methods=['POST'])
def input_getinfo_mentormun():
    pais = request.form.get('pais')
    tema = request.form.get('tema')
    Comision = request.form.get('Comision')

    
    '''data = request.get_json()
    pais = data.get('pais')
    tema = data.get('tema')
    Comision = data.get('Comision')'''

    envioinfo=(f"""Estoy participando en un Modelo de Naciones Unidas y 
    estaré representando a {pais} en la Comisión {Comision}.Necesito saber la relación 
    que guarda {pais} con el tema {tema} y también en el marco de la {Comision} 
    ¿Que acciones ha tomado dicho pais en este tema? ¿En la Comunidad Internacional? 
    ¿Dentro de la Comision que estamos simulando?¿Tratados que ha firmado, iniciativas 
    que ha defendido, acciones concretas que ha desplegado con datos estadisticos?
    Investigaciones academicas que ha realizado dicho pais o alguna entidad del gobierno.
      Se muy explicito con cada punto anterior por fa. Citame las fuentes en formato APA y trae correctamente
      los enlaces que estás consultando la info, que no sean erroneos.""")

    response= openai.Completion.create(
        prompt=envioinfo,
        model=model,
        max_tokens=3500,
        temperature=0.8,
            )
    respuesta = ''
    for result in response.choices:
        respuesta += result.text
    return jsonify({"respuesta": respuesta})



#Método Hacer Papel de Posición.
@app.route('/pp_mentormun', methods=['POST'])
def input_pp_mentormun():
    pais = request.form.get('pais')
    tema = request.form.get('tema')
    Comision = request.form.get('Comision')

    envioinfo=(f"""Estoy participando en un Modelo de Naciones Unidas 
    y estaré representando a {pais} con el tema {tema} en el/la {Comision}. 
    Ayudame a hacer un papel de posición para un Modelo de Naciones Unidas 
    donde lo narres desde la optica del pais y se componga de 3 partes: 
    Explica el tema general, luego explica lo que ha hecho dicho pais 
    con relación al tema  usando estadisticas relevantes, documentos legales internacionales, 
    iniciativas concretas de gobierno, y sobre todo busca 
    la vinculación de las iniciativas del pais con el trabajo 
    del/la {Comision} para ver como se han relacionado,entre otras 
    cosas que entiendas, luego genera ideas de posibles acciones que 
    se pueden hacer para mejorar la situación y que esten dentro de la 
    jurisdiccion de la Comision  y no te olvides de citar todas las fuentes 
    que usaste en APA.""")

    response= openai.Completion.create(
        prompt=envioinfo,
        model=model,
        max_tokens=3500,
        temperature=0.8,
            )
    respuesta = ''
    for result in response. choices:
            respuesta += result.text
    return jsonify({"respuesta":respuesta})



#Método Ideas Discurso.
@app.route('/discurso_mentormun', methods=['POST'])
def input_dis_mentormun():
    data = request.get_json()
    pais = data.get('pais')
    tema = data.get('tema')
    Comision = data.get('Comision')

    envioinfo=(f"""Estoy participando en un Modelo de Naciones Unidas. 
    Estaré representando a {pais}, simulando la/el {Comision} , y se 
    estará trabajando el tema {tema}. Ayudame a hacer un discurso 
    persuasivo donde lo narres desde la optica de {pais}, expliques 
    lo que ha hecho el pais que represento con relación al tema usando 
    estadisticas relevantes, documentos legales internacionales, iniciativas 
    concretas de gobierno, entre otras cosas que entiendas, luego genera ideas 
    de posibles acciones que se pueden hacer desde el país que represento o 
    desde la/el {Comision} para mejorar la situación. Hazlo superpersuasivo 
    dirigiendote a la Comision. Puedes incluir una frase de alguna persona que se relacione
    con lo que estas defendiendo en el discurso.Al final pon la bilbiografia que usaste en formato APA.""")

    response= openai.Completion.create(
        prompt=envioinfo,
        model=model,
        max_tokens=3500,
        temperature=0.8,
            )
    respuesta = ''
    for result in response. choices:
            respuesta += result.text
    return jsonify({"respuesta":respuesta})


#Método Resumen Posturas Paises
@app.route('/posturas_mentormun', methods=['POST'])
def input_posturas_mentormun():
    data = request.get_json()
    tema = data.get('tema')
    Comision = data.get('Comision')

    envioinfo=(f"""Estoy participando en un Modelo de Naciones 
    Unidas simulando la Comision : {Comision} con el tema: {tema}. 
    Hazme una lista atendiendo a los paises que conforman el/la {Comision} 
    de las principales posturas, acciones que han tomado con relación al 
    tema con estadisticas y números concretos, y señalame alguna postura 
    conflictiva que tenga algún país con relación a este tema. Al final 
    citame las fuentes en formato APA.""")

    response= openai.Completion.create(
        prompt=envioinfo,
        model=model,
        max_tokens=3500,
        temperature=0.8,
            )
    respuesta = ''
    for result in response. choices:
            respuesta += result.text
    return jsonify({"respuesta":respuesta})

#Método Ideas Innovadoras
@app.route('/ideasdebate_mentormun', methods=['POST'])
def input_ideasdebate_mentormun():
    data = request.get_json()
    pais= data.get('pais')
    tema = data.get('tema')
    Comision = data.get('Comision')

    envioinfo=(f"""Estoy participando en un Modelo de Naciones 
    Unidas simulando la Comision : {Comision} con el tema: {tema} 
    y el pais que represento es {pais} . Dame ideas innovadoras 
    que no se han abordado anteriormente y alcanzables que podamos 
    debatir relacionado al tema que te señalo aqui en dicha Comision 
    atendiendo al alcance juridico que la/el {Comision} tenga y atendiendo 
    a la experiencia que tenga {pais}""")

    response= openai.Completion.create(
        prompt=envioinfo,
        model=model,
        max_tokens=3500,
        temperature=0.8,
            )
    respuesta = ''
    for result in response. choices:
            respuesta += result.text
    return jsonify({"respuesta":respuesta})


if __name__ == '__main__':
    app.run(debug=True)




'''@app.route('/obtener_info', methods=['POST'])
def obtener_info():
    data = request.get_json()
    pais = data.get('pais')
    tema = data.get('tema')
    comision = data.get('comision')
    respuesta = mentor_mun.obtener_info(pais, tema, comision)
    return jsonify(respuesta)'''