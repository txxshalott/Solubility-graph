### SHALOTT TAM | SCH3U | SOLUBILITY CURVE GRAPHING ASSIGNMENT | MAY 2023
# working on inter/ extrapolating based on line of best fit rather than data set, pls lmk if you know how...

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.title('Solubility Curves of various compounds', size=20)
plt.xlabel('Tempreature °C', size=12)
plt.ylabel('Mass (in grams) of solute/ 100g H\N{SUBSCRIPT TWO}O)', size=12)

# axis precision
plt.xticks(np.arange(0, 110, 10)) # from 0 to 110 with an increment of 10
plt.yticks(np.arange(0, 205, 5))

plt.grid()

## INTERPOLATION
def interpolate(name, x, y, x_temp):
    y_interp = round(np.interp(x_temp, x, y))

    plt.plot(x_temp, y_interp, 'x', color='k')

    # draw dash lines
    plt.plot([x_temp, x_temp], [plt.ylim()[0], y_interp], '--', color='k') # vertical
    plt.plot([plt.ylim()[0], x_temp], [y_interp, y_interp], '--', color='k')

    # add annotation on point (y_interp, x_temp)
    annotation = f'{name}({x_temp}°C, {y_interp}g)'
    plt.annotate(annotation, xy=(x_temp, y_interp), xytext=(x_temp + 0.5, y_interp), bbox=dict(facecolor='white', edgecolor='white', boxstyle='round, pad=0.1', alpha=0.7))

## PLOT POINTS & CURVE OF BEST FIT
def plot(x, y, name):
    plt.scatter(x, y, s=10, label=f'{name}') # SCATTER PLOT

    ## Calculate curve of best fit
    def makeLine(x, a, b, c): # relationship b/w points
        return a * x + b * x**2 + c

    # estimates optimal values for coefficients a, b, and c that best fit the data
        # popt short for optimal parameters, _ throwaway variable
    popt, _ = curve_fit(makeLine, x, y) 

    a, b, c = popt # unpack values
    print(f'y = {a} * x + {b} * x^2 + {c}')
    
    # creates array of x coords using min & max(exclusive) 'x' values, increment by 1
    x_line = np.arange(min(x), max(x)+50, 1)

    # calculate output for the range
    y_line = makeLine(x_line, a, b, c)

    plt.plot(x_line, y_line)

# KI
xKI = [0, 5, 10, 15, 20, 25] # x
yKI = [127, 131, 135, 140, 145, 150] # corresponding y
plot(xKI, yKI, 'KI')

# KNO3
xKNO3 = [0, 10, 20, 30, 40, 50, 60, 70] 
yKNO3 = [13, 22, 33, 49, 65, 88, 112, 140] 
plot(xKNO3, yKNO3, 'KNO\N{SUBSCRIPT THREE}')

# NaNO3
xNaNO3 = [0, 10, 20, 30, 40, 50, 60, 70, 80]
yNaNO3 = [74, 79, 86, 95, 104, 113, 124, 135, 148]
plot(xNaNO3, yNaNO3, 'NaNO\N{SUBSCRIPT THREE}')

# HCl
xHCl = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yHCl = [82, 77, 71, 66, 61, 58, 54, 51, 48, 45, 43]
plot(xHCl, yHCl, 'HCl')

# NH3
xNH3 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yNH3 = [90, 69, 55, 45, 37, 29, 24, 19, 14, 10, 7]
plot(xNH3, yNH3, 'NH\N{SUBSCRIPT THREE}')

# NH4Cl
xNH4Cl = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
yNH4Cl = [30, 33, 37, 41, 46, 51, 56, 61, 66, 71, 77]
plot(xNH4Cl, yNH4Cl, 'NH\N{SUBSCRIPT FOUR}Cl')

# KCl
xKCl = [30, 40, 50, 60, 70, 80, 90, 100]
yKCl = [37, 39, 42, 45, 49, 51, 55, 58]
plot(xKCl, yKCl, 'KCl')

# NaCl
xNaCl = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yNaCl = [36, 36, 36, 36, 37, 37, 38, 38, 38, 39, 39]
plot(xNaCl, yNaCl, 'NaCl')

# KClO3
xKClO3 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
yKClO3 = [5, 6, 9, 12, 16, 21, 28, 34, 43, 50, 60]
plot(xKClO3, yKClO3, 'KClO\N{SUBSCRIPT THREE}')

# SO2
xSO2 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # x
ySO2 = [22, 16, 10, 7, 5, 4, 3, 2, 2, 2, 2] # corresponding y
plot(xSO2, ySO2, 'SO\N{SUBSCRIPT TWO}')

# INTERPOLATE
interpolate('KCl', xKCl, yKCl, 85) #a
interpolate('KClO\N{SUBSCRIPT THREE}', xKClO3, yKClO3, 95) #b
interpolate('NaNO\N{SUBSCRIPT THREE}', xNaNO3, yNaNO3, 15) #c
interpolate('SO\N{SUBSCRIPT TWO}', xSO2, ySO2, 25) #d

# clean up layout
plt.xlim(left=0, right=100)
plt.ylim(bottom=0, top=200)

plt.legend(ncol=1)

plt.show()