import csv
# The process of extracting data from CSV files and writing new CSV files are mostly similar.
# Here present the process of counting tackling only.
own_success_tackling_att=[0 for i in range(38)]
own_failing_tackling_att=[0 for i in range(38)]
own_success_tackling_def=[0 for i in range(38)]
own_failing_tackling_def=[0 for i in range(38)]

def Read_The_Data():
    temp=0
    aord=0 #0 represented Huskies is controlling the ball
    with open("D:\TEST\\fullevents.csv",'r') as f:
        reader=csv.reader(f)
        print(type(reader))
        for row in reader:
            if(row[1]=="Huskies" and row[6]!="Duel"): # The condition is changed by the needs
                aord=0
            if(row[1]!="Huskies" and row[6]!="Duel"):
                aord=1

            if(row[1]=="Huskies" and row[6]=="Duel"):
                temp=1 #temp is a variable describing whether there are some pending matters
                aordtemp=aord
            if(row[6]!="Duel" and temp==1 and aordtemp==0):
                print("Reading "+row[0]+":")
                if(row[1]=="Huskies"):
                    own_success_tackling_def[int(row[0])-1]+=1
                else:
                    own_failing_tackling_def[int(row[0])-1]+=1
                temp=0
            elif(row[6]!="Duel" and temp==1 and aordtemp==1):
                if(row[1]=="Huskies"):
                    own_success_tackling_att[int(row[0])-1]+=1
                else:
                    own_failing_tackling_att[int(row[0])-1]+=1
                temp=0

def Write_The_Data():
    with open("D:\TEST\\tackling_attackordefend_summary.csv",'w',newline='') as f:
        writer=csv.writer(f)
        print(type(writer))
        writer.writerow(["Round","Success in the opponent half","Failure in the opponent half","Success in the own half","Failure in the own half"])
        for i in range(38):
            writer.writerow([i+1,own_success_tackling_att[i],own_failing_tackling_att[i],own_success_tackling_def[i],own_failing_tackling_def[i]])
                
def main():
     Read_The_Data()
     Write_The_Data()

main()
