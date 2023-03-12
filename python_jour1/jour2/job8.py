def periode(type,saison):
    if type =="fruit" and saison == "hiver":
        print("orange, mandarine,kiwi")
    elif type == "fruit" and saison == "ete":
        print("poire, fraise,cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte,, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")
    else:
        print("revient plus tard")
        
print(periode("fruit","ete"))