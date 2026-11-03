---
layout: post
title: "Siguiente Capítulo: una web para seguir tus series que avisa sola de los capítulos nuevos"
date: 2026-11-10 13:00:00 +0100
categories: [casos-de-uso]
tags: [series, anime, github-pages, supabase, automatizacion, claude]
description: "Cómo una lista de series dentro del chat acabó siendo una web propia, gratuita y con login, que busca capítulos nuevos cada tres días aunque no la abras."
image: /assets/img/siguiente/cabecera.png
lang: es
---

<link rel="stylesheet" href="{{ '/assets/css/casos-ia.css' | relative_url }}">

<figure class="post-figura">
  <img src="{{ '/assets/img/siguiente/cabecera.svg' | relative_url }}" alt="Ilustración de una cuadrícula de carteles de series sobre fondo oscuro, algunos con la etiqueta NUEVO, bajo el título Siguiente Capítulo">
</figure>

<p class="entradilla">Diecisiete series y animes, cada uno en una web distinta, y una pregunta que se repite: ¿por qué capítulo iba? ¿Ha salido ya el siguiente? <strong>Siguiente Capítulo</strong> es la respuesta: una web propia que guarda lo que has visto, enseña cada serie con su portada y su resumen, y busca sola los capítulos nuevos cada tres días. Este caso cuenta cómo pasó de ser una ayuda dentro del chat a una web que funciona sin la IA, y qué decisiones siguieron siendo humanas.</p>

<div class="resultado" markdown="0">
  <span class="resultado-titulo">③ El resultado: la web</span>
  <p><strong>Siguiente Capítulo</strong> está publicada y funciona. Se entra con una cuenta de Google.</p>
  <div class="botones">
    <a class="boton" href="https://rvillalba1983.github.io/siguiente-capitulo/" target="_blank" rel="noopener">📺 Abrir Siguiente Capítulo</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/siguiente-capitulo" target="_blank" rel="noopener">Ver el código</a>
  </div>
</div>

<div class="leyenda" markdown="0">
  Cómo leer este artículo: cada capítulo separa <strong style="color:#b5402a">① el problema</strong>, <strong style="color:#b7791f">② el proceso</strong> y <strong style="color:#2f7d4f">③ la solución</strong>. Las etiquetas distinguen
  <span class="etiqueta hecho">Hecho</span> lo que consta que se hizo y funciona,
  <span class="etiqueta propuesta">Propuesta</span> lo que se planteó, y
  <span class="etiqueta pendiente">Pendiente</span> lo que queda por hacer.
</div>

<div class="ficha" markdown="0">
  <div><strong>Proyecto</strong>Siguiente Capítulo, web personal</div>
  <div><strong>Qué hace</strong>Seguir series y anime, y avisar de capítulos nuevos</div>
  <div><strong>Asistente</strong>Claude</div>
  <div><strong>Herramientas</strong>GitHub Pages · Supabase · Google (login)</div>
  <div><strong>Coste</strong>Planes gratuitos</div>
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/siguiente/mapa-del-caso.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/siguiente/mapa-del-caso.svg' | relative_url }}" alt="Tabla visual con cinco frentes del proyecto (seguir series, dónde vive, novedades, webs caídas y acceso) y, para cada uno, el problema, el proceso y la solución"></a>
  <figcaption>El caso entero de un vistazo. Cada fila se desarrolla más abajo.</figcaption>
</figure>

<span class="capitulo-num">Capítulo 1</span>

## El problema: diecisiete series y ninguna lista

<div class="bloque bloque-problema" markdown="1">
Las series y el anime se ven en **webs gratuitas de streaming**, una para anime y otra para series. Ninguna recuerda por dónde vas si no tienes cuenta, ninguna avisa cuando sale un capítulo y, además, cambian de dirección cada cierto tiempo. Con diecisiete series a la vez, el resultado es abrir pestañas, buscar y probar suerte.
</div>

<div class="bloque bloque-proceso" markdown="1">
La idea se le planteó a la IA con unos requisitos claros:

- Ver **todas las series** con su portada y su resumen, tal cual aparece en la web de origen, sin traducir.
- **Buscar capítulos nuevos** de forma automática y avisar.
- **Guardar qué capítulos se han visto.**
- **Enlazar** a la web real para ver cada capítulo.
- Funcionar **desde cualquier dispositivo**, con los datos en la nube y **sin depender de la IA**.
</div>

<div class="bloque bloque-solucion" markdown="1">
Un encargo que cabe en cinco líneas y que, como se verá, exigió probar varias soluciones antes de dar con la buena.
</div>

<span class="capitulo-num">Capítulo 2</span>

## Seis pasos: qué se probó y por qué cambió

<figure class="post-figura">
  <a href="{{ '/assets/img/siguiente/evolucion.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/siguiente/evolucion.svg' | relative_url }}" alt="Seis pasos numerados: artefacto dentro de Claude, diseño estilo Netflix, migración a GitHub Pages y Supabase, búsqueda automática, webs alternativas y login con Google"></a>
  <figcaption>Cada paso resolvió un límite del anterior.</figcaption>
</figure>

<div class="bloque bloque-problema" markdown="1">
<span class="etiqueta hecho">Hecho</span> La primera versión fue una página creada **dentro de Claude**, con su propia base de datos y usando el navegador de Claude para buscar capítulos. Funcionaba, pero **solo allí dentro**: no servía para mirarla desde el móvil ni para dejarla trabajando sola.
</div>

<div class="bloque bloque-proceso" markdown="1">
De ahí salió la decisión más importante del proyecto: **sacar la web de la IA**.

<div class="reparto" markdown="1">
<div markdown="1">
**🤖 La IA**
Propuso la arquitectura, escribió el código de la web, la base de datos y la función de búsqueda, y fue corrigiendo los fallos.
</div>
<div markdown="1">
**👤 La persona**
Decidió que tenía que funcionar sin la IA, eligió el estilo y probó cada versión. Las contraseñas, claves y permisos los puso siempre ella.
</div>
</div>

Por el camino también cambió el diseño: un estilo inspirado en Netflix, con fondo oscuro y carteles en vertical. Las filas con desplazamiento lateral se cambiaron después por una **cuadrícula** que se recorre bajando.
</div>

<div class="bloque bloque-solucion" markdown="1">
<span class="etiqueta hecho">Hecho</span> La versión dentro de Claude se borró. La que queda vive en internet y no necesita a la IA para funcionar.
</div>

<span class="capitulo-num">Capítulo 3</span>

## Tres piezas gratuitas, cada una con su papel

<figure class="post-figura">
  <a href="{{ '/assets/img/siguiente/arquitectura.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/siguiente/arquitectura.svg' | relative_url }}" alt="Esquema con tres cajas: la web en GitHub Pages, los datos y el motor en Supabase, y las webs de vídeo; el login con Google conecta con Supabase"></a>
  <figcaption>La web enseña, Supabase guarda y busca, y las webs de vídeo se siguen viendo en su sitio.</figcaption>
</figure>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> La web pasó a **GitHub Pages** (gratis, desde un repositorio público) y los datos a **Supabase**, una base de datos en la nube con plan gratuito. Allí viven las series de cada usuario (título, portada, resumen, último capítulo publicado y último visto) y una **función en el servidor** que hace las búsquedas.

Una limitación marcó el diseño: esas webs **no dejan incrustarse** en otra página. Por eso Siguiente Capítulo no reproduce nada: te lleva a la web original, al capítulo que te toca.
</div>

<div class="bloque bloque-solucion" markdown="1">
Una web que se abre en cualquier dispositivo, con los datos guardados en la nube y actualizada en tiempo real: si marcas un capítulo en el móvil, aparece marcado en el ordenador.
</div>

<div class="bloque bloque-aprendizaje" markdown="1">
Si quieres que algo hecho con la IA dure, pide que **no dependa de ella**: código en un repositorio tuyo, datos en un servicio tuyo y la IA solo para construirlo y mejorarlo.
</div>

<span class="capitulo-num">Capítulo 4</span>

## Enterarse de los capítulos nuevos sin abrir la web

<div class="bloque bloque-problema" markdown="1">
Buscar capítulos solo al abrir la web obliga a acordarse de abrirla. Y había un problema menos evidente: el **plan gratuito de Supabase pausa los proyectos que pasan un tiempo sin usarse**.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> La búsqueda pasó al servidor. Primero cada 2 días y, al final, **cada 3**. Un temporizador de la base de datos llama cada hora a la función, que revisa como mucho a 4 usuarios cuya última búsqueda tenga más de tres días. Si al entrar en la web la última búsqueda es más antigua, la lanza también.

Para cada serie, la función lee la página, saca el capítulo más alto, la portada y la sinopsis, y **solo actualiza el último capítulo publicado**. Lo que has visto no lo toca nunca.
</div>

<figure class="post-figura">
  <a href="{{ '/assets/img/siguiente/busqueda.svg' | relative_url }}" title="Ver a tamaño completo"><img src="{{ '/assets/img/siguiente/busqueda.svg' | relative_url }}" alt="Ciclo de siete pasos: despertar cada hora, elegir usuarios, leer la página de cada serie, comprobar el siguiente capítulo, cambiar de web si falla, resumir y ver por parte de la persona"></a>
  <figcaption>El ciclo automático. La persona solo aparece al final: para ver el capítulo.</figcaption>
</figure>

<div class="bloque bloque-solucion" markdown="1">
Avisos con un resumen claro («Nuevos: …», «Cambiado a otra web», «Sin enlace que funcione», «No se pudo leer») **aunque no abras la web**. <span class="etiqueta hecho">Hecho</span> La búsqueda automática ya ha encontrado capítulos nuevos. Y de paso el proyecto se usa cada semana, así que el plan gratuito no lo pausa.
</div>

<span class="capitulo-num">Capítulo 5</span>

## Cuando la web de vídeo se cae

<div class="bloque bloque-problema" markdown="1">
Las webs gratuitas de streaming **cambian de dominio** o dejan de funcionar sin avisar. Un enlace que ayer iba, hoy da error.
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> Cada serie puede tener **webs alternativas**. La función comprueba que la web principal abre el **siguiente capítulo por ver**; si falla, prueba las alternativas y cambia a la que funcione. También corrige automáticamente los cambios de dominio conocidos.

Desde la propia web, la hoja **«Dónde verla»** permite elegir la web principal, quitar una o añadir otra pegando el enlace de un capítulo. Y para añadir una serie nueva basta con pegar su enlace.
</div>

<div class="bloque bloque-solucion" markdown="1">
El enlace que te da la web es el que funciona hoy, no el que funcionaba cuando añadiste la serie.
</div>

<span class="capitulo-num">Capítulo 6</span>

## Abrirla a más gente sin perder el control

<div class="bloque bloque-problema" markdown="1">
Si la web está en internet, otras personas podrían querer usarla. Eso trae preguntas que no aparecen en un proyecto personal: ¿cómo se separan los datos de cada uno?, ¿quién guarda las contraseñas?, ¿cuánta gente cabe en un plan gratuito?
</div>

<div class="bloque bloque-proceso" markdown="1">
<span class="etiqueta hecho">Hecho</span> Se resolvió con tres decisiones:

- **Solo se entra con Google.** No hay contraseñas propias que guardar.
- **Seguridad por filas** en la base de datos: cada usuario solo ve y edita sus propias series.
- **Un máximo de 20 usuarios.** El alta número 21 se rechaza con un mensaje claro.

La primera persona en entrar puede importar su lista inicial de series. La web tiene también su política de privacidad, que Google exige para el login.
</div>

<div class="bloque bloque-solucion" markdown="1">
Una web personal que se puede compartir con un círculo pequeño sin mezclar datos ni gestionar contraseñas.
</div>

<div class="bloque bloque-rigor" markdown="1">
Las partes sensibles las hizo siempre la persona: **pegar claves y tokens, aceptar términos y consentimientos y configurar las cuentas**. La regla del proyecto es que la IA no crea cuentas ni inicia sesión por nadie, y que pide confirmación antes de borrar datos o tocar la seguridad o el login.
</div>

<span class="capitulo-num">Capítulo 7</span>

## Los fallos también enseñan

<div class="tabla-scroll" markdown="1">

| Fallo | Qué pasaba | Cómo se resolvió |
|---|---|---|
| Solo funcionaba dentro de Claude | No se podía usar desde otro sitio | Migración a GitHub Pages + Supabase |
| Una capa gris tras el login | Un elemento oculto seguía tapando la página | Una regla de estilo que fuerza a ocultarlo |
| El plan gratuito se pausa si no se usa | Riesgo de perder la búsqueda automática | La búsqueda periódica mantiene el proyecto activo |
| Webs que se caen o cambian de dominio | Enlaces rotos | Alternativas y cambio automático |
| Las webs de vídeo no se pueden incrustar | No se puede ver el capítulo dentro | Se enlaza al capítulo en su web |

</div>

## Qué hizo la IA y qué hizo la persona

<div class="tabla-scroll" markdown="1">

| Tarea | 🤖 IA | 👤 Persona |
|---|---|---|
| Definir qué tenía que hacer la web | Ayuda a concretarlo | **Decide** |
| Elegir dónde vive (sin depender de la IA) | Propone opciones | **Decide** |
| Código de la web, base de datos y búsqueda | **Lo escribe** | Lo prueba |
| Claves, tokens y consentimientos | — | **Los pone siempre** |
| Diseño | Lo implementa | Lo elige y lo corrige |
| Buscar capítulos cada 3 días | — (lo hace el servidor) | — |
| Ver los capítulos | — | **Disfrutarlos** |

</div>

### Límites que conviene tener presentes

- **Depende de cómo están hechas otras webs.** Si una cambia su forma de mostrar los capítulos, la búsqueda puede dejar de leerla hasta que se ajuste.
- **No reproduce nada:** solo lleva a la web donde se ve el capítulo.
- **El plan gratuito tiene límites**, y por eso la web se cierra en 20 usuarios.
- <span class="etiqueta pendiente">Pendiente</span> Probar el login desde otro dispositivo o con otra persona, y limpiar ramas sobrantes del repositorio.
- <span class="etiqueta propuesta">Propuesta</span> Un token de acceso para que la IA pueda publicar cambios en Supabase sin pasar por el panel del navegador.

## Cinco ideas para tu propio proyecto

<div class="bloque bloque-aprendizaje" markdown="1">
1. **Empieza dentro del chat** para probar la idea, pero **sácala** en cuanto sepas que la vas a usar.
2. **Escribe los requisitos** en pocas líneas: son la vara para medir cada versión.
3. **Busca piezas gratuitas que encajen**: una web estática, una base de datos en la nube y un login que ya existe.
4. **Automatiza lo que se te olvida hacer** (mirar si hay capítulo nuevo) y deja a mano solo lo que quieres hacer tú.
5. **Las llaves, siempre en tus manos**: contraseñas, tokens y permisos los pones tú.
</div>

## Conclusión

Siguiente Capítulo no es una plataforma de vídeo ni pretende serlo. Es una **lista bien hecha**: sabe qué series sigues, por dónde vas, si hay algo nuevo y dónde verlo hoy. La IA escribió casi todo el código y propuso la arquitectura, pero las decisiones que lo hicieron útil fueron humanas: que no dependiera de la IA, que nunca tocara lo ya visto y que las llaves las guardara siempre la misma persona.

<div class="resultado" markdown="0">
  <span class="resultado-titulo">Prueba Siguiente Capítulo</span>
  <p>Tus series, por dónde vas y qué ha salido nuevo, en una sola página.</p>
  <div class="botones">
    <a class="boton" href="https://rvillalba1983.github.io/siguiente-capitulo/" target="_blank" rel="noopener">📺 Abrir la web</a>
    <a class="boton secundario" href="https://github.com/rvillalba1983/siguiente-capitulo" target="_blank" rel="noopener">Ver el código</a>
  </div>
</div>
