import time

rounds = [
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
        'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
        'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
        'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
        'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
        'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
        'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
        'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
    },
    {
        'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
        'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
        'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
        'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
        'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
    }
]

def calcular_puntaje(kills, assists, deaths):
    """Calcula el puntaje total de un jugador en una ronda"""
    return kills * 3 + assists * 1 - (1 if deaths else 0)

def simular_partidas(rounds):
    """Simula las partidas y genera el ranking"""
    # Inicializar estadísticas totales
    jugadores = {}
    mvp_counts = {}
    
    for i, ronda in enumerate(rounds, 1):
        # Mostrar mensaje de espera entre partidas
        print("\nJugando partida, espere...")
        time.sleep(3)  # Pausa de 5 segundos
        
        print(f"\nRanking ronda {i}:")
        puntajes_ronda = {}
        max_puntaje = -1
        mvp = None
        
        # Calcular puntajes para esta ronda
        for jugador, estadisticas in ronda.items():
            kills = estadisticas['kills']
            assists = estadisticas['assists']
            deaths = estadisticas['deaths']
            puntaje = calcular_puntaje(kills, assists, deaths)
            
            puntajes_ronda[jugador] = puntaje
            
            # Actualizar estadísticas totales
            if jugador not in jugadores:
                jugadores[jugador] = {
                    'kills': 0,
                    'assists': 0,
                    'deaths': 0,
                    'puntos': 0
                }
                mvp_counts[jugador] = 0
                
            jugadores[jugador]['kills'] += kills
            jugadores[jugador]['assists'] += assists
            jugadores[jugador]['deaths'] += (1 if deaths else 0)
            jugadores[jugador]['puntos'] += puntaje
            
            # Determinar MVP
            if puntaje > max_puntaje:
                max_puntaje = puntaje
                mvp = jugador
            elif puntaje == max_puntaje:
                # En caso de empate, el MVP es el que tiene más kills
                if kills > ronda[mvp]['kills']:
                    mvp = jugador
        
        # Actualizar conteo de MVPs
        if mvp:
            mvp_counts[mvp] += 1
        
        # Mostrar resultados de la ronda
        print("Jugador   Kills   Asistencias   Muerte   Puntos")
        for jugador, puntaje in sorted(puntajes_ronda.items(), key=lambda x: -x[1]):
            estadisticas = ronda[jugador]
            print(f"{jugador:8} {estadisticas['kills']:6} {estadisticas['assists']:12} {str(estadisticas['deaths']):8} {puntaje:7}")
        
        print(f"\nMVP de la ronda: {mvp} (Puntos: {max_puntaje})")
    
    # Mostrar ranking final
    print("\nRanking final:")
    print("Jugador   Kills   Asistencias   Muerte   MVPs   Puntos")
    for jugador in sorted(jugadores.keys(), key=lambda x: -jugadores[x]['puntos']):
        estadisticas = jugadores[jugador]
        print(f"{jugador:8} {estadisticas['kills']:6} {estadisticas['assists']:12} {estadisticas['deaths']:8} {mvp_counts[jugador]:5} {estadisticas['puntos']:7}")

# Ejecutar la simulación
simular_partidas(rounds)