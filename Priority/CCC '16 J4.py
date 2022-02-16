hour, minute = [int(x) for x in input().split(':')]

tempMinutes = 0
remMinutes = 120

if hour >= 7 and hour < 10:
    remMinutes -= int((60-minute)/2)
    tempMinutes += (60-minute)
    remMinutes -= int(60*(10-(hour+1))/2)
    tempMinutes += (10-(hour+1))*60
    if len(str((hour+int((tempMinutes+remMinutes)/60))%24)) == 1:
        if minute+(tempMinutes+remMinutes)%60 == 0:
            print('0'+str((hour+int((tempMinutes+remMinutes)/60))%24)+':00')
        else:
            print('0'+str((hour+int((tempMinutes+remMinutes)/60))%24)+':'+str(minute+(tempMinutes+remMinutes)%60))
    else:
        if minute+(tempMinutes+remMinutes)%60 == 0:
            print(str((hour+int((tempMinutes+remMinutes)/60))%24)+':00')
        else:
            print(str((hour+int((tempMinutes+remMinutes)/60))%24)+':'+str(minute+(tempMinutes+remMinutes)%60))
elif hour >= 15 and hour < 20:
    remMinutes -= int((60-minute)/2)
    tempMinutes += (60-minute)
    remMinutes -= int(60*(20-(hour+1))/2)
    tempMinutes += (20-(hour+1))*60
    if len(str((hour+int((tempMinutes+remMinutes)/60))%24)) == 1:
        if minute+(tempMinutes+remMinutes)%60 == 0:
            print('0'+str((hour+int((tempMinutes+remMinutes)/60))%24)+':00')
        else:
            print('0'+str((hour+int((tempMinutes+remMinutes)/60))%24)+':'+str(minute+(tempMinutes+remMinutes)%60))
    else:
        if minute+(tempMinutes+remMinutes)%60 == 0:
            print(str((hour+int((tempMinutes+remMinutes)/60))%24)+':00')
        else:
            print(str((hour+int((tempMinutes+remMinutes)/60))%24)+':'+str(minute+(tempMinutes+remMinutes)%60))
else:
    if len(str((hour+2)%24)) == 1:
        if minute == 0:
            print('0'+str((hour+2)%24)+':00')
        else:
            print('0'+str((hour+2)%24)+':'+str(minute))
    else:
        if minute == 0:
            print(str((hour+2)%24)+':00')
        else:
            print(str((hour+2)%24)+':'+str(minute))