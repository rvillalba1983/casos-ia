---
layout: post
title: "Radar de salas: un diario de música emergente que se mantiene con scripts e IA"
date: 2026-11-02 12:00:00 +0100
categories: [casos-de-uso]
tags: [musica-emergente, conciertos, github-pages, automatizacion, claude, spotify]
description: "Cómo una conversación para descubrir artistas con conciertos cerca acabó en una web semanal que se actualiza sola: qué hace la IA, qué hacen los scripts y qué sigue decidiendo una persona."
image: /assets/img/radar/cabecera.png
lang: es
---

<link rel="stylesheet" href="{{ '/assets/css/casos-ia.css' | relative_url }}">

<figure class="post-figura">
  <img src="{{ '/assets/img/radar/cabecera.svg' | relative_url }}" alt="Ilustración de una pantalla de radar centrada en Granada, con cinco puntos iluminados por el barrido y el título Radar de salas">
</figure>

<p class="entradilla">Hay mucha música buena tocando cada semana en bares, salas, festivales y fiestas de pueblo, y casi nunca te enteras a tiempo. <strong>Radar de salas</strong> empezó como una pregunta a la IA: «¿a quién podría ir a ver estos días?». Diez días después es un diario web que cada viernes publica cinco artistas emergentes con concierto cerca. Este caso cuenta cómo se llegó ahí y, sobre todo, cómo se repartió el trabajo entre la IA, unos scripts y una persona.</p>

<div class="resultado" markdown="0">
  <span class="resultado-titulo">③ El resultado: el diario</span>
  <p><strong>Radar de salas</strong> está publicado y se renueva cada viernes. Ya lleva tres entradas y 18 artistas.</p>
  <div class="botones">
    <a class="boton" href="https://rvillalba1983.github.io/musica-emergente/" target="_blank" rel="noopener">📡 Abrir Radar de salas</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/musica-emergente" target="_blank" rel="noopener">Ver el código</a>
  </div>
</div>

<div class="leyenda" markdown="0">
  Cómo leer este artículo: cada capítulo separa <strong style="color:#b5402a">① el problema</strong>, <strong style="color:#b7791f">② el proceso</strong> y <strong style="color:#2f7d4f">③ la solución</strong>. Las etiquetas distinguen
  <span class="etiqueta hecho">Hecho</span> lo que consta que se hizo,
  <span class="etiqueta propuesta">Propuesta</span> lo que se planteó, y
  <span class="etiqueta pendiente">Pendiente</span> lo que queda por decidir o comprobar.
</div>

<div class="ficha" markdown="0">
  <div><strong>Proyecto</strong>Radar de salas, diario web semanal</div>
  <div><strong>Qué publica</strong>Artistas emergentes con concierto cerca</div>
  <div><strong>Asistente</strong>Claude</div>
  <div><strong>Herramientas</strong>GitHub Pages · GitHub Actions · Spotify · YouTube</div>
  <div><strong>En marcha desde</strong>23 de octubre de 2026</div>
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/radar/mapa-del-caso.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/radar/mapa-del-caso.svg' | relative_url }}" alt="Tabla visual con cinco frentes del proyecto (descubrir, formato, criterio, datos y rutina) y, para cada uno, el problema, el proceso y la solución"></a>
  <figcaption>El caso entero de un vistazo. Cada fila se desarrolla más abajo.</figcaption>
</figure>

<span class="capitulo-num">Capítulo 1</span>

## Descubrir a quién ir a ver

<div class="bloque bloque-problema" markdown="1">
Los algoritmos de las plataformas tienden a recomendarte lo que ya conoces o lo que ya es grande. Y las agendas de conciertos están repartidas por webs de salas, ayuntamientos, festivales y asociaciones. Juntar las dos cosas, **música que te pueda gustar** y **que toque cerca en los próximos días**, es un trabajo de horas que nadie hace cada semana.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> El 23 de octubre empezó como una conversación: a partir de los gustos de Raúl en Spotify (canción de autor, rumba, flamenco y mestizaje, con debilidad por la guitarra flamenca y por lo que pasa en Granada), la IA propuso una primera tanda de cinco artistas. Ese mismo día se programó una tarea para repetirlo cada viernes.

<div class="reparto" markdown="1">
<div markdown="1">
**🤖 La IA**
Propuso artistas emergentes con un perfil parecido a esos gustos.
</div>
<div markdown="1">
**👤 La persona**
Definió sus gustos y qué significa «emergente», y decidió que merecía la pena hacerlo cada semana.
</div>
</div>
</div>

<div class="bloque bloque-solucion" markdown="1">
Un **recomendador semanal** que no depende de un algoritmo de plataforma, sino de unos criterios escritos por quien lo va a usar.
</div>

<span class="capitulo-num">Capítulo 2</span>

## De la charla a una web

<div class="bloque bloque-problema" markdown="1">
Las recomendaciones del chat no quedaban en un sitio fijo para consultarlas, compararlas o enseñárselas a alguien. Y sin un formato común, cada tanda salía distinta.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> El 25 de octubre se decidió el formato de **diario**: una entrada por semana, cinco artistas, y para cada uno su foto, sus redes y dos vídeos. Y una regla clave: solo entra quien tenga un concierto **entre 7 días antes y 15 días después** de la fecha de la entrada. La búsqueda se amplió a festivales, pueblos y asociaciones, no solo salas.

Ese mismo día la web quedó publicada en GitHub Pages con las entradas Nº 1 y Nº 2.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/radar/ventana.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/radar/ventana.svg' | relative_url }}" alt="Línea de tiempo con una ventana verde desde 7 días antes hasta 15 días después del día de la entrada; los conciertos dentro valen y los de fuera no"></a>
  <figcaption>La ventana de conciertos convierte «música que te puede gustar» en «música que puedes ir a ver».</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
Un **formato fijo** que la IA puede repetir semana tras semana sin reinventarlo. <span class="etiqueta hecho">Hecho</span> La Nº 1 se rehízo esa noche con el formato completo para que todas las entradas se vieran igual.
</div>

<div class="bloque bloque-rigor" markdown="1">
La Nº 1 es anterior a la regla de la ventana: sus cinco artistas no tienen por qué tener concierto en esas fechas. El repositorio y la activación de GitHub Pages se hicieron una vez desde el navegador, porque desde la IA no se podían crear repositorios públicos ni activar Pages.
</div>

<span class="capitulo-num">Capítulo 3</span>

## Un criterio escrito, no improvisado

<div class="bloque bloque-problema" markdown="1">
Una IA que escribe cada semana tiende a contar demasiado: por qué eligió a alguien, qué buscó, qué no encontró. Eso sirve para quien la usa, pero sobra en una web que lee otra gente. Y sin reglas, es fácil repetir artistas o colar a alguien que ya es conocido.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> Se fijaron las reglas por escrito:

- **La web es un diario neutro.** Nada sobre cómo se eligió, las búsquedas, los huecos ni los gustos de nadie. Las dudas van en privado.
- **Solo emergentes de verdad**, con concierto en la ventana, **sin repetir** y **sin artistas que el autor ya sigue**. Por esa regla se descartó, por ejemplo, a un artista que ya seguía.
- **Prioridad a Granada y Andalucía**, intentando incluir también Latinoamérica.
- **Todas las entradas con el mismo formato completo.**

Esas reglas se guardaron en una *skill* (unas instrucciones reutilizables para la IA) y en un archivo de instrucciones dentro del propio repositorio, para que cada viernes la IA empiece sabiendo qué hacer.
</div>

<div class="bloque bloque-solucion" markdown="1">
La IA deja de improvisar el criterio cada semana: **lo aplica**. Y la persona puede cambiarlo editando un texto, no repitiendo explicaciones en cada conversación.
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Si vas a pedirle algo a la IA más de dos veces, **escribe las reglas una vez y guárdalas** donde la IA las lea siempre. Es lo que más mejora la constancia de los resultados.
</div>

<span class="capitulo-num">Capítulo 4</span>

## Cuando los datos no se dejan leer

Una recomendación vale lo que valen sus datos: fechas correctas, el artista correcto y vídeos que funcionen. Aquí aparecieron los problemas más concretos del proyecto.

<div class="tabla-scroll" markdown="1">

| Problema | Cómo se resolvió |
|---|---|
| YouTube no se leía con la herramienta web normal de la IA | Se lee con scripts propios, en la nube y en GitHub |
| A veces YouTube daba la lista de vídeos con retraso | El refresco se lanza en GitHub, que la da al día |
| Artistas con el mismo nombre en Spotify | Se comprueba con la lista de temas de cada perfil |
| Instagram no se abre desde la nube | Solo se enlazan las cuentas que aparecen en el YouTube, la web o el Spotify del artista |
| Nombres con comillas o tildes mal leídos en las agendas | Corregido en los scripts |

</div>

<div class="bloque bloque-proceso" markdown="1">
Cada problema se trató igual: entender por qué fallaba, buscar una fuente que sí funcionara y, si la tarea era mecánica, **sacarla de la IA y pasarla a un script**.
</div>

<div class="bloque bloque-solucion" markdown="1">
Datos que se pueden comprobar sin depender de que una página «se deje» leer ese día, y sin usar el ordenador personal de nadie.
</div>

<span class="capitulo-num">Capítulo 5</span>

## Scripts para lo mecánico, IA para lo editorial

<div class="bloque bloque-problema" markdown="1">
Al principio, buena parte del trabajo pasaba por el ordenador del autor y por una única tarea de IA el viernes. Y el viernes 30 de octubre esa tarea **no llegó a ejecutarse**. Si todo depende de un solo paso, un fallo deja la semana sin entrada.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> El 2 de noviembre la Nº 3 se publicó a mano y se rediseñó la rutina: tres scripts en GitHub hacen lo que no necesita inteligencia, y la IA se queda con lo que sí.

<div class="reparto" markdown="1">
<div markdown="1">
**⚙️ Los scripts (GitHub)**
*Refrescar*, los miércoles: pone los 2 últimos vídeos de cada artista, añade fechas nuevas y repone fotos caídas.

*Recolectar*, los jueves por la tarde: lee las agendas de Granada, Sevilla y otras 17 provincias y deja una lista de candidatos.

*Revisar*, tras cada cambio: comprueba datos, repetidos, fotos y vídeos, y avisa por correo si algo falla.
</div>
<div markdown="1">
**🤖 La IA (viernes, 8:47)**
Parte de la lista de candidatos, elige cinco, comprueba si el autor ya los sigue, verifica sus datos, escribe los textos, revisa antes de publicar, publica, lanza el refresco y avisa.
</div>
</div>

Los scripts son prudentes con las webs que consultan: esperan de 6 a 10 segundos entre consultas a YouTube y de 3 a 5 con las agendas, y reintentan esperando cada vez más. Si YouTube los bloquea tres veces seguidas, **paran sin tocar los datos que ya había**.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/radar/semana.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/radar/semana.svg' | relative_url }}" alt="Ciclo semanal de siete pasos: refrescar y recolectar con scripts, elegir y escribir con IA, revisar con script, publicar y leer por parte de la persona"></a>
  <figcaption>Cada pieza hace solo lo que sabe hacer bien.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
<span class="etiqueta hecho">Hecho</span> Desde el 2 de noviembre el diario funciona **en la nube**, sin el ordenador del autor. En la primera prueba, el recolector dejó **120 candidatos** para el 6 de noviembre, el refresco encontró **vídeos nuevos de 4 artistas** y **3 fechas nuevas** de uno de ellos. Y si un viernes falla la IA, los scripts siguen manteniendo al día los datos de lo ya publicado.
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
No todo tiene que hacerlo la IA. Lo repetitivo y comprobable (leer agendas, actualizar vídeos, validar datos) es **más fiable y más barato con un script**. La IA rinde más donde hace falta criterio: elegir y contar.
</div>

<span class="capitulo-num">Capítulo 6</span>

## Lo que ya ha salido

<figure class="post-figura">
  <a href="{{ '/assets/img/radar/cronologia.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/radar/cronologia.svg' | relative_url }}" alt="Cronología del 23 de octubre al 2 de noviembre: chat, web, reglas, fallo de la tarea y paso a la nube"></a>
  <figcaption>Diez días: de una charla a un sistema.</figcaption>
</figure>

<div class="tabla-scroll" markdown="1">

| Entrada | Artistas | Algunos de ellos |
|---|---|---|
| Nº 3 · 2 nov | 5 | Miguel Company y Alfredo Robles en la JJ Taberna de Granada; Antonio de la Luz en el Festival Flamenco Joven de Huétor Tájar; Sara Sístole; la chilena Cancamusa, de gira por España |
| Nº 2 · 25 oct | 8 | Carmen y María, MAPA y Julián Heredia en la JJ Taberna; Juanito Campos y Cristian de Moret en Huétor Tájar; Calequi y Las Panteras en Murcia |
| Nº 1 · 23 oct | 5 | Riada, Gon Abril, Roura, Juan + Yerai y Carmesí |

</div>

<span class="etiqueta hecho">Hecho</span> En total, **18 artistas** en tres entradas, y **9** de ellos tocan en la provincia de Granada.

<span class="capitulo-num">Capítulo 7</span>

## Qué hizo la IA, qué hicieron los scripts y qué hace una persona

<div class="tabla-scroll" markdown="1">

| Tarea | 🤖 IA | ⚙️ Scripts | 👤 Persona |
|---|---|---|---|
| Definir gustos y criterio | Ayuda a escribirlo | — | **Decide** |
| Leer agendas y buscar candidatos | — | Cada jueves | — |
| Elegir a los cinco de la semana | Cada viernes | — | Revisa la entrada |
| Escribir los textos | Cada viernes | — | Marca el tono (diario neutro) |
| Vídeos, fechas y fotos al día | — | Cada miércoles | — |
| Comprobar datos y repetidos | Antes de publicar | Tras cada cambio | Atiende los avisos |
| Cambiar reglas o diseño | Lo aplica | — | **Lo pide** |

</div>

### Límites que conviene tener presentes

- **Las agendas cambian** y no todas están en internet: el radar ve lo que se publica, no todo lo que pasa.
- **Una tarea programada puede no ejecutarse.** Pasó el 30 de octubre. Por eso los datos se mantienen con scripts y conviene mirar que todo haya corrido.
- **Las webs se protegen de las consultas automáticas.** Los scripts esperan y reintentan, pero un bloqueo puede dejar una semana sin refresco.
- **«Emergente» es un criterio humano.** La IA lo aplica, pero hay casos dudosos que decide una persona.
- **No todo está resuelto:** <span class="etiqueta pendiente">Pendiente</span> decidir qué hacer con un artista de la Nº 1 que lleva años sin publicar y buscar foto para tres artistas sin perfil en Spotify.

## Cinco ideas para tu propio proyecto

<div class="bloque bloque-aprendizaje" markdown="1">
1. **Empieza en una conversación** y convierte en sistema solo lo que repites.
2. **Escribe las reglas** una vez y guárdalas donde la IA las lea siempre.
3. **Separa lo mecánico de lo editorial**: scripts para lo primero, IA para lo segundo.
4. **Diseña para el fallo**: si un paso no se ejecuta, el resto debe seguir en pie.
5. **Mantén el criterio en manos humanas**: qué publicar, qué tono y qué no se cuenta.
</div>

## Conclusión

Radar de salas no es un algoritmo que decide por ti qué escuchar. Es un **criterio personal convertido en rutina**: alguien dijo qué música le interesa, dónde y cuándo, y entre la IA y unos scripts se encargan de buscarla cada semana. La IA aporta lo que es difícil de automatizar (elegir y contarlo bien) y los scripts, lo que es fácil de automatizar pero pesado de hacer a mano. La persona se queda con lo importante: decidir qué es «emergente», qué se publica y qué no.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">Visita Radar de salas</span>
  <p>Cinco artistas emergentes con concierto cerca, cada viernes.</p>
  <div class="botones">
    <a class="boton" href="https://rvillalba1983.github.io/musica-emergente/" target="_blank" rel="noopener">📡 Abrir el diario</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/musica-emergente/actions" target="_blank" rel="noopener">Ver los scripts en marcha</a>
  </div>
</div>
