def arithmetic_arranger(lista, mostra_resultado=False):
    if len(lista) > 5:
        return "Error: Too many problems."

    gerenciador_linhas = dict()
    gerenciador_linhas["Linha1"] = gerenciador_linhas["Linhas2"] = \
        gerenciador_linhas["separador"] = gerenciador_linhas["resultado"] = str()

    for conta in lista:

        if "+" in conta:
            opetador = "+"
        elif "-" in conta:
            opetador = "-"
        else:
            return "Error: Operator must be '+' or '-'."

        y = conta.split(f"{opetador}")

        if y[0].strip().isnumeric() is False or y[1].strip().isnumeric() is False:
            return "Error: Numbers must only contain digits."
        elif len(y[0].strip()) > 4 or len(y[1].strip()) > 4:
            return "Error: Numbers cannot be more than four digits."

        largura_problema = max(len(y[0].strip()), len(y[1].strip()))+2
        gerenciador_linhas["Linha1"] += f"{y[0].strip().rjust(largura_problema)}{' ' * 4 if conta != lista[-1] else ''}"
        gerenciador_linhas["Linhas2"] += f"{opetador}{y[1].strip().rjust(largura_problema-1)}" \
                                         f"{' ' * 4 if conta != lista[-1] else ''}"
        gerenciador_linhas["separador"] += f"{'-' * largura_problema}{' ' * 4 if conta != lista[-1] else ''}"

        if mostra_resultado:
            resultado = f"{int(y[0]) + int(y[1]) if opetador == '+' else int(y[0]) - int(y[1])}"
            gerenciador_linhas["resultado"] += f"{resultado.strip().rjust(largura_problema)}" \
                                               f"{' ' * 4 if conta != lista[-1] else ''}"

    if mostra_resultado:
        resultado = gerenciador_linhas["Linha1"] + "\n" + gerenciador_linhas["Linhas2"] + "\n" + gerenciador_linhas[
            "separador"]+"\n" + gerenciador_linhas[
            "resultado"]
    else:
        resultado = gerenciador_linhas["Linha1"]+"\n"+gerenciador_linhas["Linhas2"]+"\n"+gerenciador_linhas["separador"]

    return resultado


problemas = ['3 + 855', '988 + 40']

if __name__ == '__main__':
    print(arithmetic_arranger(problemas, True))
