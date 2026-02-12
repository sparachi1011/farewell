"""
Created on Thu Feb 12 11:05 2026
AUTHOR : Sai Koushik Parachi
EMAIL  : Parachi.SaiKoushik@yokogawa.com
VERSION: v_final
FileName: alvida.py
Objective : This python file try to show the gratitude, emotions and farewell as message teammate.
Parameters :
  INPUT  : 4.6 Years time.
  OUPUT  : Mix of Emotions, Thankfulness, Gratitude, Farewell Message.
"""
# from Koushik import BestWishes, FarewellMessage, Emotions, etc.
import sys
import re
from typing import List, Optional


class Alvida:
    def __init__(self, name):
        self.name = name

    def say_farewell():
        intimation = (
            "\n   It is with mixed emotions that I announce that 13-Feb-2026 will be my last working day with the IT-OT SOC team and Yokogawa. This was not an easy decision, as my journey here has been incredibly rewarding both personally and professionally."
            "I am excited for the next stage of my career, but I will truly miss our daily collaboration and the unique energy this team brings. Thank you for all the memories and smiles that I will cherish for the rest of my life."
            "Yokogawa gave me the opportunity to work with global leaders, domestic clients, and gain on-site exposure that helped elevate my career to the next level."
            "Thank you, Yokogawa and team — I hope our paths cross again soon."
        )
        return intimation

    def say_goodbye(self):
        colleague = self.name
        if colleague in ['Shiozaki san', 'Shrikanth san', 'Furuya san']:
            message = (
                f"  {colleague}, thank you for giving me the opportunity to work under your guidance."
                "Your leadership, clarity of vision, and ability to steer the team with confidence and purpose have always inspired me. Working with you has been one of the most meaningful parts of my journey here."
                "Your strategic thinking, calm decision-making, and commitment to excellence have shaped not just the team, but also my own professional growth. It has truly been a privilege to learn from your experience and witness the impact of your leadership firsthand."
                "Thank you for the trust, the opportunities, and the environment you created for us to grow, contribute, and excel."
                "Wishing you continued success in everything you lead and build."
                "It has been an honor collaborating with you.\n"
            )
        elif colleague == 'Rajeev san':
            message = (
                f"  I feel truly blessed to have had you as my manager, {colleague}. Your trust, guidance, and unwavering belief in me have meant more than I can ever express. You didn't just lead the team — you shaped us, inspired us, and stood by us with patience, clarity, and purpose."
                "Your abilities in team building, motivation, composure, patience, vision, and support are extraordinary. But what makes you truly special is the heart and humility behind everything you do. You are not just a manager to me — you are a mentor, a role model, and someone I deeply respect."
                "I've learned so much from you, not only professionally but personally. Working with you has been one of the most meaningful parts of my journey. Thank you for every lesson, every encouragement, and every moment of support."
                "Wishing you nothing but the very best ahead — you deserve all the success and happiness in the world."
            )
        elif colleague == 'Jeeth':
            message = (
                f"  {colleague}, you were the first buddy I spoke to in the team 4.6 years ago, and that moment truly shaped my journey here. You completely changed my perspective toward Yokogawa and brought so much positivity into my experience."
                "I've learned a lot from you — especially from the way you handle situations and challenges with such clarity and optimism. I genuinely see you as a future leader. Your strengths in planning, organization, empathy, timely delivery, motivation, and communication really stand out and make a difference."
                "The trips we took with the team gave all of us the perfect escape into nature, and those memories will always stay close to my heart."
                "Wishing you all the very best in your professional career and on your spiritual journey. May both lead you to growth, peace, and fulfillment!"
            )
        elif colleague == 'Sumitra':
            message = (
                f"  Thank you for the opportunity to work with you, {colleague}! Your selflessness and supportive nature are truly admirable, and they make a real difference to everyone around you."
                "It has been a pleasure collaborating with you and learning from you. I genuinely appreciate the positivity and clarity you bring into every interaction."
                "Wishing you continued success and growth in everything you do!"
            )
        elif colleague in ['Pankaj', 'Gouse', 'Neel', 'Karthik', 'Chaithanya', 'Sudeep']:
            if colleague == 'Pankaj':
                message = (
                    f"  {colleague} san — Although I did not get the chance to work closely with you, "
                    "your resource management and organizational skills are truly impressive."
                )
            elif colleague == 'Gouse':
                message = (
                    f"  {colleague} anna — your inclusive and welcoming nature has always touched me more than you know. You have this rare ability to make people feel seen, heard, and genuinely valued, and that warmth creates such a positive space for everyone around you."
                    "I truly admire the depth of your understanding in technical topics not only in networking — not just the knowledge itself, but the calm, patient, and humble way you share it. You make learning easier, conversations richer, and complex things feel simple. It’s something I deeply appreciate. 😊🙏"
                    "Thank you for being the kind of person who lifts others up just by being yourself. Stay the same wonderful anna — the team is better because of you."
                )
            elif colleague == 'Neel':
                message = (
                    f"  {colleague} — it has truly been a pleasure collaborating with you. I genuinely wish that everything goes beautifully for you in both your personal and professional life. You deserve every bit of happiness and success that comes your way."
                    "I've always enjoyed your perfect timing and sense of humor — you have this natural way of lightening the mood and making even the busiest days feel easier. 😄"
                    "All the very best, bro! Stay cheerful, stay grounded, and keep spreading those good vibes. 🙂😜✨"
                )
            elif colleague == 'Karthik':
                message = (
                    f"  {colleague} bro — Your openness and wholehearted nature have always stood out to me. You bring a kind of warmth and honesty that makes people feel instantly at ease, and that's something truly rare and special."
                    "And yes… the way you skip trips at the very last minute still makes all of us laugh — sometimes it becomes a bigger story than the trip itself! Just kidding 😄😜"
                    "But beyond the jokes, I really treasure the memories we've created together in recent times. Those moments — the conversations, the laughter, the small things — have meant a lot to me, and I'll genuinely carry them forward."
                    "Wishing you all the very best, buddy. Stay the same kind-hearted, genuine, and uplifting person you are. You bring light wherever you go — never lose that. 🙂✨"
                )
            elif colleague == 'Chaithanya':
                message = (
                    f"  {colleague} bro — {colleague}, your dedication truly stands out. The way you grasp concepts with such clarity and face challenges with confidence always inspires me. It's not just your skills — it's the heart you put into everything you do that makes a real difference."
                    "You are one of the very few in the team whom I can always count on — someone I can trust and rely upon, not just professionally but personally as well. That means a lot to me."
                    "I genuinely admire the passion and positivity you bring into your work. Keep believing in yourself, keep growing, and keep shining — you're capable of so much more than you realize. 🙂💛"
                )
            elif colleague == 'Sudeep':
                message = (
                    f"  {colleague} bro — Your knowledge, your patience, and even that simple, genuine smile of yours are truly admirable. You have a calmness and kindness that make people feel comfortable around you, and that's something I've always appreciated."
                    "And yes… someday in the future, it would be fun to catch a movie with you in the theatre — just for the laughs and the good company! 😄🍿😜"
                    "Stay the same warm and wonderful person you are. Wishing you happiness and success in everything you do!"
                )
            else:
                message = "Amazing working with you!, Enjoy your journey ahead!"
        elif colleague in ['Deepali', 'Shreyanshi', 'Jyoti', 'Akshata', 'Shiv', 'Ajay', 'Sandhya', 'Amar']:
            if colleague == 'Deepali':
                message = (
                    f"  {colleague} — I'm genuinely amazed by how much you've grown — in your technical skills, your incident-mitigation approach, and especially your progress in Python programming. Watching your transformation has been inspiring, and it shows how much dedication and hard work you've put in."
                    "I truly hope you continue exploring Python and AI-based skills, because you have so much potential to go even further. Keep learning, keep experimenting, and keep pushing your limits — you're on a great path."
                    "I also hope our paths cross again in the future. Until then, keep going strong and shine brighter with each step you take!"
                )
            elif colleague == 'Sandhya':
                message = (
                    f"  {colleague} — Even though we didn't work closely together, I've always noticed your dedication to learning, taking ownership, and completing your tasks on time. These qualities are a true asset to the team and speak volumes about your commitment."
                    "Your observations and investigation techniques during incident responses are truly commendable. The way you approach problems with clarity and attention to detail shows how capable and reliable you are."
                    "Keep it up — you're growing fast, and your efforts genuinely make a difference!"
                )
            elif colleague in ['Ajay', 'Shiv']:
                message = (
                    f"  {colleague} — Your energy and enthusiasm toward work have always stood out, {colleague}. You bring a spark that lifts the whole team, and it truly makes a difference."
                    "What I appreciate even more is your willingness to step in and help team members whenever they need support. That kindness, that readiness to contribute, and that positive spirit are qualities not everyone has — and they are genuinely appreciable."
                    "Keep shining with the same passion and drive. You're doing great, and your effort never goes unnoticed!"
                )
            elif colleague in ['Amar', 'Jyoti', 'Akshata']:
                message = (
                    f"  {colleague} — Though I did not work closely with you, your dedication to learning and completing tasks on time is a great asset to the team. Keep it up!"
                )
            elif colleague == 'Shreyanshi':
                message = (
                    f"  {colleague} — You have become a key person in the smooth execution and maintenance of the project. That progress is commendable."
                )
            else:
                message = "Amazing working with you!, Enjoy your journey ahead!"
        elif colleague in ['Raja', 'Jayshankar', ]:
            if colleague == 'Raja':
                message = (
                    f"  {colleague} Ji — your dedication, your eagerness to learn new things, and your willingness to help others whenever they need it are qualities I truly admire. You’ve always shown a positive spirit and a readiness to step in, and that genuinely makes a difference in the team."
                    "It has been a real pleasure worked with you. I've appreciated your energy, your support, and the way you carry yourself with humility and sincerity."
                    "Wishing you all the very best in your future HYGIENE Endeavors, bro!"
                )
            elif colleague == 'Jayshankar':
                message = (
                    f"  {colleague} bro — You have always been so interactive and connected with everyone on the team. Even though we spent most of our time working remotely, you consistently made the effort to stay in touch and genuinely care about each individual. That quality of yours — being present even from a distance — is truly special and something I deeply admire."
                    "Your leadership, guidance, and constant support have meant a lot. You’ve been more than just a colleague — you’ve been someone the team could count on, someone who brought stability, clarity, and kindness into every interaction."
                    "Thank you for being such a wonderful colleague and an even better human being. I sincerely wish you all the success, happiness, and beautiful smiles that life has to offer in your future journey."
                    "Stay amazing, and keep inspiring everyone around you!"
                )
        elif colleague in ['Varun', 'Prajwal', 'Vandita', 'Mahesh', 'Thangella.Maheswara@yokogawa.com', 'mahes', 'maheswara', 'Sameer', 'Harsha']:
            message = (
                f"   It has been a real pleasure sharing the workspace with the Cloud Team — Varun bhai, Sameer, Mahesh, Prajwal, Vandita, and everyone else. Even though I didn't get the chance to work with you all directly, I have always admired the expertise, dedication, and professionalism each of you brings to the table.\n"
                "Your contributions, passion for learning, and commitment to excellence have always stood out, and being around such a talented team has been inspiring in itself."
                "Wishing every one of you the very best in your future endeavors — may you continue to excel, innovate, and achieve great milestones ahead!"
            )
        elif colleague in ['Satya', 'Prahlad', 'Chaitanya', 'Pradeep', 'Charvie', 'Soma', 'Kalpesh', 'Apurva', 'mahesh.naik', 'naik', 'mahesh.naik@yokogawa.com']:
            message = (
                f"    {colleague}-san, it has truly been a joy and an honor working with you. When I look back at my time in YAD/UAE, some of my fondest memories are the moments shared with colleagues like you — moments filled with warmth, support, and genuine connection."
                "Your kindness, positivity, and wholehearted acceptance made my journey not just comfortable, but truly meaningful. You brought a sense of belonging and encouragement that I will always carry with me. Working alongside you has enriched me both personally and professionally, and I’m sincerely grateful for that."
                "I wish you all the success, happiness, and fulfillment in everything that lies ahead for you. And from the bottom of my heart, I hope our paths cross again, wherever life takes us."
                "Until then, please stay safe, stay happy, and keep smiling... 🙂💛✨"
            )
        else:
            message = (
                f"Wishing you all the very best for your future, {colleague}. It has truly been wonderful working with you!\n"
                f"I’ve genuinely enjoyed every interaction — your positivity, professionalism, and the ease you bring into teamwork always made collaborations smoother and more enjoyable.\n"
                f"Amazing working with you, and I hope your journey ahead is filled with success, happiness, and exciting new opportunities. Enjoy every step forward! 🌟🙂"
            )
        return f"\nGoodbye, {colleague}!\n{message}\n"

    def say_closing_comments():
        comments = (
            "\n   I leave this Yokogawa chapter with a heart full of gratitude and countless wonderful memories. Every experience, every interaction, and every moment here has shaped me in ways I will always cherish."
            "Thank you all for being such an important part of my journey. I genuinely wish each one of you continued success, growth, and happiness in everything you pursue moving forward."
            "I would be truly happy to stay connected — please feel free to reach out anytime. Your connection and friendship will always mean a lot to me."
            "\nGitHub: https://github.com/sparachi1011/    "  "    LinkedIn: https://www.linkedin.com/in/saikoushikparachi/"
            "\nPhone: +91-8125131375 / 9819370113          "        "    Email: saikoushik.parachi@gmail.com"
        )
        return comments


def _normalize(s: str) -> str:
    """
    Lowercase, replace hyphens/underscores/dots with spaces,
    remove non-alphanumeric (except spaces), collapse multiple spaces.
    """
    s = s.lower().strip()
    s = re.sub(r'[\-._]+', ' ', s)  # treat separators as spaces
    s = re.sub(r'[^a-z0-9\s]', '', s)  # keep only letters, numbers, spaces
    s = re.sub(r'\s+', ' ', s)  # collapse spaces
    return s


def _email_to_tokens(s: str) -> List[str]:
    """
    If input is an email, take local part before '@'.
    Split on common separators and normalize.
    """
    local = s.split(
        '@', 1)[0]  # works for non-email too; returns entire string if no '@'
    norm = _normalize(local)
    return [t for t in norm.split() if t]  # tokens


def _name_tokens(name: str) -> List[str]:
    """Normalize a full name and split into tokens."""
    return [t for t in _normalize(name).split() if t]


def find_name_from_input(colleagues: List[List[str]], user_input: str) -> Optional[str]:
    """
    Return only the matched name from the colleagues list of lists,
    using robust matching against an email or free text.
    Matching rules (in order):
    1) Exact token match (name token == input token)
    2) Substring match (len >= 3) either direction: token in name_token or name_token in token
    Returns the first best match found, or None if no match.
    """
    tokens = _email_to_tokens(user_input)
    if not tokens:
        return None

    # Pass 1: exact token == token
    for group in colleagues:
        for name in group:
            ntoks = _name_tokens(name)
            if any(t in ntoks for t in tokens):
                return name

    # Pass 2: substring match with a minimum length to avoid noise (e.g., 'aj' shouldn't match 'ajay')
    MIN_SUBSTR = 4
    for group in colleagues:
        for name in group:
            ntoks = _name_tokens(name)
            for t in tokens:
                if len(t) < MIN_SUBSTR:
                    continue
                if any(t in nt or nt in t for nt in ntoks if len(nt) >= MIN_SUBSTR):
                    return name

    # fallback: return the first token as a name guess
    return tokens[0].title()


def main(input_name: str):
    """
    Run only when the user provided a non-empty Name/Email.
    If input is blank/whitespace, do NOT print any farewell/default messages.
    """
    try:
        if not (input_name and input_name.strip()):
            print("Please enter a Name or Email to see your farewell message.")
            return

        result = find_name_from_input(colleagues, input_name)

        # Show general farewell first, then a person-specific message (or fallback),
        # then the closing — only after we confirmed we have some input.
        print(Alvida.say_farewell())
        if result:
            print(Alvida(result).say_goodbye())
        else:
            print("\n", Alvida("Colleague").say_goodbye())
        print(Alvida.say_closing_comments())
    except Exception as e:
        print("Error in main execution:", e)


if __name__ == "__main__":
    colleagues = [
        ['Shiozaki san', 'Shrikanth san', 'Furuya san'],
        ['Rajeev san'], ['Jeeth'], ['Sumitra'],
        ['Pankaj', 'Gouse', 'Neel', 'Karthik', 'Chaithanya', 'Sudeep'],
        ['Deepali', 'Shreyanshi', 'Jyoti', 'Akshata',
         'Shiv', 'Ajay', 'Sandhya', 'Amar'],
        ['Varun', 'Prajwal', 'Vandita', 'Thangella.Maheswara@yokogawa.com',
            'mahes', 'maheswara', 'Sameer', 'Harsha'],
        ['Satya', 'Prahlad', 'Chaitanya', 'Pradeep',
         'Charvie', 'Soma', 'Kalpesh', 'Apurva', 'mahesh.naik', 'naik', 'mahesh.naik@yokogawa.com']
    ]
    user_value = input(
        "Hey Colleague! Good to See You...\nPlease enter your Name or Email: "
    ).strip()
    # main() now handles the "empty input" case by not printing defaults.
    main(user_value)

"""
----> to create a QR code to open webage whis is hosted in github pages -->>
pip install qrcode pillow
python build_qr_site.py --url "https://sparachi1011.github.io/farewell" --out site --logo "Yokogawa_logo.png"
python build_qr_site.py --url "https://sparachi1011.github.io/farewell" --out site --logo "Yokogawa_logo.png" 
----> to create a executable using python -->>
pip install pyinstaller
pyinstaller --onefile --name SaiKoushikParachi_Alvida_Note .\\alvida.py
"""
