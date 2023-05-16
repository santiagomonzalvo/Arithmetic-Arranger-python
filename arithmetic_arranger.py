def arithmetic_arranger(problems, bool=False):

    #****** Operandos y Operador ******
    termino1 = []
    termino2 = []
    operador = []
    #****** Separación por lineas/renglones para el output ******
    linea1 = []
    linea2 = []
    linea3 = []
    linea4 = []
    
    #****** Split de cada problema ******
    for p in problems:
        corte = p.split()
        termino1.append(corte[0])
        operador.append(corte[1])
        termino2.append(corte[2])
    #****** Checkeo de errores ******    
    for i in range(len(termino1)):
        if not (termino1[i].isdigit() and termino2[i].isdigit()):
            return "Error: Numbers must only contain digits."
    for i in range(len(termino1)):
        if len(termino1[i]) > 4 or len(termino2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
    for p in problems:
        if "*" in p or "/" in p:
            return "Error: Operator must be '+' or '-'."
    if len(problems) > 5:
        return "Error: Too many problems."
    #****** Aplicado de Formato ******
    for i in range(len(termino1)):
        max_len = max(len(termino1[i]), len(termino2[i]))
        linea1.append(termino1[i].rjust(max_len + 2))
        linea2.append(operador[i] + " " + termino2[i].rjust(max_len))

        linea3.append("-"*(max_len + 2))
    #****** Condicion para enviar Resultado ******
        if bool:
            if operador[i] == "+":
                resultado = str(int(termino1[i]) + int(termino2[i]))
            else:
                resultado = str(int(termino1[i]) - int(termino2[i]))
            linea4.append(resultado.rjust(max_len + 2))
        else:
            linea4 = []

    arranged_problems = "    ".join(linea1) + "\n" + "    ".join(linea2) + "\n" + "    ".join(linea3)
    if bool:
        arranged_problems += "\n" + "    ".join(linea4)
        
    return arranged_problems