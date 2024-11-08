
# funcoes2.py

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Testes
loginUsuario('Admin')
loginUsuario('User')
loginUsuario('usuário')
