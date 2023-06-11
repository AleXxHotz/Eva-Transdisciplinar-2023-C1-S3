import PySimpleGUI as sg
import time

def main():#funcion principal
    posicion = 0
    velocidad = 0
    aceleracion = 2  # Aceleración constante
    
    # Configuración de la interfaz gráfica
    layout = [[sg.Graph((800, 400), (0, 0), (800, 400), background_color='white', key='graph')],
              [sg.Button('Iniciar'), sg.Button('Detener')]]
    
    window = sg.Window('Simulación de Movimiento', layout)
    graph = window['graph']
    
    # Bucle principal de la simulación
    while True:
        event, values = window.read(timeout=20)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Iniciar':
            tiempo_inicial = time.time()
            while True:
                event, values = window.read(timeout=20)
                if event == 'Detener':
                    break
                
                tiempo_actual = time.time() - tiempo_inicial
                
                # Cálculo de la posición y la velocidad en función del tiempo
                posicion = velocidad * tiempo_actual + 0.5 * aceleracion * tiempo_actual ** 2
                velocidad = velocidad + aceleracion * tiempo_actual
                #objeto(momentaneo, luego sera cambiado por un auto)
                graph.erase()
                graph.draw_line((posicion, 200), (posicion + 40, 200), color='red', width=3)
                window.refresh()
        graph.erase()
    window.close()

if __name__ == '__main__':
    main()
