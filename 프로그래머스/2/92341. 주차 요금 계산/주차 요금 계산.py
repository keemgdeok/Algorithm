from datetime import datetime 

def solution(fees, records):
    ans = []
    parking={}
    for rec in records:
        time, num, act = rec.split()
        if num not in parking:
            parking.setdefault(num, [time])
        else:
            parking[num].append(time)
            
    for n in sorted(parking):
        parktime = calcParkingtime(parking[n])
        fee = calcFee(fees, parktime)
        ans.append(fee)
 
    return ans

def calcParkingtime(times):
    parktime = 0
    timeformat = '%H:%M'
    if len(times) % 2 != 0:
        times.append("23:59")
    if len(times) >= 2:
        for i in range(0, len(times), 2):
            intime = datetime.strptime(times[i],timeformat)
            outtime = datetime.strptime(times[i+1],timeformat)
            parktime += ((outtime - intime).total_seconds())/60
    return int(parktime)

def calcFee(fees, parktime):
    basetime, basefee, unittime, unitfee = fees
    if basetime >= parktime:
        return basefee
    else:
        extratime = parktime - basetime
        extraunit = -(-extratime // unittime)
        return basefee + (extraunit * unitfee)
    
    
    
    
    
    
    
    