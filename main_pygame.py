import pygame,cv2,os,sys
import pygame_init,my_functions
from stockfish import Stockfish
from ast import literal_eval
import chess,chess.pgn

os.system('cls')
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

# board.is_checkmate()
# board.is_stalemate()
# stockfish.is_move_correct('a2a3')

def next_move_funct():
    print('next')
    #Capture new image

    #run yolo model

    #Get move played

    #check if move valid

    #update in stockfish


screen = pygame_init.initialize()
clock = pygame.time.Clock()
bg_img= pygame.image.load("bg.jpg").convert()
bg_img = pygame.transform.scale(bg_img, (1080,650))

#Edge coords
path1 = script_directory+'\move0.jpg'
print(f"{path1 = }")
img = cv2.imread(path1, 1)
img = cv2.resize(img, (600, 600), interpolation = cv2.INTER_LINEAR)

with open("cords.txt", "r+") as f:
    SIZE = f.seek(0, os.SEEK_END)
    f.seek(0)
    if SIZE == 0:
        #Get coords and save to cords.txt
        edge_coords = my_functions.get_edge_coords(img)
        f.write(str(edge_coords))
        print("File write complete")
    else:
        #Load coords
        edge_coords = literal_eval(f.read())
        print("File read complete")

square_coords = my_functions.get_remaining_coords(edge_coords,img)

#Buttons
gui_font = pygame.font.SysFont('Calibri',20)
btn_color = (46,50,62)

nextmove_text = gui_font.render('Next Move',True,'white')
nextmove_btn = pygame.Rect(640,470,150,50)

edge_coords_set_text = gui_font.render('Set Board edges',True,'white')
edge_coords_set_btn = pygame.Rect(820,550,150,50)

edge_coords_see_text = gui_font.render('See Mapping',True,'white')
edge_coords_see_btn = pygame.Rect(640,550,150,50)

see_yolo_text = gui_font.render('See Camera',True,'white')
see_yolo_btn = pygame.Rect(820,470,150,50)

reset_text = gui_font.render('Reset',True,'white')
reset_btn = pygame.Rect(820,470,150,50)

# Initialize StockFish
stockfish = my_functions.sf()
current_fen = stockfish.get_fen_position()
current_fen_img = my_functions.get_board_img(current_fen)
current_fen_img.convert()

# Labels
# Stockfish init
current_eval_string : str = my_functions.get_current_eval_string(stockfish.get_evaluation())

eval_font = pygame.font.SysFont('Calibri',40 ,bold=True)
eval_bar_text = eval_font.render(current_eval_string,True,'white')
eval_bar_box = pygame.Rect(640,50,330,50)



#Pygame loop

eval_update_event = pygame.USEREVENT + 1
pygame.time.set_timer(eval_update_event,2000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == eval_update_event:
            current_eval_string : str = my_functions.get_current_eval_string(stockfish.get_evaluation())
            eval_bar_text = eval_font.render(current_eval_string,True,'white')

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if edge_coords_see_btn.collidepoint(event.pos):
                # Show square mappings
                my_functions.show_square_mapping(square_coords , img)

            elif edge_coords_set_btn.collidepoint(event.pos):
                # Updating Edge and square coords
                edge_coords = my_functions.get_edge_coords(img)
                my_functions.update_edge_coords(edge_coords)
                square_coords = my_functions.get_remaining_coords(edge_coords,img)

            elif nextmove_btn.collidepoint(event.pos):
                next_move_funct()

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                next_move_funct()

    screen.fill((18,21,28))

    # Eval bar rendering
    pygame.draw.rect(screen,btn_color,eval_bar_box)
    screen.blit(eval_bar_text , (eval_bar_box.x+10 , eval_bar_box.y+10))

    pygame.draw.rect(screen,btn_color,nextmove_btn)
    screen.blit(nextmove_text,
                (nextmove_btn.x+10,
                 nextmove_btn.y+15))

    pygame.draw.rect(screen,btn_color,edge_coords_set_btn)
    screen.blit(edge_coords_set_text,
                (edge_coords_set_btn.x+10,
                 edge_coords_set_btn.y+15))
    
    pygame.draw.rect(screen,btn_color,edge_coords_see_btn)
    screen.blit(edge_coords_see_text,
                (edge_coords_see_btn.x+15,
                 edge_coords_see_btn.y+15))

    pygame.draw.rect(screen,btn_color,see_yolo_btn)
    screen.blit(see_yolo_text,
                (see_yolo_btn.x+15,
                 see_yolo_btn.y+15))

    
    screen.blit(current_fen_img,(50,50))
    
    # Variable Updation
    

    pygame.display.update()
    clock.tick(60)
    # print(f'{clock.get_fps():.2f}')
pygame.quit()


""" 
round(edge_coords_set_btn.width*0.5)-round(edge_coords_see_text.get_width()*0.65) 
"""
