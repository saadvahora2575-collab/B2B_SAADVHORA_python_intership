import pywhatkit as py

phoneNo = input("Enter phone no. (+91xxxxxxxxxx): ")
msg = input("Enter message: ")
time_str = input("Enter time (24-hour format, e.g. 18:00): ")

try:
    time = list(map(int, time_str.split(":")))
    time_hour = time[0]
    time_min = time[1]

    if time_hour < 24 and time_min < 60:
        py.sendwhatmsg(phoneNo, msg, time_hour, time_min, 30)

        print("Successfully sent")
        print("Message sent to:", phoneNo)
        print("At:", time_str)
        print("Message:", msg)
    else:
        print("Invalid time")

except Exception as e:
    print("Error:", e)