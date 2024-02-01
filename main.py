#créé par Enzo Sanchez Valero et Mikolai Szychowski
#créé le 10\01\24
#TP4


import arcade
import random
#taille de lècran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLORS = [arcade.csscolor.BLUE, arcade.csscolor.RED, arcade.csscolor.GREEN]

class Balle():
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = random.randint(0,50)
        self.color = color

#mettre les formes
    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
           de votre jeu à l'écran.
        """


        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)
        #arcade.draw_circle_filled()


    def update(self, cercle_change_x, cercle_change_y, cercle_x, cercle_y, rayon):

        self.x += self.x_speed + delta_time
        self.y += self.y_speed + delta_time

        if self.x > 300 - 50 or self.x < 0 + 50:
            self.x_speed += -1
        if self.y > 720 - 50 or self.y < 0:
            self.y_speed += -1


class Rectangle():
    def __init__(self, x, y, change_x, change_y, width_rectangle, height_rectangle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.color = random.choice(COLORS)
        self.width_rectangle = width_rectangle
        self.height_rectangle = height_rectangle
        self.tilt_angle = 50
    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
           de votre jeu à l'écran.
        """

        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 50, arcade.color.GREEN)
        arcade.draw_rectangle_filled(self.x, self.y, 50, 50, arcade.color.BLUE, 20)




class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.liste_balle = []
            self.liste_rectangle = []


        def setup(self):

            pass



        def on_draw(self):

            pass


        def on_update(self, delta_time):
            for i in self.liste_balle:
                i.on_draw(arcade.color.BLUE)

            for i in self.liste_rectangle:
                i.on_draw(arcade.color.BLUE)

        def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
            if button == arcade.MOUSE_BUTTON_LEFT:
                ball = Balle(x, y, random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), arcade.color.BLUE)
                self.liste_balle.append(ball)
            if button == arcade.MOUSE_BUTTON_RIGHT:
                rectangle = Rectangle(x, y, random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), arcade.color.BLUE)
                self.liste_rectangle.append(rectangle)



def main():
   my_game = MyGame()
   my_game.setup()

   arcade.run()


main()