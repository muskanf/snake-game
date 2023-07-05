# snake-game


## My Snake Game Project
For this project, I used the DoublyLinkedList data structure implemented in homework. It includes the following methods:

-__init__(): initializes an empty list
-__str__(): returns a string representing the list
-is_empty(): returns True if list is empty, False otherwise
-get_size(): returns size of list
-add_first(v): adds v at head of list
-add_last(v): adds v at end of list
-remove_first(): removes and returns first value in list
-remove_last(): removes and returns last value in list
-first(): returns first value in list
-last(): returns last value in list
-search(v): returns index of value if found and -1 otherwise
-get(i): returns value at index i

I used a function to verify that my DoublyLinkedList works.

## The Game
I thought about what classes to create and what data they should have and represented the world as a grid and set the x and y scale accordingly. I also used the following starting code for the main part of my program. This ensures that keyboard presses are processed in timely fashion while also making sure the snake is moving at a reasonable speed.

        limit = 20 # number of frames to allow to pass before snake moves
        timer = 0  # timer to keep track of number of frames that passed
        while(True):
            timer += 1
            # process keyboard press here
            if timer == limit:
                timer = 0
                # draw and move snake
                # check if snake ate fruit
                # check if snake self intersects
        
            dudraw.show(40)


![Screenshot 2023-07-05 084600](https://github.com/muskanf/snake-game/assets/88496921/34c87808-6fb3-4496-94a1-e7b17134ca51)
![Screenshot 2023-07-05 084659](https://github.com/muskanf/snake-game/assets/88496921/9338ecbc-58f4-4f61-b331-86c1491f3a00)
