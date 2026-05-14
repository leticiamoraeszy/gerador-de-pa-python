print('-=-'*10)
print('Gerador de PA')
print('-=-'*10)
p1 = int(input('Primeiro termo: '))
razao = int(input('Razão da Pa: '))
termo = p1
total = 0
mais = 10
c = 1
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end=' ')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print('progressão finalizada com {} termos mostrados'.format(total))
