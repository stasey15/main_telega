from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, CallbackContext

# Стани розмови
START, CHOOSING_PROFESSION, END = range(3)

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    update.message.reply_text(
        f"Привіт, {user.first_name}!\n\n"
        "Я твій бот-помічник, який допоможе дізнатися більше про сферу IT.\n"
        "Розповім більш детально про кожну професію, дам поради, і ти зможеш вибрати, яка професія тобі сподобалась.\n\n"
        "Ти готовий продовжувати?",
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Так, звісно!", callback_data='yes'),
            InlineKeyboardButton("Ні, в інший раз)", callback_data='no')
        ]])
    )
    return START

def profession_choice(update: Update, context: CallbackContext):
    query = update.callback_query
    user_choice = query.data

    if user_choice == 'yes':
        query.edit_message_text(
            "Суперово! Тоді ось деякі затребувані професії в IT. "
            "Натисни на кнопку, щоб дізнатися більше про неї.",
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("1. Програміст", callback_data='programmer'),
                InlineKeyboardButton("2. Тестувальник (QA менеджер)", callback_data='tester'),
            ], [
                InlineKeyboardButton("3. Web-розробник", callback_data='web_developer'),
                InlineKeyboardButton("4. Game-розробник", callback_data='game_developer'),
            ], [
                InlineKeyboardButton("5. UX/UI дизайнер", callback_data='ux_ui_designer'),
                InlineKeyboardButton("6. Project менеджер", callback_data='project_manager'),
            ], [
                InlineKeyboardButton("7. Front end/Back end розробник", callback_data='frontend_backend_dev'),
            ]]))
        return CHOOSING_PROFESSION

    elif user_choice == 'no':
        query.edit_message_text("Окей, я завжди тут, якщо ти будеш готовий дізнатися більше. До побачення!")
        return END

def show_profession_info(update: Update, context: CallbackContext):
    query = update.callback_query
    profession = query.data

    if profession == 'programmer':
        text = (
            "Програміст – це фахівець, який займається програмуванням та розробкою програмного забезпечення. "
            "Вони можуть використовувати різні мови програмування, такі як Python, JavaScript, Java, C++, C#, "
            "для створення різних програм, ботів та функціоналів."
        )
    elif profession == 'tester':
        text = (
            "Тестувальник (QA менеджер) - це професія, пов'язана з якістю програмного забезпечення. "
            "Тестувальники відповідають за перевірку та виявлення помилок та недоліків в програмах перед їх випуском на ринок. "
            "Основні завдання цієї професії - розробка тест-кейсів, проведення тестування, виявлення багів і підготовка звітів."
        )
    elif profession == 'web_developer':
        text = (
            "Web-розробник - це спеціаліст, який займається розробкою веб-сайтів і веб-додатків"
            "Веб-розробники працюють з різними технологіями, такими як HTML, CSS, JavaScript та інші, для створення функціональних та естетично приємних веб-інтерфейсів. "
            "Вони також можуть працювати з різними фреймворками і бібліотеками для полегшення розробки"
        )
    elif profession == 'game_developer':
        text = (
            "Game-розробник - це фахівець, який створює відеоігри. Робота game-розробника включає в себе програмування геймплею, розробку графіки та анімацій, створення музики та звукового супроводу, а також тестування гри на наявність багів"
            "Геймдевелопмент може бути дуже творчим та захоплюючим видом роботи"
        )
    elif profession == 'ux_ui_designer':
        text = (
            "UX/UI дизайнер - це професіонал, який відповідає за створення зручних і естетичних інтерфейсів для користувачів. "
            "UX (User Experience) дизайнер займається розробкою взаємодії користувачів з продуктом, тоді як UI (User Interface) дизайнер створює зовнішній вигляд інтерфейсу."
        )
    elif profession == 'project_manager':
        text = (
            "Project менеджер - це фахівець, який відповідає за керування та організацію проектів в галузі ІТ. "
            "Вони забезпечують, щоб проекти були завершені вчасно та в рамках бюджету, спілкуються з командами розробників та клієнтами, планують та відстежують завдання"
        )
    elif profession == 'frontend_backend_dev':
        text = (
            "Front end/Back end розробник - це дві різні професії в галузі програмування.Front-end розробник відповідає за створення користувацького інтерфейсу веб-сайту або додатка. Вони працюють з HTML, CSS та JavaScript, щоб забезпечити користувачам зручність і привабливий дизайн."
            "Back-end розробник відповідає за розробку серверної частини веб-додатка або сайту. Вони працюють з мовами програмування, такими як Python, Java, PHP, а також базами даних та серверами."
        )

    query.edit_message_text(text)

def main():
    updater = Updater("6342933823:AAEJ-8LiKRsWhdNfe-mof3_GQBgvo4q8CrY", use_context=True)
    dp = updater

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [CallbackQueryHandler(profession_choice, pattern='^(yes|no)$')],
            CHOOSING_PROFESSION: [CallbackQueryHandler(show_profession_info, pattern='^(programmer|tester|web_developer|game_developer|ux_ui_designer|project_manager|frontend_backend_dev)$')],
        },
        fallbacks=[]
    )

    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


