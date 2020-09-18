print("Introcuzca Q1 , H1 , Q2 , H2 , Q3 , H3 , en ese orden.")


Q1= float (input())
H1= float (input())
Q2= float (input())
H2= float (input())
Q3= float (input())
H3= float (input())

Q12 = pow(Q1,2)
Q22 = pow(Q2,2)
Q32 = pow(Q3,2)


am = Q2 - (Q22/Q1)

ac = Q2*Q1 - Q22

u = (H3 - ((H1*Q32)/(Q12)) + ((H2*Q32)/(ac)) - ((H1*Q22*Q32)/(Q12*ac)) - ((H2*Q3)/(am)) + ((H1*Q22*Q3)/(Q1*Q1*am)))

uu = ( -((Q32)/(Q12)) - ((Q22*Q32)/(Q12*ac)) + ((Q32)/(ac)) + ((Q22*Q3)/(Q12*am)) - (Q3/am) + 1)


C = (u/uu)

B = ((H2 - ((H1*Q22)/Q12) + ((C*Q22)/Q12) - C )/( Q2 - (Q22/Q1) ))

A = ( (H1/Q12) - (B/Q1) - (C/Q12) )

print ( "Los coeficientes de la ecuación de la bomba son:" )
print("A:")
print( A )
print("B:")
print( B )
print("C:")
print( C )
