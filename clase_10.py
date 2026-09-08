
#* Operadores condicionales y bucles

temperatura= 25

if temperatura > 30:
  print("hace calor")
if temperatura <= 30:
  print("hace frio")


if temperatura > 30:
  print("hace calor")
else:
  print("hace frio")

if temperatura > 40:
  print("hace demasiado calor")
elif temperatura > 25:
  print("hace calor")
elif temperatura > 10:
  print("Esta fresco")


#OR
#AND
#NOT !

inscripto= False
if not inscripto:
  print("no esta inscripto")