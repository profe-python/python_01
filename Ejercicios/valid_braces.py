# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

def valid_braces(cadena):
    parejas = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    if len(cadena) % 2 == 1:
        return False

    valores = list(parejas.values())

    pila = []
    for s in cadena:
        if s in valores:
            pila.append(s)
        else:
            if pila == []:
                return False
            ultimo = pila.pop()
            if ultimo != parejas[s]:
                return False
    
    return pila == []






def validBraces_2(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

print(validBraces_2('[({})]()'))


