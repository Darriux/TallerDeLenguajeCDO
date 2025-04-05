<h1>Descripción</h1>

Este proyecto simula múltiples partidas de un juego de disparos en primera persona (FPS) y genera un ranking de jugadores basado en su desempeño. El sistema calcula puntajes, determina el Mejor Jugador de cada partida (MVP) y muestra estadísticas acumuladas.

<h1>Características principales</h1>
- Simulación de 5 rondas de juego con estadísticas realistas
- Sistema de puntuación basado en kills, asistencias y muertes
- Detección automática del MVP en cada ronda
- Ranking acumulativo de jugadores
- Pausas entre partidas para mayor realismo

<h1>Requisitos del sistema</h1>
- Python 3.6 o superior
- No se requieren librerías externas


<h1>Estructura del código</h1>

<h2>Funciones principales<h2>

```calcular_puntaje(kills, assists, deaths)```: Calcula el puntaje de un jugador en una ronda según:

 - Kills: +3 puntos cada uno

 - Asistencias: +1 punto cada una

 - Muertes: -1 punto cada una

```simular_partidas(rounds)```: Orquesta toda la simulación

 - Procesa cada ronda de juego
 - Calcula estadísticas individuales
 - Determina el MVP de cada ronda
 - Muestra resultados parciales y finales
 - Implementa pausas entre partidas

<h1>Datos de entrada</h1>

El script utiliza un conjunto predefinido de rondas (rounds) donde cada una contiene las estadísticas de los 5 jugadores: Shadow, Blaze, Viper, Frost, Reaper

<h1>Instalación</h1>

1. Clona el repositorio o descarga el archivo shooter_simulation.py
2. Ejecuta el script con Python: ```python simulador.py```