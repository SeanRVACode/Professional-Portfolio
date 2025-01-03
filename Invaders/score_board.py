import pygame


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.SysFont('TT Fellows',40)
        self.high_score_file_path = './Assets/high_score.txt'
        
    def draw_scoreboard(self,screen):
        score_text = self.game_font.render(f'Score: {self.score}',True,'White')
        score_x = 10
        score_y = 10 # Both of these are temp values
        screen.blit(score_text,(score_x,score_y))
    
    def ask_player_name(self,screen,question):
        # Ask the player for their name
        pass
        
    def increase_score(self):
        # Increase the score when an enemy is killed.
        self.score += 1 # Temp value for now until I decide what the scoring should be.
        
    def reset_score(self):
        # Possibly implement reset mechanic for score.
        self.score = 0
        
    def save_high_score(self):
        scores = []
        # Save the high score to a file
        with open(self.high_score_file_path,'r') as file:
            try:
                line = file.readline().strip() # Score is one line
                high_score = int(line) if line else 0
            except:
                high_score = 0

        if self.score > high_score:
            with open(self.high_score_file_path,'w') as file:
                file.write(str(self.score))
            
            
        pass
    
        
        