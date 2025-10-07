import random
import time
import os
import sys

# Configuración inicial
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    """Captura una tecla sin necesidad de presionar Enter"""
    try:
        # Para Windows
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                return msvcrt.getch().decode('utf-8')
        # Para Linux/Mac
        else:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
    except:
        return None

# JUEGO 1: SNAKE (SERPIENTE) MEJORADO
def snake_game():
    """Juego clásico de la serpiente"""
    width, height = 20, 15
    snake = [(height//2, width//2)]
    direction = (0, 1)  # Derecha
    food = (random.randint(1, height-2), random.randint(1, width-2))
    score = 0
    game_over = False
    
    print("🐍 JUEGO DE SNAKE")
    print("Controles: W (arriba), A (izquierda), S (abajo), D (derecha)")
    print("Presiona Q para salir")
    time.sleep(2)
    
    while not game_over:
        clear_screen()
        
        # Dibujar tablero
        board = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Dibujar bordes
        for i in range(width):
            board[0][i] = '═'
            board[height-1][i] = '═'
        for i in range(height):
            board[i][0] = '║'
            board[i][width-1] = '║'
        board[0][0] = '╔'
        board[0][width-1] = '╗'
        board[height-1][0] = '╚'
        board[height-1][width-1] = '╝'
        
        # Dibujar serpiente
        for segment in snake:
            y, x = segment
            if 0 < y < height-1 and 0 < x < width-1:
                board[y][x] = '●' if segment == snake[0] else '○'
        
        # Dibujar comida
        y, x = food
        if 0 < y < height-1 and 0 < x < width-1:
            board[y][x] = '🍎'
        
        # Mostrar tablero
        print(f"Puntuación: {score}")
        for row in board:
            print(''.join(row))
        
        # Capturar input
        key = get_key()
        if key and key.lower() == 'q':
            break
        
        # Cambiar dirección
        if key and key.lower() == 'w' and direction != (1, 0):
            direction = (-1, 0)
        elif key and key.lower() == 's' and direction != (-1, 0):
            direction = (1, 0)
        elif key and key.lower() == 'a' and direction != (0, 1):
            direction = (0, -1)
        elif key and key.lower() == 'd' and direction != (0, -1):
            direction = (0, 1)
        
        # Mover serpiente
        head_y, head_x = snake[0]
        new_head = (head_y + direction[0], head_x + direction[1])
        
        # Verificar colisiones
        if (new_head[0] <= 0 or new_head[0] >= height-1 or 
            new_head[1] <= 0 or new_head[1] >= width-1 or 
            new_head in snake):
            game_over = True
            break
        
        snake.insert(0, new_head)
        
        # Verificar si comió
        if new_head == food:
            score += 10
            # Generar nueva comida
            while True:
                food = (random.randint(1, height-2), random.randint(1, width-2))
                if food not in snake:
                    break
        else:
            snake.pop()
        
        time.sleep(0.2)
    
    # Fin del juego
    clear_screen()
    print("💀 GAME OVER")
    print(f"Puntuación final: {score}")
    input("Presiona Enter para continuar...")

# JUEGO 2: ADIVINA EL NÚMERO
def guess_number():
    """Juego de adivinar el número"""
    clear_screen()
    print("🎯 ADIVINA EL NÚMERO")
    print("=" * 30)
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print(f"Tengo un número entre 1 y 100. ¡Adivínalo en {max_attempts} intentos!")
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        try:
            guess = int(input(f"\nIntento {attempts}/{max_attempts}. Tu guess: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            attempts -= 1
            continue
        
        if guess < number:
            print(f"⬆️ Más alto! Te quedan {remaining} intentos")
        elif guess > number:
            print(f"⬇️ Más bajo! Te quedan {remaining} intentos")
        else:
            print(f"🎉 ¡Correcto! Adivinaste en {attempts} intentos")
            break
    else:
        print(f"💀 Game Over! El número era {number}")
    
    input("\nPresiona Enter para continuar...")

# JUEGO 3: PIEDRA, PAPEL O TIJERAS
def rock_paper_scissors():
    """Juego clásico de piedra, papel o tijeras"""
    clear_screen()
    print("✂️ PIEDRA, PAPEL O TIJERAS")
    print("=" * 30)
    
    choices = {'1': 'Piedra', '2': 'Papel', '3': 'Tijeras'}
    wins = 0
    rounds = 0
    
    while True:
        rounds += 1
        print(f"\n--- Ronda {rounds} ---")
        print("1. Piedra 🪨")
        print("2. Papel 📄")
        print("3. Tijeras ✂️")
        print("4. Salir")
        
        player_choice = input("Elige (1-4): ")
        
        if player_choice == '4':
            break
        elif player_choice not in ['1', '2', '3']:
            print("Opción inválida. Intenta de nuevo.")
            rounds -= 1
            continue
        
        computer_choice = random.choice(['1', '2', '3'])
        
        print(f"\nTú: {choices[player_choice]}")
        print(f"PC: {choices[computer_choice]}")
        
        # Determinar ganador
        if player_choice == computer_choice:
            print("🤝 Empate!")
        elif (player_choice == '1' and computer_choice == '3') or \
             (player_choice == '2' and computer_choice == '1') or \
             (player_choice == '3' and computer_choice == '2'):
            print("🎉 ¡Ganaste esta ronda!")
            wins += 1
        else:
            print("💻 La PC gana esta ronda")
        
        print(f"Victorias: {wins}/{rounds}")
    
    print(f"\nJuego terminado. Ganaste {wins} de {rounds-1} rondas")
    input("Presiona Enter para continuar...")

# JUEGO 4: BUSCAMINAS SIMPLIFICADO
def minesweeper():
    """Versión simplificada del buscaminas"""
    clear_screen()
    print("💣 BUSCAMINAS")
    print("=" * 30)
    
    size = 6
    mines = 5
    board = [[' ' for _ in range(size)] for _ in range(size)]
    revealed = [[False for _ in range(size)] for _ in range(size)]
    
    # Colocar minas
    mine_positions = []
    while len(mine_positions) < mines:
        pos = (random.randint(0, size-1), random.randint(0, size-1))
        if pos not in mine_positions:
            mine_positions.append(pos)
    
    game_over = False
    cells_revealed = 0
    total_safe_cells = size * size - mines
    
    def count_adjacent_mines(row, col):
        count = 0
        for r in range(max(0, row-1), min(size, row+2)):
            for c in range(max(0, col-1), min(size, col+2)):
                if (r, c) in mine_positions:
                    count += 1
        return count
    
    def print_board(show_mines=False):
        print("   " + " ".join(str(i) for i in range(size)))
        print("  +" + "-" * (size * 2 - 1) + "+")
        for i in range(size):
            row_str = f"{i} |"
            for j in range(size):
                if show_mines and (i, j) in mine_positions:
                    row_str += "💣 "
                elif revealed[i][j]:
                    if (i, j) in mine_positions:
                        row_str += "💣 "
                    else:
                        count = count_adjacent_mines(i, j)
                        row_str += f"{count} " if count > 0 else "  "
                else:
                    row_str += "■ "
            row_str += "|"
            print(row_str)
        print("  +" + "-" * (size * 2 - 1) + "+")
    
    while not game_over and cells_revealed < total_safe_cells:
        print_board()
        print(f"Celdas seguras reveladas: {cells_revealed}/{total_safe_cells}")
        
        try:
            row = int(input("Fila (0-5): "))
            col = int(input("Columna (0-5): "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue
        
        if row < 0 or row >= size or col < 0 or col >= size:
            print("Posición fuera del tablero.")
            continue
        
        if revealed[row][col]:
            print("Ya revelaste esta celda.")
            continue
        
        revealed[row][col] = True
        
        if (row, col) in mine_positions:
            game_over = True
            print("💥 ¡BOOM! ¡Pisaste una mina!")
        else:
            cells_revealed += 1
            # Revelar celdas adyacentes si no hay minas alrededor
            if count_adjacent_mines(row, col) == 0:
                # Revelar recursivamente (simplificado)
                for r in range(max(0, row-1), min(size, row+2)):
                    for c in range(max(0, col-1), min(size, col+2)):
                        if not revealed[r][c] and (r, c) not in mine_positions:
                            revealed[r][c] = True
                            cells_revealed += 1
    
    # Fin del juego
    print_board(show_mines=True)
    if not game_over:
        print("🎉 ¡GANASTE! Encontraste todas las celdas seguras.")
    else:
        print("💀 Game Over! Mejor suerte la próxima vez.")
    
    input("Presiona Enter para continuar...")

# JUEGO 5: TETRIS SIMPLIFICADO
def tetris_simple():
    """Versión simplificada de Tetris"""
    width, height = 10, 16
    board = [[' ' for _ in range(width)] for _ in range(height)]
    score = 0
    
    # Piezas básicas
    pieces = [
        [['■', '■'], ['■', '■']],  # Cuadrado
        [['■', '■', '■', '■']],    # Línea
        [['■', '■', '■'], [' ', '■', ' ']],  # T
    ]
    
    current_piece = random.choice(pieces)
    piece_x = width // 2 - len(current_piece[0]) // 2
    piece_y = 0
    
    def rotate_piece(piece):
        """Rota la pieza 90 grados"""
        return [list(row) for row in zip(*piece[::-1])]
    
    def check_collision(board, piece, x, y):
        """Verifica si hay colisión"""
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] != ' ':
                    if (y + i >= height or x + j < 0 or x + j >= width or 
                        (y + i >= 0 and board[y + i][x + j] != ' ')):
                        return True
        return False
    
    def merge_piece(board, piece, x, y):
        """Fusiona la pieza con el tablero"""
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] != ' ' and 0 <= y + i < height:
                    board[y + i][x + j] = piece[i][j]
    
    def clear_lines(board):
        """Limpia líneas completas y devuelve el número de líneas limpiadas"""
        lines_cleared = 0
        for i in range(height):
            if all(cell != ' ' for cell in board[i]):
                del board[i]
                board.insert(0, [' ' for _ in range(width)])
                lines_cleared += 1
        return lines_cleared
    
    print("🎮 TETRIS SIMPLIFICADO")
    print("Controles: A (izquierda), D (derecha), W (rotar), S (bajar rápido)")
    print("Presiona Q para salir")
    time.sleep(2)
    
    game_over = False
    while not game_over:
        clear_screen()
        
        # Crear tablero temporal para mostrar
        temp_board = [row[:] for row in board]
        
        # Mostrar pieza actual
        for i in range(len(current_piece)):
            for j in range(len(current_piece[0])):
                if (0 <= piece_y + i < height and 0 <= piece_x + j < width and 
                    current_piece[i][j] != ' '):
                    temp_board[piece_y + i][piece_x + j] = current_piece[i][j]
        
        # Mostrar tablero
        print(f"Puntuación: {score}")
        print("+" + "-" * width + "+")
        for row in temp_board:
            print("|" + "".join(row) + "|")
        print("+" + "-" * width + "+")
        
        # Capturar input
        key = get_key()
        if key and key.lower() == 'q':
            break
        
        # Mover pieza
        new_x, new_y = piece_x, piece_y + 1
        
        if key and key.lower() == 'a':
            new_x = piece_x - 1
            new_y = piece_y
        elif key and key.lower() == 'd':
            new_x = piece_x + 1
            new_y = piece_y
        elif key and key.lower() == 'w':
            rotated = rotate_piece(current_piece)
            if not check_collision(board, rotated, piece_x, piece_y):
                current_piece = rotated
        elif key and key.lower() == 's':
            new_y = piece_y + 2
        
        # Verificar colisión
        if not check_collision(board, current_piece, new_x, new_y):
            piece_x, piece_y = new_x, new_y
        else:
            if new_y == piece_y + 1:  # Colisión al bajar
                merge_piece(board, current_piece, piece_x, piece_y)
                
                # Limpiar líneas
                lines = clear_lines(board)
                score += lines * 100
                
                # Nueva pieza
                current_piece = random.choice(pieces)
                piece_x = width // 2 - len(current_piece[0]) // 2
                piece_y = 0
                
                # Verificar game over
                if check_collision(board, current_piece, piece_x, piece_y):
                    game_over = True
        
        time.sleep(0.3)
    
    print(f"\n💀 Game Over! Puntuación final: {score}")
    input("Presiona Enter para continuar...")

# MENU PRINCIPAL
def show_menu():
    clear_screen()
    print("🎮 ARCADE DE JUEGOS EN TERMINAL")
    print("=" * 40)
    print("1. 🐍 Snake (Serpiente)")
    print("2. 🎯 Adivina el Número")
    print("3. ✂️ Piedra, Papel o Tijeras")
    print("4. 💣 Buscaminas")
    print("5. 🎮 Tetris Simplificado")
    print("6. 🚪 Salir")
    print("=" * 40)
    
    try:
        choice = input("Selecciona un juego (1-6): ").strip()
        return choice
    except (KeyboardInterrupt, EOFError):
        return '6'

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            snake_game()
        elif choice == '2':
            guess_number()
        elif choice == '3':
            rock_paper_scissors()
        elif choice == '4':
            minesweeper()
        elif choice == '5':
            tetris_simple()
        elif choice == '6':
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("Opción inválida. Presiona Enter para continuar...")
            input()

if __name__ == "__main__":
    main()
    
    
    """kasdkd
    lasdkas
    asldkasl
    asldmka
    alsd
    """