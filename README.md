# ToonTown Corporate Clash Bot
*A Discord Bot that utilizes the Corporate Clash API to provide information about the game.*

### Current Feature Set
* **About** - Displays the about page for the bot
* **Cog** - Displays information about a specific cog.
* **Districts** - Displays information about the online districts in the game.
* **Game** - Displays information about the game, including whether the game is running and how many toons are online.
* **Help** - Displays the help page for the bot with command descriptions
* **Invasions** - Displays information about the active invasions in the game.
* **News** - Displays the latest news from the TTCC website.
* **NPC** - Displays information about a specific NPC.
* **Ping** - Allows users to ping the bot and receive the bot's latency in milliseconds.

### Changelog
* **0.6.0** (*20MAY*)
  * NPC Support! `/npc <npc name>` provides information about various NPC's.  Unfortunately, this database is limited to whether the NPC has a wiki article about them.
  * Modified `/cog` to concatenate exe and regular cogs into one branch.  Gets rid of a lot of repetitive code for a very simple change.
* **0.5.0** (*20MAY*)
  * We now support a `/cog` command that can provide information about any cog! Format the command `/cog <cog name>`.  The command should be case-insensitive and supports acronyms of the bosses (VP, CFO,...).
  * Currently the code for this functionality isn't the best due to various exceptions that are made in the Clash Wiki databse.  This has caused a good bit of repeat code that in the future I would like to remove.
* **0.4.2** (*20MAY*)
  * Bug fixes for `/about` command
* **0.4.1** (*20MAY*)
  * Improved `/districts` and `/invasions` to allow for search terms!
  * Both queries allow for searching for a specific district.  `/invasions` allows you to search by cog as well!
* **0.4.0** (*20MAY*)
  * Built the `/game` command which provides macro-information about the game, including whether the game is running and toons online!
* **0.3.0** (*20MAY*)
  * We support news now! Use `/news` to get the latest news from the TTCC website.
* **0.2.0** (*20MAY*)
  * Our first update with real-time TTCC information!
  * Implemented both the `/districts` and `/invasions` commands, which provide information about online districts and active invasions, respectively.
  * My goal is to make full use of each API before moving on to new API requests.
* **0.1.0** (*20MAY*)
  * Initial Commit to GitHub
  * This commit contains the shell of the bot, plus working **ping** command.

*Bot Name: `LordLowdenClear#2417`*