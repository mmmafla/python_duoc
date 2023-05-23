ops=0
total=0
sub_total=0
tratamiento=0
cant_carillas_porcelana=0
cant_implantes_dentales=0
cant_ortodoncia_brackets=0
carillas_porcelana=250000
implantes_dentales=475000
ortodoncia_brackets=800000
while True:
    print("¡Bienvenido a Diente de Oro! ")
    try:
        ops=int(input("|¿Que desea hacer?| \n|(1) - Cotizacion | \n|(2) -  Renunciar | \n|(3) -    Salir   | \nOpcion: "))
    except ValueError:
        print("ERROR. Debe ingresar valores numericos. ")
    except:
        print("Numero fuera de rango. ")
    while True:
        if ops==1:
            print("Se le presentara los tratamientos disponibles y sus respectivos precios. ")
            print("(1) Carillas Porcelana  - $250.000 ") 
            print("(2) Implantes Dentales  - $475.000 ")
            print("(3) Ortodoncia Brackets - $800.000" )
            print("(4) Descuento. ")
            print("(5) Volver. ")
            while True:
                try:
                    tratamiento=int(input("Opcion: "))
                except ValueError:
                    print("ERROR. Debe ingresar valores numericos. ")
                except:
                    print("Numero fuera de rango. ")
                if tratamiento==1:
                    cant_tratamiento=int(input(f"¿Cuantos tratamientos desea del tratamiento {tratamiento}? "))
                    sub_total=carillas_porcelana*cant_tratamiento
                    print(f"Ha sumado {cant_tratamiento} tratamiento(s). ${carillas_porcelana*cant_tratamiento}. ")
                    cant_carillas_porcelana=cant_carillas_porcelana+1
                    total=total+sub_total
                    break
                elif tratamiento==2:
                    cant_tratamiento=int(input(f"¿Cuantos tratamientos desea del tratamiento {tratamiento}? "))
                    sub_total=implantes_dentales*cant_tratamiento
                    print(f"Ha sumado {cant_tratamiento} tratamiento(s). ${implantes_dentales*cant_tratamiento}. ")
                    cant_implantes_dentales=cant_implantes_dentales+1
                    total=total+sub_total
                    break
                elif tratamiento==3:
                    cant_tratamiento=int(input(f"¿Cuantos tratamientos desea del tratamiento {tratamiento}? "))
                    sub_total=ortodoncia_brackets*cant_tratamiento
                    print(f"Ha sumado {cant_tratamiento} tratamiento(s). ${ortodoncia_brackets*cant_tratamiento}. ")
                    cant_ortodoncia_brackets=cant_ortodoncia_brackets+1
                    total=total+sub_total
                    break
                elif tratamiento==4:
                    print(f"El total a efectuar es de ${total}. ")
                    descuento=int(input("¿Tiene algun descuento? |(1) Si / (2) No | "))
                    if descuento==1:
                        print("(1) Trabajador Auxiliar       - Descuento: 15% ")
                        print("(2) Trabajador Administrativo - Descuento: 10% ")
                        print("(3) Trabajador Docente        - Descuento: 5% ")
                        sub_descuento=int(input("Seleccione el tipo de descuento. "))
                        if sub_descuento==1:
                            sub_descuento=15
                            total=(total*85)/100
                        elif sub_descuento==2:
                            sub_descuento=10
                            total=(total*90)/100
                        elif sub_descuento==3:
                            sub_descuento=5
                            total=(total*95)/100
                        print(f"El total a pagar con descuento aplicado es ${total} ")
                elif tratamiento==5:
                    print(f"El total a efectuar es de ${total}. ")
                    cuotas=total/12
                    print(f"Cada cuota sera de ${cuotas} ")
                break
        elif ops==2:
            print("Se ha renunciado a la cotizacion anterior. ")
            total=0
            break
        elif ops==3:
            break
    break
print("-"*25)
print("Cotizacion. ")
print("-"*25)
print(f"--> {cant_carillas_porcelana} tratamiento(s) Carillas Porcelanas  - ${sub_total} ")
print(f"--> {cant_implantes_dentales} tratamiento(s) Implantes Dentales   - ${sub_total} ")
print(f"--> {cant_ortodoncia_brackets} tratamiento(s) Ortodoncia Brackets - ${sub_total} ")
print("-"*25)
print(f"Sub Total: {sub_total} ")
print(f"Descuento {sub_descuento}: {(total*descuento)/100}")
print("-"*25)
print(f"Total: {total} ")
print("-"*25)
print(f"Son 12 cuotas de: {cuotas} ")
print("-"*25)
print("¡Sonria bonito! ")