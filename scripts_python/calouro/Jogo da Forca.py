palavra = 'vasco'

x = 6
erro = 0

palavra2 = palavra

for i in range(0, len(palavra)):
    trocar = palavra2.replace(palavra2[0 + i], '_')
    palavra2 = trocar

print('A palavra e:', trocar)

while erro < 7:

    if '_' in trocar:
        
        letra = input('Digite uma letra: ')

        if letra in palavra:
                change = (palavra.find(letra))

                l = list(trocar)
                l[change] = letra
                trocar = ''.join(l)

                trocar = trocar.upper()
                print(trocar)
            
        else:
            erro += 1
            if erro < 7:
                print('Errado! Você ainda tem', (x-erro), 'tentativas restantes')
            else:
                print('Fim de jogo!')
    
    else:
        print('Parabéns, você acertou a palavra!')
        break

    
        
        
        


    
