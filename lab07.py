# Diccionario de usuarios y sus calificaciones de bandas musicales
users = {
    "Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, 
                 "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, 
                 "Vampire Weekend": 2.0},
    "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, 
             "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
    "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, 
             "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
    "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, 
            "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, 
            "Vampire Weekend": 2.0},
    "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, 
               "The Strokes": 4.0, "Vampire Weekend": 1.0},
    "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, 
               "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, 
               "Vampire Weekend": 4.0},
    "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, 
            "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
    "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, 
                 "Slightly Stoopid": 2.5, "The Strokes": 3.0}
}

# Función para calcular la distancia de Manhattan
def manhattan(rating1, rating2):
    """Calcula la distancia de Manhattan entre dos usuarios.
    Ambas calificaciones son diccionarios con las bandas y sus puntuaciones.
    """
    distance = 0
    # Solo consideramos las bandas que ambos usuarios han calificado
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
    return distance

# Función para encontrar el vecino más cercano (distancia mínima)
def computeNearestNeighbor(username, users):
    """Crea una lista ordenada de usuarios basada en su distancia a 'username'."""
    distances = []
    for user in users:
        if user != username:  # No comparamos el usuario consigo mismo
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    # Ordenamos la lista de distancias, de menor a mayor
    distances.sort()
    return distances

# Ejemplo de prueba
if __name__ == "__main__":
    # Calcular la distancia de Manhattan entre "Hailey" y "Veronica"
    print("Distancia entre Hailey y Veronica:", manhattan(users["Hailey"], users["Veronica"]))
    
    # Encontrar el vecino más cercano para "Hailey"
    nearest_neighbors = computeNearestNeighbor("Hailey", users)
    print("Vecinos más cercanos a Hailey:", nearest_neighbors)
