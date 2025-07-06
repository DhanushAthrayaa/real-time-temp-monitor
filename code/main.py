from gpio import *
from time import *

def pad(n):
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)

def main():
    pinMode(0, INPUT)      # Analog Temp Sensor
    pinMode(1, OUT)        # AC
    pinMode(2, OUT)        # Heater
    pinMode(3, OUT)        # LCD

    print("Room Temperature Monitoring with Clock")

    hours = 0
    minutes = 0
    seconds = 0

    while True:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0

        time_str = pad(hours) + ":" + pad(minutes) + ":" + pad(seconds)

        temp = analogRead(0)
        print("[" + time_str + "] Temperature: " + str(temp))

        if temp >= 506:
            digitalWrite(1, HIGH)
            digitalWrite(2, LOW)
            customWrite(3, "AC-ON " + time_str)
            print("AC ON")

        elif temp <= 504:
            digitalWrite(1, LOW)
            digitalWrite(2, HIGH)
            customWrite(3, "Heater-ON " + time_str)
            print("Heater ON")

        else:
            digitalWrite(1, LOW)
            digitalWrite(2, LOW)
            customWrite(3, "Normal " + time_str)
            print("Normal Mode")

        delay(1000)

if __name__ == "__main__":
    main()
