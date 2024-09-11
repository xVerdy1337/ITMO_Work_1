def convert_seconds(seconds: int) -> str:
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

seconds = int(input('Введите секунды\n'))
print(convert_seconds(seconds))
