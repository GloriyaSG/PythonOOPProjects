class Time:
    max_hours, max_minutes, max_seconds = 23, 59, 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds) -> None:
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def update_valid_time(self) -> None:
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1

                if self.hours > Time.max_hours:
                    self.hours = 0

    def next_second(self) -> str:
        self.seconds += 1

        self.update_valid_time()

        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())