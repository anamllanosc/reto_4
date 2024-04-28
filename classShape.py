class Point: #clase punto
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def compute_distance(self,p2):
        distance=((self.x-p2.x)**2 + (self.y-p2.y)**2)**0.5
        return(distance)
    
class Line: #clase linea compuesta de puntos (punto inicial y final)
    def __init__(self,start_point:Point,end_point:Point):
        
        self.length=start_point.compute_distance(end_point)#distancia entre ambos puntos => longitud de la arista
        self.start_point=start_point
        self.end_point=end_point

class Shape: #clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        
        self.is_regular=is_regular
        self.vertices=vertices
        self.edges=edges
        self.inner_angles=inner_angles

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar area()") #se usa polimorfismo para definir el metodo area de manera diferente dependiendo de la figura
    
    def compute_perimeter(self):# el perimetro se calcula igual en cualquier caso, por lo que se define inicialmente en la clase shape (la suma de las longitudes se las aristas dentro de la lista "edges")
        perimeter=0
        for edge in self.edges:
            perimeter += edge.length
        return perimeter
    
    def compute_inner_angles(self):# la suma de los angulos internos 
        angle_sum=0
        for angle in self.inner_angles:
            angle_sum+=angle
        return angle_sum
            
    
class Rectangle(Shape): #clase rectangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): 
        width=min(edge.length for edge in self.edges) #la arista con la menor longitud se toma como el ancho del rectangulo
        height=max(edge.length for edge in self.edges) #la arista con la mayor longitud se toma como el alto del rectangulo
        area=width*height
        return area 
    
class Square(Rectangle): #clase cuadrado que hereda de la super clase rectangulo
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        
        area=self.edges[0].length**2 #todos sus lados son iguales, por lo que simplemente se toma el primero y se eleva al cuadrado
        return area 

class Triangle(Shape): #clase triangulo que hereda de super clase figura
    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

class Isosceles(Triangle): #clase isosceles (dos de tres lados iguales) que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):#se verifica que lado es el que tiene una longitud diferente para tomarlo como la base den triangulo
                           #poder hallar su altura y por tanto su area
        if self.edges[0].length==self.edges[1].length:

            heigth=(self.edges[0].length**2+(self.edges[2].length/2)**2)**0.5
            area=(self.edges[2].length*heigth)/2

            return area


        elif self.edges[0].length==self.edges[2].length:

            heigth=(self.edges[0].length**2+(self.edges[1].length/2)**2)**0.5
            area=(self.edges[1].length*heigth)/2

            return area

        elif self.edges[1].length==self.edges[2].length:

            heigth=(self.edges[1].length**2+(self.edges[0].length/2)**2)**0.5
            area=(self.edges[0].length*heigth)/2

            return area
        
        else: 
            print("El triangulo no es isosceles") #si no tiene dos lados iguales, no es isosceles

class Equilateral(Triangle): #clase equilatero que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self): #todos los lados son iguales, por lo que se toma la longitud de unicamente primero para hallar altura y area del triangulo equilatero

        heigth=(self.edges[0].length**2+(self.edges[0].length/2)**2)**0.5
        area=(self.edges[0].length*heigth)/2

        return area

class TriRectangle(Triangle): #clase triangulo rectangulo que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):
        ordered_edges=sorted(edge.length for edge in self.edges)#se ordena la lista de aristas de menor a mayor longitud

        #la arista con mayor longitud sera la hipotenusa, por lo que para hallar el area solo se toman las dos primeras aristas (las mas pequeñas)
        #como base y altura del rectangulo

        widht=ordered_edges[0]
        height=ordered_edges[1]
        area=(widht*height)/2

        return area
    

class Scalene(Triangle): #clase escaleno que hereda de super clase triangulo

    def __init__(self,vertices:list,edges:list,inner_angles:list,is_regular:bool=True):
        super().__init__(vertices,edges,inner_angles,is_regular)

    def compute_area(self):

        s=(self.edges[0].length+self.edges[1].length+self.edges[2].length)/2 #semiperimetro= (perimetro/2)
        area=(s*(s-self.edges[0].length)*(s-self.edges[1].length)*(s-self.edges[2].length))**0.5 # formula de Herón , usando el semiperimetro, 
                                                                                                  #para hallar el area del triangulo escaleno sin necesidad de hallar su altura.

        return area
    
def main():
    point_1 = Point(2,1)
    point_2 = Point(6,1)
    point_3 = Point(4,6)
    edges = [
        Line(point_1, point_2),
        Line(point_1, point_3), 
        Line(point_2, point_3)]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = Isosceles(vertices, edges, [50,65,65]) #Se crea un triangulo isosceles
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}") 

if __name__ == "__main__":
    main()


        

    

        

        


        



       

        
    






