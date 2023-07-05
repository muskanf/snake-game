

#importing all of the stuff I'll use
import dudraw
import random
from random import randint



#This is the node classs which will store all the nodes of the doubly linked list
class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        self.reversed = False
#this is the main doublylinkedslist which will store all the parts of the snake
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.reversed = False
    #function to check if the list is empty
    def is_empty(self):
        return self.size == 0
    # function to get the size of the list
    def get_size(self):
        return self.size
    #fthis funtion adds the first node
    def add_first(self, value):
        new_node = Node(value, self.head, self.head.next)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    #this function gets the index
    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("The index is out of the range!")
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.value
    #this function gets the current head
    def currentHead(self):
        return self.tail if self.reversed else self.head.next
    #this function removes the last node 
    def remove_last(self):
        if self.is_empty():
            raise Exception("This list is empty!")
        last_node = self.tail.prev
        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev
        self.size -= 1
        return last_node.value
# this functions searches for a specific node
    def search(self, value):
        curr = self.head.next
        index = 0
        while curr != self.tail:
            if curr.value == value:
                return index
            curr = curr.next
            index += 1
        return -1
    #this function verifies if the list has been implemented correctly
    def verify(self):
        curr = self.head.next
        index = 0
        while curr != self.tail:
            if curr.prev.next != curr or curr.next.prev != curr:
                print("Error: Node at index " + str(index) + " is not properly linked")
                return False
            curr = curr.next
            index += 1
        if index != self.size:
            print("Wrong list size")
            return False
        return True

     

#THIS IS THE SNAKE CLASS 
class Snake:
    def __init__(self):
        self.body = DoublyLinkedList()
        self.body.add_first((10, 10))
        self.direction = None
        self.dead = False #the snake isn't dead yet
        self.food = self.get_random_location() #the food must spawn at some random location
#DRAWING MAXIMUS :)
    def draw(self):
        
        for i in range(self.body.get_size()):
            body_part = self.body.get(i)
            if body_part is not None:
                dudraw.set_pen_color(dudraw.BLACK)
                dudraw.filled_rectangle(*body_part, 0.6, 0.6)
                dudraw.set_pen_color_rgb(0, 0, randint(100, 255))
                dudraw.filled_rectangle(*body_part, 1/2, 1/2)
#GET A RANDOM LOCATION ON THE SCREEN
    def get_random_location(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        return (x, y)
#CHECK IF MAXIMUS COLLIDED WITH THE FOOD
    def check_collision_food(self):
        head = self.body.get(0)
        if head == self.food:
            new_body_part = self.body.get(0)
            self.body.add_first(new_body_part)
            self.food = None
            self.add_food()
#ADD THE FOOD ON THE SCREEN SO MAXIMUS CAN EAT MORE AND GROW BIGGER
    def add_food(self):
        while True:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            overlap = False
            for i in range(self.body.get_size()):
                body_part = self.body.get(i)
                if body_part == (x, y):
                    overlap = True
                    break
            if not overlap:
                self.food = (x, y)
                break
    #MOVE MAXIMUS ON THE SCREEN
    def move(self):
        snake_x_pos, snake_y_pos = self.body.get(0)
        if self.direction == "UPWARDS":
            if snake_y_pos == 19: # check if snake hits bottom border
                self.dead = True
            new_head = (snake_x_pos, snake_y_pos + 1)
        elif self.direction == "DOWNWARDS":
            if snake_y_pos == 0: # check if snake hits top border
                self.dead = True
            new_head = (snake_x_pos, snake_y_pos - 1)
        elif self.direction == "LEFT":
            if snake_x_pos == 0: # check if snake hits left border
                self.dead = True
            new_head = (snake_x_pos - 1, snake_y_pos)
        elif self.direction == "RIGHT":
            if snake_x_pos == 19: #this checks if the snake collides with the border of the screen
                self.dead = True
            new_head = (snake_x_pos + 1, snake_y_pos)
        
#DID MAXIMUS EAT HIMSELF?
        collision = False
        current = self.body.head
        while current.next is not None:
            if current.value == new_head:
                collision = True
                break
            current = current.next

        if collision: # IF MAXIMUS ATE HIMSELF THEN GAME WILL END AND MAXIMUS WILL DIE 
            self.dead = True

        self.body.add_first(new_head)
        self.body.remove_last()

        return True
#This class will store all the food for MAXIMUS OUR SNAKE
class Food:
    def __init__(self,snake:Snake):
        #NO FOOD ON THE BODY OF MAXIMUS
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        while not snake.body.search((x,y)) == -1:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
        self.position = (x, y)
        self.hide_food = False
        

    #MORE FOOD FOR MAXIMUS
    def spawn_food(self):
        
        
        if self.hide_food == False:
            dudraw.set_pen_color_rgb(206, 232, 119)
            dudraw.filled_circle(*self.position, 0.6)
            dudraw.set_pen_color_rgb(240, 93, 93)
            dudraw.filled_circle(*self.position, 1/2)
            dudraw.set_pen_color_rgb(184, 104, 68)
            dudraw.filled_rectangle(*self.position, 0.2, 0.2)
        

#this is the main driver function where evrything comes together
def main():
    #setting the nice canvas size
    dudraw.set_canvas_size(400,400)

    #Alex gave us this scale in class so I used it. no questions asked xd

    dudraw.set_x_scale(-.5,19.5)
    dudraw.set_y_scale(-.5,19.5)

    #make MAXIMUS
    maximus = Snake()
    food = Food(maximus) 


    #define the directions for the snake. I want MAXIMUS to start at RIGHT
    maximus.direction = 'RIGHT'

    limit = 1
    timer = 0
    score=0
    while True:
        timer += 1
        if timer == limit:   
            dudraw.clear_rgb(255, 181, 122)
            dudraw.set_font_size(20)
            dudraw.text(10,10, f'{score}')
            dudraw.set_font_family("Comic Sans") #ah yes my favorite font
            timer = 0
        
        #drawing and moving MAXIMUS
        maximus.draw()
        maximus.move()

        #maximus eating the food
        if maximus.body.get(0) == food.position:
            #rremoving the food from the canvas if maximus ate the food
            food.hide_food = True
            
            #MAKE MAXIMUS BIGGER
            maximus.body.add_first(food.position)
            score+=1
            #FOOD 
            food = Food(maximus)

        #spawning the food at random locations
        food.spawn_food()
        food.hide_food = False

 
       #checking user press
        if dudraw.has_next_key_typed():
                    key=dudraw.next_key_typed()
                    if key=='w':
                        maximus.direction = 'UPWARDS'
                    elif key=='a':
                        maximus.direction = 'LEFT'
                    elif key=='s':
                       maximus.direction = 'DOWNWARDS'
                    elif key=='d':
                        maximus.direction = 'RIGHT'
        dudraw.show(200)
#if maximus ded then game end
        if maximus.dead == True:
            dudraw.clear_rgb(255,255,255)
            dudraw.set_font_size(20)
            dudraw.text(10,10, "You have lost the game!")
            dudraw.set_font_family("Comic Sans")
            dudraw.show(1500)
            break

 

#run game
if __name__=='__main__':
    main()
