"""
Created on Thu Feb 12 11:05 2026

AUTHOR      : Sai Koushik Parachi
EMAIL       : Parachi.SaiKoushik@yokogawa.com
VERSION     : v_final
FileName    : alvida.py
Objective   : This python file try to show the gratitude, emotions and farewell as message teammate.

Parameters  :
    INPUT   : 4.6 Years time.
    OUPUT   : Mix of Emotions, Thankfulness, Gratitude, Farewell Message.

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
            "\nIt is with mixed emotions that I announce that 13-Feb-2026 will be my LWD "
            "from the IT-OT SOC team and Yokogawa. "
            "This was not an easy decision, as my journey here has been incredibly rewarding "
            "both personally and professionally. "
            "I am excited for the next stage of my career, but I will truly miss our daily collaboration "
            "and the unique energy this team brings. "
            "Thank you for all the memories and smiles that I will cherish for the rest of my life. "
            "Yokogawa gave me the opportunity to work with global leaders, domestic clients, and gain on-site exposure "
            "that helped elevate my career to the next level. "
            "Thank you, Yokogawa and team — I hope our paths cross again soon."
        )
        return intimation

    def say_goodbye(self):
        colleague = self.name
        if colleague in ['Shiozaki san', 'Shrikanth san', 'Furuya san']:

            message = (
                f"Thank you for the opportunity to work with you, {colleague}! "
                "Your leadership and vision are truly unmatched. "
                "It has been a pleasure collaborating with you and learning from your experiences. "
                "Wishing you all the very best!\n"
            )

        elif colleague == 'Rajeev san':
            message = (
                f"I'm blessed to have had you as a manager, {colleague}. "
                "Your trust and guidance have been invaluable. "
                "Your skills — team building, motivation, composure, patience, vision, and support — are exceptional. "
                "I can confidently say that you are a true leader beyond just a manager. "
                "It has been a pleasure working with you, and I've learned a lot. "
                "Wishing you all the very best!"
            )

        elif colleague == 'Jeeth':
            message = (
                f"{colleague} were the first buddy I spoke to in the team 4.6 years ago. "
                "You completely changed my perspective towards Yokogawa and brought positive vibes into my journey. "
                "I've learned so much from the way you approach situations and challenges with positivity and clarity. "
                "I truly see you as a future leader — your skills in planning, organization, empathy, timely delivery, "
                "motivation, and communication stand out. "
                "The trips we had with the team gave everyone the perfect escape into nature, and those memories will always be cherished. "
                "Wishing you all the very best in your professional career and spiritual journey!"
            )

        elif colleague == 'Sumitra':
            message = (
                f"Thank you for the opportunity to work with you, {colleague}! "
                "Your selflessness and supportive nature are truly admirable. "
                "It has been a pleasure collaborating with you and learning from you."
            )

        elif colleague in ['Pankaj', 'Gouse', 'Neel', 'Karthik', 'Chaithanya', 'Sudeep']:
            if colleague == 'Pankaj':
                message = (
                    f"{colleague} san — Although I did not get the chance to work closely with you, "
                    "your resource management and organizational skills are truly impressive. :P"
                )
            elif colleague == 'Gouse':
                message = (
                    f"{colleague} anna — Your inclusive and welcoming nature is inspiring, "
                    "and your depth of understanding in technical topics is highly appreciated. :P"
                )
            elif colleague == 'Neel':
                message = (
                    f"{colleague} — It has been a pleasure collaborating with you. Hope Everything goes well in your personal and Professional Life. "
                    "I always enjoyed your timing and sense of humor. :P"
                )
            elif colleague == 'Karthik':
                message = (
                    f"{colleague} bro — Your openness and wholehearted nature are truly admirable. "
                    "And yes, the way you skip trips at the last minute is sometimes more fun than the trip itself! Jut Kidding :P"
                )
            elif colleague == 'Chaithanya':
                message = (
                    f"{colleague} bro — Your dedication, clarity in understanding concepts, "
                    "and confidence while handling challenges are awesome. Keep it up! :) :P"
                )
            elif colleague == 'Sudeep':
                message = (
                    f"{colleague} bro — Your knowledge, patience, and simple smile are truly admirable. I wish in future i could like to see a movie with you in Theater :P"
                )
            else:

                message = "Amazing working with you!, Enjoy your journey ahead!"

        elif colleague in ['Deepali', 'Shreyanshi', 'Jyoti', 'Akshata', 'Shiv', 'Ajay', 'Sandhya', 'Amar']:
            if colleague == 'Deepali':
                message = (
                    f"{colleague} — I'm amazed by your transformation in technical skills, incident mitigation,and Python programming. Keep going strong! "
                )
            elif colleague == 'Sandhya':
                message = (
                    f"{colleague} — Though I did not work closely with you, your dedication to learning and completing tasks on time is a great asset to the team. Keep it up!"
                )
            elif colleague in ['Ajay', 'Shiv']:
                message = (
                    f"{colleague} — Your energy, enthusiasm towards work, and willingness to help team members are truly appreciable."
                )
            elif colleague in ['Amar', 'Jyoti', 'Akshata']:
                message = (
                    f"{colleague} — Though I did not work closely with you, your dedication to learning and completing tasks on time is a great asset to the team. Keep it up!"
                )
            elif colleague == 'Shreyanshi':
                message = (
                    f"{colleague} — You have become a key person in the smooth execution and maintenance of the project. That progress is commendable."
                )
            else:
                message = "Amazing working with you!, Enjoy your journey ahead!"
        elif colleague in ['Raja', 'Jayshankar',]:
            if colleague == 'Raja':
                message = (
                    f"{colleague} bro — Your dedication, learning new things, and willingness to help others are truly admirable. "
                    "It has been a pleasure working with you, and I wish you all the best in your future endeavors!"
                )
            elif colleague == 'Jayshankar':

                message = (
                    f"{colleague} bro — Your leadership, guidance, and support have been invaluable. "
                    "Thank you for being such a great colleague!"
                )
        elif colleague in ['Varun', 'Prajwal', 'Vandita', 'Mahesh', 'Sameer', 'Harsha']:
            message = (
                "It has been a pleasure sharing the workspace with the Cloud Team — "
                "Sameer, Mahesh, Varun, Prajwal, Vandita, and everyone else. "
                "Although I didn't get the opportunity to work directly with you, "
                "I have always admired your expertise and dedication. "
                "Wishing you all the very best in your future endeavors!"
            )

        else:
            message = (
                "Wishing you the very best for your future. "
                "It was truly great working with you!"
                "Amazing working with you!, Enjoy your journey ahead!"
            )

        return f"\nGoodbye, {self.name}!\n{message}\n"

    def say_closing_comments():
        comments = (
            "I leave this Yokogawa chapter with a heart full of gratitude and wonderful memories. "
            "I wish you all continued success and happiness in your future endeavors.\n\n"
            "I would be happy to stay connected — please feel free to reach out anytime!\n"
            "GitHub: https://github.com/sparachi1011/      "   "  LinkedIn: https://www.linkedin.com/in/saikoushikparachi/\n"
            "Phone: +91-8125131375/9819370113     " "           Email: saikoushik.parachi@gmail.com\n"
        )
        return comments


def _normalize(s: str) -> str:
    """
    Lowercase, replace hyphens/underscores/dots with spaces,
    remove non-alphanumeric (except spaces), collapse multiple spaces.
    """
    s = s.lower().strip()
    s = re.sub(r'[-._]+', ' ', s)          # treat separators as spaces
    s = re.sub(r'[^a-z0-9\s]', '', s)      # keep only letters, numbers, spaces
    s = re.sub(r'\s+', ' ', s)             # collapse spaces
    return s


def _email_to_tokens(s: str) -> List[str]:
    """
    If input is an email, take local part before '@'.
    Split on common separators and normalize.
    """
    local = s.split(
        '@', 1)[0]  # works for non-email too; returns entire string if no '@'
    norm = _normalize(local)
    return [t for t in norm.split() if t]   # tokens


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
    try:
        result = find_name_from_input(colleagues, input_name)
        alvida = Alvida("Yokogawa Team")
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
        ['Varun', 'Prajwal', 'Vandita', 'Mahesh', 'Sameer', 'Harsha'],
    ]

    user_value = sys.argv
    user_value = input(
        "Hey Colleague! Good to See You...\nPlease Enter your Name or Email: ").strip()
    main(user_value)
    input("\nPress Enter to exit...")


"""
---> to create a QR code to open webage whis is hosted in github pages --->> 
pip install qrcode pillow   
python build_qr_site.py --url "https://sparachi1011.github.io/farewell" --out site --logo "Yokogawa_logo.png"   
---> to create a executable using python --->> 
pip install pyinstaller  
pyinstaller --onefile --name SaiKoushikParachi_Alvida_Note .\alvida.py

"""
