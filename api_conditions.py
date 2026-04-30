from predictor import (
    channel_cat_score_system,
    convert_score_to_percent,
    get_score_rating,
    recommend_channel_cat_location,
    recommended_channel_cat_bait,
    display_prediction
)


def get_auto_conditions():
    conditions = {
        "body_of_water": "lake",
        "water_level": "stable",
        "current": "unknown",
        "cloud": "yes",
        "rain": "no",
        "storm": "no"
    }

    return conditions

def run_auto_prediction():
    conditions = get_auto_conditions()

    score = channel_cat_score_system(conditions)
    score_total_rounded = convert_score_to_percent(score)
    rating = get_score_rating(score_total_rounded)
    location = recommend_channel_cat_location(conditions)
    bait = recommended_channel_cat_bait()

    display_prediction(score_total_rounded, rating, bait, location)

