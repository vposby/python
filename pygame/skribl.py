"""
Desktop/Software/Python/Pygame
Notepad-esque
"""

import sys, pygame, random
pygame.init()

size=width,height=(512,512)

black=(0,0,0)
white=(255,255,255)
grey=(196,196,196)
red=(224,0,0)
orange=(255,128,0)
yellow=(224,224,0)
green=(0,224,0)
cyan=(0,255,255)
blue=(0,0,224)
purple=(128,0,128)
pink=(224,0,224)

screen=pygame.display.set_mode(size)
pressed=pygame.key.get_pressed()
userFont=pygame.font.Font(None,14)
x=0
y=0
displayText=[]
line=""

lowercase = {
	pressed[pygame.K_a]: "a",
	pressed[pygame.K_b]: "b",
	pressed[pygame.K_c]: "c",
	pressed[pygame.K_d]: "d",
	pressed[pygame.K_e]: "e",
	pressed[pygame.K_f]: "f",
	pressed[pygame.K_g]: "g",
	pressed[pygame.K_h]: "h",
	pressed[pygame.K_i]: "i",
	pressed[pygame.K_j]: "j",
	pressed[pygame.K_k]: "k",
	pressed[pygame.K_l]: "l",
	pressed[pygame.K_m]: "m",
	pressed[pygame.K_n]: "n",
	pressed[pygame.K_o]: "o",
	pressed[pygame.K_p]: "p",
	pressed[pygame.K_q]: "q",
	pressed[pygame.K_r]: "r",
	pressed[pygame.K_s]: "s",
	pressed[pygame.K_t]: "t",
	pressed[pygame.K_u]: "u",
	pressed[pygame.K_v]: "v",
	pressed[pygame.K_w]: "w",
	pressed[pygame.K_x]: "x",
	pressed[pygame.K_y]: "y",
	pressed[pygame.K_z]: "z",
	pressed[pygame.K_0]: "0",
	pressed[pygame.K_1]: "1",
	pressed[pygame.K_2]: "2",
	pressed[pygame.K_3]: "3",
	pressed[pygame.K_4]: "4",
	pressed[pygame.K_5]: "5",
	pressed[pygame.K_6]: "6",
	pressed[pygame.K_7]: "7",
	pressed[pygame.K_8]: "8",
	pressed[pygame.K_9]: "9",
	pressed[pygame.K_SPACE]: " ",
	pressed[pygame.K_COMMA]: ",",
	pressed[pygame.K_PERIOD]: ".",
	pressed[pygame.K_SLASH]: "/",
	pressed[pygame.K_SEMICOLON]: ";",
	pressed[pygame.K_QUOTE]: "'",
	pressed[pygame.K_LEFTBRACKET]: "[",
	pressed[pygame.K_RIGHTBRACKET]: "]",
	pressed[pygame.K_BACKSLASH]: "\\",
	pressed[pygame.K_MINUS]: "-",
	pressed[pygame.K_EQUALS]: "="
}

uppercase = {
	pressed[pygame.K_a]: "A",
	pressed[pygame.K_b]: "B",
	pressed[pygame.K_c]: "C",
	pressed[pygame.K_d]: "D",
	pressed[pygame.K_e]: "E",
	pressed[pygame.K_f]: "F",
	pressed[pygame.K_g]: "G",
	pressed[pygame.K_h]: "H",
	pressed[pygame.K_i]: "I",
	pressed[pygame.K_j]: "J",
	pressed[pygame.K_k]: "K",
	pressed[pygame.K_l]: "L",
	pressed[pygame.K_m]: "M",
	pressed[pygame.K_n]: "N",
	pressed[pygame.K_o]: "O",
	pressed[pygame.K_p]: "P",
	pressed[pygame.K_q]: "Q",
	pressed[pygame.K_r]: "R",
	pressed[pygame.K_s]: "S",
	pressed[pygame.K_t]: "T",
	pressed[pygame.K_u]: "U",
	pressed[pygame.K_v]: "V",
	pressed[pygame.K_w]: "W",
	pressed[pygame.K_x]: "X",
	pressed[pygame.K_y]: "Y",
	pressed[pygame.K_z]: "Z"	
}

while 1:
	for event in pygame.event.get():
		if event.type==pygame.QUIT: sys.exit()

	screen.fill(black)
	if event.type==pygame.KEYDOWN:
		if len(line)>40:
			displayText.append(line)
		else:
			#these return "" and not the mapped key values
			if pressed[pygame.K_RSHIFT] or pressed[pygame.K_LSHIFT]:
				line+=uppercase.get(pressed,"")
			else:
				line+=lowercase.get(pressed,"")
	if len(displayText)<1:
		screen.blit(userFont.render(line,1,white),(0,0))
	else:
		for z in range(0,len(displayText)):
			y=(z)*16
			screen.blit(userFont.render(displayText[z],1,white),(0,y))
	pygame.display.update()