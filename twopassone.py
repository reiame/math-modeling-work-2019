import csv
import os

tpo=[0 for i in range(38)]

def suc(a,b,atemp,btemp):
    if(a == btemp and b == atemp):
        return True
    return False

def Read_The_Data():
    with open("D:\TEST\passingevents.csv",'r') as f:
        reader=csv.reader(f)
        print(type(reader))
        temp_ori=" "
        temp_des=" "
        for row in reader:
            print("Reading Data of Round "+ str(row[0]))
            if(row[1]=="Huskies" and suc(row[2],row[3],temp_ori,temp_des)):
                tpo[int(row[0])-1]+=1
            temp_ori=row[2]
            temp_des=row[3]

def Write_The_Data():
    with open("D:\TEST\\twopassonesummary.csv",'w',newline='') as f:
        writer=csv.writer(f)
        print(type(writer))
        writer.writerow(["Round","二过一次数"])
        for i in range(38):
            writer.writerow([i+1,tpo[i]])

def main():
    Read_The_Data()
    Write_The_Data()

main()