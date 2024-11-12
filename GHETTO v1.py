print("GHETTO")
print("Un minijeu second degré par A²MK")
print("Ce jeu est déconseillé aux arabes, aux islamo-gauchistes, aux moutons, aux femmes voilées, aux terroristes, aux pilotes d'avion, aux juifs et aux gens premier degré. Surtout aux gens premier degré")
print("Jouez à vos risques et périls")
start=str(input("Commencer ?"))
if start=="oui":
  print("Que le jeu commence...")
if start!="oui":
  print("On commence quand même, clochard.")
#Début
print("Il y a un an maintenant, vous avez évité les attentats du 11 septembre en devenant ami avec Mamadou Hamed Benzema.")
print("Aujourd'hui, vous partez en vacances avec lui dans son pays natal, le Maroc. Mais à l'entrée de la ville de Wallawah, il part acheter du sable (comme votre père il y a fort longtemps)... Maintenant seul, vous devez trouver quoi faire.")
print("(1) : Retourner dans le désert")
print("(2) : Entrer à Wallawah")
c1=int(input(""))
#Mauvaise fin
if c1==1:
  print("Vous retournez dans le désert. Vous vous perdez, et vous mourez comme une merde.")
  print("Vous auriez pu faire un effort... Il y avait tout un jeu après !")
#Entrée à Wallawah
if c1==2:
  print("Vous entrez à Wallawah.")
  print("CHAPITRE 1 : LE MARCHÉ")
  print("Vous êtes à l'entrée de la ville, dans le marché de Wallawah. Partout autour de vous, des commerçants vendent leurs produits. Des épices, des moutons, des esclaves, des tapis, des céréales...Vous vous approchez d'un marchand pour vous orienter dans la ville. Mais il n'accepte de vous aider que si vous lui achetez un mouton.")
  print("Le problème, c'est que vous n'avez pas d'argent sur vous. Choisissez bien votre réponse.")
  print("(1) : Désolé, je n'ai pas d'argent sur moi... (2) : Ne t'inquiète pas mon frère, je te paierai demain !")
  c2=int(input(""))
  if c2==1:
    print("Wallah ! s'exclame le marchand. Va t'en, jeune gueux !")
    print("Vous vous perdez dans la ville et vous êtes mangé par les mendiants.")
  if c2==2:
    print("Wallah d'accord ! Le marchand accepte, et vous emmène vers la place de Wallawah.")
    print("Vous voilà à la place ! dit le marchand")
    print("(1) : 'Ok merci, à demain mon reuf ! (2) : 'Non' 3 : 'Tu ne reverras jamais ton argent")
    cMouton=int(input(""))
    if cMouton==1:
      print("De rien ! dit le marchand alors qu'il s'éloigne dans la rue.")
      #La Place
      print("CHAPITRE 2 : LA PLACE")
      print("Arrivé à la place, plusieurs chemins s'offrent à vous. Au bout du premier, vous voyez des immeubles de plusieurs étages. Au bout du deuxième apparaît un somptueux palais oriental. Au bout du troisième, enfin, il y a une oasis.")
      print("(1) : Premier chemin (2) : Deuxième chemin (3) : Troisième chemin")
      c3=int(input(""))
      if c3==1:
        print("CHAPITRE 2A : Les HLM")
        print("Vous entrez dans la zone des immeubles. Les bâtiments s'étalent à perte de vue (ce qui ne fait pas loin, car l'air est saturé de sable). Partout des femmes font griller du mouton, et les hommes se tirent dessus.")
        print("Le marchand revient en courant. 'Mon ami ! Mon ami !' dit-il. 'J'aurais besoin que tu me rendes un petit service...'")
        print("(1) : Quoi, mon ami ? (2) : Va te faire voir")
        c3a=int(input(""))
        if c3a==1:
          print("'Ma grand-mère est très malade' dit le marchand. 'J'aurais besoin que tu lui apportes ceci', dit-il en vous remettant un mouton saucisonné. Sa laine brille comme de l'or.")
          print("(1) : Accepter (2) : Refuser")
          c3a2=int(input(""))
          if c3a2==1:
            print("Le marchand vous donne le mouton. En route vers la maison de madame Hal-Wakbar...")
            print("Vous arrivez dans le hall de l'immeuble de la grand-mère. Elle habite au cinquième étage.")
            print("(1) : Prendre l'escalier (2) : Prendre l'ascenseur")
            c3a3=int(input(""))
            if c3a3==1:
              print("Vous prenez l'escalier. Après trois étages, l'escalier s'effondre devant vous. Il y a un tapis volant d'urgence pour ce genre de situation, mais il vous demande 50 dinars pour passer.")
              print("(1) : Payer (2) : Ne pas payer")
              c3a4=int(input(""))
              if c3a4==1:
                print("Vous payez 50 dinars et le tapis volant se déplie... sur un mètre.")
                print("(1) : Sauter (2) : Courir sur le mur")
                c3a5=int(input(""))
                if c3a5==1:
                  print("Vous essayez de sauter...")
                  print("Trop court. C'est ce qu'elle disait aussi...")
                  print("Vous tombez de trois étages et vous étalez comme un caca.")
                  print("FIN du parkour")
                if c3a5==2:
                  print("Vous courez sur le mur, avec toute la force que vous confère le Mouton Doré. Vous atteignez l'autre côté.")
                  print("Vous arrivez devant la porte de madame Hal-Wakbar. Il y a une sonnette et un heurtoir.")
                  print("(1) : Sonner (2) : Toquer")
                  c3a6=int(input(""))
                  if c3a6==1:
                    print("Vous sonnez. Une vieille dame ouvre la porte. 'Oh, bonjour mon enfant...' Elle vous accueille à l'intérieur. 'Prenez donc un peu de thé...' Vous vous installez sur un tabouret, et elle installe une théière sur la table basse.")
                    print("(1) : Boire (2) : Lui lancer la tasse à la figure.")
                    c3a7=int(input(""))
                    if c3a7==1:
                      print("Vous buvez son thé à la menthe...C'est de la menthe, pas vrai ?")
                      print("FIN empoisonnée")
                    if c3a7==2:
                      print("Vous balancez la tasse au visage de la vieille femme. Elle meurt. Le marchand arrive, furieux : 'Tu as tué ma mamie !!! ALLAH WAKBAR !' Vous vous enfuyez, mais vous entendez derrière vous l'explosion du marchand. Les gardes arrivent derrière vous : 'Il a tué madame Hal-Wakbar !'")
                      print("Vous quittez Wallawah et vous enfuyez dans le désert. Au nord, vous voyez des montagnes. Au sud, des dunes.")
                      print("(1) : Vers les montagnes (2) : Vers les dunes")
                      c3a8=int(input(""))
                      if c3a8==1:
                        print("Vous rejoignez un groupe de migrants dans les montagnes. Vous partez tous ensemble vers la France, pays de la Liberté et du Racisme.")
                        print("À SUIVRE...")
                      if c3a8==2:
                        print("Vous allez vers les dunes, où vous mourez de soif.")
                        print("FIN asséchée")
                  if c3a6==2:
                    print("Vous frappez la porte avec le heurtoir. Mais elle est fragile, et explose en un million d'éclats de bois. Derrière, la vieille dame vous attend avec un pistolet-mitrailleur...")
                    print("FIN mitraillée")
              if c3a4==2:
                print("Vous refusez de payer. Une armée de tapis remonte du sous-sol et vous pourchasse. Vous trébuchez et tombez de trois étages. Vous finissez en marmelade.")
                print("FIN juive")
            if c3a3==2:
              print("Vous entrez dans l'ascenseur, qui commence à monter. Après trois étages, il s'arrête.")
              print("(1) : Attendre (2) : Sortir par en haut")
              c3a4=int(input(""))
              if c3a4==1:
                print("Après trois mois, l'ascenseur n'a pas bougé. Vous mourez d'ennui.")
                print("FIN stupide")
              if c3a4==2:
                print("Vous sortez par la trappe et commencez à escalader le câble.")
                print("C'est là que l'ascenseur redémarre et vous emporte. Votre gros orteil se coince dans la poulie et vous mourez écrasé dans d'atroces souffrances.")
                print("FIN ascensionnelle")
          if c3a2==2:
            print("Le marchand vous brise le crâne avec un mouton.")
            print("Vous vous réveillez dans un lit blanc. Un homme s'approche de vous. 'Bravo, vous êtes sortis de la Matrice'...")
            print("FIN de la Matrice")
        if c3a==2:
          print("Le marchand vous brise le crâne avec un mouton.")
          print("Vous vous réveillez dans un lit blanc. Un homme s'approche de vous. 'Bravo, vous êtes sortis de la Matrice'...")
          print("FIN de la Matrice")
      if c3==2:
        print("CHAPITRE 2B : Le Palais")
        print("Vous arrivez devant le mur du palais. Deux gardes protègent la porte. Vous vous approchez d'eux.")
        print("(1) : Demander à entrer (2) : Saluer les gardes")
        c3b=int(input(""))
        if c3b==1:
          print("'Non.'")
          print("Les gardes vous ayant refusé l'entrée, vous hésitez à partir.")
          print("(1) : Forcer l'entrée (2) : Partir (3) : S'introduire de nuit")
          c3b1=int(input(""))
          if c3b1==1:
            print("Vous faites mine de partir, mais au dernier moment vous foncez sur les gardes. L'un d'entre eux vous stoppe d'une main avant de vous plaquer au sol.")
            print("Vous perdez connaissance.")
            print("Vous vous réveillez dans un lit blanc. Un homme s'approche de vous. 'Bravo, vous êtes sortis de la Matrice'...")
            print("FIN de la Matrice")
          if c3b1==2:
            print("Vous partez.")
            print("...")
            print("...")
            print("...")
            print("Vous trébuchez sur un mendiant et vous vous cassez le crâne.")
            print("Vous vous réveillez dans un lit blanc. Un homme s'approche de vous. 'Bravo, vous êtes sortis de la Matrice'...")
            print("FIN de la Matrice (alternative)")
          if c3b1==3:
            print("Vous décidez de vous introduire à la nuit tombée. Après des heures à attendre, le moment arrive enfin...")
            print("Vous arrivez dans les jardins du palais. Plusieurs gardes font leur ronde. Vous évaluez les différents moyens d'entrer dans le bâtiment. Après vous être rappelé les raisons qui vous ont poussé à vous introduire par effraction dans le palais du calife de Wallawah (il n'y en a pas), vous vous préparez à entrer.")
            print("(1) : Escalader le mur (2) : Entrer par en bas")
            c3b2=int(input(""))
            if c3b2==1:
              print("Vous escaladez le mur et arrivez sur le balcon. Par la fenêtre, vous voyez un lit qui semble occupé. Vous entrez dans la chambre et découvrez le calife endormi.")
              print("(1) : Réveiller le calife (2) : Marcher silencieusement")
              c3b3=int(input(""))
              if c3b3==1:
                print("Vous réveillez le calife. Malheureusement, en bon mari, celui-ci dort avec sa ceinture...")
                print("FIN honteuse...")
              if c3b3==2:
                print("Vous marchez aussi silencieusement que possible dans la chambre du calife. Vous arrivez enfin dans le couloir.")
                print("Soudain, une alarme se met à sonner !")
                print("(1) : Sauter du balcon (2) : Se cacher sous le lit.")
                c3b4=int(input(""))
                if c3b4==1:
                  print("Vous courez à travers la chambre et sautez du balcon. Au dernier moment, vous vous rattrapez à la corniche. Plusieurs gardes arrivent à votre poursuite et enjambent la rambarde, croyant que vous avez sauté. Vous entendez des bruits ressemblant à ceux de bombes à eau en train de s'écraser...")
                  print("Le calife lui-même se penche au balcon pour voir ses soldats, mais sa masse immense le fait basculer... Cela fait cette fois le son d'une boulette de viande tombant de dix mètres. C'en est une, après tout.")
                  print("Vous jetez un regard en bas pour contempler la marmelade qui tache le sol et votre casier judiciaire, puis vous remontez dans la chambre de feu le calife.")
                  print("Vous quittez le palais en vitesse, avant qu'on découvre ce qui est arrivé au calife, et récupérez au passage une statue de mouton en or. Vous voilà fugitif...")
                  print("Vous achetez quelques provisions et un mouton(en promettant de payer le lendemain) puis quittez Wallawah. Vous voilà dans le désert.")
                  print("(1) : Partir dans les montagnes (2) : Partir dans les dunes")
                  c3b5=int(input(""))
                  if c3b5==1:
                    print("Vous partez dans les montagnes. Là, vous trouvez un campement, où se trouvent une vingtaine de personnes. Un vieux barbu vous explique qu'ils se préparent à traverser la méditerranée pour se rendre en France.")
                    print("(1) : Partir avec eux (2) : Rester dans le désert")
                    c3b6=int(input(""))
                    if c3b6==1:
                      print("Vous voyagez jusqu'à la Méditerranée, et arrivez en France, pays de la Liberté et du Racisme.")
                      print("À SUIVRE...")
                    if c3b6==2:
                      print("Le barbu vous vole vos provisions et vous mourez de faim dans le désert.")
                      print("FIN de victime, va")
                  if c3b5==2:
                    print("Vous partez dans les dunes. Wallawah disparaît déjà à l'horizon, lorsque vous entendez un grondement.")
                    print("Vous mourrez dévoré par un ver de sable.")
                    print("FIN sablonneuse")
                if c3b4==2:
                  print("Vous vous cachez sous le lit du calife. Là, vous tombez nez à nez avec un enfant porté disparu... C'est quand vous commencez à sortir la tête que le gros calife tombe du lit.")
                  print("FIN écrabouillée")
            if c3b2==2:
              print("Vous passez par une fenêtre du rez-de-chaussée... Pour déboucher sur un cercle de moutons buvant du thé.")
              print("Vous mourez encorné.")
              print("FIN")
        if c3b==2:
          print("Vous saluez les gardes, mais ce geste est ici considéré comme Haram. Vous êtes exécuté.")
          print("FIN Haram")
      if c3==3:
        print("CHAPITRE 2C : L'Oasis")
        print("Vous approchez de l'Oasis. L'eau est verte.")
        print("(1) : Se baigner (2) : Boire")
        c3c=int(input(""))
        if c3c==1:
          print("Vous vous baignez dans l'oasis. Malheureusement, il y avait des crocodiles...")
          print("Vous mourez dévoré.")
          print("FIN")
        if c3c==2:
          print("Vous goûtez l'eau de l'oasis. Si seulement vous aviez vu le chameau en train d'y pisser...")
          print("Vous mourez d'intoxication.")
          print("FIN")
    #Quête alternative Mouton
    if cMouton==2 or cMouton==3:
      print("Par Allah, vous êtes si malpoli que le marchand vous transforme en mouton.")
      print("(1) : Manger de l'herbe (2) : Manger du sable")
      cMouton2=int(input(""))
      if cMouton2==1:
        print("Il n'y a pas d'herbe à manger.")
        print("Soudain, vous entendez des cris. Tous les habitants de Wallawah vous poursuivent pour vous manger.")
        print("(1) : Courir (2) : Se cacher (3) : Attaquer")
        cMouton3=int(input(""))
        if cMouton3==1:
          print("Les habitants vous rattrapent et font une bonne tajine.")
          print("FIN")
        if cMouton3==2:
          print("Vous vous cachez dans un enclos de cochons.")
          print("Mais c'est tellement Haram que vous mourez.")
          print("FIN Haram")
        if cMouton3==3:
          print("Vous essayez de vous défendre, mais le marchand se fait exploser sur vous et vous finissez en couscous.")
          print("FIN")
      if cMouton2==2:
        print("Tu vas vraiment manger du sable, mon reuf ? Ok, tu meurs.")
        print("FIN")