# reto_4

## Class Shape
```python
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
        Line(point_1, point_2, point_1.compute_distance(point_2)),
        Line(point_1, point_3, point_1.compute_distance(point_3)), 
        Line(point_2, point_3, point_2.compute_distance(point_3))]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = Isosceles(vertices, edges, [50,65,65]) #Se crea un triangulo isosceles
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}") 

if __name__ == "__main__":
    main()

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
        Line(point_1, point_2, point_1.compute_distance(point_2)),
        Line(point_1, point_3, point_1.compute_distance(point_3)), 
        Line(point_2, point_3, point_2.compute_distance(point_3))]
    vertices = [point_1, point_2, point_3] 
    triangle_1 = Isosceles(vertices, edges, [50,65,65]) #Se crea un triangulo isosceles
    print(f"Área: {triangle_1.compute_area()},Perimetro: {triangle_1.compute_perimeter()}, Suma de ángulos internos: {triangle_1.compute_inner_angles()}") 

if __name__ == "__main__":
    main()
```
## Restaurant Scenario
```python
class MenuItem:
    def __init__(self,name:str,price:int):
        self.name=name #Nombre del producto
        self.price=price #Precio del producto

class Beverage(MenuItem): #Clase derivada de MenuItem (Bebidas)
    def __init__(self,name,price,temperature:str):
        super().__init__(name,price)# Hereda el inicializador de la super clase MenuItem
        self.__temperature=temperature# Temperatura -> Atributo de unico de la clase Beverage

    def get_temperature(self):
        return self.__temperature

class Appetizer(MenuItem): #Clase derivada de MenuItem (Entradas)
    def __init__(self,name,price,pieces:int): 
        super().__init__(name,price) # Hereda el inicializador de la super clase MenuItem
        self.__pieces=pieces# Numero de piezas -> Atributo de unico de la clase Appetizer

    def get_pieces(self):
        return self.__pieces
    
class MainCourse(MenuItem): #Clase derivada de MenuItem (Plato principal)
    def __init__(self,name,price,accompainments):
        super().__init__(name,price) # Hereda el inicializador de la super clase MenuItem
        self.__accompainments=accompainments # Acompañamientos -> Atributo de unico de la clase MainCourse

    def get_accompainments(self):
        return self.__accompainments
```
Se tiene como argumentos privados a cada uno de los argumentos exclusivos de cada clase (temperatura, numero de piezas y acompañamientos), por lo que se utilizan getters para acceder a sus valores a la hora de querer mostrar la orden , para que puedan aparecer cada una de sus caracteristicas.

```python

class Order:
    def __init__(self):

        self.order_list=[] #Lista vacia para guardar los productos ingresados por el usuario
        

    def add_item(self): #metodo para crear la orden
        
        while True:
            item= str(input("Ingrese el producto que desea agregar a su pedido o (fin) para terminar: "))
            if item.lower()=="fin":
                break #El pedido terminara de hacerse cuando el usuario escriba "fin"
            elif item.lower() in menu_items:
                self.order_list.append(menu_items[item.lower()].name) #Los productos de agregan a la lista "order_list unicamente si hacen parte de las claves del diccionario "menu_items"
                                                                      #A la lista se agraga el nombre objeto que corresponidia a la clave ingresada por el usiario
            else:
                print(f"El producto '{item}' no esta en el menu. Ingrese nuevamente su pedido: ")
                True #En caso de que el producto ingresado no corresponda a ninguna de las claves del diccionario, se guardara lo 
                     #anteriormente ingresado y se volvera a hacer el pedido.
        
        print("\nOrden:")
        for product in self.order_list:
            print(f"- {product}: ", end="")
            
            
            if product.lower() in menu_items:
                if isinstance(menu_items[product.lower()], Beverage): #Si el producto es una bebida, se imprime la temperatura con el metodo get_temperature()
                    print(menu_items[product.lower()].get_temperature())
            
            
                elif isinstance(menu_items[product.lower()], Appetizer):
                    print(f"Piezas:{menu_items[product.lower()].get_pieces()}")#Si el producto es una entrada, se imprime la temperatura con el metodo get_pieces()
                
                elif isinstance(menu_items[product.lower()], MainCourse):
                    print(f"Acompañamientos:{menu_items[product.lower()].get_accompainments()}")#Si el producto es un plato principal, se imprime la temperatura con el metodo get_accompainments()

        print("\n")
    

    def total_bill(self): #metodo para calcular el valor total a pagar por el pedido

        self.bill=0 #se inicializa la la cuenta en 0
        for product in self.order_list: #por cada producto en la lista de la orden del usuario
            if product.lower() in menu_items: #si el producto hace parte de las claves del diccionario  "menu_items"
                self.bill+=menu_items[product.lower()].price #se accede al atributo "price" de cada uno de los objetos y se acumulan a 0.
        self.final_bill = self.bill
        print(f"->TOTAL A PAGAR = ${self.bill}") #"->TOTAL A PAGAR = $suma de los precios"


    def discounts(self): #metodo para hacer descuentos al pedido
        
        beverage_count=sum(isinstance(menu_items[item.lower()], Beverage) for item in self.order_list)
        # Suma 1 al contador de bebidas si el elemento en la orden es una instancia de la clase Beverage
        appetizer_count=sum(isinstance(menu_items[item.lower()], Appetizer) for item in self.order_list)
        # Suma 1 al contador de bebidas si el elemento en la orden es una instancia de la clase Appetizer
        main_course_count=sum(isinstance(menu_items[item.lower()], MainCourse) for item in self.order_list)
        # Suma 1 al contador de bebidas si el elemento en la orden es una instancia de la clase MainCourse
        
        discount=0
        # Aplica descuentos basados en la cantidad y tipo de productos

        if   beverage_count== appetizer_count== main_course_count and 3>=beverage_count >=1:
            
            #si se piden entre uno y tres productos de cada categoria: descuento del 5%
            discount=(self.bill*0.05)#valor a restar del total
     

        elif beverage_count== appetizer_count== main_course_count and beverage_count >=4:

            #si se piden 4 o mas productos cateroria: descuento del 10%
            discount=(self.bill*0.10)


        elif beverage_count==main_course_count and beverage_count==4:

            #si se piden 4 bebidas y cuatro platos principales: descuento del 8%
            discount=(self.bill*0.08)

        else: 
            print(f"Descuento a aplicar: 0$")# En caso de que no se cumpla con ninguno de los requisitos para descuento
                                             #se imprimira que el "Descuento a aplicar es igual a 0$"
        
        final_bill=self.bill-discount
        print(f"Descuento a aplicar: -{discount}$")
        print(f"TOTAL A PAGAR (Descuento aplicado)=> {final_bill}$")
        self.final_bill=final_bill# Almacena final_bill como un atributo de instancia para poder acceder a el fuera de la clase
```
```python

class Payment():
    def __init__(self):
        pass

    def pay(self):
        raise NotImplementedError("Subclases deben implementar pagar()")

class Card(Payment):
    def __init__(self, c_number, cvv):
        self.c_number=c_number
        self.cvv=cvv

    def pay(self, final_bill):
        print(f"Pago de {final_bill} realizado con la tarjeta #{self.c_number} ")
    
class Cash(Payment):
    def __init__(self,cash,):
        self.cash=cash

    def pay(self,final_bill):
        if self.cash>=final_bill:
            change=self.cash-final_bill
            print(f"Total de {final_bill} cancelado con exito\nCambio:{change}")

        else:
            print(f"Fondos insuficientes. Faltan {final_bill-self.cash}")
```
Se añadio la nueva clase payment para que el usuario elija el metodo de pago. Se usa polimorfismo para definir de maneras diferentes el metodo pay en cada subclase que hereda de la clase payment (card y cash).
```python
  
    
#Objetos de la clase Beverages
coffe=Beverage("Coffe",3000,"Hot")
chocolate=Beverage("Chocolate",3500,"Hot")
lemonade=Beverage("Lemonade",2500,"Cold")
water=Beverage("Water",2000,"Hot")

#Objetos de la clase Appetizer
spicy_shrimp=Appetizer("Spicy Shrimp",20000,"6")
mini_quiches=Appetizer("Mini Quiches",18000,"4")
fried_platains=Appetizer("Fried Platains",15000,"8")
capresse_salad=Appetizer("Capresse Salad",15000,"1")

#Objetos de la clase Main Course
grilled_salmon=MainCourse("Grilled Salmon",38000," Mashed Potatoes and Mango Salad")
BBQ_ribs=MainCourse("Bbq Ribs",34000," Fries")
stuffed_chicken=MainCourse("Stuffed Chicken",30000,"Parsley Rice")
vegetarian_curry=MainCourse("Vegetarian Curry",30000,"Pita Bread")

#Objeto de la clase orden 
order = Order()


#Diccionario con todos los productos del menu
menu_items={"coffe":coffe,"chocolate":chocolate,"lemonade":lemonade,"water":water,
            "spicy shrimp":spicy_shrimp,"mini quiches":mini_quiches,"fried platains":fried_platains,"capresse salad":capresse_salad,
            "grilled salmon":grilled_salmon,"bbq ribs":BBQ_ribs,"stuffed chicken":stuffed_chicken,"vegetarian curry":vegetarian_curry}


#Impresion del menu
print ("\nMENU:\n")
for item in menu_items:
    print(f"-{menu_items[item].name}")

#Lista de descuentos
print("\n")
print("DESCUENTOS:\n-Entre uno y tres productos de cada categoria: 5% de descuento\n-Desde cuatro productos de cada categoria: 10% de descuento\n-Cuatro bebidas y cuatro platos principales:8% de descuento")
print("\n")
    
order.add_item()# Llama al método add_item() de la clase Order para agregar productos a la orden. Imprime la orden.
order.total_bill()# Calcula el total de la factura llamando el método total_bill() de la clase Order.
order.discounts()#Calcula los descuentos llamando al método discounts() de la clase Order.
final_bill = order.final_bill # Obtiene el valor de final_bill almacenado en la instancia de Order

payment_method=str(input("¿Con que metodo desea pagar?: "))

if payment_method=="card":
    c_number_=int(input("Ingrese el numero de su tarjeta: "))
    cvv_=int(input("Ingrese el CCV de su tarjeta: "))

    payment = Card(c_number=c_number_,cvv=cvv_)
    payment.pay(final_bill)

elif payment_method=="cash":
    cash_=int(input("Monto entregado: "))

    payment = Cash(cash=cash_)
    payment.pay(final_bill)

else:
    print("Metodo invalido de pago")

```
