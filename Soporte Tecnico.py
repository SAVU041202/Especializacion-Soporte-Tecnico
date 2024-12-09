# Programa para planificar tu especialización en soporte técnico

def mostrar_menu():
    print("\n--- Planificador de Especialización en Soporte Técnico ---")
    print("1. Explorar áreas de especialización")
    print("2. Generar lista de habilidades necesarias")
    print("3. Crear un plan de aprendizaje")
    print("4. Salir")

def explorar_areas():
    print("\nÁreas de especialización en soporte técnico:")
    areas = [
        "1. Redes y conectividad",
        "2. Soporte de hardware",
        "3. Sistemas operativos (Windows, Linux, macOS)",
        "4. Seguridad informática",
        "5. Soporte de software empresarial (ERP, CRM, etc.)",
        "6. Asistencia técnica remota"
    ]
    for area in areas:
        print(area)
    seleccion = input("\nIngresa el número del área que más te interesa: ")
    return seleccion

def generar_lista_habilidades(area):
    habilidades = {
        "1": ["Configurar routers y switches", "Solucionar problemas de red", "Administrar VPNs"],
        "2": ["Diagnosticar y reparar equipos", "Instalar componentes", "Mantenimiento preventivo"],
        "3": ["Gestionar usuarios", "Actualizar sistemas operativos", "Solucionar problemas comunes"],
        "4": ["Proteger datos y redes", "Detectar malware", "Implementar firewalls"],
        "5": ["Personalizar software empresarial", "Resolver errores", "Capacitar a usuarios"],
        "6": ["Configurar herramientas de soporte remoto", "Asistir a usuarios en tiempo real", "Documentar soluciones"]
    }
    return habilidades.get(area, [])

def crear_plan(habilidades):
    print("\nPlan de aprendizaje sugerido:")
    for i, habilidad in enumerate(habilidades, 1):
        print(f"{i}. {habilidad} - (Tiempo estimado: 2 semanas)")
    print("\n¡Organiza tu tiempo y comienza a aprender!")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        if opcion == "1":
            area = explorar_areas()
            print(f"\nElegiste el área {area}. ¡Perfecto!")
        elif opcion == "2":
            if 'area' in locals():
                habilidades = generar_lista_habilidades(area)
                if habilidades:
                    print("\nHabilidades necesarias en tu área seleccionada:")
                    for habilidad in habilidades:
                        print(f"- {habilidad}")
                else:
                    print("\nÁrea no válida. Por favor, explora nuevamente.")
            else:
                print("\nPrimero debes seleccionar un área de especialización.")
        elif opcion == "3":
            if 'habilidades' in locals():
                crear_plan(habilidades)
            else:
                print("\nPrimero debes generar una lista de habilidades.")
        elif opcion == "4":
            print("\n¡Gracias por usar el planificador! ¡Éxito en tu aprendizaje!")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
