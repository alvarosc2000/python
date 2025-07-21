def life_in_weeks(age):
    year_remaining = 90-age
    month_weeks = 4
    year_weeks = 12*month_weeks
    weeks_remainigs = (year_remaining * year_weeks)
    print(weeks_remainigs)
    print(f"You have {weeks_remainigs} weeks left")


life_in_weeks(56)