def reglas_puntuacion(opcion):
    # pass
    punto = """
    El punto es el signo de puntuación que se utiliza para indicar el final de un enunciado, de un texto o de un párrafo. Los puntos tienen dos reglas principales que deben respetarse en cualquier tipo de texto o mensaje escrito:

    1. La letra inicial de la palabra que aparezca después del punto se escribe con mayúscula.

    2. Los puntos nunca son empleados después de un enunciado interrogativo o exclamativo.

    Un punto señala los límites entre las palabras, las oraciones y los enunciados con el objetivo de distribuir las ideas dentro de un párrafo. Esta organización de las ideas o de los argumentos que necesites expresar con el lenguaje escrito, dependerá de cómo estén relacionadas las ideas con el contenido general de un párrafo. Habrá algunas ideas que necesiten expresarse independientemente sin alterar el sentido general de un sólo párrafo; habrá, sin embargo, otras ideas que no presenten coherencia entre sí. Con el fin de organizar correctamente las ideas dentro de un texto, el punto se clasifica de la siguiente manera:
    """

    punto_seguido = """
    De manera formal podemos decir que el punto y seguido se escribe cuando, al final de una oración, le sigue una segunda sobre el mismo renglón. El uso principal de un punto y seguido es hacer una breve pausa entre dos ideas que desarrollan el contenido de un mismo tema. Recordemos que, un texto está formado por un número específico de párrafos, cada uno de estos párrafos es una unidad independiente dentro de la cual se busca exponer argumentos o información específica al lector. Si dos oraciones tienen relación con el mismo tipo de información de la cual se está tratando podemos utilizar el punto y seguido para separarlas.

    Observa el siguiente ejemplo de la utilización del punto y seguido en los textos periodísticos:

    Un estudio publicado en Nature Astronomy revela la existencia de una multitud de microcráteres que contienen en el fondo agua helada. Se les llama “trampas frías”. ¿De dónde viene esta agua? Probablemente de la caída de asteroides que chocaron contra la Luna hace miles de millones de años. Lo mismo que se cree que ha ocurrido con la Tierra. Las moléculas de agua expulsadas durante la caída de estos cuerpos habrían caído al fondo de estos cráteres, donde quedaron “atrapadas para siempre” por el frío, explica Francis Rocard, especialista en sistema solar del Centro Nacional de Estudios Espaciales (CNES).

    La Jornada
    """

    punto_aparte = """
    Para organizar las ideas dentro de un texto, utilizamos los párrafos. Ya hemos explicado anteriormente que los párrafos son unidades independientes entre sí, cada párrafo es utilizado para exponer puntos de vista, argumentos o información diferentes entre sí. La estructura de un texto nos exige que cada párrafo sea separado por espacios en blanco conocidos como sangrías. Sin embargo, este no es el único recurso ortográfico utilizado para separar dos párrafos; el punto y aparte es también necesario para distribuir los bloques de la información.

    Con palabras más claras podemos decir que, el punto y aparte nos permite abordar distintos tipos de contenido dentro un mismo texto. Los textos periodísticos son, de nueva cuenta, una fuente de ejemplos claros de la utilización del punto y aparte. La intención de un texto periodísticos es ofrecer información concreta sobre sucesos de la vida cotidiana. Para lograrlo, el autor de un texto periodístico necesita integrar diferentes ideas dentro de su misma publicación. Observa el siguiente ejemplo de la utilización del punto y aparte.

    Aswani, que vive en San Clemente, California, es una de las muchas personas que han experimentado algún tipo de interrupción en sus rutinas habituales de sueño desde que comenzó la pandemia en marzo. Para algunos, los cambios son sutiles: más inquietud o una peor calidad de sueño. Para otros, la nueva realidad es un infierno: una falta crónica de sueño suficiente o un insomnio total.

    Algunos expertos han llegado a apodar la tendencia actual como «coronasomnia», dijo Christina Pierpaoli Parker, becaria postdoctoral de psicología clínica y medicina conductual del sueño en la Universidad de Alabama en Birmingham.

    CNN
    """
    
    punto_final ="""
    El punto final es el signo de puntuación que deberás utilizar para concluir una narración, un ensayo o incluso un mensaje de texto pequeño. Su utilización dependerá de la intención comunicativa de tu texto. Si el texto que estás escribiendo tiene una dimensión mayor a la de un artículo, el punto final también te servirá para concluir una sección o un capítulo.

    El siguiente párrafo es un extracto de la entrevista realizada por el medio informativo ABC a la ganadora del premio nobel de literatura, Louise Glück. Hemos omitido toda la entrevista, agregando sólo la conclusión con la intención de que puedas observar en ella una manera eficaz de finalizar un texto informativo.

    Justo antes de terminar, el interlocutor sueco trató de llevar la conversación a los «acontecimientos» que ahora estamos viviendo, pero la Nobel prefirió no entrar en esa materia. «Oh, los acontecimientos… Eso es demasiado grande, y demasiado pronto, apenas son las siete de la mañana aquí… Los dos minutos se han acabado», remató, y se fue a por su café.

    ABC
    """


    if opcion == 1:
        return punto
    elif opcion == 2:
        return punto_seguido
    elif opcion == 3:
        return punto_aparte
    elif opcion == 4:
        return punto_final


def run():
    # pass


    menu = """
    Los signos de puntuación son marcas gráficas que ayudan a leer los textos escritos. Su función es separar las ideas de un texto para interpretar correctamente su contenido.

    Si las dudas sobre la utilización de los signos de puntuación te invaden con frecuencia a la hora de escribir, este programa te aclarará cuáles son las reglas de ortografía del punto, la coma, el punto y coma, los dos puntos y los puntos suspensivos.

    1 - El punto
    2 - Punto y seguido
    3 - Punto y aparte
    4 - Punto final
    """


    print(menu)
    seleccion = int(input("¿Qué signo de puntuación te causa duda?: "))
    print(reglas_puntuacion(seleccion))


if __name__ == "__main__":
    run()
