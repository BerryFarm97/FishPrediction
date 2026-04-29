import time

def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()

        if answer == "y" or answer == "yes":
            return "yes"
        elif answer == "n" or answer == "no":
            return "no"
        else:
            print("Please enter y/n")


def ask_menu_choice(question, options):
    print(question)

    for number, item in options.items():
        print(f"{number}. {item}")

    while True:
        qst_ans = input("Enter a number: ")
        try:
            answer = int(qst_ans)
            if 1 <= answer <= len(options):
                return options[answer]
            else:
                print(f"Please enter a number 1-{len(options)}")
        except ValueError:
            print(f"Please enter only a number 1-{len(options)}")


def get_prediction_conditions():
    conditions = {}


    conditions["body_of_water"] = get_body_of_water().lower()
    conditions["water_level"] = water_level().lower()
    conditions["current"] = type_current().lower()

    weather_answers = get_weather_conditions()

    conditions.update(weather_answers)

    return conditions

def get_weather_conditions():
    weather_questions = {
        "cloud": "Is it cloudy?: ",
        "rain": "Has it rained recently?: ",
        "storm": "Is there dangerous weather?: "
    }

    result_answer = {}

    for key, question in weather_questions.items():
        answer = ask_yes_no(question)
        result_answer[key] = answer.strip().lower()
    return result_answer

def get_body_of_water():
    water_options = {
        1: "River",
        2: "Lake",
        3: "Pond",
        4: "Bayou"
    }

    return ask_menu_choice("Where are you wanting to fish today?", water_options)


def water_level():
    level_questions = {
        1: "Rising",
        2: "Stable",
        3: "Falling",
        4: "Unknown"
    }

    return ask_menu_choice("Do you know the water level today?", level_questions)


def type_current():
    current_questions = {
        1: "None",
        2: "Slow",
        3: "Moderate",
        4: "Fast",
        5: "Unknown"
    }

    return ask_menu_choice("What is the water current today?", current_questions)


def channel_cat_score_system(conditions):
    score = 0
    water_level_scores = {
        "rising": 15,
        "stable": 8,
        "falling": 2,
        "unknown": 5,
    }

    score += water_level_scores[conditions["water_level"]]

    cloud_score = {
        "yes": 8,
        "no": 2
    }

    score += cloud_score[conditions["cloud"]]

    rain_score = {
        "yes": 7,
        "no": 0
    }

    score += rain_score[conditions["rain"]]

    storm_score = {
        "yes": -20,
        "no": 0
    }

    score += storm_score[conditions["storm"]]

    water_current_score = {
        "moderate": 5,
        "slow": 4,
        "fast": 2,
        "unknown": 0,
        "none": 0
    }

    score += water_current_score[conditions["current"]]

    body_water_score = {
        "river": 10,
        "bayou": 9,
        "lake": 7,
        "pond": 6
    }

    score += body_water_score[conditions["body_of_water"]]
    """
    water_temp_score = {
        "good": 10,
        "unknown": 5,
        "bad": 2
    }
    
    score += water_temp_score[conditions["water_temp"]]
    """
    return score

def get_score_rating(score):

    if score >= 45:
        return "Excellent"
    elif 35 <= score <= 44:
        return "Good"
    elif 25 <= score <= 34:
        return "Fair"
    elif 15 <= score <= 24:
        return "Poor"
    else:
        return "Bad"

def recommend_channel_cat_location(conditions):

    location = conditions["body_of_water"]

    if location == "river":
        return f"{location.title()}: current seams, deep bends, bridges"
    elif location == "lake":
        return f"{location.title()}: creek channels, docks, wind-blown banks"
    elif location == "pond":
        return f"{location.title()}: shaded banks, deepest side, structure (if available)"
    elif location == "bayou":
        return f"{location.title()}: bends, bridges, current breaks"
    else:
        return "Failed to get location type"

def recommended_channel_cat_bait():
    bait = ["stink bait", "chicken liver", "worms", "shrimp", "cut bait"]
    return bait

def recommend_channel_cat_time():
    pass

def display_recommended_bait(bait):
    print("Recommended bait:")
    for i, item in enumerate(bait, start=1):
        print(f"{i}. {item}")

def display_prediction(score, rating, bait, location):

    print("\nChannel Catfish Prediction")
    print("-----------------------")
    print(score)
    print(f"{rating}\n")
    display_recommended_bait(bait)
    print(f"\nRecommended location:\n{location}")


def run_prediction():
    conditions = get_prediction_conditions()
    score = channel_cat_score_system(conditions)
    rating = get_score_rating(score)
    location = recommend_channel_cat_location(conditions)
    bait = recommended_channel_cat_bait()

    display_prediction(score, rating, bait, location)

def main():
    title = "fish bite predictor"
    options = ["Predict channel catfish bite", "Exit"]
    while True:

        print(title.title())
        for i, item in enumerate(options, start=1):
            print(f"{i}. {item}")

        try:
            choice = int(input("What would you like to do?: "))

            if choice == 1:
                run_prediction()
                time.sleep(5)
                print("Returning to main menu", end="")
                for _ in range(5):
                    for dots in range(4):
                        print(f"\rReturning to main menu{'.' * dots}", end="", flush=True)
                        time.sleep(0.5)
            elif choice == 2:
                print("Thank you for using the fish predictor.\n Enjoy your trip!\U0001F3A3")
                time.sleep(1.25)
                break
            else:
                print("Invalid option. Please choose 1 or 2")
        except ValueError:
            print("Invalid option. Please choose 1 or 2")

main()