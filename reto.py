# Realiza un examen con 3 preguntas que tu desees, el usuario debera responder "SI" o "NO" y al final otorgarle una calificacion (la calificacion se otorga con una variable que inicia en 0 y por cada respuesta correcta incrementa en 1)


pregunta_uno= input("le gusta el futbol? \r\n" )

if pregunta_uno == "Si":
  print("Suma un punto")
else:
  print("Tu puntuje es 0")

puntaje_total = 0
if pregunta_uno == "Si":
  puntaje_total += 1
else:
  puntaje_total += 0
  print(puntaje_total)