mat = [[1, 3, 4],[3, 2, 1],[2, 4, 3]]
vet_resultado = [-5, 8, 4]

def resolve_sup(mat, vet_resultado):
    tamanho_mat = len(mat)
    vetor_solucao = [0.] * tamanho_mat

    for linha in range (tamanho_mat - 1, -1, -1):
        soma = 0

        for coluna in range (linha + 1, tamanho_mat):
            soma += mat[linha][coluna] * vetor_solucao[coluna]

        vetor_solucao[linha] = (vet_resultado[linha] - soma)/ mat[linha][linha]

    return vetor_solucao

def transforma_sup(mat, vet_resultado):
    tamanho_mat = len(mat)

    for k in range (0, tamanho_mat - 1):

        for linha in range (k + 1, tamanho_mat):
            fator_escalonamento = mat[linha][k]/mat[k][k]
            vet_resultado[linha] -= fator_escalonamento * vet_resultado[k]
            
            for coluna in range (k, tamanho_mat):
                mat[linha][coluna] -= fator_escalonamento * mat[k][coluna]

    return mat, vet_resultado

print_mat, print_resultado = transforma_sup(mat, vet_resultado)
print_solucao = resolve_sup(print_mat, print_resultado)

print(f"\nMatriz triangular superior: {print_mat}")
print(f"Resultado: {print_resultado}")
print(f"Solucao: {print_solucao}\n")