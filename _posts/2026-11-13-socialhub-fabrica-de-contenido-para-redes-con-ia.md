---
layout: post
title: "SocialHub: una fábrica de contenido para redes, programada con IA en 19 días"
date: 2026-11-13 00:00:00 +0100
categories: [casos-de-uso]
tags: [redes-sociales, instagram, tiktok, automatizacion, claude, desarrollo]
description: "Cómo las promociones de un libro y un disco se convirtieron en una aplicación que planifica, produce, revisa y publica contenido, con Claude trabajando a través de un buzón en Google Drive. Y por qué aún no ha publicado nada."
image: /assets/img/socialhub/cabecera.png
lang: es
---

<link rel="stylesheet" href="{{ '/assets/css/casos-ia.css' | relative_url }}">

<figure class="post-figura">
  <img src="{{ '/assets/img/socialhub/cabecera.svg' | relative_url }}" alt="Ilustración de un anillo de seis estaciones (planificar, producir, revisar, programar, publicar y medir) alrededor de un sobre que hace de buzón, bajo el título SocialHub">
</figure>

<p class="entradilla">Promocionar un libro y un disco en redes es un trabajo de cada semana: decidir qué contar, preparar imágenes y vídeos, escribir textos, programarlos y mirar qué tal fue. <strong>SocialHub</strong> nació para convertir todo eso en un proceso automático, visible y repetible. En 19 días pasó de una especificación a una aplicación instalable con 48 cambios revisados y más de 400 pruebas. Este caso cuenta cómo se construyó con la IA, qué salió mal al usarla de verdad y algo poco habitual en estos relatos: <strong>todavía no ha publicado nada</strong>.</p>

<div class="resultado" markdown="0">
  <span class="resultado-titulo">③ El resultado: la aplicación</span>
  <p><strong>SocialHub</strong> es de código abierto y se instala en Windows o macOS. La versión 1.1.0 está publicada como versión previa.</p>
  <div class="botones">
    <a class="boton" href="https://github.com/rvillalba1983/socialhub-content-factory" target="_blank" rel="noopener">💻 Ver el proyecto</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/socialhub-content-factory/releases" target="_blank" rel="noopener">Instaladores</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/socialhub-content-factory/blob/main/docs/TUTORIAL.md" target="_blank" rel="noopener">Tutorial</a>
  </div>
</div>

<div class="leyenda" markdown="0">
  Cómo leer este artículo: cada capítulo separa <strong style="color:#b5402a">① el problema</strong>, <strong style="color:#b7791f">② el proceso</strong> y <strong style="color:#2f7d4f">③ la solución</strong>. Las etiquetas distinguen
  <span class="etiqueta hecho">Hecho</span> lo programado y probado,
  <span class="etiqueta propuesta">A medias</span> lo programado pero sin probar en real, y
  <span class="etiqueta pendiente">Pendiente</span> lo que falta.
</div>

<div class="ficha" markdown="0">
  <div><strong>Proyecto</strong>SocialHub, aplicación de escritorio</div>
  <div><strong>Para qué</strong>Promocionar El DeLito y Litoques en Instagram y TikTok</div>
  <div><strong>Asistente</strong>Claude (Opus, Sonnet y Haiku)</div>
  <div><strong>Tecnología</strong>Java · Spring Boot · PostgreSQL · React</div>
  <div><strong>Desarrollo</strong>24 oct – 12 nov 2026</div>
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/socialhub/mapa-del-caso.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/socialhub/mapa-del-caso.svg' | relative_url }}" alt="Tabla visual con cinco frentes del proyecto (punto de partida, Claude, publicar gratis, uso real y estado) y, para cada uno, el problema, el proceso y la solución"></a>
  <figcaption>El caso entero de un vistazo.</figcaption>
</figure>

<span class="capitulo-num">Capítulo 1</span>

## De las promociones a mano a una especificación

<div class="bloque bloque-problema" markdown="1">
Las promociones de [El DeLito](https://rvillalba1983.github.io/casos-ia/delito-libro-ilustrado-con-ia/) y [Litoques](https://rvillalba1983.github.io/casos-ia/litoques-un-disco-hecho-en-casa-con-ia/) ya funcionaban con ayuda de la IA, pero repartidas: Claude preparaba y programaba con tareas programadas, un script propio generaba las piezas y Raúl revisaba y pulsaba enviar. Cada promoción era un pequeño montaje distinto.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> El 24 de octubre llegó al proyecto una **especificación maestra**, con una nota clara: «usaremos todo lo aprendido» en esas promociones. El objetivo era una gestión de redes **automática, visible y repetible**, con la mínima intervención humana: primero con supervisión y después con más autonomía.

Al día siguiente la IA preparó **dos prototipos de interfaz**: uno estilo juego de estrategia en *pixel art*, con edificios, humo y llamas para los errores, y otro limpio y moderno. Raúl eligió el moderno y guardó el otro.
</div>

<div class="bloque bloque-solucion" markdown="1">
Un plan por **fases**, de la 0 a la 12, con la interfaz decidida y las reglas de las promociones como punto de partida.
</div>

<span class="capitulo-num">Capítulo 2</span>

## Claude no puede llamarse a sí mismo: el buzón

<div class="bloque bloque-problema" markdown="1">
Lo natural sería que la aplicación le pidiera cosas a Claude directamente. Pero **la API de Claude es de pago y no entra en la suscripción Claude Pro**. Y la regla del proyecto era clara: solo herramientas gratuitas.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> La solución fue un **buzón**: SocialHub deja sus encargos como archivos en una carpeta de Google Drive y recoge allí los resultados. Al otro lado, **dos tareas programadas de Claude** pasan a recoger las «cartas»: una en la nube, para propuestas, textos y revisiones, y otra con Chrome en el PC, para lo que exige navegar.

SocialHub nunca da por bueno lo que devuelve la IA: **valida cada resultado** y la IA no cambia estados por su cuenta.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/socialhub/buzon.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/socialhub/buzon.svg' | relative_url }}" alt="Esquema: SocialHub intercambia archivos cada 30 segundos con un buzón en Drive, que leen dos tareas de Claude; abajo, tres vías de publicación por orden: API de Instagram, Publer y Publora"></a>
  <figcaption>El buzón y las tres vías de publicación. Todas gratuitas.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
La IA trabaja para la aplicación sin que la aplicación tenga que pagarla. A cambio, el sistema depende de que el PC, Drive y las tareas de Claude estén en marcha.
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Cuando una pieza es cara o no está disponible, **cambia la forma de comunicarse** con ella. Una carpeta compartida y unas tareas programadas pueden sustituir a una API.
</div>

<span class="capitulo-num">Capítulo 3</span>

## Publicar gratis: tres vías y un plan C

<div class="bloque bloque-problema" markdown="1">
Cada servicio gratuito pone su límite. La API de Publer es de pago. Publer gratis admite 10 publicaciones programadas por cuenta y 3 cuentas. Publora gratis, 15 al mes, y sus estadísticas no sirven para Instagram ni TikTok. La API oficial de Instagram no programa: hay que publicar a la hora y con las imágenes en una dirección pública. Y la de TikTok, sin auditoría, solo publica en privado.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> En lugar de elegir una, SocialHub las ordena:

1. **API oficial de Instagram:** SocialHub publica él mismo a la hora, con las imágenes en una carpeta pública de Drive.
2. **Publer:** respaldo de Instagram y vía de TikTok. Claude la maneja con Chrome. SocialHub cuenta las 10 publicaciones, avisa de «Publer lleno» y ofrece pasar a la siguiente vía.
3. **Publora:** la reserva.
4. Si todo falla, deja un **LEEME** para publicar a mano.

El orden cambió tres veces durante el desarrollo. La API de Instagram, aparcada el 3 de noviembre, pasó a vía principal el 12, cuando se vio que podía ahorrar depender de Publer.
</div>

<div class="bloque bloque-solucion" markdown="1">
Ninguna publicación depende de un servicio de pago ni de una sola vía.
</div>

<div class="bloque bloque-rigor" markdown="1">
<span class="etiqueta propuesta">A medias</span> Las tres vías están programadas y probadas por partes, pero **ninguna ha hecho todavía una publicación real** de principio a fin. La clave y la cuota de Instagram (100 publicaciones cada 24 horas) están comprobadas con Meta.
</div>

<span class="capitulo-num">Capítulo 4</span>

## El recorrido de una publicación

<figure class="post-figura">
  <a href="{{ '/assets/img/socialhub/recorrido.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/socialhub/recorrido.svg' | relative_url }}" alt="Ciclo de ocho pasos: Claude propone, Raúl aprueba, Claude especifica, SocialHub genera las piezas, Claude escribe, Raúl programa, SocialHub publica y Claude mide"></a>
  <figcaption>La IA propone, SocialHub valida y Raúl aprueba.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
Cada publicación pasa por ocho pasos. Claude propone las de la semana y Raúl aprueba o rechaza cada una, con motivo. Con tres pendientes, SocialHub pide a Claude la especificación de las piezas y las **genera en el propio PC**: carruseles, historias, reels o clips. Claude escribe textos y hashtags, SocialHub hace sus comprobaciones y Claude una revisión de calidad. Raúl aprueba y programa, **siempre con 6 horas de margen como mínimo**. Después, SocialHub publica y, a los 7 días, Claude lee las métricas.

<div class="reparto" markdown="1">
<div markdown="1">
**⚙️ Lo automático**
*Cada 30 segundos*, intercambio con el buzón. *Cada minuto*, revisión de lo que hay que publicar. *Cada día*, copia de seguridad. *Cada semana*, propuestas y balance. Un encargo fallido se repite solo, hasta tres veces.
</div>
<div markdown="1">
**👤 Lo que sigue siendo de Raúl**
Aprobar cada propuesta y cada publicación, decidir el calendario y pegar las claves. Y una regla de oro: los versos de El DeLito, siempre literales.
</div>
</div>
</div>

<div class="bloque bloque-solucion" markdown="1">
Una publicación solo pasa a «Publicada» **con el enlace o el identificador de la red**. Nada se simula y las cifras que no se ven quedan como «sin dato».
</div>

<span class="capitulo-num">Capítulo 5</span>

## Construir con la IA: 13 fases en 19 días

<figure class="post-figura">
  <a href="{{ '/assets/img/socialhub/cronologia.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/socialhub/cronologia.svg' | relative_url }}" alt="Cronología del 24 de octubre al 12 de noviembre: especificación, prototipos, construcción, publicación, instalador, semana real y versión 1.1.0"></a>
  <figcaption>Del 24 de octubre al 12 de noviembre.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> El código lo escribió **Claude**, y cada fase empezaba igual: preguntas a Raúl, **de una en una y con la opción recomendada primero**. Raúl revisó la primera gran entrega y pidió 11 cambios técnicos, entre ellos una arquitectura más ordenada y una auditoría con una librería probada. Desde entonces él aprueba cada cambio antes de unirlo.

A mitad de camino cambió también la forma de trabajar: de una conversación larga se pasó a **una fase por conversación**, con subagentes de distintos modelos según la tarea. Haiku vigila las pruebas, Sonnet documenta y programa los pasos aprobados y Opus hace la revisión final. El motivo fue gastar menos.

<div class="reparto" markdown="1">
<div markdown="1">
**🤖 La IA**
Programó y documentó (235 de los 285 commits), investigó planes y límites de cada servicio con sus fuentes, preparó los instaladores y escribió el manual y un tutorial con capturas.
</div>
<div markdown="1">
**👤 La persona**
Escribió los requisitos, eligió la interfaz, respondió las preguntas de cada fase, revisó y unió los cambios, creó las cuentas y la app de Meta, puso las claves y probó la aplicación en su PC.
</div>
</div>
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/socialhub/cifras.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/socialhub/cifras.svg' | relative_url }}" alt="Seis cifras: 48 pull requests, 285 commits de los que 235 son de Claude, 417 pruebas automáticas, 13 fases, 26 migraciones y 0 publicaciones reales todavía"></a>
  <figcaption>Mucho construido y nada estrenado todavía: las dos cosas son ciertas.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
Una aplicación completa, con instaladores para Windows y macOS, 304 pruebas en el servidor y 113 en la interfaz, un manual y un tutorial para empezar de cero.
</div>

<span class="capitulo-num">Capítulo 6</span>

## Lo que solo destapó el uso real

Las pruebas automáticas pasaban. Al instalarlo en casa y usarlo una semana con Litoques aparecieron los fallos que de verdad enseñan.

<div class="tabla-scroll" markdown="1">

| Qué pasó | Por qué | Cómo se arregló |
|---|---|---|
| El primer instalador no arrancaba en el PC de casa | Faltaban bibliotecas que en GitHub sí estaban | SocialHub las lleva consigo |
| Dos clics seguidos rompieron la base de datos | La app arrancó dos veces y la segunda borró a medias | Bloqueo de un solo arranque |
| Un buen lote de 14 propuestas, descartado | Un lunes por medio cambió «la semana que viene» al leerlas | La semana se fija al crear el encargo |
| La tarea de Claude con Chrome se paró y nadie avisó | Llegó al límite de uso de Claude | SocialHub vigila a quien tiene que trabajar y avisa |
| La app estuvo cerrada dos días | Nadie la volvió a abrir | Un script que la mantiene abierta |
| Las publicaciones se movían una hora | La zona horaria | Se guarda en hora de España |

</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Los fallos más caros no estaban en el código: estaban en **el encaje con la vida real**. Un lunes, un doble clic, un límite de uso. Ninguna prueba automática los habría encontrado; una semana de uso sí.
</div>

## Límites que conviene tener presentes

- **Necesita el PC encendido**, con Drive, la app de Claude y Chrome abiertos. Si se apaga, publica con retraso al volver.
- **Depende de terceros:** Google Drive, Meta, Publer, Publora y las tareas de Claude, cada uno con sus planes y límites.
- **El límite de uso de Claude** ya paró una tarea una vez. Y el coste en tokens no se conoce, porque la suscripción no lo muestra.
- **Instaladores sin firmar:** Windows y macOS avisan al abrirlos.
- **No hace:** la API oficial de TikTok, YouTube ni métricas de cuenta como seguidores o clics.
- <span class="etiqueta pendiente">Pendiente</span> La primera publicación real, las pruebas funcionales completas de Raúl y conectar cada marca con sus cuentas.

## Cinco ideas para tu propio proyecto

<div class="bloque bloque-aprendizaje" markdown="1">
1. **Parte de lo que ya te funciona** a mano: sus reglas son la mejor especificación.
2. **Que la IA pregunte antes de construir**, de una en una y con una recomendación.
3. **No te fíes de lo que devuelve la IA:** valídalo en código antes de cambiar nada.
4. **Planes gratuitos, sí, pero en cadena:** cuando uno se llena, que entre el siguiente.
5. **Úsalo en serio cuanto antes.** Una semana real enseña lo que no enseñan cientos de pruebas.
</div>

## Conclusión

SocialHub es el caso más ambicioso del blog y también el más honesto con sus límites: una aplicación completa, construida casi entera por la IA en 19 días, que **aún no ha publicado ni una sola vez**. Lo que demuestra no es que la IA haga el trabajo de redes sola, sino algo más útil. Con reglas claras, una persona que decide y pruebas de verdad, se puede montar en semanas una herramienta que antes habría exigido un equipo. El estreno, la primera publicación con enlace real, queda para el próximo capítulo.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">Explora SocialHub</span>
  <p>Código abierto, con manual, tutorial e instaladores.</p>
  <div class="botones">
    <a class="boton" href="https://github.com/rvillalba1983/socialhub-content-factory" target="_blank" rel="noopener">💻 Ver el proyecto</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/socialhub-content-factory/blob/main/MANUAL.md" target="_blank" rel="noopener">Manual</a>
    <a class="boton secundario" href="https://www.instagram.com/litoques/" target="_blank" rel="noopener">@litoques</a>
  </div>
</div>
