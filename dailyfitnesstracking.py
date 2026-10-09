def performance_summary(goal_results):
    days_met = sum(goal_results)
    total_days = len(goal_results)

    print(f"Goal achieved on {days_met} out of {total_days} days.")