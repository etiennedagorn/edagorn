#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===============================================================
#  TP Python - L2 Économie - CORRIGÉ LINÉAIRE (sans fonctions)
#  À exécuter dans VS Code ou dans un terminal : python3 tp_corrige_lineaire.py
#  Astuce : commente/décommente des blocs pour tester progressivement.
# ===============================================================

print("\n===============================================================")
print("0) VÉRIFIER L'INSTALLATION (indicatif)")
print("===============================================================\n")

# (Rappel - à faire dans un terminal, pas dans Python)
# Windows :  python --version   (ou)   py -3 --version
# macOS/Linux :  python3 --version
# VS Code : installer l'extension « Python » (Microsoft) + « Jupyter » (optionnel).

print("Si vous voyez ce message, Python s'exécute correctement.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("1) ORGANISATION DE DOSSIERS (rappel, à faire dans le terminal)")
print("===============================================================\n")

# À taper dans un terminal (pas dans Python) :
# macOS / Linux :
#   cd ~/Bureau
#   mkdir Python_L2
#   cd Python_L2
#   mkdir TP1 data scripts notes
#   ls
# Windows (PowerShell) :
#   cd $env:USERPROFILE\Desktop
#   mkdir Python_L2
#   cd Python_L2
#   mkdir TP1, data, scripts, notes
#   dir
print("Voir les commandes dans les commentaires ci-dessus.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("2) SCRIPT VS INTERPRÉTEUR (démo)")
print("===============================================================\n")

print('Exemple de contenu de scripts/hello.py : print("Bonjour Python !")')
print("Différences : interpréteur = interactif ligne par ligne ; script = fichier réutilisable.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("3) PYTHON COMME CALCULATRICE")
print("===============================================================\n")

print("2 + 5 =", 2 + 5)          # 7
print("10 - 3 =", 10 - 3)        # 7
print("4 * 7 =", 4 * 7)          # 28
print("20 / 6 =", 20 / 6)        # 3.333... (float)
print("20 // 6 =", 20 // 6)      # 3 (division entière)
print("20 % 6 =", 20 % 6)        # 2 (reste)
print("2 ** 5 =", 2 ** 5)        # 32 (puissance)

print("\n→ En Python, '/' renvoie toujours un float. '//' fait la division entière. '%' donne le reste.\n")

# ----------------------------------------------------------------
#je fais la question 4 pour tester xx
# print(int(3.4))
# Messageur d'erreur car 
# print("\n===============================================================")
print("4) ORDRE DES OPÉRATIONS")
print("===============================================================\n")

print("2 + 3 * 4 =", 2 + 3 * 4)      # 14 (multiplication avant addition)
print("(2 + 3) * 4 =", (2 + 3) * 4)  # 20

print("\n→ Python respecte les priorités usuelles. Utilisez des parenthèses pour la lisibilité.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("5) CHAÎNES DE CARACTÈRES")
print("===============================================================\n")

print('"Bonjour" + " le monde" =', "Bonjour" + " le monde")  # concaténation
print('"Python" * 3 =', "Python" * 3)                        # répétition

texte = "Université de Lille"
print('len("Université de Lille") =', len(texte))            # 21 (espaces inclus)
mot = "Python"
print('mot = "Python"')
print("mot[0] =", mot[0])         # 'P'
print("mot[-1] =", mot[-1])       # 'n'

print("\n→ len(...) compte tous les caractères, y compris les espaces.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("6) VARIABLES ET TYPES DE BASE")
print("===============================================================\n")

nom = "Alice"        # str
age = 22             # int
revenu = 1450.75     # float
etudiant = True      # bool

print("nom =", nom, "(type:", type(nom), ")")
print("age =", age, "(type:", type(age), ")")
print("revenu =", revenu, "(type:", type(revenu), ")")
print("etudiant =", etudiant, "(type:", type(etudiant), ")")

print("\nDiff. int vs float : int = entier, float = nombre à virgule.")
print("Ex : 22 == 22.0 ->", 22 == 22.0, "mais type(22) != type(22.0)\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("7) CONVERSIONS DE TYPES (CASTS)")
print("===============================================================\n")

age_str = "22"
print('int("22") + 3 =', int(age_str) + 3)       # 25
print('str(22) + " ans" =', str(22) + " ans")     # "22 ans"

print("\nTentative int('3.14') -> erreur :")
try:
    print(int("3.14"))
except ValueError as e:
    print("ValueError attrapée :", e)

print("float('3.14') =", float("3.14"))           # 3.14

print("\n→ Toujours convertir clairement les types avant les opérations.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("8) AFFICHAGE FORMATÉ")
print("===============================================================\n")

print(nom, "a", age, "ans")             # ajoute des espaces par défaut
print(f"{nom} a {age} ans")             # f-string : plus compact, lisible

montant = 1234.56789
print(f"Montant formaté à 2 décimales : {montant:.2f} €")

print("\n→ Les f-strings permettent d’intégrer expressions, arrondis, etc.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("9) LISTES")
print("===============================================================\n")

notes = [12, 15, 9]
print("notes =", notes)
print("notes[0] =", notes[0])   # accès par indice
notes.append(14)                # ajoute à la fin
print("Après append(14) :", notes)
notes[0] = 20                   # modifie l'élément 0
print("Après modification notes[0]=20 :", notes)
moyenne = sum(notes) / len(notes)
print("Moyenne =", moyenne)

print("\n→ Les listes sont mutables (modifiables). Les chaînes ne le sont pas.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("10) INDEXATION ET TRANCHES (SLICING) DE CHAÎNES")
print("===============================================================\n")

mot = "Python"
print("mot =", mot)
print("mot[0] =", mot[0])        # 'P'
print("mot[-1] =", mot[-1])      # 'n'
print("mot[0:3] =", mot[0:3])    # 'Pyt'
print("mot[2:] =", mot[2:])      # à partir de l'indice 2 -> 'thon'
print("mot[::-1] =", mot[::-1])  # renverse la chaîne -> 'nohtyP'
print("mot[-3:] =", mot[-3:])    # 3 dernières lettres -> 'hon'

print("\n→ Tranches : [début:fin:pas], fin exclus. Les indices négatifs partent de la fin.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("11) MISE À JOUR DE VARIABLE")
print("===============================================================\n")

x = 5
print("x démarre à :", x)
x = x + 1
print("x = x + 1 ->", x)
x += 1
print("x += 1 ->", x)

print("\n→ 'x += 1' est un raccourci de 'x = x + 1'.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("12) BOOLÉENS SIMPLES")
print("===============================================================\n")

x = 10
print("x =", x)
print("x > 5 ->", x > 5)     # True
print("x == 10 ->", x == 10) # True
print("x != 8 ->", x != 8)   # True
print("x < 5 ->", x < 5)     # False

print("\n→ '=' affecte une valeur ; '==' compare l'égalité.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("13) OPÉRATEURS LOGIQUES")
print("===============================================================\n")

a = True
b = False
print("a and b ->", a and b)  # False
print("a or b  ->", a or b)   # True
print("not a   ->", not a)    # False

print("\nTables de vérité (rappel) :")
print("and : True si les deux sont True")
print("or  : True si au moins un est True")
print("not : inverse le booléen\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("14) BOOLÉENS IMPLICITES")
print("===============================================================\n")

print("bool(0)      ->", bool(0))       # False
print("bool(42)     ->", bool(42))      # True
print('bool("")     ->', bool(""))      # False (chaîne vide)
print('bool(" ")    ->', bool(" "))     # True (chaîne non vide)
print("bool([])     ->", bool([]))      # False (liste vide)
print("bool([1,2])  ->", bool([1,2]))   # True (liste non vide)
print("bool({})     ->", bool({}))      # False (dict vide)

print("\n→ Les « conteneurs » vides (0, '', [], {}) sont False. Le reste est True.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("15) MINI-DÉFIS")
print("===============================================================\n")

# 15.1 Somme, différence, produit, quotient
x, y = 8, 3
print(f"x={x}, y={y}")
print("Somme =", x + y)
print("Différence =", x - y)
print("Produit =", x * y)
print("Quotient (/) =", x / y)     # division réelle
print("Division entière (//) =", x // y)
print("Reste (%) =", x % y)

# 15.2 input() - en environnement non interactif, on protège avec try/except
print("\nDémo input() (peut être désactivée en environnement non interactif) :")
try:
    # Décommentez la ligne suivante pour tester en local :
    prenom = input("Est-ce que tu aimes beaucoup python ")
    print("", prenom)
    print(prenom*2)
    print("→ (Exercice interactif : utiliser input('Votre prénom : ') puis afficher Bonjour ...)")
except Exception as e:
    print("Input non disponible ici :", e)

# 15.3 Liste de prénoms
prenoms = ["Lucie", "Amine", "Sara"]
print("\nprenoms =", prenoms)
print("Le deuxième prénom (index 1) est :", prenoms[1])

# 15.4 Erreur de type puis conversion
print('\n"2" + 3 -> erreur de type ; int("2") + 3 ->', int("2") + 3)

# 15.5 Bonus : multiplication d’une chaîne
print('"2" * 3 ->', "2" * 3, "(répète la chaîne)")

# Longueur d’une liste
print("len(prenoms) ->", len(prenoms))

print("\n→ Ces défis illustrent l’importance des types et des conversions explicites.\n")

# ----------------------------------------------------------------
print("\n===============================================================")
print("ANNEXE : MESSAGES D’ERREUR FRÉQUENTS (récapitulatif)")
print("===============================================================\n")

print("SyntaxError: invalid syntax  -> parenthèse, guillemet, deux-points manquants, etc.")
print("NameError: name 'x' is not defined -> variable utilisée avant d'être définie.")
print('TypeError: can only concatenate str (not "int") to str -> il faut convertir, ex: str(2) ou int("2").')
print("ValueError: invalid literal for int() with base 10 -> ex: int('3.14') impossible, utiliser float('3.14').")

print("\n=== Fin du corrigé linéaire. Bon travail ! ===\n")
