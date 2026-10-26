---
layout: post
title: "Litoques: grabar, diseñar y publicar un disco en casa con la IA como compañera de taller"
date: 2026-10-26 10:00:00 +0100
categories: [casos-de-uso]
tags: [musica, guitarra, chatgpt, audacity, davinci-resolve, kling, emubands, produccion-musical]
description: "Cómo un guitarrista usó ChatGPT y herramientas digitales para resolver los problemas de sonido, imagen, vídeo y distribución de su disco, sin delegar la autoría."
image: /assets/img/litoques/cabecera.png
lang: es
---

<link rel="stylesheet" href="{{ '/assets/css/casos-ia.css' | relative_url }}">

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/cabecera.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/cabecera.svg' | relative_url }}" alt="Ilustración de una guitarra en un patio andaluz de noche, con farolillos y el título Litoques"></a>
</figure>

<p class="entradilla">Saber tocar la guitarra no es lo mismo que saber grabarla. Ni mezclarla, ni diseñar una portada, ni montar un vídeo, ni subir un álbum a las plataformas. Este es el caso de <strong>Litoques</strong>, un disco acústico que avanzó problema a problema con la inteligencia artificial como interlocutora técnica. La IA no hizo el disco. Ayudó a que su autor pudiera entender y resolver lo que, de otro modo, le habría obligado a llamar a media docena de especialistas.</p>

<div class="ficha" markdown="0">
  <div><strong>Proyecto</strong>Litoques, disco acústico</div>
  <div><strong>Autor</strong>Lito, guitarrista</div>
  <div><strong>Estilo</strong>Guitarra española y acústica, influencia flamenca</div>
  <div><strong>Asistente</strong>ChatGPT</div>
  <div><strong>Herramientas</strong>Audacity · DaVinci Resolve · Kling · EmuBands</div>
</div>

<div class="resultado" markdown="0">
  <span class="resultado-titulo">③ El resultado: escucha el disco</span>
  <p><strong>Litoques</strong>, de Lito, ya está publicado. Es el disco del que trata este caso.</p>
  <div class="botones">
    <a class="boton" href="https://open.spotify.com/album/58NEzKaxV9MBQJ0cqzJ5IH" target="_blank" rel="noopener">▶ Escuchar en Spotify</a>
    <a class="boton secundario" href="https://open.spotify.com/artist/35esiCfNa15JxyDhy94JuM" target="_blank" rel="noopener">Perfil de Lito</a>
  </div>
</div>

<div class="leyenda" markdown="0">
  Cómo leer este artículo: cada capítulo separa <strong style="color:#b5402a">① el problema</strong>, <strong style="color:#b7791f">② el proceso</strong> y <strong style="color:#2f7d4f">③ la solución</strong>. Además, las etiquetas distinguen
  <span class="etiqueta hecho">Hecho</span> lo que consta que se hizo,
  <span class="etiqueta propuesta">Propuesta</span> lo que se planteó o exploró como punto de partida, y
  <span class="etiqueta pendiente">Por verificar</span> lo que conviene confirmar.
</div>

## El punto de partida: muchas disciplinas, una sola persona

Imagina que llevas años tocando. Tienes composiciones propias, piezas con aire de taranto, alguna nana, temas de cantautor. Un día decides que ya está bien de que vivan solo en tus dedos: quieres un disco. Y descubres que «hacer un disco» son en realidad seis trabajos distintos.

Hay que **grabar** sin que la habitación se coma el sonido. Hay que **mezclar** para que la guitarra suene cercana y no embarrada. Hay que **masterizar** para que las canciones convivan a un volumen parecido. Hace falta una **portada** que no parezca una foto de móvil con un texto encima. Para mostrar la música en redes hacen falta **vídeos**. Y al final, hay que **distribuir**: metadatos, identificadores, distribuidores y perfiles de artista.

Lito no partía de cero. Tiene experiencia técnica y se mueve con soltura entre herramientas digitales. Pero no era ingeniero de sonido, ni diseñador, ni editor de vídeo, ni conocía por dentro la distribución musical. La pregunta que da sentido a este artículo es sencilla:

> ¿Puede una persona usar la IA para cubrir parte de esas necesidades sin un estudio profesional y sin contratar a un especialista para cada tarea?

Litoques es una respuesta práctica, con sus aciertos, sus límites y su letra pequeña.

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/mapa-del-caso.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/mapa-del-caso.svg' | relative_url }}" alt="Tabla visual con seis frentes del proyecto (sonido, álbum, archivos, imagen, vídeo y publicación) y, para cada uno, el problema, el proceso y la solución"></a>
  <figcaption>El mapa completo del caso. Cada fila es un capítulo de este artículo.</figcaption>
</figure>

<span class="capitulo-num">Capítulo 1</span>

## La idea y los obstáculos iniciales

Una interpretación puede tener todo el valor artístico del mundo y, aun así, sonar mal grabada. Los síntomas son conocidos para cualquiera que haya intentado grabar en casa: la guitarra suena apagada o demasiado brillante, los graves retumban, se cuela ruido de fondo, unas canciones suenan más fuerte que otras y, cuando se intenta corregir, aparece el efecto contrario: un sonido artificial por exceso de procesamiento.

<div class="bloque bloque-problema" markdown="1">
El autor sabía **qué sonido quería**, natural, cálido y cercano, pero no siempre sabía **qué parámetro tocar** para conseguirlo. Buscar tutoriales genéricos daba respuestas pensadas para otras guitarras, otras habitaciones y otros micrófonos.
</div>

<div class="bloque bloque-proceso" markdown="1">
En lugar de buscar a ciegas, Lito empezó a **describir su problema** en una conversación con ChatGPT: qué buscaba, qué datos tenía de la grabación y qué no le convencía. La IA respondía con causas probables y propuestas que se podían comprobar.

<div class="reparto" markdown="1">
<div markdown="1">
**🤖 La IA**
Traducía frases como «quiero que la guitarra suene más clara y cercana» en hipótesis técnicas concretas.
</div>
<div markdown="1">
**🎸 El músico**
Aportaba el contexto, aplicaba los cambios y decidía con el oído si el resultado le convencía.
</div>
</div>
</div>

<div class="bloque bloque-solucion" markdown="1">
Un **método**: convertir una necesidad subjetiva en experimentos ordenados. Esta forma de trabajar se repitió después en todos los frentes del disco.
</div>

<span class="capitulo-num">Capítulo 2</span>

## Grabar una guitarra en casa

El equipo con el que se trabajó o que se contempló durante el proyecto incluye un **Boss RC-500** como parte de la configuración de guitarra, micrófonos externos como un **RØDE M3** y un micrófono **Maono** en distintas configuraciones, y una interfaz **Maono PS22 Lite**. Conviene aclararlo: no fue una única cadena de grabación fija. La configuración cambió según la etapa y la necesidad.

<div class="bloque bloque-problema" markdown="1">
¿Dónde se pone el micrófono para que la guitarra suene natural? Demasiado cerca, la guitarra retumba. Demasiado lejos, entra la habitación y el ruido. Y cada guitarra, cada micro y cada cuarto se comportan distinto.
</div>

<div class="bloque bloque-proceso" markdown="1">
La IA explicó los fundamentos: cómo la distancia afecta a la presencia, al ambiente y al ruido, para qué sirve un filtro de graves y por qué conviene comparar grabaciones cambiando **un solo factor cada vez**. A partir de ahí se definieron unas referencias de colocación:

- <span class="etiqueta propuesta">Propuesta</span> Micrófono a unos **20–25 cm del traste 12**, ligeramente orientado hacia la boca de la guitarra.
- <span class="etiqueta propuesta">Propuesta</span> Filtro de graves en torno a **80 Hz**, solo cuando hiciera falta controlar vibraciones o retumbes.

<div class="reparto" markdown="1">
<div markdown="1">
**🤖 La IA**
Explicaba conceptos, proponía posiciones de partida y diseñaba pruebas comparativas sencillas.
</div>
<div markdown="1">
**🎸 El músico**
Colocaba el micrófono, tocaba, grababa y escuchaba las diferencias.
</div>
</div>
</div>

<div class="bloque bloque-solucion" markdown="1">
Un **asesor técnico disponible en cualquier momento** que explica el porqué de cada ajuste y propone experimentos. No sustituye la escucha crítica, pero evita empezar a ciegas.
</div>

<div class="bloque bloque-rigor" markdown="1">
Las distancias y frecuencias de este capítulo son **puntos de partida**, no reglas universales. La colocación definitiva depende de la guitarra, la habitación, el micrófono y la forma de tocar.
</div>

<span class="capitulo-num">Capítulo 3</span>

## Entender un problema de sonido a partir de datos reales

El ejemplo más ilustrativo del proyecto es **«Faroles»**. En una etapa del proceso, la medición daba una sonoridad aproximada de **−15,4 LUFS**. Es una cifra razonable. Pero la misma pista tenía **picos que llegaban a 0 dBFS**, el techo absoluto de la señal digital.

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/faroles-diagnostico.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/faroles-diagnostico.svg' | relative_url }}" alt="Diagrama con dos paneles: a la izquierda, la sonoridad media de −15,4 LUFS frente a picos de 0 dBFS; a la derecha, las bandas de frecuencia que se propuso revisar"></a>
  <figcaption>La media era correcta; los picos, no. Y la ecualización se planteó como hipótesis que había que escuchar.</figcaption>
</figure>

<div class="bloque bloque-problema" markdown="1">
Una canción puede tener una **sonoridad media correcta** y, al mismo tiempo, **picos que no dejan margen**. A simple vista, los dos datos parecen contradecirse. En la práctica, apuntan a dos problemas distintos que se resuelven de forma diferente.
</div>

<div class="bloque bloque-proceso" markdown="1">
La IA ayudó a relacionar los síntomas con causas posibles y propuso un plan de trabajo para **esa grabación concreta**:

1. <span class="etiqueta propuesta">Propuesta</span> Atenuar graves innecesarios por debajo de unos **75–80 Hz**.
2. <span class="etiqueta propuesta">Propuesta</span> Investigar acumulaciones de energía en torno a **180–280 Hz**, la zona donde suele aparecer el «barro».
3. <span class="etiqueta propuesta">Propuesta</span> Valorar un realce suave de presencia alrededor de **3,5–4,5 kHz** para recuperar claridad en las cuerdas.
4. <span class="etiqueta propuesta">Propuesta</span> Aplicar **compresión moderada**.
5. <span class="etiqueta propuesta">Propuesta</span> Usar un **limitador** con techo cercano a **−1 dBFS**.
6. **Medir de nuevo después de cada cambio.**
</div>

<div class="bloque bloque-solucion" markdown="1">
La IA convirtió un problema técnico confuso en un **proceso de experimentación ordenado**: una lista de hipótesis que se comprueban una a una, escuchando y midiendo.
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Cuando hables con una IA sobre un problema técnico, **dale datos**. «Suena raro» da respuestas genéricas. «Tengo −15,4 LUFS de media y picos a 0 dBFS» permite un diagnóstico.
</div>

<span class="capitulo-num">Capítulo 4</span>

## Mezclar y preparar las canciones en Audacity

La herramienta principal de edición y procesamiento fue **Audacity**, en una de las etapas documentadas en su versión 3.7.8. Allí se abordaron la ecualización, la compresión, el control de picos, la normalización de sonoridad, la reducción de ruido, la exportación a WAV y la comprobación final.

<div class="bloque bloque-problema" markdown="1">
Audacity tiene decenas de efectos y cada uno, varios parámetros. Sin saber qué hace cada uno ni en qué orden aplicarlos, es fácil acabar con una guitarra aplastada, con artefactos o sin vida.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/cadena-audio.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/cadena-audio.svg' | relative_url }}" alt="Cadena de cinco pasos: ecualización correctiva, compresión moderada con sus parámetros, ajuste de sonoridad, limitación de picos y exportación con escucha, con un bucle de vuelta atrás"></a>
  <figcaption>Una de las cadenas de procesamiento exploradas en el proyecto. Es un punto de partida, no una receta.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
La IA ayudó a **interpretar parámetros y ordenar el flujo de trabajo**. Para la compresión, por ejemplo, se exploró esta configuración:

<div class="tabla-scroll" markdown="1">

| Parámetro | Valor explorado | Qué controla |
|---|---|---|
| Umbral | −18 dB | A partir de qué nivel empieza a actuar |
| Proporción | 2:1 | Con cuánta fuerza reduce lo que supera el umbral |
| Ataque | 25 ms | Lo rápido que reacciona; deja pasar el golpe de la púa |
| Recuperación | 150 ms | Lo rápido que deja de actuar |

</div>

Como referencias de trabajo para determinadas mezclas se manejaron una sonoridad cercana a **−15 LUFS** y un **techo de pico de −1 dBFS**. <span class="etiqueta hecho">Hecho</span> Una decisión del proyecto fue **dejar la reducción de ruido para el final** de la cadena de procesamiento.
</div>

<div class="bloque bloque-solucion" markdown="1">
Lo más valioso no fueron los números, sino **entender qué hace cada parámetro, qué artefactos puede producir y por qué conviene cambiar una sola cosa cada vez**. Con ese conocimiento, cada ajuste dejaba de ser una apuesta.
</div>

<div class="bloque bloque-rigor" markdown="1">
Los valores −15 LUFS y −1 dBFS fueron **referencias del proyecto**, no requisitos universales. Tampoco garantizan que una plataforma reproduzca todas las canciones a ese volumen. El orden de la cadena depende del material y de las herramientas.
</div>

<span class="capitulo-num">Capítulo 5</span>

## Coherencia entre canciones diferentes, sin uniformarlas

Litoques no es una grabación, sino un conjunto de piezas con atmósferas muy distintas. Estas son algunas de las intenciones con las que el autor describía sus temas:

<div class="tabla-scroll" markdown="1">

| Tema | Intención o referencia del autor |
|---|---|
| «Faroles» | Amplitud y ambiente de escenario |
| «Cuento» | Cálido y onírico, cercano a una nana |
| «Caminando» | Resonancia dulce y sensación de espacio |
| «Marinera» | Un pub irlandés de madrugada |
| «Flora» | Carácter íntimo, con referencias al taranto |
| «Me ofrezco» | Sensibilidad de cantautor |
| «Misterio» | Un resultado que se consideraba especialmente conseguido |
| «Otoño», «Púa», «De patas», «Galicia» | Entre los temas que figuraban como finalizados |

</div>

<div class="bloque bloque-problema" markdown="1">
¿Cómo consigues que un disco suene **a disco** sin que todas las canciones suenen **iguales**? Y, sobre todo, ¿cómo mantienes los mismos criterios cuando trabajas en sesiones separadas por días o semanas?
</div>

<div class="bloque bloque-proceso" markdown="1">
La identidad sonora se fijó en unos criterios comunes: conservar el **ataque y el detalle de las cuerdas**, la **dinámica** de la interpretación, la **resonancia natural**, la **calidez** y la **cercanía**, y evitar tanto la reverberación excesiva como los graves embarrados.

Una conversación continuada con la IA permitía volver a esos criterios en cada sesión, comparar objetivos entre temas y no empezar de cero cada vez. Las descripciones de cada pieza eran **intenciones artísticas del autor**: no todas las canciones recibieron el mismo tratamiento técnico.
</div>

<div class="bloque bloque-solucion" markdown="1">
**Coherencia sin uniformidad.** La IA ayudaba a poner palabras a las sensaciones y a traducirlas en decisiones comprobables. Pero era el músico quien decidía qué sonido le emocionaba y qué toma había que conservar por su valor expresivo.
</div>

<span class="capitulo-num">Capítulo 6</span>

## Crear una identidad visual sin ser diseñador

Un disco necesita una cara. La dirección artística de Litoques buscaba una atmósfera **cálida y cinematográfica, inspirada en una taberna o un patio andaluz**, con el guitarrista como figura central y los nombres «Litoques» y «Lito» integrados en la portada.

<div class="bloque bloque-problema" markdown="1">
Sin formación en diseño, era difícil pasar de una idea («un patio andaluz de noche, luz cálida») a una imagen que **comunicara la personalidad del álbum** y que, además, **sirviera técnicamente** como portada y como recurso para cada plataforma.
</div>

<div class="bloque bloque-proceso" markdown="1">
La IA ayudó a traducir la idea en descripciones visuales detalladas y a explorar ambientes, iluminación, composición y encuadre. También se probaron <span class="etiqueta hecho">Hecho</span> transformaciones artísticas de fotografías: **carboncillo**, **pintura de pinceladas a dos colores** y **estética de fotografía antigua**.

Después llegó la parte menos visible: preparar cada imagen para su destino.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/destinos-visuales.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/destinos-visuales.svg' | relative_url }}" alt="Diagrama: la dirección artística alimenta tres destinos con proporciones distintas: portada cuadrada, fondo visual de 2660 por 1140 píxeles y vídeos"></a>
  <figcaption>Generar la imagen y procesar el archivo son dos trabajos distintos.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
Un flujo en dos capas. La **IA generativa** crea o transforma el contenido visual. Las **herramientas convencionales** recortan, redimensionan, convierten y comprueban medidas. ChatGPT ayudaba a interpretar especificaciones, calcular proporciones y planificar las exportaciones.
</div>

<div class="bloque bloque-rigor" markdown="1">
Una imagen generada no garantiza que los textos estén bien escritos, que el encuadre cumpla los requisitos de una plataforma ni que el archivo tenga las dimensiones correctas. Para un fondo visual de Spotify se trabajó con una **referencia de 2660 × 1140 píxeles** <span class="etiqueta pendiente">Por verificar</span>; las medidas definitivas deben comprobarse siempre en la especificación vigente del servicio.
</div>

<span class="capitulo-num">Capítulo 7</span>

## Vídeos para un disco instrumental

Publicar en plataformas de audio no basta. Un proyecto independiente necesita imágenes y vídeos que permitan **mostrar la música** a quien todavía no la conoce. Y rodar un videoclip profesional por tema no era una opción realista.

<div class="bloque bloque-problema" markdown="1">
¿Cómo produces piezas audiovisuales con una estética coherente para un disco sin letra y sin presupuesto para rodajes?
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta propuesta">Plan</span> Se planteó aprovechar un conjunto de **unas 30 imágenes procedentes de un libro de poemas** y convertirlas en recursos para vídeos asociados a las canciones. El flujo audiovisual contemplaba dos herramientas con papeles muy distintos:

<div class="reparto" markdown="1">
<div markdown="1">
**✨ Kling Standard (IA generativa)**
Crear movimiento o variaciones a partir de imágenes y referencias, cuando las funciones y condiciones de uso lo permitan.
</div>
<div markdown="1">
**🎬 DaVinci Resolve Free 21 (edición)**
Montar, sincronizar con la música, ajustar duraciones, añadir títulos y transiciones, corregir y exportar.
</div>
</div>

La metodología propuesta sigue ocho pasos: elegir la canción, seleccionar imágenes acordes con su atmósfera, definir una dirección visual, generar o preparar los recursos, montar, sincronizar con la música, revisar errores y transiciones, y exportar y comprobar.
</div>

<div class="bloque bloque-solucion" markdown="1">
Una **estrategia híbrida**: IA donde aporta creatividad (movimiento, variaciones, transformaciones difíciles de hacer a mano) y software tradicional donde aporta control (cortar, sincronizar, titular, exportar). Muchas tareas, como recortar una imagen, unir clips o añadir subtítulos, son más rápidas y previsibles con una herramienta convencional.
</div>

<div class="bloque bloque-rigor" markdown="1">
Este capítulo describe un **flujo planificado y desarrollado por fases**. No todas las imágenes del libro se han convertido necesariamente en vídeos terminados, ni todas las etapas se automatizaron.
</div>

<span class="capitulo-num">Capítulo 8</span>

## Publicar el disco en plataformas digitales

Terminar las canciones no es terminar el disco. Faltaba la parte menos creativa y más desconocida: archivos de entrega, títulos, nombre de artista, metadatos, identificadores y requisitos del distribuidor.

<div class="bloque bloque-problema" markdown="1">
El primer intento de distribución topó con un obstáculo práctico: **dificultades con CD Baby, entre ellas un problema de acceso relacionado con Cloudflare**. Y, además, todo el vocabulario de la distribución musical resultaba nuevo.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/camino-publicacion.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/camino-publicacion.svg' | relative_url }}" alt="Camino de publicación en cuatro pasos: material, metadatos con el UPC, distribuidor (CD Baby con problema de acceso y EmuBands como alternativa) y presencia en plataformas"></a>
  <figcaption>El tramo administrativo, donde la IA no genera nada pero ayuda a entenderlo todo.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
Aquí la IA no generó contenido. Hizo algo igual de útil: **ayudar a investigar alternativas, comparar distribuidores y entender el procedimiento**. Ayudó a explicar qué es cada pieza (distribuidor, plataforma de escucha, perfil de artista, canal oficial), a ordenar metadatos y a preparar listas de comprobación.

- <span class="etiqueta hecho">Hecho</span> El lanzamiento tiene asociado el **UPC 5063930086686**.
- <span class="etiqueta propuesta">Contemplado</span> Distribución mediante **EmuBands** como alternativa.
- <span class="etiqueta hecho">Hecho</span> Se trabajó en la presencia del artista: la gestión de un **perfil generado automáticamente** y la solicitud de un **Official Artist Channel**.
</div>

<div class="bloque bloque-solucion" markdown="1">
Un camino claro donde antes había un muro. La IA no resolvió el problema de Cloudflare, pero sí ayudó a **encontrar y evaluar alternativas** en lugar de quedarse bloqueado.
</div>

<div class="bloque bloque-rigor" markdown="1">
La IA no garantiza la aprobación de ninguna solicitud ni sustituye las validaciones del distribuidor o de la plataforma. Identificadores y estado de publicación se comprueban siempre en las fuentes oficiales.
</div>

<span class="capitulo-num">Capítulo 9</span>

## Organizar el trabajo y documentar decisiones

Un disco genera una montaña de archivos: tomas originales, mezclas, pruebas, versiones corregidas y exportaciones finales. En el historial del proyecto aparecen nombres como **«Faroles2(6)»** o **«17 vivir tranquilo(3).wav»**, que distinguen versiones sucesivas.

<div class="bloque bloque-problema" markdown="1">
Cuando se mezclan archivos antiguos y nuevos, o se pierde la relación entre una recomendación técnica y **el archivo exacto al que se refería**, los errores se multiplican. Y las conversaciones con una IA no son una base de datos fiable.
</div>

<div class="bloque bloque-proceso" markdown="1">
La solución fue documental. A medida que crecían las canciones, las decisiones y las herramientas, se reunió todo en una **«biblia del disco»**: concepto artístico, criterios de sonido, procedimientos, estado de cada canción, versiones finales y pendientes, identidad visual, vídeos, distribución, organización de archivos y una lista de comprobación antes de publicar.

La IA puede ayudar a **resumir, estructurar y relacionar** información dispersa, y a proponer estructuras de carpetas, convenciones de nombres, registros de decisiones y resúmenes de continuidad entre sesiones.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/litoques/ciclo-de-trabajo.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/litoques/ciclo-de-trabajo.svg' | relative_url }}" alt="Ciclo de seis pasos: detectar, describir, proponer, ejecutar, escuchar y documentar, indicando qué parte hace la persona y qué parte la IA"></a>
  <figcaption>El método que se repitió en sonido, imagen, vídeo y publicación. Documentar cierra el ciclo.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
La IA resulta mucho más útil **dentro de un sistema de organización fiable**. La biblia evita depender de la memoria o de conversaciones dispersas y funciona como un profesor particular con apuntes: cada problema resuelto queda escrito para la próxima vez.
</div>

<div class="bloque bloque-rigor" markdown="1">
Los resúmenes pueden omitir detalles o mezclar decisiones confirmadas con recomendaciones provisionales. Por eso, **los archivos finales y las decisiones verificadas mandan sobre cualquier resumen**.
</div>

<span class="capitulo-num">Capítulo 10</span>

## Qué hizo la IA y qué siguió haciendo el humano

Este reparto es **funcional y orientativo**. Describe el tipo de aportación de cada parte, no una lista cerrada de herramientas usadas en cada fase.

<div class="tabla-scroll" markdown="1">

| Área | 🤖 Aportación de la IA | 🎸 Aportación humana |
|---|---|---|
| Grabación | Explicar conceptos y proponer configuraciones | Colocar el micrófono, tocar y escuchar |
| Diagnóstico de audio | Interpretar datos y sugerir causas posibles | Validar los problemas y comparar resultados |
| Mezcla | Recomendar parámetros y explicar efectos | Ajustar el audio y decidir qué sonido conservar |
| Masterización | Orientar sobre sonoridad, picos y exportación | Comprobar el resultado final |
| Organización | Proponer estructuras y listas de comprobación | Mantener los archivos y validar versiones |
| Identidad visual | Desarrollar conceptos y generar imágenes cuando corresponda | Definir el estilo y seleccionar resultados |
| Vídeos | Apoyar la generación de recursos y la planificación | Editar, sincronizar y revisar el montaje |
| Distribución | Explicar procesos y alternativas | Gestionar cuentas, metadatos y entregas |
| Decisiones artísticas | Explorar opciones y verbalizar intenciones | **Componer, interpretar y decidir** |
| Documentación | Resumir y estructurar información | Corregir, verificar y mantener la referencia oficial |

</div>

### Los límites que conviene tener presentes

- **La IA puede equivocarse.** Una recomendación técnica precisa en apariencia puede no funcionar en una grabación concreta.
- **Los parámetros no son universales.** Una ecualización buena para una guitarra puede estropear otra grabación.
- **La escucha manda.** Un número no decide por sí solo si una mezcla suena bien.
- **Lo generado requiere revisión.** Imágenes y vídeos pueden traer errores de composición, anatomía, continuidad o texto.
- **Las plataformas cambian.** Especificaciones, requisitos y funciones deben comprobarse en el momento de publicar.
- **Las conversaciones no son un archivo.** Hay que conservar archivos, decisiones confirmadas y versiones de referencia.
- **Sin participación, no hay resultado.** Cuanto mejor se describe el problema, más útil es la respuesta.
- **La IA no garantiza el éxito.** Ayudar a producir y publicar un disco no significa conseguir audiencia ni ingresos.

## Diez ideas para tu propio proyecto

<div class="bloque bloque-aprendizaje" markdown="1">
1. No necesitas dominar todas las disciplinas antes de empezar.
2. Pregunta por **problemas concretos**, no por soluciones generales.
3. Da **contexto y datos**, y describe el resultado que buscas.
4. Trata cada parámetro como una **hipótesis**: compruébala.
5. El **software convencional** sigue siendo imprescindible.
6. La IA puede ser tutor, asesor técnico, asistente creativo y organizador, todo en un mismo canal.
7. **Documenta**: una biblia del proyecto te ahorra repetir trabajo.
8. En el arte, el **criterio humano** pesa más que en ningún otro sitio.
9. Un flujo **híbrido** suele funcionar mejor que intentar automatizarlo todo.
10. El beneficio real es **ampliar lo que puedes hacer**, no dejar de participar.
</div>

## Conclusión: la IA como acceso, no como atajo

Litoques muestra que un proyecto musical personal necesita conocimientos de sonido, diseño, vídeo, organización y distribución, y que una misma herramienta conversacional puede ayudar a abordar muchos de esos frentes. Su mayor valor no fue sustituir a nadie ni automatizarlo todo. Fue **permitir que una persona entendiera mejor los problemas que iba encontrando** y tuviera ayuda para resolverlos, de uno en uno.

La IA no eliminó el esfuerzo, no garantizó la calidad y no tocó una sola nota. La composición, la interpretación, la elección de tomas y el criterio siguen siendo de Lito. Pero convirtió un proyecto que habría resultado más caro, más lento o directamente inabordable en solitario en algo que se podía empezar.

Y quizá esa sea la lección: si tienes un proyecto personal guardado en un cajón porque «hacen falta demasiadas cosas que no sabes hacer», puede que ya no sea así.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">Escucha Litoques</span>
  <p>Este es el resultado de todo el proceso: guitarra, oído y criterio humano, con la IA como compañera de taller.</p>
  <iframe src="https://open.spotify.com/embed/album/58NEzKaxV9MBQJ0cqzJ5IH" height="352" loading="lazy" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" title="Litoques en Spotify"></iframe>
</div>
