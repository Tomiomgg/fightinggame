import math
import random

class Player:
    def __int__(self, name="player", health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max


    def attack(self):
        attack_max = self.attack_max * (random.random() + .5)
        return attack_amt
    def block(self):
        block_max = self.block_max * (random.random() + .5)
        return block_amt


class battle:
    def start_fight(self, player1, player2):
        while True:
            if get_attack_result(player1, player2) == "Game Over":
                break

            if get_attack_result(player2,player1) == "Game Over":
                break


    def get_attack_result(self, playerA, playerB):
        player_a_attack_amt = playerA.attack()
        player_b_block_amt = playerB.block()
        damage_2_player_b = math.ceil(player_a_attack_amt - player_b_block_amt)
        playerB.health = playerB.health - damage_2_player_b
        print("{} attacks {} and deals {} damage".format(playerA.name, playerB.name, damage_2_player_b))
