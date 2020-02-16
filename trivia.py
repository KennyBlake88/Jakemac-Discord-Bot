import random
class Trivia:
    def __init__(self, questions):
        self.questions = questions
        self.qKeys = list(questions.keys())
        self.q = ""
        self.users = []
        self.sithPoints = 0
        self.jediPoints = 0

    def getQuestion(self, answered):
        if len(self.qKeys) == 0:
            if self.jediPoints > self.sithPoints:
                return "j"
            elif self.sithPoints > self.jediPoints:
                return "s"
        else:
            self.q = random.choice(self.qKeys)
            self.qKeys.pop(self.qKeys.index(self.q))
        return self.q


    
    def checkAnswer(self, userAnswer, role):
        a = userAnswer
        r = role
        if self.questions.get(self.q) == a:
            if r == "Jedi":
                self.jediPoints += 1
                return True
            elif r == "Sith":
                self.sithPoints += 1
                return True
            else:
                return "Sorry, you must play in either sith-gang or jedi-gang."
        else:
            return False


t = Trivia({"What is JakeMac's most popular video?": "Proof that Chandler, Ross and Joey dancing fits with anything.",
            "Who is darth vader actually?": "Anakin Skywalker",
            "When did the first star wars movie come out? (year only)": "1977",
            "In what movie did yoda die?": "Return of the Jedi",
            "Who is the original creator of StarWars?": "George Lucas",
            "Who can be seen on JakeMacs' channel Art? (Left to right, first names only)": "Shaggy, Jake, Yoda, Kermit, Anakin",
            "When did Jake join YouTube?(year only)": "2015",
            "What was the original Empire base called?" : "Death Star",
            "Who bought LucasFilms LTD?": "Disney",
            "Which starwars movie made the most money?": "A new hope"})
