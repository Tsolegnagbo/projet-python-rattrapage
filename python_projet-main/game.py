import random


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
    
    def make_choice(self):
        self.choice = input(f"{self.name}, faites votre choix (Pierre, Feuille, Ciseaux) : ").capitalize()


class Bot(Player):
    def __init__(self, name="Bot"):
        super().__init__(name)
    
    def make_choice(self):
        self.choice = random.choice(["Pierre", "Feuille", "Ciseaux"])


class SmartBot(Bot):
    def __init__(self, name="SmartBot"):
        super().__init__(name)
        self.player_choices = []
    
    def make_choice(self):
        if len(self.player_choices) < 3:
            
            super().make_choice()
        else:
            
            most_common_choice = max(set(self.player_choices[-3:]), key=self.player_choices[-3:].count)
            if most_common_choice == "Pierre":
                self.choice = "Feuille"  
            elif most_common_choice == "Feuille":
                self.choice = "Ciseaux"  
            else:
                self.choice = "Pierre"  

    def record_player_choice(self, choice):
        self.player_choices.append(choice)


class Game:
    def __init__(self):
        self.player_score = 0
        self.bot_score = 0
        self.rounds = 0
    
    def resolve_round(self, player_choice, bot_choice):
        if player_choice not in ["Pierre", "Feuille", "Ciseaux"]:
            print("Choix invalide. Veuillez choisir parmi Pierre, Feuille, ou Ciseaux.")
            return None
        
        if player_choice == bot_choice:
            print(f"Égalité! Vous avez tous les deux choisi {player_choice}.")
            return "Draw"
        elif (player_choice == "Pierre" and bot_choice == "Ciseaux") or \
             (player_choice == "Feuille" and bot_choice == "Pierre") or \
             (player_choice == "Ciseaux" and bot_choice == "Feuille"):
            print(f"{player_choice} bat {bot_choice}! {self.player.name} gagne ce tour.")
            self.player_score += 1
            return "Player"
        else:
            print(f"{bot_choice} bat {player_choice}! Le bot gagne ce tour.")
            self.bot_score += 1
            return "Bot"
    
    def play_round(self):
        self.player.make_choice()
        self.bot.make_choice()
        result = self.resolve_round(self.player.choice, self.bot.choice)
        if isinstance(self.bot, SmartBot):
            self.bot.record_player_choice(self.player.choice)
        self.rounds += 1
        return result

if __name__ == "__main__":
    game = Game()
    game.player = Player("Joueur")
    game.bot = SmartBot() 
    
    while True:
        game.play_round()
        print(f"Score : {game.player.name} {game.player_score} - {game.bot.name} {game.bot_score}")
        play_again = input("Voulez-vous jouer un autre tour? (o/n) : ").lower()
        if play_again != 'o':
            break