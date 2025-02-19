from pyrogram import Client, filters
from AnonXMusic import app

# Define your fonts as a list
fonts = [
    "🤍 ⍣⃪͜ ᶦ ͢ᵃᵐ⛦⃕‌!❛𝆺𝅥⤹࿗𓆪ꪾ™",
    "ᯓ𓆰𝅃🔥!⃪⍣꯭꯭𓆪꯭🝐",
    "➺ ‌⃪⃜ !✦ 𝆺𝅥⎯ꨄ",
    "❛ .𝁘ໍ!𓆪ִֶָ ֺ⎯꯭‌ 𓆩💗𓆪𓈒",
    "𓆰𝅃꯭᳚𓄂️𝆺𝅥⃝🔥 ⃪ͥ͢ ᷟ𓆩 ! 乛|⁪⁬⁮⁮⁮⁮ ‌⁪⁬𓆪🐼™",
    "ᯓ𓆰𝅃꯭᳚🦁!˶꯭꯭꯭꯭꯭꯭֟፝͟͝ ⚡꯭꯭꯭꯭꯭",
    "◄❥‌‌❥ ⃝⃪⃕🦚⟵᷽᷍!˚‌‌‌‌◡‌⃝🐬᪳ ‌⃪𔘓❁‌‌❍•:➛",
    "➺꯭ ꯭𝅥‌꯭𝆬‌🦋⃪꯭ ─⃛͢┼ 𝞄⃕𝖋𝖋 !🥵⃝⃝ᬽ꯭ ⃪꯭ ꯭𝅥‌꯭𝆬‌➺꯭⎯⎯᪵᪳",
    "ᯓ𓆰 𝅃!™ ٭ - 𓆪ꪾ⌯ 🜲 ˹ 𝐎ᴘ ˼",
    "—͟͞ 𝐈тᷟʑ꯭ͤ𓄂︪︫︠𓆩〭〬!⍣⃪͜ ꭗ̥̽𝆺꯭𝅥𔘓༌🪽⎯꯭̽⎯꯭ ꯭",
    "𓆰𓏲!𓂃ֶꪳ 𓆩〭〬🦋𓆪ꪾ",
    "𓆰⎯꯭꯭֯‌⌯ !𓂃ֶꪳ 𓆩〭〬🔥𓆪ꪾ",
    "🍹𝆺𝅥⃝🤍 ⃪ͥ͢ ᷟ●!🤍᪳𝆺꯭𝅥⎯꯭̽⎯꯭",
    "⋆⎯፝֟፝֟⎯᪵ 𝆺꯭𝅥! ᭄꯭🦋꯭᪳᪳᪻⎯̽⎯🐣",
    "⟶̽ꭙ⋆\"🔥𓆩〬 !⎯᳝֟፝֟⎯‌ꭙ⋆\"🔥",
    "⟶̽ꭙ⋆\"🔥𓆩〬 !🤍᪳𝆺꯭𝅥⎯᳝֟፝֟⎯‌",
    "⋆─፝─᪵།‌꯭! ا۬͢𝆺𝅥⃝🌸𝄄꯭꯭𝄄꯭꯭ ̶꯭𝅥ͦ𝆬👑",
    "❛ .𝁘ໍ!ꨄ 🦋𓂃•",
    "⟶̽𓆩〬𝁘ໍ!𓂃˖ॐ🪼⎯᳝֟፝⎯‌ꭙ⋆\"",
    "⏤͟͞ !𓂃 🔥𝆺𝅥 🜲 ⌯",
    "𓆰⎯꯭꯭֯‌!𓂃ֶꪳ 𓆩〭〬🔥𓆪ꪾ",
    ".𝁘ໍ⎯꯭̽- !⌯ 𝘅𝗗 𓂃⎯꯭‌ ִֶָ ֺ🎀",
    "𓂃❛ ⟶̽! ❜ 🌙⤹🌸",
    "❍⏤͟͞●!●───♫▷"
]

@app.on_message(filters.text)
def insert_name(client, message):
    name = message.text.strip()
    if not name:
        message.reply("Please send a name.")
        return

    # Pick a random font from the list
    font = fonts[0]  # You can randomize this if you prefer

    # Insert the name in the middle of the font
    mid_point = len(font) // 2
    new_text = font[:mid_point] + name + font[mid_point:]

    # Send the modified text back
    message.reply(new_text)
