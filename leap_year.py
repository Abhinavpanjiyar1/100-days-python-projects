def is_leap(year):
    if year%2==0:
        if year%100==0:
            if year%400==0:
                print("leap year")
            else:
                print("not leap year")
        else:
            print("leap year")
    else:
        print("not leap year")
                            
def day_in_month(year,month):
    month_days=[31,28,30,31,30,31,30,31,30,30,31,31]
    if month ==2 and is_leap(year):
        return 29
    else:
        return month_days==28
    
year= int(input())
month=int(input())
days= day_in_month(year,month)
print(days)
