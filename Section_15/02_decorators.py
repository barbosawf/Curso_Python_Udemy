"""
Decoradores (Decorators)

O que são decorators?
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators têm uma sintaxe própria, usando "@" (Syntact Sugar /  Açúcar Sintático)

Function Decorator:

"""

a = '\033[0;33m'
b = '\033[0;36m'
c = '\033[m'

# Exemplo 01: Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)
print(f'\n{a}Exemplo 01: Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático){c}')

print(f"""{b}
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo a Geek University!')


teste = seja_educado(saudacao)  # A função seja_educado está aprimorando/decorando a função saudação.

teste(){c}
""")


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia')
    return sendo


def saudacao():
    print('Seja bem vindo a Geek University!')


teste = seja_educado(saudacao)  # A função seja_educado está aprimorando/decorando a função saudação.

teste()

# Exemplo 02: Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)
print(f'\n{a}Exemplo 02: Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático){c}')

print(f"""{b}
def raiva():
    print('EU TE ODEIO!')
    
    
raiva_educada = seja_educado(raiva)

raiva_educada(){c}
""")


def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()


# Exemplo 03: Decorators com Syntax Sugar
print(f'\n{a}Exemplo 03: Decorators com Syntax Sugar{c}')

print(f"""{b}
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro!')


apresentando(){c}
""")


def seja_educado_mesmo(funcao):  # Decorator Function
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo  # Decorator
def apresentando():
    print('Meu nome é Pedro!')


apresentando()


print(f"""{b}
@seja_educado_mesmo
def dormir():
    print('Quero dormir...')
    
    
dormir(){c}
""")


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()