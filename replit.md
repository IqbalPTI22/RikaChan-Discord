# RikaChan-Discord Bot

## Overview
This is a Discord bot called "RikaChan" that helps server administrators set up and organize Discord servers with predefined categories and channels in Indonesian. The bot can completely restructure a Discord server with organized channels for information, main chat, entertainment, and configuration sections.

## Recent Changes (September 13, 2025)
- ✅ Set up Python 3.11 environment with discord.py library
- ✅ Improved security: Added proper TOKEN environment variable handling with error checking
- ✅ Configured Discord Bot workflow to run the bot continuously
- ✅ Successfully connected bot to Discord (running as "Rika")

## Project Architecture
- **Language**: Python 3.11
- **Main Library**: discord.py (v2.6.3)
- **Bot Type**: Discord server management bot
- **Command Prefix**: `!` (e.g., `!setup`)

## Bot Features
- **Server Setup Command** (`!setup`): Completely reorganizes a Discord server
  - Requires administrator permissions
  - Asks for confirmation before proceeding
  - Deletes all existing channels and categories
  - Creates new structured channel layout with Indonesian naming

## Channel Structure Created
1. **Information Section** (`『 ⛩️ 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 ⛩️ 』`)
   - 📣│pengumuman (announcements)
   - 📜│peraturan (rules)
   - 📢│pemberitahuan (notifications)

2. **Main Chat Section** (`『 💬 𝐎𝐁𝐑𝐎𝐋𝐀𝐍 𝐔𝐓𝐀𝐌𝐀 💬 』`)
   - network-chat
   - 💬│obrolan-utama (main chat)
   - 🎨│media
   - 🎤│voice-chat (voice channel)

3. **Entertainment Section** (`『 🎮 𝐇𝐈𝐁𝐔𝐑𝐀𝐍 🎮 』`)
   - 🤖│bot-commands
   - 🃏│game-lobby
   - 📺│spoiler-anime
   - 😂│meme

4. **Configuration Section** (`『 ⚙️ 𝐏𝐄𝐍𝐆𝐀𝐓𝐔𝐑𝐀𝐍 ⚙️ 』`)
   - 🔒│verifikasi (verification)

## Environment Setup
- **TOKEN**: Discord bot token (securely stored in Replit Secrets)
- **Workflow**: "Discord Bot" runs `python main.py`

## Discord Developer Portal Setup Required
Before using the bot, ensure the following are enabled in the Discord Developer Portal:
1. **Bot Token**: Generated and added to Replit Secrets as `TOKEN`
2. **Privileged Gateway Intents**:
   - Message Content Intent (required for reading message content like "ya" confirmations)
   - Server Members Intent (required for server management features)
   - All other intents are automatically granted
3. **Bot Permissions**: Administrator permissions in target Discord servers

## Security Features
- Proper environment variable handling with error checking
- Administrator permission requirement for setup command
- Confirmation prompt before destructive operations
- Graceful error handling for permission issues

## Current Status
✅ **Ready to Use**: Bot is connected and running successfully in the Replit environment.