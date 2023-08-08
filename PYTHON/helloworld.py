# calcule le salaire mensuel
def salaire_mensuel(a) :
    """
    Cette fonction calcule le salaire mensuel
    
    Parameter :
    a (int) : le salaire annuel
    
    Return :
    int : le salaire mensuel
    """
    return a / 12

# calcul le salaire hebdomadaire
def salaire_hebdomadaire(a) :
    """
    Cette fonction calcule le salaire hebdomadaire
    
    Parameter :
    a (int) : le salaire mensuel
    
    Return :
    int : le salaire hebdomadaire
    """
    return a / 4

# calcul le salaire horaire
def salaire_horaire(a, b) :
    """
    Cette fonction calcule le salaire horaire
    
    Parameter :
    a (int) : le salaire hebdomadaire
    b (int : le nombre d'heures travaillées)
    
    Return :
    int : le salaire horaire
    """
    return a / b

# demande le salaire annuel à l'utilisateur
def demander_salaire() :
    """
    Cette fonction demande le salaire annuel à l'utilisateur
    
    Parameter :
    none
    
    Return :
    int : le salaire annuel
    """
    return int(input("Quel est votre salaire annuel ?"))

# demande le nombre d'heures travaillées par semaine à l'utilisateur
def demander_heures() :
    """
    Cette fonction demande le nombre d'heures travaillées par semaine à l'utilisateur
    
    Parameter :
    none
    
    Return :
    int : le nombre d'heures travaillées par semaine
    """
    return int(input("Nombre d'heures travaillées par semaine ?"))

def main() :
    s = demander_salaire()
    h = demander_heures()
    s = salaire_mensuel(s)
    s = salaire_hebdomadaire(s)
    s = salaire_horaire(s, h)
    print(f"Votre salaire horaire est de {s} euros.")

main()
