def bmi(weight, height):
    """Calculate BMI."""
    h = height / 100
    return round(weight / (h * h), 2)

def calorie_target(weight, height, age, activity):
    # ---------- SAFETY DEFAULTS ----------
    if age is None:
        age = 25  # sensible default

    if activity is None:
        activity = "Moderate"
    # ------------------------------------

    # Mifflin-St Jeor Equation (Male baseline)
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    activity_factor = {
        "Low": 1.2,
        "Moderate": 1.55,
        "High": 1.75
    }.get(activity, 1.55)

    return int(bmr * activity_factor)



