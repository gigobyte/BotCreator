# BotCreator
Create a bot that can click, move the mouse and press keys

###How to Run
`pip install pyHook`  and 
`pip install PyUserInput`

`python botcreator.py`

###How to Use
| Command  | What is does   |
|:---------|:---------------|
| add click | Waits for a click to happen anywhere on the screen. The click location will be added to the list of commands that the bot will execute.
| add typing     | Asks for a string that will be typed by the bot. |
| add key      | Asks for a key that will be pressed by the bot, how many times to repeat and the delay between the keystrokes. For supported keys see below |
| reset   | Resets all commands to the bot |
| run [n] | Runs all commands. (n = times to repeat (-1 is infinite, invalid arguments are treated as 1))

####Supported keys
| Keys  | Supported?   | How to Add |
|:---------|:---------------|:------|
| a-Z | Yes | No special rule |
| 0-9 | Yes | No special rule |
| Numpad Keys | No | |
| Virtual-Keys | Partially | [See LUT](docs/virtual-keys.md) |
| Function Keys | Yes (to F12), No (F13 and up) | [See LUT](docs/function-keys.md) |
| Media Keys | Yes | [See LUT](docs/media-keys.md) |
