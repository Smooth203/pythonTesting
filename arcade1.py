import sys
import arcade

screenW = 800
screenH = 600
screenTitle = "Building Test"
		
#Define Variables
mouseX = 0
mouseY = 0
viewportL = 0
viewportR = 10
viewportB = 0
viewportT = 0

class MyGame(arcade.Window):
	
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		arcade.set_background_color(arcade.color.WHITE)

		self.cursorList = None
		self.cursorSprite = None

	def setup(self):
		#Setup Game - call to reset game#
		

		#Create sprite lists
		self.cursorList = arcade.SpriteList()

		#set up player
		cursorImg = "cursor.png"
		self.cursorSprite = arcade.Sprite(cursorImg)
		self.cursorSprite.center_x = 0
		self.cursorSprite.center_y = 0
		self.cursorList.append(self.cursorSprite)

	def on_draw(self):
		arcade.start_render()

		#draw shit
		self.cursorList.draw()
		#

	def on_update(self, delta_time):
		pass

	def on_key_press(self, key, key_modifiers):
		#QUIT#
		if key == arcade.key.ESCAPE:
			arcade.close_window()
			quit()
		##

	def on_mouse_motion(self, x, y, dx, dy):
		self.cursorSprite.center_x = x
		self.cursorSprite.center_y = y

def main():
	#Main Method#
	game = MyGame(screenW, screenH, screenTitle)
	game.setup()
	arcade.run()

if __name__ == "__main__":
	main()