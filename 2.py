def f(inp):
    inp = inp.replace(" ", "")
    q = inp.split("=")

    ifod = q[0]
    nat = int(q[1])

    n = list(map(int, ifod.split("*")))

    nat_str = str(n[0])

    for i in range(1, len(n)):
        jami = eval(nat_str.replace("=", "-").split()[0])
        
        if jami - n[i] >= nat:
            nat_str += " - " + str(n[i])
        else:
            nat_str += " + " + str(n[i])

    nat_str += " = " + str(nat)
    return nat_str

inp = input("Ifodani kiriting (m: '3 * 5 * 8 * 10 * 4 = 12') >>> ")
natija = f(inp)
print(natija)

