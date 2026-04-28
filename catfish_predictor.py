from datetime import datetime
import time


def get_time():
    while True:
        time_input = input("Enter what time you fished, example 7:30 PM: ").strip().upper()

        try:
            valid_time = datetime.strptime(time_input, "%I:%M %p").time()

            print("\nThank you, I successfully recorded the time.")
            time.sleep(1.5)

            return valid_time

        except ValueError:
            print("Invalid format. Please enter again like 7:30 PM")

def get_weather_info():
    weather_questions = {
        "cloudy": "Was it cloudy? (y/n): ",
        "rain": "Did it rain recently? (y/n): ",
        "wind": "Was it windy? (y/n): "
    }

    weather_answers = {}

    for key, questions in weather_questions.items():
        while True:
            user_answers = input(questions).strip().lower()

            if user_answers == 'y' or user_answers == 'n':
                weather_answers[key] = user_answers
                break
            else:
                print("Please enter y or n")

    return weather_answers

def get_tide_current_info():
    water_questions = {
        "tide": "Was the tide high or low?: ",
        "current": "Was it a fast or slow current?: ",
        "body": "Did you fish a lake, river, pond, or bay?: "
    }

    valid_answers = {
        "tide": ["high", "low"],
        "current": ["fast", "slow"],
        "body": ["lake", "river", "pond", "bay"]
    }

    water_answers = {}

    for key, question in water_questions.items():
        while True:
            user_answer = input(question).strip().lower()

            if user_answer in valid_answers[key]:
                water_answers[key] = user_answer
                break
            else:
                print(f"Invalid answer. Please enter one of these: {valid_answers[key]}")

    return water_answers

def get_bait_info():
    bait_types = {
        1: "stink bait",
        2: "chicken liver",
        3: "worms",
        4: "shrimp",
        5: "cut bait",
        6: "other"
    }
    print("Choose your bait:")

    for number, bait in bait_types.items():
        print(f"{number}. {bait}")

    while True:
        bait_used = input("What bait was used?: ")

        try:
            bait_choice = int(bait_used)
            if 1 <= bait_choice <= 6:
                selected_bait = bait_types[bait_choice]
                return selected_bait
            else:
                print("Please enter a number 1-6")
        except ValueError:
            print("Please only enter a number 1-6")

def get_location_info():
    location_type = {
        1: "creek mouth / drain",
        2: "deep hole / channel edge",
        3: "bridge / dock / structure",
        4: "open bank",
        5: "other"
    }

    print("Location Details")

    for number, location in location_type.items():
        print(f"{number}. {location}")

    while True:
        loc_details = input("Which best describes the spot?: ")

        try:
            loc_choice = int(loc_details)
            if 1 <= loc_choice <= 5:
                selected_loc = location_type[loc_choice]
                return selected_loc
            else:
                print("Please enter a number 1-5 that best fits")
        except ValueError:
            print("Please only enter a number 1-5")

def classify_time(fishing_time):
    hour = fishing_time.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 21:
        return "evening"
    else:
        return "night"


print(get_bait_info())