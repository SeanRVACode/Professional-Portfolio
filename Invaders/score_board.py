import pygame


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.SysFont('TT Fellows',40)
        
    def draw_scoreboard(self,screen):
        score_text = self.game_font.render(f'Score: {self.score}',True,'White')
        score_x = 10
        score_y = 10 # Both of these are temp values
        screen.blit(score_text,(score_x,score_y))
        
    def increase_score(self):
        # Increase the score when an enemy is killed.
        self.score += 1 # Temp value for now until I decide what the scoring should be.
        
    def reset_score(self):
        # Possibly implement reset mechanic for score.
        pass
    
        
        