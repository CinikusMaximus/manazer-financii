#financie instalacia/reset.py
#program vytvorí súbor s nižšie uvedenými údajmi, prípadne resetuje doterajší súbor
import os
file = open("financie","w")
file.write("0.05\n0\n")
file.write("0.10\n0\n")
file.write("0.20\n0\n")
file.write("0.50\n0\n")
file.write("1.00\n0\n")
file.write("2.00\n0\n")
file.write("5.00\n0\n")
file.write("10.00\n0\n")
file.write("20.00\n0\n")
file.write("50.00\n0\n")
file.write("100.00\n0\n")
file.write("200.00\n0\n")
file.write("500.00\n0")
file.close()