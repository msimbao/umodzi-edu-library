import json

# Redefine the full quiz and quiz3 data since the code state was reset
from pathlib import Path

# Load quiz and quiz3 definitions from previous messages
# We use only quiz and quiz3 here since quiz1 wasn't fully provided

# Manually reimporting the quizzes from text since the state was reset

quiz = [
    {
    "id": "eng-g7-001",
    "title": "Grammar & Vocabulary Mastery",
    "subject": "English",
    "grade": "7",
    "questions": [
        {
            "question": "Choose the correct verb: She ____ very fast.",
            "options": ["run", "ran", "runs", "running"],
            "answer": "runs",
            "explanation": "'She' needs the singular verb 'runs' in the present tense."
        },
        {
            "question": "Which word is a noun?",
            "options": ["quick", "run", "happiness", "slowly"],
            "answer": "happiness",
            "explanation": "'Happiness' is a thing (idea), so it's a noun."
        },
        {
            "question": "What is the antonym of 'polite'?",
            "options": ["rude", "kind", "soft", "shy"],
            "answer": "rude",
            "explanation": "'Rude' is the opposite of 'polite'."
        },
        {
            "question": "Which word is an adverb?",
            "options": ["loud", "quickly", "happy", "teacher"],
            "answer": "quickly",
            "explanation": "Adverbs describe verbs and often end in '-ly'."
        },
        {
            "question": "Identify the preposition: The cat is under the table.",
            "options": ["cat", "under", "is", "table"],
            "answer": "under",
            "explanation": "'Under' shows position, so it’s a preposition."
        },
        {
            "question": "Select the correct sentence.",
            "options": [
                "He go to school.",
                "He goes to school.",
                "He going to school.",
                "He gone to school."
            ],
            "answer": "He goes to school.",
            "explanation": "Correct subject-verb agreement: 'He goes...'"
        },
        {
            "question": "Choose the correct pronoun: ____ is my best friend.",
            "options": ["Her", "She", "Them", "They"],
            "answer": "She",
            "explanation": "'She' is the subject pronoun needed here."
        },
        {
            "question": "Which word is misspelled?",
            "options": ["becuase", "friend", "school", "family"],
            "answer": "becuase",
            "explanation": "Correct spelling is 'because'."
        },
        {
            "question": "What is a synonym for 'intelligent'?",
            "options": ["smart", "lazy", "silly", "boring"],
            "answer": "smart",
            "explanation": "A synonym is a word with the same meaning."
        },
        {
            "question": "Complete the sentence: They ____ playing football.",
            "options": ["was", "is", "are", "be"],
            "answer": "are",
            "explanation": "'They' takes the verb 'are'."
        },
        {
            "question": "Which sentence is in the future tense?",
            "options": [
                "She dances well.",
                "She danced yesterday.",
                "She will dance tomorrow.",
                "She is dancing now."
            ],
            "answer": "She will dance tomorrow.",
            "explanation": "Future tense uses 'will'."
        },
        {
            "question": "Identify the conjunction: I like tea and coffee.",
            "options": ["like", "tea", "and", "coffee"],
            "answer": "and",
            "explanation": "A conjunction joins two words or phrases."
        },
        {
            "question": "Choose the correct article: I saw ____ elephant.",
            "options": ["a", "an", "the", "some"],
            "answer": "an",
            "explanation": "Use 'an' before vowel sounds like 'elephant'."
        },
        {
            "question": "What is the plural of 'child'?",
            "options": ["childs", "childes", "children", "childrens"],
            "answer": "children",
            "explanation": "It's an irregular plural."
        },
        {
            "question": "Which word is an interjection?",
            "options": ["Wow!", "Run", "Walk", "Never"],
            "answer": "Wow!",
            "explanation": "'Wow!' expresses emotion, making it an interjection."
        },
        {
            "question": "Which is a complete sentence?",
            "options": [
                "Running through the field.",
                "The boy running fast.",
                "The boy ran through the field.",
                "Ran fast in the field."
            ],
            "answer": "The boy ran through the field.",
            "explanation": "A complete sentence has a subject and a verb."
        },
        {
            "question": "Find the correct contraction: He is not here.",
            "options": ["Heisn't", "He not's", "He isn't", "He'sn't"],
            "answer": "He isn't",
            "explanation": "The correct contraction of 'He is not' is 'He isn't'."
        },
        {
            "question": "Which is a compound word?",
            "options": ["sun", "shine", "sunshine", "light"],
            "answer": "sunshine",
            "explanation": "'Sunshine' is made from two words: sun + shine."
        },
        {
            "question": "Which is an example of a question?",
            "options": [
                "What time is it?",
                "He is late.",
                "You are happy.",
                "Close the door."
            ],
            "answer": "What time is it?",
            "explanation": "It asks something and ends with a question mark."
        },
        {
            "question": "Choose the sentence with correct capitalization.",
            "options": [
                "i live in zambia.",
                "I live in zambia.",
                "i live in Zambia.",
                "I live in Zambia."
            ],
            "answer": "I live in Zambia.",
            "explanation": "Start with a capital 'I' and capitalize proper nouns."
        }
    ]
}
]

# Function to convert correct answers to indices
def convert_answers_to_indices(quiz):
    for q in quiz["questions"]:
        if "answer" in q and "options" in q:
            try:
                q["answer"] = q["options"].index(q["answer"])
            except ValueError:
                q["answer"] = None
    return quiz

# Convert and save
quiz_indexed = convert_answers_to_indices(quiz)
quiz_path = "fixedQuiz.json"

with open(quiz_path, "w") as f:
    json.dump(quiz_indexed, f, indent=2)

# quiz_path