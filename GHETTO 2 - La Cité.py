#Variables
money=0
billet=0
#Introduction
print("GHETTO")
print("Épisode 2 : La Cité")
print("Un mini-jeu de A²MK")
print("Ce jeu est toujours déconseillé aux gens premier degré, aux banlieusards, aux immigrés, aux racistes, aux beaufs, aux gauchistes, à Zemmour et aux policiers")
print("La complétion de GHETTO peut s'avérer nécessaire pour comprendre l'histoire.")
print("Jouez à vos risques et périls.")
start = str(input("Commencer ?"))
if start == "oui":
  print("Retour au jeu...")
else:
  print("Retour au jeu, rageux")
#Début du jeu
print("  Un an après avoir évité les attentats du 11 septembre grâce à votre amitié avec Mamadou Hamed Benzema, vous vous êtes rendu dans la ville marocaine de Wallawah. Là, vous avez vécu des aventures palpitantes avant de prendre la mer vers la France, pays de la Liberté et du Racisme...")
print("")
print("#CHAPITRE 3 : LA MER")
print("")
print("  Vous êtes sur la mer Méditerranée, de nuit, au coeur d'une tempête. Les adultes crient, les enfant passent par-dessus bord. Vous vous inquiétez de la suite du voyage, et vous voulez interroger le capitaine.")
print("(1) : Laisser le capitaine, il est bien assez occupé (2) : Bah, il peut bien répondre à une question ! ")
c = int(input("Option:"))
if c == 1:
  print("  Vous préférez ne pas déranger le capitaine. Mais c'est à ce moment-là qu'une grosse vague l'aspire dans l'eau (RIP).")
if c == 2:
  print("  Vous interpellez le capitaine. Mais lorsqu'il se retourne, une grosse vague l'entraîne dans la mer (RIP).")
print("Le capitaine venant de vous claquer sous les yeux, vous hésitez sur la conduite à suivre. Vous n'avez pas de permis bateau, mais tous les autres passagers sont à moitié noyés.")
print("(1) : Un bateau, c'est comme une voiture, non ? NON ? (2) : Nager, vous étiez champion en CE1 (3) : 'Inch'allah' ")
c1 = int(input("Option:"))
if c1 == 1:
  print( "  Vous prenez les commandes du bateau, avant de vous rappeler que vous n'avez pas de permis de conduire. Et non, ce n'est pas comme la Toyota de votre mère. Le bateau a vite fait de se retourner, plongeant tout le monde dans la mer. Y compris vous.")
  print("Vous venez de commencer le jeu, et vous mourez noyé...")
  print("FIN du permis")
if c1 == 2:
  #Suite
  print("  Vous vous élancez à la nage dans la mer Méditerranée. C'est drôlement froid. Après pas mal de mètres, vous vous retournez : le bateau n'est plus là. Soit vous êtes très rapide, soit le fond de la mer n'est pas visible...")
  print("  Vous nagez de toute la force de vos bras, jusqu'à croiser un autre bateau. Dessus, deux hommes jouent aux cartes, pendant qu'un troisième tient le gouvernail. Ces trois hommes ressemblent à cet oncle que les parents n'invitent jamais aux repas de famille. Vous savez, celui qui a fait de la prison...")
  print("  Ce bateau représente votre salut, mais ses passagers semblent peu fréquentables.")
  print("(1) : Monter sur le bateau (2) : Continuer à la nage ")
  c2 = int(input("Option:"))
  if c2 == 1:
    #Suite
    print("  Vous montez sur le bateau. Les deux hommes en train de jouer aux cartes vous regardent comme si vous étiez un immigré clandestin. Oh, attendez, c'est le cas. Ils s'approchent de vous et vous jaugent du regard. Soudain, vous trébuchez sur le pont glissant, et poussez accidentellement l'un des deux à la mer. L'autre, un gros baraqué tatoué - pourquoi n'est-ce pas celui-là qui s'est noyé ?? - se penche au-dessus du bastingage et crie son nom. C'est une occasion à saisir.")
    print("(1) : Le pousser (2) : Le tirer ")
    c3 = int(input("Option:"))
    if c3 == 1:
      print("  Vous poussez le baraqué par-dessus bord. En tombant, il produit un grand 'plouf' qui attire l'attention du conducteur, un colosse chauve qui vous fonce dessus. Heureusement, le pont est glissant pour tout le monde, et il bascule sur la barrière. Et voilà, bon appétit les poissons.")
      print("  Vous voilà propriétaire d'un bateau...")
      print("(1) : Bon, ce bateau-là a l'air facile à conduire... (2) : Mieux vaut nager avant que la Marine vous retrouve ! ")
      c4 = int(input("Option:"))
      if c4 == 1:
        print("  Par chance, ce bateau-là est facile à piloter. Si vous aviez essayé le vieux Zodiac du passeur qui vous avait amené ici, vous seriez déjà par le fond...")
        print("  Après plusieurs heures de galères, la tempête se termine. Vous décidez d'aller voir le contenu de la cale. Vous descendez et trouvez une boîte pleine de billets. Vous hésitez à la prendre")
        print("(1) : Mais... euh... voler c'est mal, non ? (2) : BIZNESS IS BIZNESS ")
        cMoney = int(input("Option:"))
        if cMoney == 1:
          print("  Vous décidez de laisser l'argent en place.")
        if cMoney == 2:
          money = 20
          print("  Vous ramassez l'argent. Vous avez maintenant %s euros sur vous." % money)
        print("Vous ressortez de la cale du bateau. Vous recommencez à conduire et, après quelques heures plus agréables que la tempête, vous arrivez enfin sur une plage. Elle semble déserte. Vous mettez enfin pied à terre. Vous voici enfin en France.")
        print("  Le jour commence à se lever. Une journée durant laquelle vous allez essayer de vous en sortir dans la ville de Port-Ghetto... Quelque chose vous dit que ça risque d'être pire que Wallawah.")
        print("")
        print("#CHAPITRE 4 : PORT-GHETTO")
        print("")
        print("  Vous voudriez demander à quelqu'un de vous orienter dans la ville, mais vous vous souvenez du marchand de Wallawah. Vous préférez aller voir une carte affichée sur un arrêt de bus. Là, vous voyez une gare, d'où part un TGV qui peut vous ramener à Paris. Voilà votre nouvel objectif !")
        print("  Cependant, la gare est assez loin, et vous risquez d'avoir besoin d'une voiture.")
        print("(1) : Partir à pied (2) : Aller louer une voiture ")
        c5 = int(input("Option:"))
        #Vers la gare à pied (A)
        if money == 0 or c5 == 1:
          if c5 == 2:
            print("  Vous n'avez pas d'argent pour louer une voiture.")
          print("  Vous vous mettez en route vers la gare, à pied.")
          print("  Vous longez la route quand vous voyez des policiers arrêtés, en train de contrôler un véhicule. C'est une occasion risquée.")
          print("(1) : Voler la voiture (2) : Continuer à pied ")
          c6a=int(input("Option:"))
          if c6a==1:
            print("  Vous passez discrètement derrière eux et montez dans la voiture. Avant qu'ils aient pu comprendre, vous démarrez en trombe. Les policiers essaient de vous poursuivre, mais à pied ce n'est pas très efficace.")
          if c6a==2:
            print("  Vous marchez des heures durant, avant de vous effondrer sur le bord de la route, et de finir écrasé par un camion qui se renverse sur la route.")
            print("FIN écrasée")
        #Vers la gare en voiture (B)
        if c5 == 2 and money == 20:
          print("  Vous vous rendez à l'agence de location de voitures.")
          print("  Il y a des voitures de tous types dans le garage : des citadines, des SUV, des pick-up, des chevaux, des voitures de sport... Cherchant le véhicule le moins cher, vous trouvez un tacot, une antiquité si éloignée des normes de sécurité que le simple fait de la regarder représente un crime. 'Elle n'est pas à vendre' vous dit l'employé. Apparemment, ils comptent récupérer les pièces détachées. Comme s'il allaient en faire quelque chose !")
          money=money-10
          print("  Vous négociez, et il vous la loue finalement pour 10 euros. C'est un prix convenable, alors vous payez. Il vous reste maintenant %s euros en poche." % money)
          print("  Vous vous mettez au volant de la voiture. Vous essayez de démarrer : la voiture démarre en marche arrière (Vous n'avez pas de permis...) Vous tirez sur le levier de vitesse, et elle part cette fois-ci à l'endroit.")
          print("  Vous vous engagez sur la route, en direction de la gare de Port-Ghetto.")
          print("  Vous conduisez tranquillement, quand des policiers vous arrêtent pour vous contrôler (la routine). 'Papiers ?' demandent-ils (vous n'en avez pas) 'Permis de conduire ?'(vous n'en avez pas non plus). Vous allez devoir vous sortir de cette situation épineuse.")
          print("(1) : Vous enfuir (2) : Payer pour leur silence ")
          c6b=int(input("Option:"))
          if c6b==1:
            print("  Vous démarrez en trombe. Derrière vous, les policiers sautent dans leur voiture et se lancent à votre poursuite. Vous accélérez pour leur échapper. Soudain, l'un des policiers sort son bras par la fenêtre, un pistolet à la main. Vous devez réagir, et vite.")
            print("(1) : Accélérer encore (2) : Changer de file")
            c7b=int(input("Option:"))
            if c7b==1:
              print("  Vous accélérez encore plus, mais ce n'est pas suffisant? La rafale de balles du policier atteint votre pneu, et vous dérapez sur la route. Vous reprenez le contrôle de votre véhicule... pour voir l'énorme camion.")
              print("FIN du voyage")
            if c7b==2:
              print("  Vous vous déportez violemment sur le côté. La balle déchire le pneu du véhicule à côté de vous, qui dérape sur la route et s'écrase sur un camion. Le camion, déséquilibré par le choc, se renverse au milieu de la route. Vous commencez déjà à paniquer, quand une pile de pneus tomber du camion vous sert de tremplin, vous projetant par-dessus le camion. Derrière vous, la voiture de police explose en percutant l'épave.")
          if c6b==2:
            money=money-10
            print("  Les policiers acceptent l'argent avec plaisir. Vous n'avez plus rien en poche, mais vous êtes libre.")
        #Arrivée à la gare, indifféremment du scénario choisi.
        print("  Vous arrivez finalement à la gare.")
        print("")
        print("#CHAPITRE 5 : LA GARE")
        print("")
        print("  Vous vous rendez au guichet pour acheter un billet de train pour Paris.")
        if money>0:
          print("  Vous achetez le billet avec l'argent qui vous reste.")
          money=0
          billet=1
        else:
          print("  C'est là que vous réalisez que vous n'avez pas d'argent pour le train... Comment allez-vous rentrer à Paris ?")
          print("(1) : Voler le billet, c'est pour la bonne cause ! (2) : S'introduire dans le train. ")
          c8=int(input("Option:"))
          if c8==1:
            print("  Vous attendez que l'employée parte prendre sa pause déjeuner pour vous introduire. Vous forcez sans problème la porte, et vous retrouvez à l'intérieur. Là, vous voyez la borne qui imprime les tickets. Cependant, lorsque vous appuyez sur le bouton, rien ne se passe : la machine est débranchée. Lorsque vous essayez de la brancher, une alarme se déclenche. Vous hésitez sur la marche à suivre.")
            print("(1) : Arrêter l'alarme (2) : Récupérer le ticket ")
            c9a=int(input("Option:"))
            if c9a==1:
              print("  Vous essayez d'arrêter l'alarme. Ne trouvant pas le disjoncteur, vous attrapez ce qui ressemble à un presse-papier et le lancez sur la lumière rouge.")
              print("  Celle-ci se brise, et une pluie d'éclats de verre vous tombe dessus. Alors que vous tentez de vous protéger avec vos bras, plusieurs policiers arrivent. Quelques coups de feu plus tard, en bons gardiens de l'ordre, ils abandonnent ce qui reste de vous dans le guichet.")
              print("  Si vous aviez une famille, ils pourraient porter plainte. Mais bon, votre père est parti acheter du sable il y a fort longtemps...")
              print("FIN des forces de l'ordre")
            if c9a==2:
              print("  Vous branchez fébrilement la borne, et récupérez le billet de train qui en sort, avant de partir en courant du guichet.")
              print("  Vous embarquez quelques heures plus tard.")
          if c8==2:
            print("  Vous décidez de vous introduire dans le train. Reste à trouver la marche à suivre...")
            print("(1) : Vous glisser dans cette valise, elle est sans surveillance... (2) : Vous mêler à la foule qui monte dans le train ")
            c9b=int(input("Option:"))
            if c9b==1:
              print("  Vous entrez aussi discrètement que possible dans la valise abandonnée. Vous êtes embarqué dans le train avec les autres bagages.")
              print("  C'est là que vous découvrez que vous partagez votre valise avec un engin explosif...")
              print("FIN arabe")
            if c9b==2:
              print("  Vous entrez dans le train avec la foule. Vous avez réussi !")
        print("  Vous voici dans le train...")
        #Dans le train
        print("")
        print("#CHAPITRE 6 : LE TRAIN")
        print("")
        print("  Vous avez réussi à trouver une bonne place dans le train et vous commencez à vous assoupir, lorsque le contrôleur arrive.")
        print("  Il vous demande vos billets.")
        if billet==0:
          print("  C'est là que vous réalisez que vous n'en avez pas.")
          print("(1) : S'enfuir (2) : Attaquer le contrôleur ")
          c10a=int(input("Option:"))
          if c10a==1:
            print("  Sans réfléchir davantage, vous sautez au plafond et sortez par une trappe. Vous voilà sur le toit du train.")
            print("  Le contrôleur monte pour vous rattraper, en pointant un pistolet sur vous.")
            print("(1) : Désarmer le contrôleur (2) : Sauter du train ")
            c11a=int(input("Option:"))
            if c11a==1:
              print("  Vous sautez sur le contrôleur. Son pistolet tombe.")
              print("  Vous vous retrouvez à vous battre au corps-à-corps. Vous réussissez à prendre le dessus sur le frêle contrôleur de train.")
              print("(1) : Épargner le contrôleur (2) : Le tej du train ")
              c12a=int(input("Option:"))
              if c12a==1:
                print("  Vous laissez le contrôleur se relever. Mais ce faisant, il vous pousse du train...")
                print("FIN par bonté")
              if c12a==2:
                print("  Vous poussez le contrôleur sur le côté. Il tombe au sol et roule sur plusieurs dizaines de mètres avant de s'arrêter. Il va bien, c'est juste une chute à 400km/h !")
                print("  Vous retournez dans le train comme si de rien n'était, et vous reprenez votre sieste...")
            if c11a==2:
              print("  Vous sautez du train. À 400km/h. Je ne vais même pas entrer dans le détail.")
              print("FIN violente")
          if c10a==2:
            print("  Vous vous élancez sur le contrôleur, mais celui-ci avait un pistolet.")
            print("  Dommage, vous étiez presque à la fin de GHETTO 2 !")
            print("FIN presque au bout")
        else:
          print("(1) : Lui présenter votre billet (2) : Flemme ")
          c10b=int(input("Option:"))
          if c10b==1:
            print(" Vous lui montrez votre billet et vous rendormez. ")
          if c10b==2:
            print("  Vous êtes trop fatigué pour présenter le billet au contrôleur, et vous vous recouchez.")
            print("  Il vous le prend cependant de force et, trop fatigué pour riposter, vous vous rendormez.")
        print("  Quand vous vous réveillez, cependant, le paysage ne vous est pas familier. Une voix annonce : 'Mesdames et messieurs, la voie de TGV Port-Ghetto - Paris a été détournée vers la Seine Saint-Denis !'")
        print("  Vous vouliez rentrer à Paris, vous voilà servi. Vous allez devoir vous en sortir dans le 93...")
        print("À SUIVRE...")
        cGénérique=str(input("  Voir le générique ?"))
        if cGénérique!="oui":
          print("  Eh ben on envoie le générique quand même.")
        print("  GHETTO 2 : Un jeu par A²MK")
        print("  Scénario : A²MK")
        print("  Réalisation : A²MK")
        print("  Support : Replit")
        print("  Jeu original : GHETTO par A²MK")
        print("  Musique : Non")
        print("  'GHETTO', 'GHETTO 2', les noms 'Mamadou Hamed Benzema' et 'Hal-Wakbar', les noms de ville 'Wallawah' et 'Port-Ghetto' appartiennent techniquement à A²MK")
        print("  MERCI D'AVOIR JOUÉ")
      if c4 == 2:
        print("  Vous replongez dans l'eau... et vous sentez une main vous aggriper le poignet. Apparemment, le baraqué n'avait pas dit son dernier mot... Vous êtes entraîné sous l'eau.")
        print("FIN débile")
    if c3 == 2:
      print("  Vous tirez l'homme, qui croit que vous voulez vous battre. Il vous frappe et vous perdez connaissance.")
      print("  Vous vous réveillez dans un lit blanc. Un homme s'approche de vous. 'Bravo, vous êtes sortis de la Matrice'...")
      print("FIN de la Matrice")
  if c2 == 2:
    print("  Vous avez bêtement laissé gagner vos préjugés... Après plusieurs kilomètres, vous n'en pouvez plus. Vous buvez beaucoup d'eau et rejoignez vos anciens compagnons d'infortune.")
    print("FIN décevante")
if c1 == 3:
  print("  Vous priez une fois, deux fois, trois fois...")
  print("...")
  print("  Apparemment, Allah ne vous a pas entendu.")
  print("FIN athée")