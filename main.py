import qexpy as q

x = 0.0005
corriente = q.Measurement(2.04,x)
voltaje = q.Measurement(203,x)

datos = [
  [q.Measurement(302,x),q.Measurement(349,x),q.Measurement(407,x),q.Measurement(463,x),q.Measurement(505,x)],
  [q.Measurement(3.75,0.3),q.Measurement(4.1,0.1),q.Measurement(4.5,0.2),q.Measurement(4.9,0.1),q.Measurement(5.1,0.3)],
  [q.Measurement(1.07,x),q.Measurement(1.33,x),q.Measurement(1.51,x),q.Measurement(1.67,x),q.Measurement(1.97,x)],
  [q.Measurement(5.2,0.2),q.Measurement(4.55,0.2),q.Measurement(4.02,0.2),q.Measurement(3.75,0.3),q.Measurement(2.65,0.1)]
  
]

for i in range(5):
  em = (2*(15**2)*(5**3)*datos[0][i])/((4**3)*(130*corriente*datos[1][i]))
  print(em)

print()

for i in range(5):
  em = (2*(15**2)*(5**3)*voltaje)/((4**3)*(130*datos[2][i]*datos[3][i]))
  print(em)
