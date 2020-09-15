import pygame
import cv2


# We inizialize the pygame
pygame.init()

# We set our window 
win = pygame.display.set_mode((600,600)) 
pygame.display.set_caption("BACKGROUN ANIMATED")

# Image of our avatar
avatar = pygame.image.load('YOUR_AVATAR.png')

# Image for cv2 (Background)
img = cv2.imread("BACKGROUND.png")

# x, y and speed of our avatar
x = 1000
y = 1000
speed = 15

# Clock for pygame
clock = pygame.time.Clock()

# Variables for the game
walkCount = 0

# Function that animate the sprite and set the background with cv2
def Animate_BackGround():
    global walkCount
    
    # Use try/except for error in cv2
    try:
        resized_image = cv2.resize(img, (2000, 2000)) # Tip: use a big background like 2000x2000 or 3000x3000...
        crop_img = resized_image [int(y)-300:int(y)+300, int(x)-300:int(x)+300]  # Select a 600x600 square of background
        cv2.imwrite('crop_img.png', crop_img) # Save the image
        bg = pygame.image.load('crop_img.png') # Use the image for our background
        win.blit(bg, (0,0))   # Draw the background
    except:
        pass
    
    
    win.blit(avatar, (300,300))

            
    pygame.display.update() 
    

# Key that user press for move background.
run = True
while run:
    clock.tick(28)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]: 
        x -= speed
        
    if keys[pygame.K_UP]: 
        y -= speed
    
    if keys[pygame.K_DOWN]: 
        y += speed
        
    elif keys[pygame.K_RIGHT] :  
        x += speed

    
    print(x,y)
    pygame.display.update()
    Animate_BackGround()
    
    
    
# QUIT PYGAME
pygame.quit()
