from Laberinto import Laberinto


laberinto = [[1,1,1,1,1,1,1,1,1,1], \
            [1,0,0,1,0,0,0,1,0,1], \
            [1,0,0,1,0,0,0,1,0,1], \
            [1,0,0,0,0,1,1,0,0,1], \
            [1,0,1,1,1,0,0,0,0,1], \
            [1,0,0,0,1,0,0,0,0,1], \
            [1,0,1,0,0,0,1,0,0,1], \
            [1,0,1,1,1,0,1,1,0,1], \
            [1,1,0,0,0,0,0,0,0,1], \
            [1,1,1,1,1,1,1,1,1,1]]

l = Laberinto(laberinto, 1, 0, len(laberinto)-1, len(laberinto[0])-2)

print("El laberinto es:")
l.mostrar()

