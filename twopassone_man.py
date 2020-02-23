import csv

passing = [[] for i in range(3)]#第一个是传球人，第二个是接球人，第三个是传球数
passing[0].append("Source")
passing[1].append("Target")
passing[2].append("Weight")

def suc(a,b,atemp,btemp):
    if(a == btemp and b == atemp):
        return True
    return False

def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

def main():
    Read_The_Data()
    Output_The_Result()
    Write_The_Data()

def In_List(data):
    if(len(passing[0])==1):
        return False
    for i in range(len(passing[0])):
        if (passing[0][i]==data[2] and passing[1][i]==data[3]) or(passing[0][i]==data[3] and passing[1][i]==data[2]):
            return i 
    return False

def Read_The_Data():
    with open("D:\TEST\\passingevents.csv",'r') as f:
        reader=csv.reader(f)
        temp_ori=" "
        temp_des=" "
        print(type(reader))
        for row in reader:
            if(row[1]=="Huskies" and suc(row[2],row[3],temp_ori,temp_des)):
                nil=In_List(row)
                if(not nil):
                    passing[0].append(row[2])
                    passing[1].append(row[3])
                    passing[2].append(int(1))
                else:
                    passing[2][nil]+=1
            temp_ori=row[2]
            temp_des=row[3]
                    

def Analyze_The_Pass():
    pass
        
def Output_The_Result():
        tplt = "{0:^10}\t{1:^10}\t{2:^10}"
        print(tplt.format("Source","Target","Weight"))
        for i in range(len(passing[0])):
            print(tplt.format(passing[0][i],passing[1][i],passing[2][i]))

def Write_The_Data():
    with open("D:\TEST\\wallpass_man.csv",'w',newline='') as f:
        writer=csv.writer(f)
        print(type(writer))
        writer.writerows(transpose(passing))
main()


