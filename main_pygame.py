import pygame,cv2,os,sys
import pygame_init,my_functions
from stockfish import Stockfish
from ast import literal_eval
import chess,chess.pgn
from saveimage import get_cur_img
from YOLOv8py import run_yolo
from ultralytics import YOLO

os.system('cls')
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
move_no = 1

# board.is_checkmate()
# board.is_stalemate()
# stockfish.is_move_correct('a2a3')
# myenv\Scripts\activate
# pip freeze > requirements.txt
# pip install -r requirements.txt

def next_move_funct():
    global current_eval_string,eval_bar_text,current_fen,current_fen_img,comment_text,comment_box_text,move_no
    print('Playing...')
    #Capture new image
    move = input_string
    #run yolo model

    #Get move played

    #check if move valid
    if (stockfish.is_move_correct(move)):
        board1 = chess.Board()
        #make move in sf , update eval and top moves
        stockfish.make_moves_from_current_position([move])
        current_eval_string = my_functions.get_current_eval_string(stockfish.get_evaluation())
        eval_bar_text = eval_font.render(current_eval_string,True,'white')
        bm_plot()

        #Image
        current_fen = stockfish.get_fen_position()
        current_fen_img = my_functions.get_board_img(current_fen)
        current_fen_img.convert()
        
        comment_text = str(move_no)+" Move(s) played"
        move_no += 1
        comment_box_text = comment_box_font.render(comment_text,True,'white')
        
    else:
        comment_text = "Incorrect Move. Try again"
        comment_box_text = comment_box_font.render(comment_text,True,'white')
        
    #update in stockfish,fentoimg,

print("loading model")
model = YOLO('./YOLOv8/runs/detect/train/weights/best2.pt')

screen = pygame_init.initialize()
clock = pygame.time.Clock()

#Edge coords
path1 = script_directory+'\move0.jpg'
img = cv2.imread(path1,1)
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
nextmove_btn = pygame.Rect(640,490,150,50)

edge_coords_set_text = gui_font.render('Set Board edges',True,'white')
edge_coords_set_btn = pygame.Rect(820,560,150,50)

edge_coords_see_text = gui_font.render('See Mapping',True,'white')
edge_coords_see_btn = pygame.Rect(640,560,150,50)

see_yolo_text = gui_font.render('See Camera',True,'white')
see_yolo_btn = pygame.Rect(820,490,150,50)

reset_text = gui_font.render('Reset',True,'white')
reset_btn = pygame.Rect(640,420,150,50)

play_text = gui_font.render('Play',True,'white')
play_btn = pygame.Rect(640,350,150,50)

input_string = ''
inputselected = True
inputfield_text = gui_font.render(input_string,True,'white')
inputfield_btn = pygame.Rect(820,350,150,50)

# Initialize StockFish
stockfish = my_functions.sf()

# stockfish.make_moves_from_current_position(["e2e4"])
# stockfish.make_moves_from_current_position(["e7e5"])
# stockfish.make_moves_from_current_position(["b1c3"])
# stockfish.make_moves_from_current_position(["d8g5"])
# stockfish.make_moves_from_current_position(["d2d4"])
# stockfish.make_moves_from_current_position(["d7d5"])

current_fen = stockfish.get_fen_position()
current_fen_img = my_functions.get_board_img(current_fen)
current_fen_img.convert()

# Labels
# Stockfish init
current_eval_string : str = my_functions.get_current_eval_string(stockfish.get_evaluation())

eval_font = pygame.font.SysFont('Calibri',40 ,bold=True)
eval_bar_text = eval_font.render(current_eval_string,True,'white')
eval_bar_box = pygame.Rect(640,50,330,50)

best_move_font = pygame.font.SysFont('Calibri',25 ,bold=True)
best_move_box = pygame.Rect(640,120,330,100)
best_move_text = best_move_font.render("Best Moves:",True,'white')

comment_box_font = pygame.font.SysFont('Calibri',20 ,bold=True)
comment_box_box = pygame.Rect(640,230,330,50)

comment_text = "Playing.."
comment_box_text = comment_box_font.render(comment_text,True,'white')

best_move_move_font = pygame.font.SysFont('Calibri',20 ,bold=True)
m1,m2,m3 = 0,0,0
m1_plot=m2_plot=m3_plot = best_move_move_font.render("Null",True,'white')
def bm_plot():
    global m1,m2,m3,m1_plot,m2_plot,m3_plot
    topmoves = stockfish.get_top_moves(3)

    if (len(topmoves)==0):
        m1=m2=m3="-"
    else:
        m1 = topmoves[0]["Move"]
        m2 = topmoves[1]["Move"]
        m3 = topmoves[2]["Move"]

    m1_plot = best_move_move_font.render(m1,True,'white')
    m2_plot = best_move_move_font.render(m2,True,'white')
    m3_plot = best_move_move_font.render(m3,True,'white')

bm_plot()

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
            bm_plot()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if inputfield_btn.collidepoint(event.pos):
                print("inputfield selected")
                inputselected = True

            else :
                pass
                # inputselected = False

            if edge_coords_see_btn.collidepoint(event.pos):
                # Show square mappings
                cur_img = get_cur_img()
                my_functions.show_square_mapping(square_coords , cur_img)

            elif edge_coords_set_btn.collidepoint(event.pos):
                # Updating Edge and square coords
                cur_img = get_cur_img()
                edge_coords = my_functions.get_edge_coords(cur_img)
                my_functions.update_edge_coords(edge_coords)
                square_coords = my_functions.get_remaining_coords(edge_coords,cur_img)

            elif play_btn.collidepoint(event.pos):
                next_move_funct()

            elif nextmove_btn.collidepoint(event.pos):
                next_move_funct()

            elif reset_btn.collidepoint(event.pos):
                print("reset")

            elif see_yolo_btn.collidepoint(event.pos):
                print("showing yolo")
                cur_img = get_cur_img()
                print("Runnimg model")
                yolo_dictionary = run_yolo(model,cur_img)
                print("Loading camera")
                my_functions.see_yolo_working(yolo_dictionary , cur_img , square_coords)

        if inputselected:
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]

                else:
                    input_string += event.unicode

                inputfield_text = gui_font.render(input_string,True,'white')


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

    pygame.draw.rect(screen,btn_color,reset_btn)
    screen.blit(reset_text,
                (reset_btn.x+15,
                 reset_btn.y+15))
    
    pygame.draw.rect(screen,btn_color,play_btn)
    screen.blit(play_text,
                (play_btn.x+15,
                 play_btn.y+15))
    
    pygame.draw.rect(screen,btn_color,inputfield_btn)
    screen.blit(inputfield_text,
                (inputfield_btn.x+15,
                 inputfield_btn.y+15))
    
    pygame.draw.rect(screen,btn_color,comment_box_box)
    screen.blit(comment_box_text,
                (comment_box_box.x+15,
                 comment_box_box.y+15))
    
    pygame.draw.rect(screen,btn_color,best_move_box)
    screen.blit(best_move_text,
                (best_move_box.x+15,
                 best_move_box.y+15))
    screen.blit(m1_plot,
                (best_move_box.x+50,
                 best_move_box.y+60))
    screen.blit(m2_plot,
                (best_move_box.x+150,
                 best_move_box.y+60))
    screen.blit(m3_plot,
                (best_move_box.x+250,
                 best_move_box.y+60))
    
    screen.blit(current_fen_img,(40,50))
    
    # Variable Updation
    

    pygame.display.update()
    clock.tick(60)
    # print(f'{clock.get_fps():.2f}')
pygame.quit()



