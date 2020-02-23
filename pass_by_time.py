import csv
import math

time_sta=["0-5","5-10","10-15","15-20","20-25","25-30","30-35","35-40","40-45","45-50","50-55","55-60","60-65","65-70","70-75","75-80","80-85","85-90"]
p_time_avr=[0 for i in range(18)]
p_time_full = [[0 for i in range(38)] for i in range(18)]

def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

def Read_The_Data():
    with open("D:\TEST\\passingevents.csv",'r') as f:
        reader=csv.reader(f)
        print(type(reader))
        for row in reader:
          print(10+int(float(row[5])/300))
          print(int(float(row[0])))
          if(("_M" in row[2] or "_F" in row[2]) and row[1]!="Huskies" and row[4]=="1H" and float(row[5])<2700):
                p_time_full[int(float(row[5])/300)][int(float(row[0]))-1]+=1
          elif(("_M" in row[2] or "_F" in row[2]) and row[1]!="Huskies" and row[4]=="2H" and float(row[5])<2700):
                p_time_full[9+int(float(row[5])/300)][int(float(row[0]))-1]+=1

def Analyze_The_Pass():
    for i in range(18):
        for j in range(38):
            p_time_avr[i]+=p_time_full[i][j]
        p_time_avr[i]=int(p_time_avr[i])/38

def Write_The_Data():
    with open("D:\TEST\\p_time_mid_oppo.csv",'w',newline='') as f:
        writer=csv.writer(f)
        print(type(writer))
        print(type(p_time_avr))
        print(type(p_time_avr[0]))
        writer.writerows(transpose([time_sta,p_time_avr]))

def main():
    Read_The_Data()
    Analyze_The_Pass()
    Write_The_Data()

main()