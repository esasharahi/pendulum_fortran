PROGRAM rg4
IMPLICIT NONE
INTEGER, PARAMETER :: eq_number = 2
REAL, PARAMETER :: g = 9.8, l = 1.0
REAL :: h
REAL :: x
REAL, DIMENSION(eq_number) :: y
REAL, DIMENSION(eq_number) :: k1, k2, k3, k4
INTEGER :: counter
INTEGER :: iter

PRINT*, 'This code solves the pendulum DE y" = - g/l * sin(y) by the initial conditions y_0 = y(x_0) and dy/dx(x_0).'

PRINT*, 'x_0: '
READ*, x

PRINT*, 'y(x_0): '
READ*, y(1)

PRINT*, 'dy/dx(x_0): '
READ*, y(2)

PRINT*, 'Enter the step length: '
READ*, h

PRINT*, 'Enter the iteration number (a natural number): '
READ*, iter

PRINT*, '*****************************************'
PRINT*, '*****************************************'



OPEN(UNIT = 1, FILE = "pendulum.txt") 

DO counter = 1, iter
    k1 = h * f(eq_number, x, y)
    k2 = h * f(eq_number, x + h / 2.0, y + k1 / 2.0)
    k3 = h * f(eq_number, x + h / 2.0, y + k2 / 2.0)
    k4 = h * f(eq_number, x + h, y + k3)
    y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    PRINT*, 'Step: ', counter
    PRINT*, 'x: ', x
    PRINT*, 'y: ', y
    PRINT*, '*********'
    WRITE(1, *) x, y(1)
    x = x + h
    y = y + h
END DO

CONTAINS

FUNCTION f(eq_number, x, y)
    IMPLICIT NONE
    INTEGER eq_number
    REAL :: x
    REAL, DIMENSION(eq_number) :: y
    REAL, DIMENSION(eq_number) :: f
    x = x
    f(1) = y(2)
    f(2) = - (g / l) * SIN(y(1))
END FUNCTION f


END PROGRAM rg4
