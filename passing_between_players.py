import csv
import matplotlib.pyplot as plt

list_original_x=[]
list_original_y=[]
list_des_x=[]
list_des_y=[]

def main():
    Read_The_Data()
    Draw_The_Line()
    plt.show()

def Read_The_Data():
    with open("D:\TEST\passingevents.csv",'r') as f:
        reader=csv.reader(f)
        print(type(reader))
        for row in reader:
            if(row[1]=="Huskies" and row[0]=='1'):
                list_original_x.append(row[7])
                list_original_y.append(row[8])
                list_des_x.append(row[9])
                list_des_y.append(row[10])

def Draw_The_Line():
    for i in range(len(list_original_x)):
        plt.plot([list_original_x[i],list_des_x[i]],[list_original_y[i],list_des_y[i]], color='r',lw=1)
        plt.scatter([list_original_x[i],list_des_x[i]],[list_original_y[i],list_des_y[i]], color='b', marker=1)
        print('draw '+str(i))        

main()

