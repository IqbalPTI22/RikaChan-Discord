import discord
from discord.ext import commands
import os
import asyncio

# Get Discord bot token from environment variable
TOKEN = os.environ.get('TOKEN')
if not TOKEN:
    print("ERROR: TOKEN environment variable not found!")
    print("Please set your Discord bot token using the TOKEN environment variable.")
    exit(1)

# Prefix untuk perintah bot, contoh: !setup
# Kamu bisa ganti sesuai keinginanmu.
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Susunan channel dan kategori yang akan kita buat
# Kamu bisa ubah atau tambahkan sesuai keinginanmu
CHANNELS_TO_CREATE = {
    "『 ⛩️ 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐒𝐈 ⛩️ 』": [
        "📣│pengumuman",
        "📜│peraturan",
        "📢│pemberitahuan"
    ],
    "『 💬 𝐎𝐁𝐑𝐎𝐋𝐀𝐍 𝐔𝐓𝐀𝐌𝐀 💬 』": [
        "network-chat",
        "💬│obrolan-utama",
        "🎨│media",
        "🎤│voice-chat"
    ],
    "『 🎮 𝐇𝐈𝐁𝐔𝐑𝐀𝐍 🎮 』": [
        "🤖│bot-commands",
        "🃏│game-lobby",
        "📺│spoiler-anime",
        "😂│meme"
    ],
    "『 ⚙️ 𝐏𝐄𝐍𝐆𝐀𝐓𝐔𝐑𝐀𝐍 ⚙️ 』": [
        "🔒│verifikasi"
    ]
}

# Event saat bot sudah siap (online)
@bot.event
async def on_ready():
    print(f'Bot sudah masuk sebagai {bot.user.name}!')
    print('Bot siap digunakan di server.')

# Perintah untuk mengatur server
@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    """
    Perintah untuk menghapus semua channel yang ada dan membuat susunan channel baru.
    Hanya bisa digunakan oleh user dengan izin administrator.
    """
    
    # Konfirmasi sebelum menjalankan perintah
    await ctx.send("Apakah kamu yakin ingin mengatur ulang server? Proses ini akan menghapus semua channel dan kategori yang ada. Ketik `ya` untuk melanjutkan.")

    def check(m):
        return m.author == ctx.author and m.content.lower() == 'ya' and m.channel == ctx.channel

    try:
        # Menunggu konfirmasi dari user
        await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        await ctx.send("Waktu habis. Proses pengaturan server dibatalkan.")
        return

    # Kirim pesan bahwa proses dimulai
    await ctx.send("Memulai proses pengaturan server...")
    
    # Simpan reference ke user untuk DM jika diperlukan
    user = ctx.author
    
    # Hapus semua channel yang ada
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except discord.errors.Forbidden:
            print(f"Tidak bisa menghapus channel {channel.name} karena tidak punya izin.")
        except Exception as e:
            print(f"Terjadi kesalahan saat menghapus channel {channel.name}: {e}")

    # Buat kategori dan channel baru sesuai daftar di atas
    announcements_channel = None
    
    for category_name, channel_list in CHANNELS_TO_CREATE.items():
        try:
            # Buat kategori baru
            category = await ctx.guild.create_category(category_name)
            
            # Buat channel di dalam kategori tersebut
            for channel_name in channel_list:
                # Buat channel teks
                if "voice-chat" not in channel_name:
                    new_channel = await category.create_text_channel(channel_name)
                    # Simpan announcements channel untuk pesan status
                    if "pengumuman" in channel_name:
                        announcements_channel = new_channel
                # Buat channel suara
                else:
                    await category.create_voice_channel(channel_name)
                    
            print(f"Kategori '{category_name}' dan channel-nya berhasil dibuat.")

        except discord.errors.Forbidden:
            # Gunakan DM jika tidak bisa kirim ke channel
            try:
                await user.send("Bot tidak memiliki izin untuk membuat channel atau kategori. Pastikan bot memiliki izin Administrator.")
            except:
                print("Tidak bisa mengirim pesan ke user karena DM tertutup.")
            return
        except Exception as e:
            print(f"Terjadi kesalahan saat membuat kategori {category_name}: {e}")
            # Gunakan DM jika tidak bisa kirim ke channel
            try:
                await user.send(f"Terjadi kesalahan: {e}")
            except:
                print(f"Tidak bisa mengirim pesan error ke user: {e}")
            return

    # Kirim pesan sukses ke announcements channel atau DM
    success_message = "Server berhasil diatur! Selamat datang di server wibu yang rapi dan keren!"
    if announcements_channel:
        await announcements_channel.send(success_message)
    else:
        try:
            await user.send(success_message)
        except:
            print("Setup selesai, tapi tidak bisa mengirim konfirmasi ke user.")

# Jalankan bot
bot.run(TOKEN)
