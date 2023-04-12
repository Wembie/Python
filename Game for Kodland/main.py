import pygame
import random

# Define algunas constantes
WIDTH = 600
HEIGHT = 600
PLAYER_SIZE = 50
COIN_SIZE = 20
ENEMY_SIZE = 40

# Define algunos colores
WHITE = ( 255, 255, 255 )
BLACK = ( 0, 0, 0 )
BLUE = ( 0, 0, 255 )
YELLOW = ( 255, 255, 0 )
RED = ( 255, 0, 0 )

class Player( pygame.sprite.Sprite ):
    def __init__( self ):
        super().__init__()
        self.image = pygame.Surface( ( PLAYER_SIZE, PLAYER_SIZE ) )
        self.image.fill( BLUE )
        self.rect = self.image.get_rect()
        self.rect.center = ( WIDTH // 2, HEIGHT - PLAYER_SIZE )
        self.vel_x = 0
        self.vel_y = 0
        self.score = 0

    def update( self ):
        self.rect.x += self.vel_x  # Mueve al jugador en el eje x
        self.rect.y += self.vel_y  # Mueve al jugador en el eje y
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def add_score( self, points ):
        self.score += points

class Enemy( pygame.sprite.Sprite ):
    def __init__( self ):
        super().__init__()
        self.image = pygame.Surface( ( ENEMY_SIZE, ENEMY_SIZE ) )
        self.image.fill( RED )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, WIDTH - ENEMY_SIZE )
        self.rect.y = random.randint( -HEIGHT, 0 )
        self.vel_y = random.randint( 1, 3 )

    def update( self ):
        self.rect.y += self.vel_y
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint( 0, WIDTH - ENEMY_SIZE )
            self.rect.y = random.randint( -HEIGHT, 0 )
            self.vel_y = random.randint( 1, 3 )

class Coin( pygame.sprite.Sprite ):
    def __init__( self ):
        super().__init__()
        self.image = pygame.Surface( ( COIN_SIZE, COIN_SIZE ) )
        self.image.fill( YELLOW )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint( 0, WIDTH - COIN_SIZE )
        self.rect.y = random.randint( -HEIGHT, 0 )
        self.points = random.randint( 1, 5 )

    def update( self ):
        self.rect.y += 3
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint( 0, WIDTH - COIN_SIZE )
            self.rect.y = random.randint( -HEIGHT, 0 )

class Game:
    def __init__( self ):
        pygame.init()
        self.screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
        pygame.display.set_caption( "Colombian Colors - Simple Python Game - By Wembie" )
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font( None, 36 )

        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add( self.player )

        for i in range( 10 ):
            enemy = Enemy()
            self.all_sprites.add( enemy )
            self.enemies.add( enemy )
            
        """for i in range( 10 ):
            coin = Coin()
            self.all_sprites.add( coin )
            self.coins.add( coin )"""

        self.score = 0

    def run( self ):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.vel_x = -5
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.vel_x = 5
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.vel_y = -5
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.vel_y = 5
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.player.vel_x = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.player.vel_x = 0
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.player.vel_y = 0
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.player.vel_y = 0
                coin = Coin()
                self.all_sprites.add( coin )
                self.coins.add( coin )

            # Verifica si hay colisiones entre el jugador y las monedas
            hits = pygame.sprite.spritecollide( self.player, self.coins, True )
            if hits:
                self.score += 10

            # Verifica si hay colisiones entre el jugador y los enemigos
            hits = pygame.sprite.spritecollide( self.player, self.enemies, False )
            if hits:
                running = False

            # Actualiza sprites
            self.all_sprites.update()

            # Dibuja en la pantalla
            self.screen.fill( BLACK )
            self.all_sprites.draw( self.screen )

            # Dibuja la puntuación
            score_text = self.font.render( f"Puntuación: { self.score}", True, WHITE )
            self.screen.blit( score_text, ( 10, 10 ) )

            # Actualiza la pantalla
            pygame.display.flip()

            # Ajusta la velocidad de fotogramas
            self.clock.tick( 60 )

        pygame.quit()
        print( f"Puntuación alcanzada: { self.score }" )

if __name__ == "__main__":
    game = Game()
    game.run()
