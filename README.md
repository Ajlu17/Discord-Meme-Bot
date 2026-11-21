# Discord Bot in Python

I built this Discord bot as the final project for my first Python course at Codédex. It can say hello, share random memes, report its connection latency, and send a formatted message.

## Commands

| Command | What it does |
| --- | --- |
| `/hello` or `$hello` | Replies with “Hello World!” |
| `/meme` or `$meme` | Sends a link to a random meme from Meme API. |
| `/ping` | Replies with “Pong!” and shows the bot’s connection latency to Discord in milliseconds. |
| `/embed` | Sends an embedded message with a title, a description, and a blue sidebar. |

## How to run it

You’ll need Python 3 and permission to add the bot to a Discord server.

1. Open a terminal in the project folder and install the dependencies.

   ```bash
   python -m pip install discord.py requests python-dotenv
   ```

2. Create an application in the Discord Developer Portal. Under **Bot**, get your bot token and enable **Message Content Intent** so the bot can read commands that start with `$`. [Discord Developer Portal](https://discord.com/developers/applications) · [Discord’s guide to privileged intents](https://support-dev.discord.com/hc/en-us/articles/6207308062871-What-are-Privileged-Intents)

3. Under **Installation**, configure **Guild Install** with the `bot` and `applications.commands` scopes. Give the bot permission to view the channel and send messages, then use the installation link to add it to your server. [Discord’s application commands documentation](https://docs.discord.com/developers/docs/interactions/slash-commands)

4. Create a file named `.env` in the same folder as `bot.py` and replace `your_bot_token_here` with your bot token. Git ignores this file to keep the token out of the repository.

   ```dotenv
   DISCORD_TOKEN=your_bot_token_here
   ```

5. Start the bot.

   ```bash
   python bot.py
   ```

   When you see `Logged as ...!` in the terminal, try `/hello` in a channel on your server.

## What I practiced

- Using classes and events with `discord.py` to respond to messages and register commands.
- Making HTTP requests with `requests` and reading JSON to get a meme URL.
- Loading the bot token from an environment variable with `python-dotenv`.
- Using `async` and `await` to send responses to Discord.
