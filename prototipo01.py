import pickle

# Entrando
nome = pickle.load(open("nome.dat", "rb"))
print(f'Seja bem-vindo novamente {nome}!')
input('')
print("Se quiser saber como é o menu é só digitar 'menu'!\n")

sim = ['', 's', 'sim', 'yes']
nao = ['n', 'nao', 'não','no']

resposta = input('')

def mudar_nome():
    print('\nComo devo te chamar?')
    nome = input('')
    pickle.dump(nome, open("nome.dat", "wb"))
    nome = pickle.load(open("nome.dat", "rb"))
    print(f'Oi, {nome}! Seja bem-vindo!')

if resposta == 'menu':
    mudar_nome()

resposta = input('')
