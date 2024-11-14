depositos = ["Tierra del fuego", "Tucuman", "Mendoza", "Bs As", "Misiones", "Santa Fe"] 
Equipos = ["Barcelona", "Inter Miami", "PSG", "Manchester City", "Real Madrid"]

def cargar_existencias() -> None:
    existencias = [[0 for _ in range(len(Equipos))] for _ in range(len(depositos))]
    for i in range(len(depositos)):
        for j in range(len(Equipos)):
            existencias [i][j] = int(input(f"Ingrese la cantidad de camisetas de {Equipos[j]} en {depositos[i]}: "))
        return existencias
    
def mostrar_existencias(existencias) -> None:
    print("Existencias de camisetas en los depositos:\n")
    print("Deposito\tBarcelona\tInter Miami\tPSG\tManchester City\tReal Madrid")
    for i in range(len(existencias)):
        print(f"{depositos[i]}\t", end="")
        for j in range(len(existencias[i])):
            print(f"{existencias[i][j]}\t", end="")
            print()

def mostrar_depositos_mayores_10000(existencias) -> int:
    for i in range(len(existencias)):
        total_camisetas = sum(existencias[i])
        if total_camisetas > 10000:
            print(f"Deposito {depositos[i]} tiene un total de {total_camisetas} camisetas.")

def mostrar_equipos_mayores_5000(existencias) -> int:
    for j in range(len(existencias[0])):
        total_camisetas = sum(existencias[i][j] for i in range(len(existencias)))
    if total_camisetas > 5000:
        print(f"Equipo{Equipos[j]} tiene un total de {total_camisetas} camisetas en stock.")


existencias = cargar_existencias()
mostrar_existencias (existencias)
mostrar_depositos_mayores_10000 (existencias)
mostrar_equipos_mayores_5000 (existencias)