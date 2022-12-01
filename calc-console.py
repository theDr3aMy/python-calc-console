import time
import os

def clear_console():
    os.system('cls')

while(True): 
  print("----------------KALKULATOR----------------")
  print("1. Dodawanie")
  print("2. Odejmowanie")
  print("3. Mnożenie")
  print("4. Dzielenie")
  print("5. Wyłącz kalkulator")
  answer = int(input("Wybierz opcję: "))

#dodawanie   
  if(answer == 1):
    print("")
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    result = a + b
    print("Suma liczby", a, "i", b, "wynosi:",result,".")
    time.sleep(1)
    clear_console()
#odejmowanie    
  elif(answer == 2):
    print("")
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    result = a - b
    print("Różnica liczby", a, "i", b, "wynosi:",result,".")
    time.sleep(1)
    clear_console()
#mnozenie        
  elif(answer == 3):
    print("")
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    result = a * b
    print("Iloczyn liczby", a, "i", b, "wynosi:",result,".")
    time.sleep(1)
    clear_console()
#dzielenie   
  elif(answer == 4):
    print("")
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))
    result = a / b
    print("Iloraz liczby", a, "i", b, "wynosi:",result,".")
    time.sleep(1)
    clear_console()

  elif (answer == 5):
    print("")
    print("Wyłączam kalkulator")
    time.sleep(0.5)
    clear_console()
    print(".")
    time.sleep(0.5)
    clear_console()
    print("..")
    time.sleep(0.5)
    clear_console()
    print("...")
    break
  else:
    print("")
    print("Nie prawidlowa opcja.")
    time.sleep(0.5)
    clear_console()