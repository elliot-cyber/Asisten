from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Fungsi untuk memulai bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}! Selamat datang di Bot Asisten Belajar. "
        "Ketik /menu untuk melihat pilihan."
    )

# Fungsi untuk menampilkan menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Pilih opsi:\n"
        "/materi - Materi pelajaran\n"
        "/latihan - Soal latihan\n"
        "/tanya - Tanya jawab\n"
    )

# Fungsi untuk memberikan materi
async def materi(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Materi: Silakan pilih topik yang ingin dipelajari.")

# Fungsi untuk latihan soal
async def latihan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Latihan soal: Silakan pilih tingkat kesulitan.")

# Fungsi untuk tanya jawab
async def tanya(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Tanya jawab: Apa yang ingin kamu tanyakan?")

async def main() -> None:
    # Token API yang didapat dari BotFather
    application = ApplicationBuilder().token("7586237226:AAHPMFLJKX91meJaUdlhQKHvOz2n41PRZnI").build()

    # Daftar handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("materi", materi))
    application.add_handler(CommandHandler("latihan", latihan))
    application.add_handler(CommandHandler("tanya", tanya))

    # Mulai bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main()
