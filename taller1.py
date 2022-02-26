def calcularsueldo(salario, diastrabajados): 
    sueldo = salario/30 * diastrabajados
    return(sueldo)
    



def main():
    SALARIO_MIN = 1000000
    SUB_ALIM = 120000
    SUB_TRAMP = 80000
    BONO = 50000
    nombre = input("Digite el nombre ==>  ")
    salario = int (input("Digite el salario Mensual ==>  "))
    diastrabajados = int (input("Digite las dias trabajados ==>  "))
    sueldo = calcularsueldo(salario, diastrabajados)

    if salario < (SALARIO_MIN * 2):
        sueldo = sueldo + SUB_ALIM + SUB_TRAMP
    else:
        sueldo = sueldo + BONO
    
    print(f"mi nombre es : {nombre} y mi salario a pagar es : {sueldo:.0f}")

  




if __name__== "__main__":
    main()