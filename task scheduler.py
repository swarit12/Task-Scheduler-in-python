import datetime
from plyer import notification
from playsound import playsound

print("HEY THIS IS A TASK SCHEDULER!! SCHEDULE YOUR TASKS HERE AND ALLOW ME TO REMIND YOU ")
print("******DONT FORGET TO PUT TIME!!********")

title1= input("Please write the task for your reminder: ")
print("Please tell the time:\n")
hour= int(input("Hour: "))
minute= int(input("Minute: "))
amPm= str(input("am or pm: "))
print("We'll remind you when the time hits the clock!!")

if (amPm.lower()== 'pm'):
    hour= hour+12

while True:
    if hour==datetime.datetime.now().hour and minute==datetime.datetime.now().minute:

        if __name__ == '__main__':
            notification.notify(

                title="reminder from task scheduler",
                message=title1,
                timeout=20,
                app_name="task scheduler"
            )
            playsound('C:\\Users\Shashank-dt\Downloads\piece-of-cake-611.mp3')
        break
print("exited")