import random 
import matplotlib.pyplot as plt 
 

def galton_simulation(num_balls, num_rows):
    # Crear los compartimentos de acuerdo al número de filas #
    compartments = [0] * (num_rows + 1)

# Simulamos el movimiento de cada bola #
    for _ in range(num_balls):
        position = 0  
        for _ in range(num_rows):
            position += random.choice([0, 1])  
        compartments[position] += 1  

        return compartments
    
def plot_distribution(compartments):
    # Graficar la distribución #
    plt.bar(range(len(compartments)), compartments, color='blue')  
    plt.xlabel('Compartimentos')  
    plt.ylabel('Número de bolas')  
    plt.title('Distribución de la máquina de Galton')
    plt.show()

    # Parámetros de la simulación #
num_balls = 3000
num_rows = 12

# Simulación y visualización #
compartments = galton_simulation(num_balls, num_rows) 
plot_distribution(compartments)