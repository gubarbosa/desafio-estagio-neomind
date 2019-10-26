from datetime import datetime

hora_atual = int(datetime.now().strftime('%H'))        #Uso da biblioteca para definir horario atual
minuto_atual = int(datetime.now().strftime('%M'))

if hora_atual > 12:
    hora_atual = hora_atual // 2          #Divisão exata para obter os ponteiros entre 0 e 12
else:
    pass

def AnguloHora(hora_atual, minuto_atual):
    angulo_por_hora = 30                               #Relação do ângulo com cada hora
    angulo_hora = hora_atual * angulo_por_hora         #Cálculo do ângulo da hora
    angulo_hora += minuto_atual * 0.5                #Alteração no ângulo da hora devido os minutos corridos
    return angulo_hora


def AnguloMinuto(minuto_atual):
    angulo_por_minuto = 6                                 #Relação do ângulo por cada minuto
    angulo_minuto = minuto_atual * angulo_por_minuto      #Cálculo do ângulo do minuto
    return angulo_minuto


def AnguloRelogio():
    angulo_da_hora = AnguloHora(hora_atual, minuto_atual)
    angulo_do_minuto = AnguloMinuto(minuto_atual)
    if angulo_da_hora > angulo_do_minuto:                          #Condição para maior e menor ângulo
        angulo_relogio = angulo_da_hora - angulo_do_minuto
    else:
        angulo_relogio = angulo_do_minuto - angulo_da_hora         #Cálculo do ângulo do relógio com a diferença entre os ângulos de horas e minutos
    return angulo_relogio

# Atribuir uma variável ao valor do ângulo do relógio
angulo_relogio = AnguloRelogio()

#Comentário teste
#Printar no console horário atual e seu respectivo ângulo
print('O ângulo entre os ponteiros de hora e minuto atual: {} é {}º'.format(datetime.now().strftime('%H:%M'), angulo_relogio))


