# BotCreator 1.0.7
Create a bot that can click, move the mouse and press keys

### How to Prepare
Install [pyHook](http://sourceforge.net/projects/pyhook/)

Install [Intel PyWin](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win32-py2.7.exe/download) or [AMD PyWin](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py2.7.exe/download)

### How to Use
| Command  | What is does   |
|:---------|:---------------|
| add click | Waits for a click to happen anywhere on the screen. The click location will be added to the list of commands that the bot will execute.
| add string    | Asks for a string that will be typed by the bot. |
| add key      | Asks for a key that will be pressed by the bot, how many times to repeat and the delay between the keystrokes. For supported keys see below |
| load [file] | Loads a BotCreator script |
| save [file] | Save all current commands to a BotCreator script |
| reset   | Resets all commands to the bot |
| run [n] | Runs all commands. (n = times to repeat (-1 is infinite, invalid arguments are treated as 1))
| list commands | Shows all current commands |

#### Supported keys
| Keys  | Supported?   | How to Add |
|:---------|:---------------|:------|
| a-Z | Yes | No special rule |
| 0-9 | Yes | No special rule |
| Numpad Keys | No | |
| Virtual-Keys | Partially | [See LUT](docs/virtual-keys.md) |
| Function Keys | Yes (to F12), No (F13 and up) | No special rule |
| Media Keys | Partially | [See LUT](docs/media-keys.md) |

#### Changelog
* Mostly bugfixes

#### TODO List
> More keys support

> More script customizations

> Multi-keystroke support

> 'exec' command that will launch programs
