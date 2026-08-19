total_seconds = int(input("Введіть кількість секунд: "))
seconds_in_day = 24 * 60 * 60
seconds_in_hors = 60 * 60
seconds_in_minute = 60
days, remainder = divmod(total_seconds, seconds_in_day)
hours, remainder = divmod(remainder, seconds_in_hors)
minutes, seconds = divmod(remainder, seconds_in_minute)
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"
time_string = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(f"{days} {day_word}, {time_string}")