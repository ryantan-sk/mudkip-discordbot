from discord.ext import commands
from PIL import Image

import discord


# Function to generate a game id for each game instance running
def game_id():
    num = 0
    while num < 9999:
        yield num
        num += 1


# Generator being called
generator = game_id()


class GameInstance(commands.Cog):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1  # Player 1 user.id from discord
        self.player_2 = player_2  # Player 2 user.id from discord
        self.player_turn = player_1
        self.game_id = next(generator)
        self.winner = ""

        self.board = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: "",
            9: ""
        }

    def __repr__(self):
        return "%04d" % self.game_id

    def switch_player(self):
        if self.player_turn == self.player_1:
            self.player_turn = self.player_2
        else:
            self.player_turn = self.player_1

    # List all empty spots left on the board
    def list_empty_spot(self):
        empty_spots = []

        for spot in self.board:
            if self.board[spot] == "":
                empty_spots.append(spot)

        return empty_spots

    # Checks if the board has reached a win state
    def check_win_state(self):
        # Horizontal win states
        if self.board[1] != "" and self.board[1] == self.board[2] and self.board[2] == self.board[3]:
                self.winner = self.board[1]
                return True

        elif self.board[4] != "" and self.board[4] == self.board[5] and self.board[5] == self.board[6]:
            self.winner = self.board[4]
            return True

        elif self.board[7] != "" and self.board[7] == self.board[8] and self.board[8] == self.board[9]:
            self.winner = self.board[7]
            return True

        # Vertical win states
        elif self.board[1] != "" and self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            self.winner = self.board[1]
            return True

        elif self.board[2] != "" and self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            self.winner = self.board[2]
            return True

        elif self.board[3] != "" and self.board[3] == self.board[6] and self.board[6] == self.board[9]:
            self.winner = self.board[3]
            return True

        # Diagonal win states
        elif self.board[1] != "" and self.board[1] == self.board[5] and self.board[5] == self.board[9]:
            self.winner = self.board[1]
            return True

        elif self.board[3] != "" and self.board[3] == self.board[5] and self.board[5] == self.board[7]:
            self.winner = self.board[3]
            return True

        else:
            return False

    # Checks if the board has reached a draw state, i.e. all 9 spots on-board are marked.
    def check_draw_state(self):
        if "" in self.board.values():
            return False
        else:
            return True

    def evaluate_board(self):
        if GameInstance.check_win_state(self) and self.winner == self.player_2:
            score = +10

        elif GameInstance.check_win_state(self) and self.winner == self.player_1:
            score = -10

        else:
            score = 0

        return score

    def minimax(self, depth, player):
        # Since AI is always player 2, self.player_2 is used to represent AI player
        if player == self.player_2:
            best = ["", -2]
            next_player = self.player_1

        # Likewise, human player is always designated as player 1 (called from discord)
        elif player == self.player_1:
            best = ["", +2]
            next_player = self.player_2

        # Base case for the recursive function minimax
        if depth == 0 or GameInstance.check_win_state(self):
            final_score = GameInstance.evaluate_board(self) - depth
            return ["", final_score]

        for spot in self.board:
            if self.board[spot] == "":
                test_position = spot
                self.board[test_position] = player

                # Recursive function which repeats until depth = 0 or win state is reached
                score = GameInstance.minimax(self, depth - 1, next_player)

                self.board[test_position] = ""
                score[0] = test_position

                # AI player looking to maximise its score
                if player == self.player_2:
                    if score[1] > best[1]:
                        best = score

                # Human player assumed to play optimally, minimising the score
                else:
                    if score[1] < best[1]:
                        best = score
            else:
                pass

        return best


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.current_players = []
        self.active_games = []

        self.image_coordinates = {
            1: (20, 20),
            2: (290, 20),
            3: (560, 20),
            4: (20, 290),
            5: (290, 290),
            6: (560, 290),
            7: (20, 550),
            8: (290, 550),
            9: (560, 550)
        }

    @staticmethod
    async def create_channel(player_1: discord.Member, player_2: discord.Member):
        await player_1.create_dm()
        channel_1 = player_1.dm_channel

        if player_2.bot:
            return channel_1, None
        else:
            player_2.create_dm()
            channel_2 = player_2.dm_channel
            return channel_1, channel_2

    @staticmethod
    async def send_intro_message(channel_1, channel_2):
        intro = discord.Embed(
            title="Tic Tac Toe Instructions",
            description="The board is accessed using numbers. Use the command !mark to play."
                        "\nFor example, entering !mark 5 will place a marker in the middle of the board."
                        "\nThe board is represented as follows:",
            colour=discord.Colour.blue()
        )

        intro.set_image(url="attachment://instructions.jpg")

        await channel_1.send(embed=intro, file=discord.File("cogs/library/games-files/TicTacToe/instructions.jpg"))

        if channel_2 is None:
            return
        else:
            await channel_2.send(embed=intro)

    async def render_board(self, server, user_input=0, player=0):
        # Rendering initial clean board
        if user_input == 0 and player == 0:
            path = "cogs/library/games-files/TicTacToe/TicTacToeBoard.jpg"
            board = Image.open(path)
            board.save(f"cogs/library/games-files/TicTacToe/{server}.jpg")
            return

        # Player 1 always plays with cross markers
        elif player == server.player_1 :
            player_symbol_path = "cogs/library/games-files/TicTacToe/cross.jpg"

        # Player 2 always play with circle markers
        else:
            player_symbol_path = "cogs/library/games-files/TicTacToe/circle.jpg"

        player_symbol = Image.open(player_symbol_path)

        current_board_path = f"cogs/library/games-files/TicTacToe/{server}.jpg"
        current_board_state = Image.open(current_board_path)

        # Places a marker both on the board and board image
        current_board_state.paste(player_symbol, self.image_coordinates[int(user_input)])
        server.board[int(user_input)] = player

        # Overwrites the previous board state image with the new one
        current_board_state.save(current_board_path)

    async def bot_turn(self, server, current_channel):
        GameInstance.switch_player(server)
        bot_player = server.player_2
        current_board_path = f"cogs/library/games-files/TicTacToe/{server}.jpg"

        depth = len(GameInstance.list_empty_spot(server))

        if depth != 0:
            move = GameInstance.minimax(server, depth, bot_player)
            position = move[0]

            await TicTacToe.render_board(self, server, position, bot_player)
            print(server.board)
            print(GameInstance.check_win_state(server))

        if GameInstance.check_win_state(server):
            if server.winner == bot_player:
                await current_channel.send("Tough luck! You lost!", file=discord.File(current_board_path))
            else:
                await current_channel.send("Congratulations! You won!", file=discord.File(current_board_path))
            TicTacToe.close_game(self, server)

        elif GameInstance.check_draw_state(server):
            string = "It's a draw!"
            await current_channel.send(string, file=discord.File(current_board_path))
            TicTacToe.close_game(self, server)

        else:
            await current_channel.send("Your opponent has made his move! Its your turn now."
                                    "\n Current board state:",
                                    file=discord.File(current_board_path))
            GameInstance.switch_player(server)

    def close_game(self, server):
        # Removes players and server from active players and games
        self.current_players.remove(server.player_1)
        self.current_players.remove(server.player_2)
        self.active_games.remove(server)

    async def update_board(self, server, user_input, player):
        await TicTacToe.render_board(self, server, user_input, player)

        current_board_path = f"cogs/library/games-files/TicTacToe/{server}.jpg"
        current_player = player

        # Identifying current player and next player
        if current_player == server.player_1:
            next_player = server.player_2
        elif current_player == server.player_2:
            next_player = server.player_1

        current_channel, next_channel = await TicTacToe.create_channel(current_player, next_player)

        if next_player.bot and next_player.name == "Mudkip":
            await TicTacToe.bot_turn(self, server, current_channel)
            return

        elif GameInstance.check_win_state(server):
            if server.winner == current_player:
                await current_channel.send("Congratulations! You won!", file=discord.File(current_board_path))
                await next_channel.send("Tough luck! You lost!", file=discord.File(current_board_path))
            else:
                await next_channel.send("Congratulations! You won!", file=discord.File(current_board_path))
                await current_channel.send("Tough luck! You lost!", file=discord.File(current_board_path))
            TicTacToe.close_game(self, server)

        elif GameInstance.check_draw_state(server):
            string = "It's a draw!"
            await current_channel.send(string, file=discord.File(current_board_path))
            await next_channel.send(string, file=discord.File(current_board_path))
            TicTacToe.close_game(self, server)

        else:
            await current_channel.send("You made your move. Waiting for the opponent.."
                                       "\n Current board state:", file=discord.File(current_board_path))
            await next_channel.send("Your opponent has made his move! Its your turn now."
                                    "\n Current board state:",
                                    file=discord.File(current_board_path))

            GameInstance.switch_player(server)

    @commands.command(name="tictactoe")
    async def start_tictactoe_game(self, ctx, member: discord.Member):

        player_1 = ctx.author
        player_2 = member

        # Checking if either of the players are currently in game
        if player_1 in self.current_players or player_2 in self.current_players:
            return

        # Creating a game instance
        new_server = GameInstance(player_1, player_2)

        # Adding to list of active games and players
        self.current_players.append(player_1)
        self.current_players.append(player_2)
        self.active_games.append(new_server)

        channel_1, channel_2 = await TicTacToe.create_channel(player_1, player_2)
        await TicTacToe.render_board(self, new_server)
        await TicTacToe.send_intro_message(channel_1, channel_2)

    @commands.command(name="mark")
    @commands.dm_only()
    async def mark_position_on_board(self, ctx, message):
        player = ctx.author

        # Prevents inactive players from using this command
        if player not in self.current_players:
            return

        # Finds the game server id
        for game_server in self.active_games:
            if player == game_server.player_1 or player == game_server.player_2:
                current_game_server = game_server

        # Prevents user from playing if it is not his/her turn
        if current_game_server.player_turn != player:
            await ctx.send("It is not your turn yet.")
            return

        # Prevents user from using string, out-of-bound integers and marked positions as arguments
        try:
            user_input = int(message)
        except ValueError:
            await ctx.send("Invalid move. Please enter a number between 1 and 9.")
            return

        if user_input < 1 or user_input > 9:
            await ctx.send("Invalid arguments. Please enter a number between 1 and 9.")
            return

        if current_game_server.board[int(user_input)] != "":
            await ctx.send("A marker has already been placed in that box.")
            return

        await TicTacToe.update_board(self, current_game_server, user_input, player)


def setup(bot):
    bot.add_cog(TicTacToe(bot))