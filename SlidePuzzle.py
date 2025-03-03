import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import random
import numpy as np

class SlidePuzzle:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Slide Puzzle")
        
        # Game state
        self.size = 3  # 3x3 grid
        self.buttons = []
        self.current_state = []
        self.empty_pos = None
        self.tile_size = 135  # Size of each tile in pixels
        self.image_tiles = []
        
        # Create UI elements
        # self.load_image()
        self.create_menu()

        self.num_moves = 0
        
    def create_menu(self):
        # Create a frame for the menu
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=10)
        
        # Add solve game button
        load_btn = tk.Button(menu_frame, text="Solve Game", 
                            command=self.solve_game)
        load_btn.pack(side=tk.LEFT, padx=5)

        # Add shuffle button (initially disabled)
        self.shuffle_btn = tk.Button(menu_frame, text="Shuffle",
                                   command=self.shuffle_board,
                                   state=tk.DISABLED)
        self.shuffle_btn.pack(side=tk.LEFT, padx=5)
        self.load_image()
        self.shuffle_board()
        
    def load_image(self):
        # Open file dialog to choose an image
        file_path = 'img.jpg'
        
        if file_path:
            # Load and resize image
            image = Image.open(file_path)
            image = image.resize((self.tile_size * self.size, 
                                self.tile_size * self.size))
            
            # Split image into tiles
            self.image_tiles = []
            for i in range(self.size):
                for j in range(self.size):
                    # Calculate tile coordinates
                    left = j * self.tile_size
                    top = i * self.tile_size
                    right = left + self.tile_size
                    bottom = top + self.tile_size
                
                    # Crop tile from image
                    tile = image.crop((left, top, right, bottom))
                    # make it black if it is the empty tile
                    if i == self.size - 1 and j == self.size - 1:
                        tile = Image.new('RGB', tile.size, color='black')
                    photo = ImageTk.PhotoImage(tile)
                    self.image_tiles.append(photo)
            
            

            # Create game board
            self.create_board()
            self.shuffle_btn.config(state=tk.NORMAL)
            
    def create_board(self):
        # Create or clear game frame
        if hasattr(self, 'game_frame'):
            self.game_frame.destroy()
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=10)
        
        # Create buttons for each cell
        self.buttons = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                number = i * self.size + j
                # Create button with command for ALL tiles
                btn = tk.Button(self.game_frame,
                            image=self.image_tiles[number],
                            command=lambda x=i, y=j: self.make_move(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                row.append(btn)
            self.buttons.append(row)
            
        # Initialize game state
        self.current_state = [[i * self.size + j 
                            for j in range(self.size)]
                            for i in range(self.size)]
        
        # Set the empty position to the bottom right
        self.empty_pos = (self.size - 1, self.size - 1)
            
    def shuffle_board(self):
        # Perform random moves
        for _ in range(100):
            possible_moves = self.get_possible_moves()
            i, j = random.choice(possible_moves)
            self.swap_tiles(i, j)
        self.num_moves = 0
        # Update display
        self.update_display()
        
    def get_possible_moves(self):
        moves = []
        i, j = self.empty_pos
        
        # Check all adjacent positions
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < self.size and 0 <= new_j < self.size:
                moves.append((new_i, new_j))
    
        return moves
        
    def make_move(self, i, j):
        # Check if the clicked tile is adjacent to empty space
        if (i, j) in self.get_possible_moves():
            self.num_moves += 1
            self.swap_tiles(i, j)
            self.update_display()
            # Check if puzzle is solved
            if self.check_win():
                messagebox.showinfo("Congratulations!", 
                                  "You solved the puzzle in " +str(self.num_moves) + " moves!")
                
    def swap_tiles(self, i, j):
        # Swap values in current_state
        empty_i, empty_j = self.empty_pos
        self.current_state[empty_i][empty_j] = self.current_state[i][j]
        self.current_state[i][j] = self.size * self.size - 1
        self.empty_pos = (i, j)
        
    def update_display(self):
        # Update button images based on current_state
        for i in range(self.size):
            for j in range(self.size):
                value = self.current_state[i][j]
                if value == self.size * self.size - 1:
                    # This is the empty tile
                    self.buttons[i][j].config(image=self.image_tiles[value])
                else:
                    self.buttons[i][j].config(image=self.image_tiles[value])
                    
    def check_win(self):
        # Check if current state matches solved state
        for i in range(self.size):
            for j in range(self.size):
                expected = i * self.size + j
                if self.current_state[i][j] != expected:
                    return False
        return True
    
    # def solve_game(self):
    #     print("left to students")
    #     while not self.check_win():
    #         possible = self.get_possible_moves()
    #         move = random.choice(possible)
    #         print(possible)
    #         print(move)
    #         self.make_move(move[0],move[1])
    #         if self.num_moves > 100:
    #             break


    def solve_game(self):
        """A simple solver that uses breadth-first search to find a solution"""
        import queue
        import copy
        
        # Display solving message
        messagebox.showinfo("Solver", "Finding solution... This may take a moment.")
        
        # Reset move counter
        self.num_moves = 0
        
        # Use a breadth-first search to find the solution
        # Start with current state
        q = queue.Queue()
        # Store state and path to reach it
        q.put((copy.deepcopy(self.current_state), self.empty_pos, []))
        
        # Keep track of visited states to avoid cycles
        visited = set()
        
        # Keep track of iterations to prevent infinite loops
        iterations = 0
        max_iterations = 100000  # Limit search to prevent hanging
        
        while not q.empty() and iterations < max_iterations:
            iterations += 1
            
            # Get next state to explore
            state, empty_pos, path = q.get()
            
            # Skip if we've seen this state before
            state_tuple = tuple(tuple(row) for row in state)
            if state_tuple in visited:
                continue
            
            # Mark as visited
            visited.add(state_tuple)
            
            # Check if we've found the solution
            is_solved = True
            for i in range(self.size):
                for j in range(self.size):
                    expected = i * self.size + j
                    if state[i][j] != expected:
                        is_solved = False
                        break
                if not is_solved:
                    break
            
            if is_solved:
                # We found the solution!
                print(f"Solution found in {len(path)} moves")
                
                # Apply the solution
                self.execute_solution(path, 0)
                return
            
            # Try all possible moves from this state
            i, j = empty_pos
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i + di, j + dj
                
                # Check if move is valid
                if 0 <= new_i < self.size and 0 <= new_j < self.size:
                    # Create new state by making this move
                    new_state = copy.deepcopy(state)
                    new_state[i][j] = new_state[new_i][new_j]
                    new_state[new_i][new_j] = self.size * self.size - 1
                    
                    # Add to queue with updated path
                    new_path = path + [(new_i, new_j)]
                    q.put((new_state, (new_i, new_j), new_path))
        
        # If we get here, we didn't find a solution
        messagebox.showinfo("Solver", "Could not find a solution within the search limit.")

    def execute_solution(self, path, index):
        """Execute the solution moves one by one with a delay"""
        if index < len(path):
            # Make the next move
            i, j = path[index]
            self.make_move(i, j)
            
            # Schedule the next move
            self.root.after(300, lambda: self.execute_solution(path, index + 1))
        else:
            messagebox.showinfo("Solver", f"Puzzle solved in {self.num_moves} moves!")
        

if __name__ == "__main__":
    root = tk.Tk()
    game = SlidePuzzle(root)
    root.mainloop()