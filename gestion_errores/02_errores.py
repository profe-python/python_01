# import os
# x = os.path.exists('no_existe.txt')


def esto_falla():
    try:
        f= open('no_existe2.txt','r')
        print('-----TRY ----------')
    except FileNotFoundError as e:
        print(e)
    else:
        print('--------else--------------')
    finally:
        print('----------finally ----------')



def genera_error(num):
    if num < 10:
        raise FileNotFoundError('Error de número demasiado pequeño.')
    else:
        print('Funciona!!!!!!!')


genera_error(9)





















