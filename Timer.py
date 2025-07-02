import time as t

Seconds=float(input("Enter Seconds: "))
Minutes=float(input("Enter Minutes: "))
Hours=float(input("Enter Hours: "))

Total_seconds= int(Seconds+(Minutes*60)+(Hours*3600))

for i in range(Total_seconds,0,-1):
    second= i%60
    minute= int(i/60)%60
    hour=int(i/3600)
    print(f"{hour:02}:{minute:02}:{second:02}")
    t.sleep(1)

print("Time's Up")

 
