import random

# List of spicy truth questions
truths = [
    "What's the most adventurous thing you've done in bed?",
    "Have you ever had a naughty dream about someone here?",
    "What's your biggest turn-on?",
    "Have you ever sent a spicy text to the wrong person? What happened?",
    "What's the wildest place you've ever gotten freaky?",
    "Have you ever had a crush on a friend's partner?",
    "If you could only do one position for the rest of your life, which one would it be?",
    "Have you ever tried roleplay? If yes, what character did you play?",
    "What's your guilty pleasure when it comes to intimacy?",
    "Have you ever had a one-night stand?",
    "What's the most embarrassing thing that's happened to you during intimacy?",
    "Would you rather be dominant or submissive?",
    "Have you ever had a secret friends-with-benefits situation?",
    "What’s the weirdest thing someone has asked you to do in bed?",
    "Have you ever sent nudes? If yes, to who?",
    "What's the sexiest dream you've ever had?",
    "If you could sleep with any celebrity, who would it be?",
    "Have you ever kissed more than one person in 24 hours?",
    "Do you prefer morning or night action? Why?",
    "Have you ever had a crush on a teacher or boss?",
    "What’s the longest you've gone without getting some action?",
    "Do you think you’re good in bed? Why or why not?",
    "Have you ever faked it? Why?",
    "What's something you've always wanted to try in bed but haven't?",
    "Would you rather have a public quickie or an all-night private session?",
    "Have you ever had a spicy video call? How did it go?",
    "What's the most unexpected place you've ever gotten turned on?",
    "Have you ever had a wardrobe malfunction in public?",
    "If you had to describe your last intimate experience in one word, what would it be?",
    "What’s your opinion on toys in the bedroom?",
    "Have you ever been caught doing something naughty? What happened?",
    "What’s the most daring thing you’ve ever worn out in public?",
    "Have you ever had a secret crush on a friend’s sibling?",
    "If you had to pick one, would you rather be kissed on the neck or whispered to in the ear?",
    "What’s the sexiest compliment you’ve ever received?",
    "Have you ever had a sneaky moment in public?",
    "Do you prefer slow and sensual or fast and rough?",
    "What’s your favorite body part on yourself and why?",
    "What’s your go-to move to turn someone on?",
    "Have you ever had a spicy moment in a car?",
    "Have you ever lied about your body count?",
    "Would you ever consider an open relationship?",
    "What’s one thing you wish your past partners did better?",
    "If you had to pick one, would you rather have a steamy shower session or a cozy cuddle session?",
    "What’s the naughtiest thought you’ve had today?",
    "Have you ever flirted with someone just to get something you wanted?",
    "Have you ever made the first move? How did it go?",
    "Would you rather have a secret affair or be in an open relationship?",
    "Have you ever been attracted to someone much older than you?",
    "If you could change one thing about your past intimate experiences, what would it be?"
]

# List of spicy dares
dares = [
    "Send a flirty text to the third person in your chat list.",
    "Whisper something naughty to the person on your right.",
    "Let someone write something on your body with a marker.",
    "Describe your best intimate experience in detail.",
    "Give someone in the group a 10-second seductive stare.",
    "Do your sexiest dance for 30 seconds.",
    "Call your crush and say ‘I can’t stop thinking about you...’",
    "Lick your lips and bite them while looking at someone in the group.",
    "Send a voice note saying something seductive to your last text contact.",
    "Give someone a back massage for one minute.",
    "Do a body shot off someone (or pretend to).",
    "Put an ice cube in your mouth and kiss the back of your hand.",
    "Say something super flirty to the next person who walks in.",
    "Write a naughty text but don’t send it—just show it to the group.",
    "Pretend to give someone in the group a lap dance.",
    "Let someone scroll through your gallery for 10 seconds.",
    "Tell the group your wildest fantasy.",
    "Read a spicy text from your phone out loud.",
    "Describe in detail how you’d seduce your crush.",
    "Let the group decide what part of your body you should kiss.",
    "Do a slow-motion kiss in the air like it's a movie scene.",
    "Do 10 squats while making seductive eye contact with someone.",
    "Recreate the last flirty text you sent but say it out loud.",
    "Do a roleplay scene where you're hitting on someone in a bar.",
    "Let someone in the group send an emoji-only text to your crush.",
    "Find a romantic song and sing along to it seductively.",
    "Let the group pick someone for you to call and say 'I miss you.'",
    "Text your ex ‘I still think about you sometimes…’",
    "Give someone a genuine, deep compliment about their looks.",
    "Look into someone's eyes and say 'I want you' without laughing.",
    "Act out how you'd confess your feelings to your crush.",
    "Take off one piece of clothing (nothing extreme, lol).",
    "Let someone in the group choose a pickup line for you to use on someone.",
    "Say the most attractive thing about everyone in the group.",
    "Show the last person you searched for on Instagram.",
    "Blow a kiss to someone in the group.",
    "Send a mysterious ‘We need to talk…’ text to a random contact.",
    "Give someone a tight hug and don’t let go for 10 seconds.",
    "Let someone write something flirty on your arm with a pen.",
    "Take a video saying 'I have a crush on you' and send it to your best friend.",
    "Let the group pick a contact for you to send 'I love you' to.",
    "Do a sexy pose and let the group take a picture.",
    "Make an exaggerated seductive face for 5 seconds.",
    "Act like you're on a romantic date with the person next to you.",
    "Whisper a flirty compliment to someone’s ear.",
    "Let someone play with your hair for 30 seconds.",
    "Send a winking selfie to the last person you texted.",
    "Say your most used flirty line in your most seductive voice."
]

random.shuffle(truths)
random.shuffle(dares)

print("🔥 Welcome to Spicy Truth or Dare! 🔥")
while truths or dares:
    choice = input("\nPick one - Truth (T) or Dare (D)? (Press Q to quit): ").strip().lower()

    if choice == 't' and truths:
        print("🗣️ Truth:", truths.pop())
    elif choice == 'd' and dares:
        print("💪 Dare:", dares.pop())
    elif choice == 'q':
        print("Game Over! 😈 Hope you had fun! 🎉")
        break
    else:
        print("No more questions left, game over! 🔥")
