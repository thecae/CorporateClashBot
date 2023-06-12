# ToonTown Corporate Clash Bot
*A Discord Bot that utilizes the Corporate Clash API to provide information about the game.*

### Current Feature Set
* **About** - Displays the about page for the bot
* **Cog** - Displays information about a specific cog.
* **Department** - Displays information about a specific department.
* **Districts** - Displays information about the online districts in the game.
* **Game** - Displays information about the game, including whether the game is running and how many toons are online.
* **HQ** - Displays information about headquarters in the game.
* **Help** - Displays the help page for the bot with command descriptions
* **Invasions** - Displays information about the active invasions in the game.
* **News** - Displays the latest news from the TTCC website.
* **NPC** - Displays information about a specific NPC.
* **Percentages** - Displays the percentages of each cog in the game.
* **Ping** - Allows users to ping the bot and receive the bot's latency in milliseconds.
* **Playground** - Displays information about a specific playground.
* **Street** - Displays information about a specific street.

### Changelog
* **1.4.0** (*12JUN*)
  * No super big updates this time around, haven't had much time to think of an implement big changes!
  * Running through the game, I realized I wanted to be able to run the percentages by playground.  Thus, `/p bossbots ttc` will filter only for ToonTown Central!
  * Minor bug when writing out `/p bossbots toontown central`, fix coming soon!
* **1.3.1** (*27MAY*)
  * Reply to messages rather than just sending a message. Just makes it easier to see what command resulted in that output.
  * Future updates will hopefully figure out how to delete the original message and still hold onto the reply to avoid the crowding of the chat.
* **1.3.0** (*26MAY*)
  * Added `/percentages` to get a list of street percentages for a department.  Streets are sorted from highest to lowest percentages.
  * Suggestion provided by Cones (*FORBO#7686*)
* **1.2.0** (*26MAY*)
  * Added `/department` command to get information about a department.
  * Biggest drawback is that Discord embeds have a limit of 25 fields per embeds and lawbots have more than 25 types of cogs.  This probably will soon affect the other types when they receive their "overclocked" updates.
  * Added aliases to some of the longer commands to make them easier.
* **1.1.0** (*23MAY*)
  * Added `/hq` to get information about headquarters.  Not much information here, but might add some more in the future.
  * Removed the `commands.on_ready()` function in each cog.  It's no longer necessary now that the CLI is remote.
  * Fixed some alignment issues because of the newlines in embeds for `/cog` and `/street`.
* **1.0.0** (*22MAY*)
  * We have gone remote! The bot is now hosted on a remote server and is running 24/7.
  * There are no feature updates this change; I will be using this update to test the bot running remotely.
  * I removed *update_log.py* just because it wasn't contributing to the actual bot functionality.  I'm still using it privately.
* **0.7.0** (*21MAY*)
  * Bringing street data to the bot! `/street <street name>` provides information about a specific street.
  * Bringing playground data to the bot! `/playground <playground name>` provides information about a specific playground.
  * All street data is localized and won't automatically update if changes are made to information such as cog levels, .exe percentage, and the suit distributions.  Hoping to fix this in the future, just having trouble with processing the request!
  * Made some formatting updates to `/cog` with newlines.
* **0.6.0** (*20MAY*)
  * NPC Support! `/npc <npc name>` provides information about various NPC's.  Unfortunately, this database is limited to whether the NPC has a wiki article about them.
  * Modified `/cog` to concatenate exe and regular cogs into one branch.  Gets rid of a lot of repetitive code for a very simple change.
* **0.5.0** (*20MAY*)
  * We now support a `/cog` command that can provide information about any cog! Format the command `/cog <cog name>`.  The command should be case-insensitive and supports acronyms of the bosses (VP, CFO,...).
  * Currently, the code for this functionality isn't the best due to various exceptions that are made in the Clash Wiki databse.  This has caused a good bit of repeat code that in the future I would like to remove.
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
  * This commit contains the shell of the bot, plus working `/ping` command.

*Bot Name: `LordLowdenClear#2417`*