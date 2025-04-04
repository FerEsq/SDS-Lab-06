'''
 * Nombre: scapyTest.py
 * Descripción: Script para verificar la correcta instalación de Scapy mediante la captura y análisis de paquetes de red.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 02.03.2025
    - Finalizado el 03.03.2025
'''

from scapy.all import sniff, raw
import sys
import os

def testScapy():    
    #Capturar 25 paquetes de la red doméstica y asignarlos a una variable
    try:
        #Utilizamos iface=None para que scapy use la interfaz por defecto
        packages = sniff(count=25, timeout=30)
        print("Captura de 25 paquetes completada.\n")
        
        #Imprimir tipo de variable, longitud y contenido
        print(f"Tipo de variable: {type(packages)}")
        print(f"Longitud (cantidad de paquetes): {len(packages)}")
        print("\nContenido de la variable paquetes (resumen):")
        print(packages)
        print("\n" + "~" * 70 + "\n")
        
        #Imprimir el tipo de dato del primer paquete capturado
        if len(packages) > 0:
            print(f"Tipo de dato del primer paquete: {type(packages[0])}")
            print("\n" + "~" * 70 + "\n")
        else:
            print("No se capturaron paquetes para analizar.")
            return
        
        #Imprimir el contenido de 5 paquetes
        print("Contenido de los primeros 5 paquetes:")
        numPackages = min(5, len(packages))
        for i in range(numPackages):
            print(f"\nPaquete #{i+1}:")
            print(packages[i].show(dump=True))  #dump=True para retornar como string en lugar de imprimir
            print("~" * 100)
            
    except Exception as e:
        print(f"Error durante la verificación: {e}")

if __name__ == "__main__":
    #Ejecutar la verificación
    testScapy()