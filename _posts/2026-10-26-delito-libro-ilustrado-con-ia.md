---
layout: post
title: "DeLito: cómo la IA ayudó a convertir un cuaderno de emociones en un libro ilustrado listo para imprimir"
subtitle: "Personajes que no deben cambiar de cara, una cubierta que se mide en milésimas de pulgada y una campaña que no puede olvidar decir dónde se compra: un caso real, problema a problema."
date: 2026-10-26 12:00:00 +0100
categories: [casos-de-uso]
tags: [libro-ilustrado, autopublicacion, amazon-kdp, generacion-de-imagenes, instagram, preimpresion]
description: "Caso real: cómo se usó la IA para llevar DeLito, un libro ilustrado y participativo, de la idea a la impresión bajo demanda y la promoción en Instagram."
image: /assets/img/delito/cabecera.png
lang: es
---

<link rel="stylesheet" href="{{ '/assets/css/casos-ia.css' | relative_url }}">

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/cabecera.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/cabecera.svg' | relative_url }}" alt="Ilustración: una hoja de cuaderno con garabatos y un corazón, unida por un hilo rojo a una fotografía con dos figuras y un globo de diálogo, bajo el título DeLito"></a>
</figure>

<p class="subtitulo">Personajes que no deben cambiar de cara, una cubierta que se mide en milésimas de pulgada y una campaña que no puede olvidar decir dónde se compra: un caso real, problema a problema.</p>

Hay ideas que caben en una frase y proyectos que no caben en ninguna. **DeLito**, también llamado **El Delito**, es de los segundos. Empezó como un libro ilustrado, pero quien intenta describirlo acaba enumerando: es un poemario visual, un diario emocional, un confesionario, un juego visual, un mapa de amistades, una carta de amor y un objeto artístico en el que el lector también participa. Lo protagonizan **Lito y Pachi**, dos personajes con un universo propio de ilustraciones, globos de diálogo, hilos rojos y personajes escondidos.

Tener la idea era la parte fácil. Convertirla en un libro que se pudiera **imprimir, vender en Amazon y promocionar en Instagram** exigía ilustrar, maquetar, entender la preimpresión, diseñar una cubierta y preparar una campaña. Este artículo cuenta cómo se usó la inteligencia artificial en cada uno de esos frentes y, sobre todo, qué tuvo que seguir haciendo una persona.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">③ El resultado: el libro</span>
  <p><strong>El DeLito</strong> ya está a la venta en Amazon, en Kindle y en tapa blanda. Es el libro del que trata este caso.</p>
  <div class="botones">
    <a class="boton" href="https://www.amazon.es/dp/B0HD1CZ64C" target="_blank" rel="noopener">📖 Tapa blanda en Amazon</a>
    <a class="boton" href="https://www.amazon.es/dp/B0HCDKP4B7" target="_blank" rel="noopener">Kindle</a>
    <a class="boton secundario" href="https://books2read.com/u/3kxoo8" target="_blank" rel="noopener">Otras tiendas</a>
    <a class="boton secundario" href="https://www.instagram.com/elde_lito/" target="_blank" rel="noopener">@elde_lito</a>
  </div>
</div>

<div class="leyenda" markdown="0">
  Para leer con rigor: <span class="etiqueta hecho">Hecho documentado</span> consta que se trabajó en ello ·
  <span class="etiqueta propuesta">Aplicación explicativa</span> cómo puede usarse la IA en una tarea así ·
  <span class="etiqueta futuro">Posibilidad futura</span> mejora que podría incorporarse.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/mapa-del-caso.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/mapa-del-caso.svg' | relative_url }}" alt="Tabla visual con siete frentes del proyecto DeLito y, para cada uno, el problema, el proceso y la solución"></a>
  <figcaption>El caso entero de un vistazo. Cada fila se desarrolla más abajo.</figcaption>
</figure>

## 1. Una idea con demasiadas formas

<div class="bloque bloque-problema" markdown="1">
Un libro que es a la vez poesía, juego, diario y carta tiene un riesgo evidente: **dispersarse**. Cada página puede pedir un tono distinto, cada juego una regla nueva, cada personaje un estilo diferente. Sin una referencia común, el proyecto se reconstruye desde cero en cada sesión de trabajo.
</div>

<div class="bloque bloque-proceso" markdown="1">
Un asistente conversacional sirve aquí como compañero de pensamiento: ayuda a **explorar alternativas, convertir ideas vagas en requisitos concretos y documentar las decisiones**. En DeLito, ese trabajo cristalizó en una <span class="etiqueta hecho">Hecho documentado</span> **biblia del proyecto**, un documento maestro que debía recoger:

- el concepto y la personalidad del libro;
- los personajes principales y sus relaciones, incluidos los triángulos narrativos;
- el estilo narrativo y visual;
- los globos, los hilos rojos y los personajes escondidos;
- los juegos y las preguntas dirigidas al lector;
- los archivos y sus versiones;
- los criterios para generar imágenes;
- la maquetación y la publicación.
</div>

<div class="bloque bloque-solucion" markdown="1">
Con la biblia, cada conversación con la IA puede empezar **con contexto** en lugar de con explicaciones. Eso sí: no se escribe sola ni sale perfecta a la primera. La revisa y la actualiza el autor, porque es suya la última palabra sobre qué es DeLito.
</div>

## 2. Lito y Pachi tienen que ser siempre Lito y Pachi

Generar una imagen bonita es relativamente fácil. Conseguir que los **mismos personajes** se reconozcan en veinte escenas distintas es otra historia. Las herramientas generativas tienden a «reinterpretar»: cambian una nariz, una proporción, una prenda o un detalle que para el lector es la seña de identidad del personaje.

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/personajes-coherentes.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/personajes-coherentes.svg' | relative_url }}" alt="Diagrama en tres pasos: referencia fiable en la página 3 del libro, instrucción concreta en lugar de 'dibuja al mismo personaje', y lista de revisión del autor, con bucle de corrección"></a>
  <figcaption>Referencia, instrucción concreta y revisión. Si algo falla, se corrige y se vuelve a empezar.</figcaption>
</figure>

<div class="bloque bloque-problema" markdown="1">
Pedir «dibuja al mismo personaje» no basta. Sin una referencia visual fiable, cada imagen nueva corre el riesgo de alejarse un poco más de la anterior.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> Se fijaron **modelos de referencia** de Lito y Pachi y se indicó expresamente que las imágenes posteriores debían respetarlos, tomando como base **la página 3 del libro**, identificada en el flujo de trabajo como el archivo «page 04». La diferencia entre «página 3» y «page 04» (la numeración de los archivos no siempre coincide con la del libro) es un buen ejemplo de por qué conviene dejar estas equivalencias por escrito.

El método tiene siete pasos: identificar una referencia fiable, reutilizar los modelos, describir la escena nueva, señalar qué rasgos no pueden cambiar, revisar las diferencias, corregir con instrucciones nuevas y comprobar que la ilustración encaja en el libro.
</div>

<div class="bloque bloque-solucion" markdown="1">
Un procedimiento repetible, no una garantía. La consistencia **mejora** con referencias e instrucciones precisas, pero cada imagen hay que mirarla junto a las demás antes de darla por buena.
</div>

## 3. Imágenes que parezcan del mismo libro

<div class="bloque bloque-problema" markdown="1">
Una colección de imágenes puede ser preciosa una a una e incoherente en conjunto: estilos que no casan, texturas distintas, papeles de otro mundo, niveles de detalle desiguales. **Una imagen atractiva no es lo mismo que una imagen apropiada para esta obra.**
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> Se especificó que los papeles y elementos generados debían parecer **pertenecientes al propio universo del libro**. En la práctica, eso significa trabajar con una descripción de estilo compartida, referencias del propio libro y una idea clara del tipo de papel y sus texturas. Después vienen los ajustes sucesivos de composición, la comparación de variantes y la integración de los elementos gráficos.
</div>

<div class="bloque bloque-solucion" markdown="1">
La calidad no se mide imagen a imagen, sino **por cómo encaja en el resto**. La IA explora; la selección de las definitivas es humana.
</div>

## 4. Nadie acierta a la primera: el ciclo de iteración

Si hay una enseñanza que atraviesa todo el proyecto, es esta: **la primera propuesta casi nunca es la buena**. Suele cumplir parte del encargo y fallar en un detalle que importa.

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/ciclo-iteracion.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/ciclo-iteracion.svg' | relative_url }}" alt="Ciclo de siete pasos: objetivo, proponer, revisar, señalar, ajustar, comparar y validar, indicando cuáles decide la persona y cuáles genera la IA"></a>
  <figcaption>De los siete pasos, la IA protagoniza dos. El resto es criterio.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> En las imágenes promocionales se pidieron variantes y ajustes concretos: escenas en las que **el libro perseguía a los personajes** y otras con una **lluvia de libros**. También **hubo que insistir** en que las piezas incluyeran la información comercial solicitada.

Cada vuelta del ciclo funciona mejor si la petición es **delimitada**: no «hazlo más bonito», sino «mantén la composición, corrige este rasgo y añade este texto».
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Las instrucciones precisas, las referencias y las correcciones **son trabajo creativo**. La IA no elimina la necesidad de criterio: cambia la manera de ejercerlo.
</div>

## 5. Unir el interior sin perder páginas por el camino

<div class="bloque bloque-problema" markdown="1">
Un libro ilustrado acumula documentos, páginas sueltas, globos de diálogo, cambios y versiones intermedias. Al juntarlo todo aparecen los riesgos clásicos: **duplicados, páginas en el orden equivocado y versiones antiguas que se cuelan**.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> Se trabajó con un **interior unificado** y con versiones identificadas por el nombre del archivo. Una de ellas es `DeLito_final_A5_v7_unificado_con_globos.pdf`: el nombre ya cuenta una historia (versión 7, unificada, con los globos incorporados).

<span class="etiqueta propuesta">Aplicación explicativa</span> En una fase así, la IA puede ayudar a crear inventarios de archivos, resumir diferencias entre versiones, proponer listas de control, documentar decisiones editoriales y diagnosticar problemas de producción. Lo que no hace por sí sola es **garantizar** que una fusión de PDF salga bien: eso se ejecuta con herramientas de edición o scripts y se comprueba página a página.
</div>

<div class="bloque bloque-solucion" markdown="1">
La IA organiza el proceso; **la integridad del documento final se verifica**. Un buen sistema de nombres de versión es la red de seguridad.
</div>

## 6. De «quiero imprimirlo» a una lista de medidas

<div class="bloque bloque-problema" markdown="1">
Un libro que se ve perfecto en pantalla puede no cumplir las especificaciones de una plataforma de impresión bajo demanda. Tamaño, paginación, márgenes, sangrado y lomo son conceptos que rara vez forman parte del día a día de quien escribe o dibuja.
</div>

<div class="bloque bloque-proceso" markdown="1">
Aquí la IA actúa como **intermediaria entre un objetivo y el conocimiento técnico** necesario para alcanzarlo. La frase «quiero que este libro esté listo para imprimirse» se descompone en preguntas concretas: formato final, número de páginas, márgenes y sangrado, dimensiones de la cubierta, cálculo del lomo, tipo de PDF y comprobaciones finales.

<span class="etiqueta hecho">Hecho documentado</span> Para una versión concreta del proyecto se trabajó con estos parámetros:

<div class="tabla-scroll" markdown="1">

| Parámetro | Valor de esa versión |
|---|---|
| Interior sin portadas | 63 páginas |
| Tamaño del interior | 5,06 × 7,81 pulgadas |
| Lomo calculado | 0,148 pulgadas |
| Sangrado de cubierta | 0,125 pulgadas |
| Cubierta completa | 10,518 × 8,060 pulgadas |

</div>
</div>

<div class="bloque bloque-solucion" markdown="1">
Una lista de medidas **coherente entre sí**: el ancho de la cubierta es exactamente la suma de sangrados, contraportada, lomo y portada. La IA puede ayudar a interpretar requisitos, detectar inconsistencias, entender errores de validación y preparar o revisar scripts de procesamiento de PDF.
</div>

<div class="bloque bloque-rigor" markdown="1">
Estos valores corresponden a **una versión concreta** y no son especificaciones universales. Los cálculos y la aceptación del archivo se comprueban con las especificaciones vigentes de la plataforma y con su herramienta de validación. La IA reduce la barrera técnica, pero **no sustituye la comprobación de preimpresión**.
</div>

## 7. Una cubierta no es una portada

Mucha gente imagina la portada como una imagen suelta. En un libro impreso, la cubierta es **una sola pieza** que envuelve el libro: contraportada, lomo y portada, con el sangrado alrededor.

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/cubierta-completa.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/cubierta-completa.svg' | relative_url }}" alt="Plano a escala de la cubierta completa: contraportada y portada de 5,06 por 7,81 pulgadas, lomo de 0,148 en el centro, sangrado de 0,125 alrededor; total 10,518 por 8,060 pulgadas"></a>
  <figcaption>Plano a escala de la cubierta de la versión de 63 páginas. Si cambia el número de páginas, cambia el lomo y, con él, toda la cubierta.</figcaption>
</figure>

<div class="bloque bloque-problema" markdown="1">
Hay que coordinar portada, contraportada y lomo, respetar las dimensiones totales y el sangrado, colocar textos e imágenes donde no corran peligro y mantener la **continuidad visual** entre las tres zonas.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> En DeLito se trabajó con **cubiertas completas**, con la contraportada a la izquierda, el lomo en el centro y la portada a la derecha, además de versiones auxiliares del diseño. La IA ayuda a idear composiciones, proponer recursos gráficos, revisar instrucciones y resolver dudas técnicas.
</div>

<div class="bloque bloque-solucion" markdown="1">
Un diseño pensado como un todo. Pero **una imagen generada no es un PDF de cubierta listo para producción**: los textos pequeños, las medidas exactas y las zonas sujetas a requisitos de impresión necesitan una revisión específica.
</div>

## 8. Del archivo final al escaparate de Amazon

<div class="bloque bloque-problema" markdown="1">
Terminar el contenido no significa que el libro esté listo para venderse. Quedan la presentación del producto, los textos descriptivos, los metadatos, la subida de archivos y la resolución de los avisos que comunique la plataforma.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> DeLito se preparó para su publicación en **Amazon**, con un proceso de producción orientado a la **impresión bajo demanda**, y hoy está a la venta allí en [tapa blanda](https://www.amazon.es/dp/B0HD1CZ64C) y en [Kindle](https://www.amazon.es/dp/B0HCDKP4B7).

<span class="etiqueta propuesta">Aplicación explicativa</span> La IA puede ayudar con listas de tareas previas, revisión de textos descriptivos, organización de metadatos, comprobación de la coherencia entre cubierta, interior y descripción, y diagnóstico de errores comunicados por la plataforma.
</div>

<div class="bloque bloque-solucion" markdown="1">
Hay que distinguir tres cosas: **preparar materiales**, **asistir durante la configuración** y **publicar**. La IA participa en las dos primeras. La publicación y las decisiones comerciales sobre el público, el precio, la presentación y la estrategia son humanas.
</div>

## 9. Promoción: la creatividad no basta si no dices dónde comprar

<div class="bloque bloque-problema" markdown="1">
Sin un equipo de diseño ni de publicidad, producir piezas promocionales variadas **sin perder la identidad visual** del libro es difícil. Y hay un error clásico: una imagen espectacular que no le dice a nadie qué hacer a continuación.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho documentado</span> Se prepararon propuestas visuales con **Lito y Pachi** como protagonistas, manteniendo la estética del libro: los personajes **perseguidos por el propio libro**, una **lluvia de libros** y variantes de estas composiciones. Las piezas tenían que comunicar que **El Delito estaba disponible en Amazon** y que el **enlace de compra estaba en la descripción del perfil de Instagram [@elde_lito](https://www.instagram.com/elde_lito/)**.

Antes de publicar, cada pieza pasa por una revisión: legibilidad, identidad de los personajes, coherencia con el libro, claridad del mensaje, información de compra y adaptación al formato de la red social.
</div>

<div class="bloque bloque-solucion" markdown="1">
Una campaña que reutiliza personajes y recursos del propio libro y que **no olvida el paso que permite al público actuar**. Una pieza promocional sin «dónde se compra» es solo una ilustración bonita.
</div>

## 10. La organización también es un resultado

<figure class="post-figura">
  <a href="{{ '/assets/img/delito/cadena-produccion.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/delito/cadena-produccion.svg' | relative_url }}" alt="Cadena de producción en tres bandas: crear (idea, concepto, biblia, personajes), producir (imágenes, organizar, unificar interior, cubierta, validar impresión) y lanzar (Amazon, Instagram)"></a>
  <figcaption>El orden es orientativo: en la práctica las fases se solapan y se vuelve atrás.</figcaption>
</figure>

Un proyecto largo acumula decisiones y dependencias: cambiar el número de páginas altera el lomo, que altera la cubierta, que altera las piezas promocionales que la muestran. En DeLito, la biblia del proyecto, los modelos de referencia, los nombres de archivo, las versiones del libro y los criterios de las piezas promocionales forman una red que hay que cuidar.

<span class="etiqueta propuesta">Aplicación explicativa</span> La IA puede ayudar a mantener una lista de tareas pendientes, un registro de decisiones, una relación de archivos definitivos, una lista de problemas conocidos, criterios de aceptación, un historial de cambios, una guía de estilo e instrucciones reutilizables para tareas recurrentes.

<span class="etiqueta futuro">Posibilidad futura</span> Convertir esas instrucciones recurrentes, como la de mantener a Lito y Pachi a partir de la página 3, en plantillas fijas reduciría aún más el trabajo de cada nueva pieza.

## Límites y control humano

La IA no es una solución mágica. Estos son los puntos de control que importan en un proyecto así. Son **riesgos generales**, no incidentes concretos de DeLito:

- **Inconsistencias en las imágenes**: rasgos, proporciones o ropa que cambian.
- **Instrucciones interpretadas a medias**: se cumple una parte del encargo y se olvida otra.
- **Textos dentro de las imágenes** con errores o difíciles de leer.
- **Atractivo frente a objetivo**: una imagen preciosa puede no cumplir su función comercial.
- **Medidas de impresión** que hay que verificar, y **PDF** que necesitan comprobaciones técnicas.
- **Nombres de archivo y versiones** que, mal gestionados, inducen a error.
- **Respuestas técnicas** que pueden ser incorrectas.
- **Precisión**: hay tareas que piden herramientas convencionales además de IA.
- **Decisiones**: publicar y promocionar siguen siendo responsabilidad humana.

El autor decide qué representa la obra, qué imágenes encajan, qué cambios acepta y cuándo algo está terminado.

## Ocho aprendizajes para tu propio proyecto

<div class="bloque bloque-aprendizaje" markdown="1">
**A. El contexto importa.** La IA responde mejor cuando conoce el proyecto, sus objetivos, sus límites y sus referencias.

**B. Las referencias visuales son la base.** Para mantener personajes, aporta modelos y revisa diferencias.

**C. Sé concreto.** «Hazlo más bonito» sirve de poco; «cambia esto y conserva aquello» funciona.

**D. Itera.** Generar, evaluar, corregir y validar es más eficaz que esperar el acierto a la primera.

**E. Crear y producir son problemas distintos.** Una ilustración puede ser buena y no servir para imprimir; un PDF puede abrirse bien y no cumplir las medidas.

**F. Documenta.** Biblia, guía visual y nombres de archivo ahorran trabajo repetido.

**G. El control es humano.** Tú decides qué es la obra y cuándo está terminada.

**H. No hace falta saber formularlo técnicamente.** Puedes partir de una necesidad cotidiana y descubrir en la conversación qué datos, herramientas y comprobaciones necesitas.
</div>

## Conclusión

DeLito no salió de una instrucción ni de una tarde de prompts. Salió de muchas conversaciones, muchas versiones y muchas decisiones de alguien que sabía qué quería contar. Lo que cambió la IA fue la distancia entre esa idea y las disciplinas necesarias para materializarla: ilustración, documentación, preimpresión, diseño de cubierta y promoción dejaron de ser muros y pasaron a ser escalones.

**La IA no hizo desaparecer la complejidad de crear un libro. Ayudó a hacerla abordable, permitió explorar soluciones y facilitó que una idea personal avanzara por disciplinas que, de otro modo, habrían sido mucho más difíciles de coordinar.** El hilo rojo que une todo lo demás sigue siendo el criterio de quien lo firma.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">Consigue El DeLito</span>
  <p>El cuaderno ya es libro: 30 poemas que se leen y se juegan, con Lito y Pachi.</p>
  <div class="botones">
    <a class="boton" href="https://www.amazon.es/dp/B0HD1CZ64C" target="_blank" rel="noopener">📖 Tapa blanda</a>
    <a class="boton" href="https://www.amazon.es/dp/B0HCDKP4B7" target="_blank" rel="noopener">Kindle</a>
    <a class="boton secundario" href="https://www.instagram.com/elde_lito/" target="_blank" rel="noopener">Síguelo en Instagram</a>
  </div>
</div>
