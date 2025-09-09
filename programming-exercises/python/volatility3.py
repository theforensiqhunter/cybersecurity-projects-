import volatility3.framework as vol
from volatility3.framework import contexts
from volatility3.framework.configuration import requirements
from volatility3.plugins import pslist
import sys
import logging

# Configuración de la salida del log
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def obtener_procesos(volcado_memoria):
    """
    Función que analiza un volcado de memoria y obtiene información de los procesos activos
    :param volcado_memoria: ruta al archivo del volcado de memoria (p.ej., 'memory.dmp')
    :return: Listado de procesos activos
    """
    try:
        # Cargar el contexto de Volatility
        context = contexts.Context()

        # Inicializar el motor de Volatility
        config = vol.Config()
        config.add_value('location', volcado_memoria)
        
        # Crear un plugin de PSList para obtener la lista de procesos
        pslist_plugin = pslist.PSList(context, config)

        # Obtener todos los procesos activos
        pslist_plugin.calculate()

        # Recorrer los procesos y mostrar los resultados
        procesos = pslist_plugin.results
        log.info("Procesos activos encontrados:")
        for proceso in procesos:
            log.info(f"PID: {proceso['pid']}, Nombre: {proceso['name']}, Estado: {proceso['status']}")
        
    except Exception as e:
        log.error(f"Error al obtener los procesos: {e}")

def main():
    if len(sys.argv) != 2:
        log.error("Uso: python3 analisis_memoria.py <ruta_al_volcado_de_memoria>")
        sys.exit(1)
    
    volcado_memoria = sys.argv[1]
    obtener_procesos(volcado_memoria)

if __name__ == '__main__':
    main()
