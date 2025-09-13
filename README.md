# 🎌 RikaChan - Discord Bot 🎌

[![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Discord.py Version](https://img.shields.io/badge/discord.py-2.3.2-yellowgreen?style=for-the-badge)](https://discordpy.readthedocs.io/en/latest/)

Welcome to the RikaChan-Discord Bot repository! This project contains the source code for a Discord bot designed to help server administrators quickly organize their communities. The bot automatically creates a clean and structured channel layout, perfect for any otaku community.

---

## 🚀 Key Features

-   **Automatic Server Setup**: Use a single command to instantly restructure your server's channels.
-   **Wibu-Themed Channels**: The bot creates a unique and aesthetic channel structure.
-   **Robust Error Handling**: The bot provides clear feedback on errors, including sending direct messages to the user if channel permissions are an issue.
-   **Secure Token Handling**: The bot code is configured to safely retrieve the bot token from an environment variable, preventing sensitive information from being exposed.

---

## 🛠️ How to Self-Host

Follow these steps to set up and run your own version of RikaChan.

### 1. Prerequisites

-   **Python 3.x**: Make sure you have Python installed on your system.
-   **A Discord Bot Token**: Create a new application and bot on the [Discord Developer Portal](https://discord.com/developers/applications). Remember to enable all **Privileged Gateway Intents**.
-   **Python Libraries**: Install the necessary libraries using `pip`:
    ```
    pip install discord.py
    ```

### 2. Configuration

1.  Clone this repository to your local machine:
    ```
    git clone [https://github.com/USERNAME/RikaChan-Discord-Bot.git](https://github.com/USERNAME/RikaChan-Discord-Bot.git)
    ```
    (Replace `USERNAME` with your GitHub username)
2.  Set your bot token as an **environment variable** named `TOKEN`.
    * **On Replit**: Use the **Secrets** tab to securely store your token.
    * **On your computer**: Use your operating system's environment variable settings.

---

### 🎨 Editing the Channel Structure

To customize the channel layout, open the `main.py` file and locate the variable named **`CHANNELS_TO_CREATE`**.

This variable is a Python dictionary, where each **"key"** is the category name, and the **"value"** is a list of channel names.

You can:
-   Change the names of categories and channels.
-   Add or remove new categories and channels.
-   Make sure to use the same format, with category names in double quotes (`""`) and the list of channels in square brackets (`[]`) separated by commas.

Example:
```python
CHANNELS_TO_CREATE = {
    "NEW CATEGORY NAME": [
        "channel-name-1",
        "channel-name-2"
    ],
    "ANOTHER CATEGORY": [
        "another-channel"
    ]
}
```
### 3. Running the Bot

Run the bot from your terminal: 
```
python main.py
```
For 24/7 uptime, consider using a cloud service like **Replit**, **Heroku**, or a dedicated server.

### 4. Bot Commands

Simply invite the bot to your server and use the following command:

```
!setup
```

**Warning**: This command will delete all existing channels and categories on the server and replace them with a new structure. Use with extreme caution!

---

## 🤝 Contributing

If you'd like to contribute, please feel free to `fork` this repository and submit a `pull request` with your changes.

---

## 📜 License

This project is licensed under the [MIT License](https://github.com/github/docs/blob/main/LICENSE).

---

## ✨ Acknowledgements

The code for this bot was significantly improved and enhanced with the help of Replit's AI agent.
