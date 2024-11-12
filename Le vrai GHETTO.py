import random as rd

#Variables et inventaire
inv = ["sable", "mouton"]
isDead = 0
doFlee = 0
win = 0
route=0
err=0
suite=0
def error():
  global err, isDead
  err=1
  isDead=1

#Introduction
input("Un jeu par A²MK")
input("Avec Ghetto Engine v2.0")
input("GHETTO : Épisode III")
input("Le vrai GHETTO")
input("Ce jeu est fortement déconseillé aux gens premier degré, aux manifestants, aux dealeurs, aux ancien.ne.s, aux gangsters, aux SWAT, aux moutons en or, aux délinquants et à madame Hidalgo")
input("Ce jeu est la suite de GHETTO et GHETTO 2, la complétion de ces jeux peut être nécessaire pour comprendre l'histoire")
input("Ce jeu est purement second degré")
input("Le développeur n'est en aucun cas responsable en cas de dommages psychologiques permanents ou temporaires suite à l'utilisation de ce jeu")
input("Ce jeu est codé avec les fesses, assurez-vous de ne répondre aux choix qu'avec les nombres 1 ou 2 ou votre appareil pourrait vous exploser dessus")
input("Ce jeu est sensiblement plus long que les opus précédents, alors installez-vous confortablement avant de commencer")
input("Jouez à vos risques et périls")
cStart = str(input("Commencer ?"))
if cStart == "oui":
  print("Le dernier volet commence...")
if cStart == "non":
  print("Eh bien on commence quand même.")
print("  Après avoir quitté Wallawah, vous êtes arrivé à Port-Ghetto, où vous avez bataillé pour monter dans un train qui vous ramènerait à Paris. Malheureusement, le trajet a été détourné et vous vous êtes retrouvé dans le Vrai Ghetto : Le 93...")
#Début de l'histoire
print("")
print("#CHAPITRE 7 : LE 93")
print("")
print("  Vous regardez tout autour de vous. Le train s'est véritablement arrêté dans le terrible 93... Partout des immeubles gris, des feux de poubelles, des coups de fusil. Vous n'avez guère envie de descendre ici, mais c'est le terminus...")
print("(1) : Bon ben quand faut y aller...")
print("(2) : Je ne mettrai pas UN PIED dans cet endroit !")
c1=int(input("Choix:"))
if c1==1:
  print("  Vous descendez du train. Il fait assez froid dehors.")
  print("  Alors que vous vous interrogez sur ce que vous faites ici, un vieil homme s'approche de vous. Il porte un bonnet de laine et un hideux blouson vert. Le bas de son visage est caché par une épaisse barbe grise.")
  print("  - Bonjour, mon garçon.")
  print("(1) : - Euh...Vous êtes qui ?")
  print("(2) : - Comment partir d'ici ?")
  c2=int(input("Choix:"))
  if c2==1:
    print("  - Lorsque le sage montre le doigt, l'imbécile regarde la lune... Je suis le sage montrant du doigt la lune...")
    print("  - Ok...Et...Comment on part d'ici ?")
    print("  - Eh bien...On ne peut pas.")
    print("  - Pourquoi ?")
    print("  - Les hommes bleus ont enfermé le peuple avec les fils de la mère...")
    print("  - Vous pouvez parler normalement ?!")
    print("  - Les policiers ont mis en place un immense barrage autour du 93 afin de protéger Paris du terrible gang de Mama Benzema.")
    print("  - Et qu'est-ce qui se passe avec ce fameux gang Benzema ?")
  elif c2==2:
    print("  - Bonjour monsieur, vous savez comment je peux partir d'ici ?")
    print("  - Beaucoup pensent que l'ailleurs est plus vert sur l'herbe...")
    print("  - ...")
    print("  - Tu ne peux pas partir d'ici, car la police a enfermé la zone dans un grand barrage...")
    print("  - Hein ? Mais pourquoi ?")
    print("  - Depuis plusieurs jours, le terrible gang Benzema sème la terreur dans le 93...")
    print("  - Et...pourquoi ?")
  else:
    print("  Félicitations, vous avez skip un dialogue important.")
    print("  Mais en gros, le gang Benzema met le dawa dans le 93.")
  print("  - Le gang Benzema veut s'emparer du Mouton Doré, relique millénaire aux pouvoirs infinis... Mme Hal-Wakbar, la soeur de Mama Benzema, devait rapporter le mouton, mais elle n'est jamais revenue... Par conséquent, le gang cherche activement le Mouton, et est devenu plus dangereux que jamais.")
  print("(1) : - Mama Benzema ?")
  print("(2) : - Et du coup, qu'est-ce que c'est exactement que ce gang ?")
  c3=int(input("Choix:"))
  if c3==1:
    print("  - Ah, Mama Benzema. C'est la femme la plus puissante de la zone. Elle dirige le gang Benzema, qu'elle a hissé en quelques années au rang de plus puissant de tout le 93. Elle voit tout, sait tout, et entend tout. Elle pourrait trouver une botte de foin dans une aiguille... Elle est très dangereuse.")
    print("  - Eh bien nous allons lui apporter ce mouton !")
  elif c3==2:
    print("  - C'est le gang le plus terrible du 93...Il est dirigé par Mama Benzema et ses fils Hamed, Hekim et Mamadou. Il a en quelques années pris le contrôle de toute la zone, et n'a plus guère d'autre ennemi que le gang Rival... Comme le dit le proverbe, la force du meilleur est toujours la plus raisonnable...")
    print("  - Alors ramenons-leur ce mouton, et le 93 sera sauvé !")
  else:
    print("  Félicitations, vous avez skip un dialogue important !")
    print("  Mais bon, en gros, vous avez décidé d'amener le Mouton au gang Benzema...")
  print("  - Quoi ?! Mais tu es malade ?! Ils vont te découper en morceaux !")
  print("  - Quand on leur ramènera le Mouton, ils verront bien qu'ils n'ont aucun intérêt à nous tuer...")
  print("  - Quel 'nous', même ?")
  print("  - Où est la planque du gang ?")
  print("  - Eh bien, je ne le sais pas.")
  print("  L'Ancien caresse sa barbe blanche.")
  print("  - Cependant, je sais qui sait. Et comme on dit, si tu sais que tu ne sauras jamais, tu ne sais pas, mais si tu ne sais jamais que tu sais, tu ne sauras pas !")
  print("  - Et qui c'est qui sait ?")
  print("  - Un ami à moi... Il s'appelle Aboubakar Abdoulaye, mais tout le monde l'appelle Boubou.")
  print("(1) : Aller voir ce 'Boubou'")
  print("(2) : Utiliser un GPS")
  c4=int(input("Choix:"))
  if c4==1:
    print("  Vous vous mettez en route avec l'Ancien pour aller voir Boubou.")
    print("  Au détour d'une rue, vous entendez un vrombissement de moteurs. Soudain, derrière vous, des motards arrivent en trombe. Ils portent des casques marqués d'un R.")
    print("  - Des Rivaux ! crie l'Ancien. Aux abris !")
    print("(1) : COURIR !!")
    print("(2) : Esquiver les motos")
    c5=int(input("Choix:"))
    if c5==1:
      print("  Vous courez soudain plus vite qu'un arc-en-ciel, mais les motos...sont des motos. Les motards vous rattrapent et prennent bien soin de vous...")
      print("FIN rivale")
      isDead=1
    elif c5==2:
      print("  Vous vous jetez sur le côté. Vous sentez l'odeur de gasoil des motos qui passent à toute vitesse à côté de vous.")
      print("  Après vous avoir dépassé d'une dizaine de mètres, les motards font un demi-tour dérapé puis reviennent à la charge, de face cette fois-ci, pour vous casser la figure. Vous regardez autour de vous : l'endroit est désert. Même l'Ancien s'est enfui...")
      print("  Une femme en blouson noir avec un bonnet met le pied à terre.")
      print("  - Donne-nous ce mouton, et  nous ne te ferons pas trop de mal...")
      print("  Même si vous ne vous l'avouez pas, vous avez peur. Peut-être faudrait-il leur donner le Mouton...")
      print("(1) : Leur donner le mouton")
      print("(2) : Garder le mouton")
      c6=int(input("Choix:"))
      if c6==1:
        print("  Vous donnez le Mouton Doré aux motards du gang Rival. La cheffe le tourne entre ses mains avec un air gourmand. Vous soufflez de soulagement : le 93 n'est peut-être pas sauvé, mais vous avez échappé à la mort...")
        print("  Malheureusement, un Benzema passait par là...")
        print("FIN par bonté (appelez ça lâcheté ou égoïsme)")
        isDead=1
      elif c6==2:
        print("  - Non, non. Je garde ce Mouton. Je ne vais pas...")
        print("  Avant que vous ayez pu finir votre phrase, deux Rivaux vous sautent dessus : un gros barbu tatoué, qui n'est pas sans vous rappeler celui que vous avez jeté à la mer, et un grand blond athlétique.")
        print("(1) : Frapper le barbu")
        print("(2) : Frapper l'athlète")
        c7=int(input("Choix:"))
        print("  Vous le frappez. Il recule, et vous en profitez pour repousser l'autre. Les deux tombent au sol. La cheffe sort de Dieu seul sait où un lance-grenades (bizarrement sa poitrine diminue), et commence à tirer. C'est une véritable pluie de bombes qui commence à tomber !")
        print("(1) : Éviter les tirs")
        print("(2) : Eh mais attends, j'ai du sable sur moi, je peux boucher le canon !")
        c8=int(input("Choix:"))
        if c8==1:
          print("  Vous courez en zigzag, et réussissez à éviter un tir, puis deux, puis trois...C'est là que vous trébuchez sur une molécule de dioxygène et vous étalez au sol. Vous voyez la dernière grenade vous retomber dessus...")
          print("FIN explosive")
          isDead=1
        elif c8==2:
          print("  Vous vous précipitez sur la cheffe et fourrez une grosse poignée de sable (premium de Wallawah) dans le canon de son arme. Sous la pression, le lance-grenade lui explose dans les mains !")
          print("  Les derniers motards vous regardent, regardent le barbu et l'athlète au sol, regardent le tas de viande hachée (hallal) qu'est devenue leur cheffe. Vous les regardez, et ramassez un morceau de tube du lance-grenades.")
          print("(1) : Les assommer")
          print("(2) : Les faire fuir")
          c9=int(input("Choix:"))
          if c9==1:
            print("  Vous les neutralisez proprement d'un coup de tube de métal bien placé.")
          elif c9==2:
            print("  Vous les menacez de votre arme de fortune. Ils fuient ventre à terre, abandonnant motos, alliés et dépouille de la cheffe.")
            doFlee=1
          else:
            print("  Votre réponse est invalide, alors on va considérer que vous n'avez rien fait, ce qui laisse le temps aux Rivaux de s'enfuir.")
            doFlee=1
          print("  Vous remarquez alors que quelques grenades subsistent de l'explosion...")
          print("(1) : Ramasser les grenades, qui sait si ça pourrait être utile, pour défoncer une porte par exemple ?")
          print("(2) : Laisser les grenades, ça pourrait être dangereux.")
          c10=int(input("Choix:"))
          if c10==1:
            print("  Vous ramassez les grenades et les rangez précautionneusement dans votre sacoche en peau de mendiant...euh...mouton.")
            inv.append("grenade")
          elif c10==2:
            print("  Vous prenez une grenade, vous éloignez, la dégoupillez et la lancez sur le tas. Tout le stock disparaît dans une grande explosion.")
          else:
            print("  *Soupir* vous choisissez donc de ne rien faire. Vous laissez les grenades en place.")
          print("  C'est alors que l'Ancien surgit d'une poubelle.")
          print("  - Oh, euh, hum...tu t'es bien débrouillé. J'étais parti...chercher de l'aide mais...hum...tu as visiblement pu t'en sortir tout seul.")
          print("  Vous reprenez votre route au côté de l'Ancien. Après quelques minutes de marche, vous arrivez dans une ruelle entre deux immeubles. Les murs sont tagués, et vous voyez un cochon errant se réfugier dans une poubelle. Un homme est assis sur une chaise de camping dans la ruelle.")
          print("(1) : Arriver en mode policier : 'Police ! Où est la planque des Benzema !'")
          print("(2) : Arriver amicalement : 'Salut Boubou ! Comment ça va ?'")
          print("(3) : Arriver en mode arabe : 'As salam aleykoum Aboubakar !'")
          c11=int(input("Choix:"))
          if c11==1:
            print("  Vous faites mine d'être policier. Ce que vous n'aviez pas prévu, c'était que Boubou avait des alliés...")
            print("FIN criminelle")
            isDead=1
          elif c11==2:
            print("  Vous saluez amicalement Boubou. Il vous salue en retour.")
            print("(1) : 'Où est la planque ?'")
            print("(2) : 'Qu'est-ce que tu vends ?")
            c12=int(input("Choix:"))
            if c12==1:
              print("  - Laquelle ? Celle du gang Rival, de Patrick Dophile, du triple K, de...")
              print("(1) : Celle du gang Benzema.")
              print("(2) : Le triple koiiiii? !")
              c12a=int(input("Choix:"))
              if c12a==1:
                print("  - Oh. Celui-là.")
              elif c12a==2:
                print("  La curiosité est un vilain défaut, vous savez...")
                print("FIN anglaise")
                isDead=1
              else:
                error()
            elif c12==2:
              print("  - De la coc...du sucre, des feuilles, et des pistolets (factices bien évidemment)")
              print("(1) : Acheter un pistolet (factice bien évidemment)")
              print("(2) : Ne rien acheter")
              c12b=int(input("Choix:"))
              if c12b==1:
                print("  Vous achetez un pistolet (factice bien évidemment)")
                inv.append("gun")
                print("  - Que veux-tu d'autre ?")
                print("  - La planque du gang Benzema.")
              elif c12b==2:
                print("  Vous n'achetez rien, tout est trop douteux.")
                print("  - Et du coup, où est la planque ?")
              else:
                error()
            else:
              error()
            if isDead==0:
              print("  - Eh bien... Je le sais mais...les informations valent cher.")
              print("  Le dealeur semble avoir une mentalité bien arabe, voire même juive.")
              print("(1) : Retenter une approche de policier")
              print("(2) : Jouer l'idiot")
              c13=int(input("Choix:"))
              if c13==1:
                print("  Vous essayez de jouer les policiers, mais Boubou avait des acolytes cachés...")
                print("FIN criminelle II")
                isDead=1
              elif c13==2:
                print("  - Qu'est-ce que vous voulez dire ?")
                print("  - Eh bien, pour mon commerce, j'aurais besoin de quelques feuilles...")
                print("  - Des feuilles.")
                print("  - Oui, de simples feuilles de canna...CANNE À SUCRE BIEN ÉVIDEMMENT !!! Hassoul, si tu m'en trouves, je t'indiquerai la planque de ces...(il regarde tout autour de lui)...ces Benzema.")
                print("(1) : Accepter")
                print("(2) : Accepter")
                c14=int(input("Choix:"))
                print("  Vous acceptez.")
                print("")
                print("#CHAPITRE 8 : À LA RECHERCHE DES FEUILLES DE CANNA...SUCRE")
                print("")
                print("  - Alors, l'Ancien, où peut-on trouver ces fameuses feuilles ?")
                print("  - Eh bien, nous pouvons nous rendre auprès d'Allah le père dans le ciel, ou dans le giron de la Terre mère...")
                print("  - En clair ?")
                print("  - Nous pouvons aller chercher les feuilles dans la serre communautaire du gratte-ciel, ou dans le laboratoire souterrain du gang Rival.")
                print("  - Eh bien, je pense que nous allons les chercher...")
                print("(1) : Dans la serre")
                print("(2) : Dans le laboratoire")
                cL=int(input("Choix:"))
                if cL==1:#Route A : la serre
                  route=1
                  print("...dans la serre.") 
                  print("  Vous vous mettez en route vers la serre. Lorsque vous arrivez au pied de l'immeuble, vous réalisez à quel point il est immense. Vous vous demandez si ce n'est pas une erreur...")
                  print("  - Les erreurs sont l'escalier qui mène au succès ! dit l'Ancien.")
                  print("  Sur ce proverbe foireux, vous commencez votre ascension. Vous escaladez pendant ce qui vous semble des heures - vous ne pouvez pas en être sûr, la montre que vous a vendu le marchand lybien compte à l'envers. En plus, elle vient avec cette grosse boîte rouge pleine de fils, franchement... - quand vous arrivez au niveau des oiseaux. C'est drôlement haut d'ailleurs.")
                  print("(1) : Continuer à monter")
                  print("(2) : Redescendre")
                  ca1=int(input("Choix:"))
                  if ca1==1:
                    print("  Vous continuez votre ascension. Vous montez encore et encore, jusqu'à atteindre le niveau des nuages...")
                    print("(1) : Continuer à monter")
                    print("(2) : Redescendre")
                    ca2=int(input("Choix:"))
                    if ca2==1:
                      print("  Vous ravalez votre vomi et vous forcez à continuer. Finalement, après une ultime centaine de marches, vous atteignez enfin le toit de l'immeuble.")
                      print("  La serre est immense. À perte de vue s'étend une étendue de plantes, véritable jungle suspendue à trois-cent mètres au-dessus du sol. Vous réalisez alors que vous êtes dans un sacré pétrin : comment retrouver un plant de canna...sucre dans tout ce bazar ? Vous commencez à fouiller tous les pots dont les plantes n'ont pas l'air trop dangereuses. Vous arrivez à une intersection.")
                      print("  Sur la gauche, vous voyez de magnifiques buissons de fleurs multicolores, avec quelques oiseaux morts dans les pots. Sur la droite, vous voyez des buissons pleins d'abeilles.")
                      print("(1) : Aller à gauche, Jean-Luc")
                      print("(2) : Aller à droite, Jean-Marie")
                      ca3=int(input("Choix:"))
                      if ca3==1:
                        print("  Vous vous engagez au milieu des magnifiques plantes. Eh bien, les plantes vénéneuses de la serre du Ghetto ne tuent pas que les oiseaux...")
                        isDead=1
                        print("FIN botanique")
                      elif ca3==2:
                        print("  Vous partez du côté des abeilles. Vous vous faites piquer quelques dizaines de fois, mais vous arrivez à l'autre bout. Dieu merci, vous n'avez pas d'allergie...")
                        print("  Vous vous remettez à la recherche des 'feuilles' de Boubou, mais ce n'est pas facile...")
                        print("  - Un proverbe dit que pour trouver une botte d'aiguilles dans de la paille...")
                        print("(1) : Frapper l'Ancien")
                        print("(2) : Vous boucher les oreilles")
                        print("(3) : Le jeter du haut de l'immeuble")
                        ca4=int(input("Choix:"))
                        if ca4==1:
                          print("  Vous mettez une solide droite à l'Ancien. Du moins vous le croyez, car il a déjà reculé de dix mètres, et vous avez frappé dans le vide.")
                        elif ca4==2:
                          print("  Vous vous bouchez les oreilles, mais ce n'est pas suffisant contre le terrible débit de parole de l'Ancien du 93 (il ferait un rappeur incroyable, si seulement il avait quelque chose à dire).")
                        elif ca4==3:
                          print("  Vous l'attrapez sous votre bras et le lancez de toutes vos forces...")
                          print("  Vous n'avez pas honte d'avoir tué un ancien ?!")
                          print("  Non mais en réalité il va bien, il a rebondi sur son bonnet.")
                        else:
                          print("  Vous faites le très judicieux choix de ne rien faire...")
                        print("  Après bien des recherches, vous trouvez enfin le plant de canne à sucre (c'est de la canne à sucre, pas vrai). C'est alors qu'un homme en blouson, coiffé d'un bonnet, surgit d'une allée. À en juger par le R sur sa doudoune, il fait partie du gang Rival. Et à en juger par son visage tunisien, il s'appelle Hamed. Il plonge sa main dans sa poche et en sort un couteau.")
                        print("  L'Ancien détale comme un lapin. Quand le combat sera fini, il sera parti chercher du secours...")
                        print("  Hamed vous lance le couteau qui vous frôle l'oreille gauche.")
                        print("(1) : Attaquer Hamed")
                        print("(2) : FUIR")
                        ca5=int(input("Choix:"))
                        if ca5==1:
                          print("  Vous vous lancez courageusement contre Hamed. Il avait d'autres couteaux.")
                          print("FIN rivale III (mais combien y en a-t-il ?")
                          isDead=1
                        elif ca5==2:
                          print("  Vous courez de toute la force de vos jambes. Vous fusez plus vite qu'un arabe poursuivi par la police. Vous zigzaguez pour éviter les couteaux qui volent tout autour de vous. Vous arrivez alors à une nouvelle intersection.")
                          print("  Sur la droite, le chemin est bordé d'énormes cactus. Sur la gauche, des plantes carnivores semblent attendre leur prochain repas...")
                          print("(1) : Aller à gauche, Anne")
                          print("(2) : Aller à droite, Marine")
                          ca6=int(input("Choix:"))
                          if ca6==2:
                            print("  Vous allez à droite. J'ai deux mauvaises nouvelles pour vous : la première, c'est que vous êtes raciste (mais est-ce vraiment une mauvaise nouvelle ?). La deuxième, c'est que vous glissez sur un clou qui dépasse et tombez tête la première sur un cactus...")
                            print("FIN du Rassemblement")
                            isDead=1
                          elif ca6==1:
                            print("  Vous allez à gauche. Vous vous jetez au sol de justesse pour éviter une mâchoire végétale. Vous continuez aussi vite que vous le pouvez au sol, sachant pertinemment que vous constituez une cible facile pour Hamed. C'est alors que vous découvrez un sécateur sous l'un des bacs.")
                            print("(1) : Bon, ça pourrait toujours servir pour...libérer un prisonnier par exemple... *le prendre*")
                            print("(2) : Saaah, qui sait où ce truc a traîné ?! *rictus de dégout*")
                            ca7=int(input("Choix:"))
                            if ca7==1:
                              print("  Vous ramassez le sécateur.")
                              inv.append("sec")
                            elif ca7==2:
                              print("  Vous laissez le sécateur.")
                            else:
                              print("  Arrivé si loin, vous avez vraiment mis une réponse invalide. Eh bien, pas de sécateur pour vous !")
                            print("  Vous poursuivez votre progression à quatre pattes, lorsque vous entendez un cri similaire à celui d'un contrôleur tombant d'un train à grande vitesse.")
                            print("(1) : Se lever pour regarder")
                            print("(2) : Continuer à avancer")
                            ca8=int(input("Choix:"))
                            if ca8==1:
                              print("  Vous vous retournez et voyez Hamed en train de se débattre contre une grosse plante carnivore qui lui a attrapé le bras. Il crie plus fort alors que les épaisses lianes le tirent dans la mâchoire du végétal. Alors que l'acide lui ronge les organes, ses cris se transforment en hurlements de douleur. Une fumée acide se dégage de la plante alors qu'elle avale entièrement le Rival, qui a arrêté de se débattre.")
                            elif ca8==2:
                              print("  Vous ne vous arrêtez pas, mais derrière vous les cris se font plus forts. Une odeur de chair brûlée se répand dans la serre.")
                            else:
                              print("  (réponse invalide) Le temps d'hésiter, vous vous éloignez du cri.")
                            print("  Vous atteignez le bout de l'allée. Vous plongez la main dans vos poches : les feuilles de canna...bref y sont toujours. Après être allé récupérer l'Ancien - il était effectivement parti chercher du secours - vous ressortez de la serre...")
                          else:
                            error()
                        else:
                          error()
                      else:
                        error()
                    elif ca2==2:
                      print("  Vous faites demi-tour")
                      print("  C'est ce moment que choisit l'escalier pour s'effondrer - en entier - sous vos pieds (au moins vous êtes redescendu).")
                      print("FIN qui tombe de haut")
                      isDead=1
                    else:
                      error()
                  elif ca1==2:
                    print("  La descente est bien plus rapide que la montée. Cependant, lorsque vous ressortez de l'immeuble, un groupe de Rivaux vous attend en bas...")
                    isDead=1
                    print("FIN rivale II")#Route A - la serre#Route A : la serre
                  else:
                    error()
                elif cL==2:#Route B : le labo
                  route=2
                  print("...dans le laboratoire.") 
                  print("  Vous vous mettez en route vers le laboratoire. Arrivé à l'entrée, vous découvrez un escalier plongeant dans l'obscurité. Vous n'êtes plus très confiant...")
                  print("  - Il faut remonter pour pouvoir toucher le fond !")
                  print("  Sur ce proverbe foireux, vous entamez votre descente. Vous descendez pendant ce qui vous semble des heures. Vous regardez votre montre : elle compte à l'envers. C'est la dernière fois que vous achetez à un marchand lybien une montre qui compte à l'envers, accrochée à un boîtier rouge plein de fils !")
                  print("  Alors que vous commencez à vous demander si vous n'allez pas finir dans l'océan Pacifique, vous arrivez à un embranchement. Sur la droite, vous entendez le bruit d'une centaine de rats ; Sur la gauche, vous voyez des chauves-souris frugivores accrochées au plafond.")
                  print("(1) : La droite, Adolphe")
                  print("(2) : La gauche, Joseph")
                  cb1=int(input("Choix:"))
                  if cb1==1:
                    print("  Vous prenez le chemin de droite. Le sol est relativement plat, et la progression est facile. Cependant, autour de vous, vous voyez de plus en plus de rats...")
                    print("  C'est alors que vous arrivez dans un cul-de-sac. Soudain, une créature géante, fusion de dizaines de rats, surgit de nulle part pour vous attaquer.")
                    print("(1) : Ouah... Il est rat-ciste du coup ?")
                    print("(2) : FUIR")
                    print("(3) : Attaquer")
                    cbRat=int(input("Choix:"))
                    if cbRat==1:
                      print("  Il était effectivement rat-ciste. Et fort.")
                      print("FIN rat-ciste")
                      isDead=1
                    elif cbRat==2:
                      print("  Vous fuyez. Mais il est plus rapide.")
                      print("FIN rat-ciste II")
                      isDead=1
                    elif cbRat==3:
                      print("  Vous vous jetez courageusement sur le monstre, mais vous vous enfoncez simplement dans sa masse et mourez dévoré, réduit en miette par une masse de rongeurs.")
                      print("FIN rat-ciste III")
                      isDead=1
                    else:
                      error()
                  elif cb1==2:
                    print("  Vous prenez à gauche, suivi par l'Ancien.")
                    print("  Vous continuez à descendre, lorsque vous entendez un grondement infernal. Peut-être qu'il y a des travaux pas loin... ou alors un dealeur s'est fait sauter dans la rue ? Vous commencez à vous inquiéter...")
                    print("(1) : Remonter")
                    print("(2) : Continuer")
                    cb2=int(input("Choix:"))
                    if cb2==1:
                      print("  Vous remontez. Mais vous avez dû vous tromper quelque part, parce que vous arrivez dans un labyrinthe souterrain aux murs jaunes pâles.")
                      print("FIN ????")
                      isDead=1
                    elif cb2==2:
                      print("  Vous continuez votre descente, jusqu'à arriver dans une rame de métro. Il y a de la poussière partout, et elle semble plus ou moins désaffectée... Autour de vous poussent des plantes dans des bacs en plastique. Des caisses d'outils sont calées contre les murs.")
                      print("  Vous vous mettez à la recherche des plants de canna...sucre. Vous fouillez chaque bac, vous piquez les doigts, plongez la main dans de l'engrais biologique, mais vous ne trouvez pas les feuilles. Vous finissez par arriver à une intersection. Il y a une porte métallique marquée d'un 3, mais elle est verouillée. Sur la droite, une fumée suspecte flotte dans l'air. Sur la gauche, rien.")
                      print("(1) : La gauche")
                      print("(2) : La droite")
                      cb3=int(input("Choix:"))
                      if cb3==1:
                        print("  Vous vous engagez dans le couloir vide. Il était hantééééééééééééééé")
                        print("FIN hantééééééééeeeeeeeeee")
                        isDead=1
                      elif cb3==2:
                        print("  Vous vous engagez dans le couloir de droite. Vous arrivez bientôt dans une salle. Il y a du matériel de chimie sur les tables, et des feuilles sont en train de sécher sur des plaques chauffantes. Vous voyez aussi des pots où sont plantés des pieds de chan...pignons. Comme Boubou n'a pas précisé s'il voulait ses feuilles fraîches ou sèches, vous prenez des deux. Alors que vous achevez votre 'récolte', un Rival surgit d'un couloir et vous aperçoit. Il porte un badge sur lequel est inscrit le nom 'Hekim'.")
                        print("  L'Ancien s'enfuit.")
                        print("  Hekim dégaine un flashball et commence à vous tirer dessus.")
                        print("(1) : FUIR")
                        print("(2) : Inch'Allah, on va se battre")
                        cb4=int(input("Choix:"))
                        if cb4==1:
                          print("  Vous vous enfuyez, mais Hekim est très doué avec son flashball, et vous n'avez plus de tête.")
                          print("FIN rivale IV")
                          isDead=1
                        elif cb4==2:
                          print("  Vous vous jetez courageusement sur Hekim - en évitant soigneusement le canon du flashball, qui tire frénétiquement - et vous réussissez à le plaquer au sol.")
                          print("(1) : Frapper aux génitales")
                          print("(2) : Frapper à la tête")
                          cb5=int(input("Choix:"))
                          if cb5==1:
                            print("  Vous frappez Hekim aux bijoux. Il hurle de douleur, et vous repousse violemment. Alors qu'il essaie de se relever, vous le poussez. Il s'effondre sur un alambic en verre, qui se brise en mille morceaux.")
                            print("  Vous vous enfuyez en courant, lorsque vous sentez une odeur de brûlé...")
                            print("(1) : Se retourner pour regarder")
                            print("(2) : Continuer")
                            cb6=int(input("Choix:"))
                            if cb6==1:
                              print("  Vous vous retournez et découvrez un spectacle terrible : Dieu seul sait ce que contenait cet alambic, mais à présent tout est en feu. Les plants sont dévorés par les flammes et toute la pièce est nimbée d'une lueur orange. Hekim revient soudain à lui, et fonce vers la porte.")
                              print("(1) : Verrouiller la porte")
                              print("(2) : Le laisser sortir")
                              cb7=int(input("Choix:"))
                              if cb7==1:
                                print("  Vous verouillez à double tour la porte en métal. Derrière, le Rival hurle et frappe de toutes ses forces. Derrière lui, les flammes prennent de l'ampleur. Il pousse un cri silencieux en disparaissant dans le brasier. Le hublot se fissure sous l'effet de la chaleur. Vous ne voyez plus l'intérieur.")
                              elif cb7==2:
                                print("  Vous ouvrez la porte, et Hekim sort comme une fusée. Après quelques mètres, il s'arrête, se retourne et vous regarde.")
                                print("FIN rivale VI (on vous passe les détails)")
                                isDead==1
                              else:
                                error()
                            elif cb6==2:
                              print("  Vous continuez, mais une odeur de joint et de chair brûlée se mêlent à la fumée.")
                            else:
                              error()
                            if isDead==0:
                              print("  Vous récupérez l'Ancien, puis vous vous échappez avant de finir asphyxiés. Vous vérifiez que vous avez toujours les feuilles de canna...sucre, puis retournez voir Aboubakar.")
                          elif cb5==2:
                            print("  Vous frappez Hekim à la tête. Mais son imposant afro le protège des coups, et il ne sent rien. Il pointe son flashball entre vos deux yeux.")
                            print("FIN rivale V")
                            isDead=1
                          else:
                            error()
                        else:
                          error()
                      elif cb3==3:
                        if "grenade" in inv:
                          print("  Vous lancez une grenade sur la porte, qui explose dans un bruit tonitruant. Vous découvrez alors un long couloir, éclairé par des lampes électriques. Vous vous y engagez...")
                          #Chapitre secret
                          print("")
                          print("#CHAPITRE 9 : PASSAGE SECRET")
                          print("")
                          print("  Après une marche bien plus confortable que la précédente, vous arrivez au niveau d'une nouvelle porte. Celle-ci est ouverte. Vous l'ouvrez, et découvrez une immense salle souterraine : la planque du gang Benzema...")
                          print("  Soudain, le SWAT qui vous avait filé depuis votre arrivée (il était juste discret, ce n'est pas un raccourci scénaristique), accompagné de l'armée, surgissent et arrêtent le gang Benzema. Et il pense que vous êtes complice.")
                          print("(1) : Vous rendre, et prier pour vous en sortir")
                          print("(2) : Bon ben... go s'enfuir hein")
                          cs1=int(input("Choix:"))
                          if cs1==1:
                            print("  Vous finissez en prison. Vous y restez des années, jusqu'à un beau jour où vous ramassez un pain de savon...")
                            print("FIN de la savonnette")
                            isDead=1
                          elif cs1==2:
                            print("  Vous vous enfuyez, avec l'armée à vos trousses...")
                            print("À SUIVRE dans GHETTO : LA TRAQUE")
                            isDead=1
                            win=1
                          else:
                            error()
                        else:
                          print("  Vous tentez de défoncer la porte. Malheureusement, vous vous cassez l'épaule.")
                          print("  Bien essayé, vous avez failli accéder à la route secrète ! Peut-être que si vous aviez eu quelque chose pour exploser la porte, ça aurait marché...")
                          print("FIN presque secrète")
                          isDead=1
                      else:
                        error()
                    else:
                      error()
                  else:
                    error()
                else:
                  error()
                if isDead==0:
                  print("  Vous arrivez dans la ruelle d'Aboubakar.")
                  print("  - Eh Boubou ! J'ai tes feuilles de canna...")
                  print("  - De CANNE À SUCRE ! dit Boubou un peu trop fort. De la canne à sucre évidemment. Ah, شكرًا mon ami ! Eh bien, chose promise chose due, voici la carte que je t'avais promise.")
                  print("  Le dealeur vous remet une carte en papier journal. Elle semble avoir été dessinée par un enfant de 3 ans. Atteint du syndrome de Down. Et de Parkinson. Et...")
                  print("  - C'est à prendre ou à laisser, déclare Aboubakar.")
                  print("  Vous prenez malgré tout le bout de papier et vous rendez à l'adresse indiquée : le 74 rue Rudolf Hitman. Là, la carte indique de descendre par... une bouche d'égout ?!")
                  print("")
                  print("#CHAPITRE 9 : LA PLANQUE BENZEMA")
                  print("")
                  if route==1:
                    print("  Après être monté au sommet d'un gratte-ciel, vous allez devoir descendre dans les égouts...")
                  if route==2:
                    print("  Vous avez déjà vécu une aventure souterraine. Et vous allez devoir recommencer...")
                  print("(1) : Non, on a dû se tromper d'endroit, avec cette carte trisomique")
                  print("(2) : Tortue Ninja ! KOWABUNGA !!!")
                  c16=int(input("Choix"))
                  if c16==1:
                    print("  Vous repartez. Vous vous perdez dans le 93.")
                    print("FIN égarée dans le 93")
                    isDead=1
                  elif c16==2:
                    print("  Vous descendez dans les égouts, flanqué de l'Ancien.")
                    print("  - Comme le disaient mes grands-parents guyanais, 'Dilo pa jen tro loin pou krapo alé lavé' !")
                    print("  Vous vous demandez si l'ancien compte se baigner dans l'eau radioactive, et surtout comment il a pu exister des gens encore plus vieux que lui. Vous continuez votre progression dans la boue. Après un temps indéterminé à longer l'eau verdâtre - cette satanée montre du marchand lybien compte toujours à l'envers ! - vous apercevez un rat.")
                    print("(1) : Bon, je vais pas assumer ma paranoïa chronique et dire que c'est juste de la prudence")
                    print("(2) : Un rat dans les égouts, on va pas en faire tout un plat !")
                    c17=int(input("Choix:"))
                    if c17==1:
                      print("  Vous continuez, sur vos gardes. Au fil de votre progression, vous rencontrez de plus en plus de rats. Vous êtes de plus en plus inquiet.")
                      print("(1) : Faire une blague raciste pour relâcher la pression")
                      print("(2) : Continuer en silence")
                      c18=int(input("Choix:"))
                      if c18==1:
                        print("  - On est en Israël ou quoi ?")
                        print("  Flop.")
                      elif c18==2:
                        print("  Vous continuez en silence.")
                      else:
                        ("  Vous ne décidez rien")
                      print("  Soudain, au détour d'un couloir, vous découvrez un sol et des murs couverts de centaines de rats noirs. Avant que vous ayez pu faire une autre blague raciste sur les fours et le poulet, les rats se rassemblent et se fondent entre eux pour former une terrifiante masse de fourrure. Une couronne d'or se matérialise au sommet de la créature que tout le 93 connaît sous le nom du Roi des Rats. Le Roi des Rats, raison pour laquelle l'eau est toujours brune au robinet, la cause de la disparition des chaussettes dans les machines à laver, le cauchemar des promoteurs immobiliers et des employés de la voirie. Souriman le Magnifique, Roi des Rats.")
                      print("  - מה אתה עושה בשטח שלי ?")
                      print("  L'ancien vous traduit l'hébreu : ça signifie 'Que venez-vous faire sur ma propriété ?'")
                      print("(1) : Les égouts appartiennent techniquement à la ville...")
                      print("(2) : Vous êtes rat-ciste ?")
                      print("(3) : *Fuir*")
                      c19=int(input("Choix:"))
                      if c19==1:
                        print("  Le Roi n'apprécie pas que vous remettiez en question son autorité, et il vous saute dessus.")
                        print("(1) : Reculer")
                        print("(2) : Le frapper")
                        print("(3) : Lui lancer un truc")
                        c20=int(input("Choix:"))
                        if c20==1:
                          print("  Vous reculez d'un bond. En atterrissant, vous tombez sur le dos dans la vase. Le monstre atterrit dans l'eau, là où vous vous tenez une seconde plus tôt...et sur l'Ancien ! Le pauvre vieux est avalé par la masse noire. Cependant, quelques instants plus tard, Souriman se met à tousser avant de recracher l'Ancien. Apparemment, même un monstre de rats ne mange pas de nourriture trop avariée...")
                          print("  Une fois sa gorge dégagée, le Roi se tourne de nouveau vers vous. Mais, au dernier moment, alors qu'il s'apprêtait à vous sauter dessus, une détonation retentit. Il pousse un couinement de douleur alors que plusieurs rats sont projetés hors de son corps. Il regarde dans la direction du tir en plaquant sa patte sur la plaie béante.")
                          print("  - Qui nous a attaqué ?! rugit-il.")
                          print("En guise de réponse, d'autres tirs retentissent. Davantage de rats sont expulsés hors du Roi, qui réduit de plus en plus de taille.")
                          print("  - QUI NOUS A ATTAQUÉ !!")
                          print("  Les tirs continuent de s'abattre sur le monstre. Lorsqu'un tir lui éclate la tête, il juge le moment bien choisi pour FUIR. Il se désagrège et les rats survivants s'enfuient par des tuyaux.")
                        elif c20==2:
                          if "sec" in inv:
                            print("  Vous donnez un gros coup de sécateur sur le Roi des Rats. Du sang gicle, et la masse recule d'un bond en sifflant. Le recul du coup vous fait cependant tomber en arrière. Vous tombez dans l'eau boueuse.")
                            print("  Le Roi des Rats vous saute dessus, bien décidé à vous achever. Alors que vous faites vos prières, une rafale de projectiles s'abat sur le monstre, qui explose en une nuée de rats. Lorsque les rats survivants tentent de reformer le corps du Roi, une nouvelle rafale disloque à nouveau le pourisseur immobilier. Vous regardez dans la direction des tirs.")
                          else:
                            print("  Vous frappez le Roi des Rats. Votre main s'enfonce dans la masse sifflante. Quand vous la ressortez, vous êtes manchot. Profitant du fait que vous êtes à sa portée, le Roi s'abat sur vous.")
                            print("FIN rat-ciste IV ")
                            isDead=1
                        elif c20==3:
                          if "grenade" in inv:
                            print("  Vous lancez une grenade sur le Roi des Rats. L'explosion violente vous projette en arrière. Le monstre, qui a pris la grenade en plein corps, est projeté et disloqué.")
                            print("  Les rats se réunissent et reforment le Roi, mais à ce moment, une détonation retentit et la tête du monstre explose. Les morceaux de rat volent de partout alors que les survivants reforment la partie détruite.")
                            print("  - Quelqu'un nous tire dessus ! s'exclame le Roi (oui, il parle de lui-même au pluriel)")
                            print("  Comme pour appuyer ses propos, une salve de tirs le réduit en rats éparpillés, qui s'enfuient bien vite.")
                          else:
                            print("  Vous ramassez un caillou dans l'eau et le lancez sur le Roi des Rats. Il absorbe immédiatement la pierre, avant de foncer sur vous comme un tsunami noir.")
                            print("  FIN rat-ciste V")
                            isDead=1
                        else:
                          print("  Le temps de vous décider, vous vous faites massacrer.")
                          isDead = 1
                        if isDead==0:
                          print("  Le tireur s'avance dans l'éclairage de la lampe électrique. Il est chauve, avec une barbe de terroriste. Il est accompagné d'autres hommes. Tous portent un pendentif avec un médaillon marqué MB. Des Benzema ! Vous devez fuir !")
                          print("(1) : FUIR")
                          print("(2) : Leur proposer de jouer au football")
                          c21=int(input("Choix:"))
                          if c21 == 1:
                            if rd.randint(1,10) == 1:
                              print("  Vous vous éloignez de la ville et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez vers le parc, et vous vous dirigez vers le parc. Vous vous dirigez...")
                              print("FIN M a t r i x é e")
                              isDead=1
                            else:
                              print("  Vous fuyez les Benzema.")
                              print("  Vous vous enfoncez dans un couloir, quand vous arrivez devant une porte. Les Benzema sont derrière vous, vous êtes acculé ! À moins que...")
                              print("(1) : Ouvrir la porte\n(2) : C'est peut-être l'intimité de quelqu'un !")
                              c22=int(input("Choix:"))
                              if c22==2:
                                print("  Vous refusez très dignement d'ouvrir la porte. Et vous vous faites très dignement massacrer par les Benzema.")
                                print("FIN Digne")
                                isDead = 1
                              elif c22 == 1:
                                print("  Vous tournez frénétiquement la poignée ancienne, jusqu'à ce que la porte cède...")
                                print("  Et vous vous retrouvez face à une armée de Benzema ! Les gangsters se ruent sur vous, prêts à vous supprimer, quand vous vous rappelez que vous possédez un certain objet de valeur...")
                                print("  Vous sortez le Mouton Doré de votre sac et les Benzema s'immobilisent.")
                                print("  Une grande et vieille femme sans âge, coiffée d'un afro blanc, apparaît au milieu de la foule. Vous ne l'avez jamais vue auparavant. Mais cette aura malveillante... Vous ressentez que vous êtes en présence de la seule, l'unique, la légendaire...")
                                print("  Mama Benzema. En personne.")
                                print("  - Voici donc le détenteur de l'artefact que je convoite...")
                                print("  - Mama Benzema pose sur vous un regard cruel.")
                                print("  - Je sais que vous avez fait tout ce voyage pour me donner le Mouton... Vous voulez simplement rentrer chez vous... Donnez-le-moi et tous vos problèmes seront réglés.")
                                print("  Vous savez que vous devez lui donner le mouton, mais votre instinct vous dit de vous méfier.")
                                print("(1) : Lui donner le Mouton \n(2) : Garder le Mouton")
                                c23=int(input("Choix:"))
                                if c23==1:
                                  print("  Vous donnez le Mouton à Mama Benzema. Il se met aussitôt à léviter au-dessus de sa main.")
                                  print("  Le visage de la vieille s'illumine de malveillance. Elle récite des formules magiques en arabe.")
                                  print("  - أعطنا القوة والنور والقوة امنحنا الشجاعة والغضب والإرادة أعطنا بركتك لنا نحن الذين نذهب إلى الحرب...")
                                  print("  Le Mouton, qui brillait auparavant d'une lumière blanche, vire au noir. Des chaînes noires émergent de la main de Mama Benzema pour s'accrocher à la statuette.")
                                  print("  La matriarche fait un geste de la main en direction de la foule de gangsters. Leurs yeux virent alors au blanc, et leurs muscles doublent de volume.")
                                  print("  Son invocation effectuée, Mama se retourne vers vous. Vous pensez qu'elle vous regarde, mais elle observe en réalité un point situé derrière votre épaule.")
                                  print("  Elle lève le bras, et le SWAT qui vous filait depuis tout ce temps (pas du tout un raccourci scénaristique eh) se retrouve soulevé en l'air, maintenu par des chaînes noires et magiques.")
                                  print("  - Et ce soir, du poulet au dîner ! dit-elle d'un ton que vous espérez humoristique.")
                                  print("  Vous rappelant que vous êtes dans le QG du gang le plus puissant, rempli de monstres magiques musculeux, avec une sorcière aux pouvoirs divins et un SWAT enchaîné, vous décidez de tirer votre révérences")
                                  print("  Lorsque vous atteignez la surface, les Benzema sont déjà dans les rues... Et ce n'est pas beau à voir. La vague de gangsters traverse les barrages de police comme du beurre, faisant voler des policiers de partout. Vous vous demandez si donner la statuette aux pouvoirs divins à Mama Benzema était une spécialement bonne idée... Puis vous vous rappelez du SWAT resté en bas.")
                                  print("(1) : Redescendre le sauver\n(2) : Fuir aussi vite que possible cette ville d'enfer")
                                  c24a=int(input("Choix:"))
                                  if c24a==2:
                                    input("  Vous profitez du chaos ambiant pour fuir la ville. Vous retrouvez votre petit appartement, votre vie normale, et laissez derrière vous les fantômes de Wallawah, Port-Ghetto et Übervilliers...")
                                    input("  Un jour, vous oublierez les épopées marines, les courses-poursuites sur l'autoroute, les trafiquants, et toutes vos aventures...")
                                    input("  Vous reviendrez à votre vie normale et ennuyeuse, votre éternel métro-boulot-dodo, loin des péripéties...")
                                    input("  Loin du danger...")
                                    input("  Loin de la peur...")
                                    input("  Loin des rêves ?")
                                    input("  Étiez-vous fait pour cela ?")
                                    input("  Étiez-vous destiné à devenir un héros ?")
                                    input("  Toutes ces interrogations s'effaceront un matin d'hiver, dans votre cocon gris, devant un bol de Chocapic.")
                                    input("  Votre avenir deviendra prévisible.")
                                    input("  Vous aurez vécu.")
                                    input("  Vous aurez vu.")
                                    input("  Vous serez mort.")
                                    input("  Et il ne restera que les souvenirs...")
                                    input("  Et le regret lorsque les médias annonceront le coup d'État orchestré par Mama Benzema.")
                                    input("  Vous avez connu la pire mort possible.")
                                    input("  L'ABANDON.")
                                    win = 1
                                  elif c24a==1:
                                    print("  Vaille que vaille, vous replongez dans les égouts, pour aller sauver le SWAT qui vous poursuit vraisemblablement depuis Port-Ghetto...")
                                    print("  Vous arrivez dans le repaire désert et trouvez le SWAT entouré de chaînes magiques.")
                                    if "sec" in inv:
                                      print("  Vous prenez le sécateur et tentez d'entamer les liens du SWAT.")
                                      print("  Bien que ses chaînes soient d'origine magique, vous réussissez tout de même à le libérer.")
                                      print("  Le SWAT se relève et se tourne vers vous, vous remercie d'un signe de tête puis fait un geste de la main.")
                                      print("  Soudain, des militaires apparaissent partout et sortent combattre les terroristes.")
                                      print("  Vous remontez avec le SWAT et apercevez Mama Benzema, qui tient toujours le Mouton Doré. Malheureusement, elle est dans un hélicoptère qui survole le champ de bataille. Alors que vous vous demandez comment l'atteindre, vous entendez un rugissement de moteur derrière vous.")
                                      print("  - Je vous emmène quelque part ?")
                                      print("  L'Ancien ! Il est au volant d'une magnifique Renault Megane débridée, qui crache des flammes par son pot d'échappement.")
                                      print("  Vous sautez dans la voiture. L'Ancien démarre à plein régime, tout à fait confiant, sur une mine anti-char.")
                                      print("  L'explosion vous projette assez haut. Vous sautez de la voiture et vous accrochez à l'hélicoptère.")
                                      print("  Vous vous hissez dans la cabine, derrière Mama Benzema. Alors que vous vous préparez à pick-pocketer le Mouton Doré à la sorcière, elle se retourne et vous regarde avec des yeux laser.")
                                      print("  - Vous avez essayé de me chourer mon Mouton.")
                                      print("  Vous commencez à vous taper dessus, mais Mama a beau être une sorcière aux pouvoirs divins, ça n'en reste pas moins un combat contre une vieille dame...")
                                      input("  Vous maîtrisez votre adversaire sans peine.")
                                      if "gun" in inv:
                                        print("  Vous dégainez votre pistolet, mais vous hésitez.")
                                        print("(1) : Tirer\n(2) : L'épargner")
                                        c25a=int(input("Choix:"))
                                        if c25a==1:
                                          print("  Vous pressez la détente. La tête de Mama Benzema explose dans une gerbe de sang, alors que la sorcière bascule dans le vide, le Mouton dans ses bras. Elle tombe dans un trou avantageusement placé et disparaît sous terre.")
                                          input("  Vous avez sauvé le monde.")
                                          input("  Vous allez enfin rentrer chez vous.")
                                          input("  C'est cool.")
                                          win = 1
                                        elif c25a==2:
                                          print("  Vous décidez de ne pas tirer. Mama Benzema, qui est quand même pute en puissance, se relève d'un coup et vous pousse dans le vide.")
                                          print("  Mais, épuisée par le combat que vous avez mené, elle perd l'équilibre et tombe avec vous.")
                                          input("  Le monde est sauvé.")
                                          input("  Mais vous êtes mort.")
                                          win = 1
                                        else:
                                          print("  Vous ne vous décidez pas, et Mama vous pousse dans le vide comme un kaka.")
                                          print("  FIN inimaginablement stupide")
                                          isDead = 1
                                      else:
                                        print("  Et maintenant quoi ?")
                                        print("  Mama Benzema sort un pistolet et vous éteint en vitesse")
                                        print("  FIN désarmée")
                                        isDead=1
                                    else:
                                      print("  Vous prenez votre courage à deux mains et commencez à ronger la chaîne.")
                                      print("  Plusieurs heures après, Mama Benzema vous surprend, à moitié mort d'épuisement, en train de sauver un flic.")
                                      print("  FIN pour absence de sécateur")
                                      isDead=1
                                  else:
                                    error()
                                elif c23==2:
                                  print("  - Non, je crois que je vais le garder.")
                                  print("  Le visage de Mama Benzema se déforme sous l'effet de la colère.")
                                  print("  - Qu'entends-je ?")
                                  if doFlee == 1:
                                    print("  Vous regagnez un peu de détermination.")
                                    print("  - J'ai dit que je garde le Mouton.")
                                    print("  Mama Benzema vous regarde comme un politicien de droite. Elle esquisse un geste de sa main, qui se nimbe d'une aura noire. Mais alors que vous vous préparez à mourir, vous entendez une clameur venant des égouts.")
                                    print("  Soudain, des Rivaux émergent de la petite porte, à moto, des lance-roquette à la main. Vous n'aurez jamais assez de sable pour ça...")
                                    print("  Dans un vacarme d'explosions, ils éliminent le gang Benzema. Vous plongez sous une table placée avantageusement (raccourci scénaristique) juste au moment ou un tir fait disparaître Mama Benzema. Lorsque la fumée se dissipe, le Mouton est là, posé sur le sol.")
                                    input("  Un instinct vous pousse à vous approcher.")
                                    input("  Vous retirez votre bonnet.")
                                    input("  Et vous en coiffez la statuette.")
                                    input("  Un Benzema vous repère et vous tire dessus.")
                                    input("  Vous mourez.")
                                    input("  Mais vous savez au fond de vous...")
                                    input("  Que vous êtes encore là.")
                                    win=1
                                  elif doFlee == 0:
                                    print("  D'un geste de la main, Mama Benzema envoie une horde de Benzema sur vous. La dernière chose que vous voyez est une barbe de terroriste.")
                                    print("  FIN de la forte-tête")
                                    isDead = 1
                                else:
                                  error()
                              else:
                                print("  Les tireurs arrivent, et vous n'avez rien fait ? Vous êtes seul responsable de la situation.")
                                isDead=1
                          elif c21 == 2:
                            print("  Vous jouez au football avec les Benzema. Un jour, la carrière du petit Karim décollera... Mais en attendant, vous prenez le ballon en pleine tête et mourez.")
                            print("Fin du REAL")
                            isDead=1
                          else:
                            error()
                      elif c19==2:
                        print("  Le Roi apprécie votre humour. Et il est effectivement rat-ciste ! Vous devenez les meilleurs amis du monde et, oubliant pourquoi vous êtes là, vous remontez à la surface avec le roi des Rats. Malheureusement, c'est à ce moment que la montre du marchand lybien arrête de compter.")
                        print("FIN explosive III")
                        isDead=1
                      elif c19==3:
                        print("  Ne jamais tourner le dos à un monstre composé d'un amalgame de centaines de rongeurs.")
                        print("  FIN du Roi des Rats")
                        isDead=1
                      else:
                        error()
                    elif c17==2:
                      print("  Vous continuez imprudemment. On ne retrouvera jamais votre corps !")
                      print("  FIN...")
                      isDead=1
                    else:
                      error()
                  else:
                    error()
              else:
                error()
          elif c11==3:
            print("  Vous arrivez comme un arabe. Aboubakar ne prend pas la blague (il est turc).")
            print("FIN explosive II")
            isDead=1
          else:
            error()
        else:
          error()
    else:
      error()
  elif c4==2:
    print("  Le GPS, acheté un bon prix à un marchand lybien, vous mène hors de l'univers observable.")
    print("FIN cosmique")
    isDead=1
  else:
    error()
elif c1==2:
  print("  Vous restez dans le train. C'était son dernier trajet.")
  print("FIN à la casse")
  isDead=1
else:
  error()
#Générique
if err == 1:
  print("  Le dieu des réponses invalides vous punit pour votre péché !")
  input("  Est-ce un moyen de maintenir un peu de cohérence dans ce code opaque et mal optimisé ?")
  print("  Oui.")
elif isDead==1:
  print("")
  print("  Dommage ! Vous ferez mieux la prochaine fois...")
if isDead==1 or win==1 or err==1:
  print("")
  print("GHETTO 3 : le vrai GHETTO")
  print("Un jeu de A²MK")
  print("Scénario : A²MK")
  print("Réalisation : A²MK")
  print("Support : Replit")
  print("Jeu original : GHETTO de A²MK")
  print("Musique : NaN")
  print("'GHETTO', 'GHETTO 2', 'le vrai GHETTO', les noms 'Mamadou Hamed Benzema', 'Hal-Wakbar', 'Mama Benzema' appartiennent techniquement à A²MK")
  print("MERCI D'AVOIR JOUÉ")