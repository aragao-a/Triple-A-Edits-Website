
def hp_percent_calculation(x):

    percent = (x / 10)

    return (int(percent))

def overlife_check():

    global hero_life
    global demon_life

    if hero_life >= 1000:

        hero_life = 1000

    if demon_life >= 1000:

        demon_life = 1000

    return(hero_life), (demon_life)

def kill_check():

    global hero_life
    global demon_life

    global hero_dead
    global demon_dead

    global game_over

    if demon_life <= 0:

        demon_dead = True
                
        print (f"O Chainsaw Man conseguiu sua vingança, o Zombie Devil está morto!")

    if hero_life <= 0:

        hero_dead = True

        print (f"Infelizmente o Chainsaw Man está morto e não há ninguém para puxar sua corrente e revive-lo.")

    if hero_dead == True or demon_dead == True:

        game_over = True

    else:

        game_over = False

    return(hero_dead), (demon_dead), (game_over)

hero_life = 1000
demon_life = 1000

print (f"Denji fez pacto com Pochita. Que comece a luta.")

hero_dead = False
demon_dead = False

game_over = False

while hero_life > 0 and demon_life > 0:

    overlife_check()

    kill_check()

    if game_over == True:

        break

    striker_name = str(input())

    if striker_name != "Denji" and striker_name != "ZombieDevil":

        print (f"Esse personagem não está lutando, escolha entre Denji ou Zombie Devil.")
    
    move_type = str(input())

    if move_type != "ataque" and move_type != "defesa":

        print (f"Esse golpe não existe, escolha entre ataque ou defesa.")

    move_damage = int(input())

    if move_type == "ataque":

        if game_over == True:

            break

        if striker_name == "Denji":

            demon_life -= move_damage

            overlife_check()

            kill_check()

            if game_over == True:

                break

            elif game_over == False:
                
                print (f"Uhu, Denji atacou! A porcentagem de vida atual do Zombie Devil é de {hp_percent_calculation(demon_life)}%.")

        elif striker_name == "ZombieDevil":

            hero_life -= move_damage

            overlife_check()

            kill_check()

            if game_over == True:

                break

            elif game_over == False:

                print (f"Ah não, Denji foi atacado pelo Zombie Devil! A porcentagem de vida atual de Denji é de {hp_percent_calculation(hero_life)}%.")

    if move_type == "defesa":

        if game_over == True:

            break

        if striker_name == "Denji":

            hero_life += move_damage
            demon_life -= move_damage

            overlife_check()

            kill_check()

            if game_over == True:

                break

            elif game_over == False:

                print (f"Isso aê! O feitiço virou contra o feiticeiro. Denji defendeu o golpe do Zombie Devil e ganhou um bônus de vida.")

                print (f"A porcentagem de vida atual de Denji é de {hp_percent_calculation(hero_life)}% e do Zombie Devil é de {hp_percent_calculation(demon_life)}%.")

        elif striker_name == "ZombieDevil":

            demon_life += move_damage
            hero_life -= move_damage

            overlife_check()

            kill_check()

            if game_over == True:

                break

            elif game_over == False:

                print (f"Ops! O Zombie Devil defendeu o ataque de Denji e ganhou um bônus de vida.")

                print (f"A porcentagem de vida atual de Denji é de {hp_percent_calculation(hero_life)}% e do Zombie Devil é de {hp_percent_calculation(demon_life)}%.")

