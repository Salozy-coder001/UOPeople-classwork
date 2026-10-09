def calculate_weekly_average(data):
    return sum(data) / len(data)

def check_goal(actual, goal):
    return actual >= goal

def performance_summary(steps, calories, minutes):
    avg_steps = calculate_weekly_average(steps)
    avg_calories = calculate_weekly_average(calories)
    avg_minutes = calculate_weekly_average(minutes)

    return {
        "Average Steps": avg_steps,
        "Average Calories": avg_calories,
        "Average Minutes": avg_minutes
    }

# Example usage
weekly_steps = [8000, 9000, 10000, 7500, 11000, 12000, 9500]
summary = performance_summary(weekly_steps,
                             [300, 350, 400, 280, 450, 500, 375],
                             [30, 40, 45, 25, 50, 60, 35])

print(summary)
fitness_data = {
    "steps": {"actual": 10500, "goal": 10000},
    "calories": {"actual": 450, "goal": 400},
    "minutes": {"actual": 45, "goal": 30}
}

fitness_data = {
    "steps": {"actual": 10500, "goal": 10000},
    "calories": {"actual": 450, "goal": 400},
    "minutes": {"actual": 45, "goal": 30}
}
def generate_report(data):
    for metric, values in data.items():
        status = "Met" if values["actual"] >= values["goal"] else "Not Met"
        print(f"{metric}: {values['actual']} / {values['goal']} - {status}")

generate_report(fitness_data)  # (variable) fitness_data: dict[str, dict[str, int]]