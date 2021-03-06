import csv

winnings=[1,35,30,31,36,17,18,14,6,27,15,11,25]

passing = [[] for i in range(3)]#第一个是传球人，第二个是接球人，第三个是传球数
passing[0].append("Source")
passing[1].append("Target")
passing[2].append("Weight")

def main():
   # print(passing[0][0])
    Read_The_Data()
  # Analyze_The_Pass()
    Output_The_Result()
    Write_The_Data()

def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

def In_List(data):
    if(len(passing[0])==1):
        return False
    for i in range(len(passing[0])):
        if (passing[0][i]==data[2] and passing[1][i]==data[3]):
            return i #若存在已有的列项，则不必新写
    return False

def Read_The_Data():
    with open("D:\TEST\passingevents.csv",'r') as f:
        reader=csv.reader(f)
        print(type(reader))
        for row in reader:
            if(row[1]=="Huskies" and int(row[0]) in winnings):
                nil=In_List(row)
                if(not nil):
                    passing[0].append(row[2])
                    passing[1].append(row[3])
                    passing[2].append(int(1))
                else:
                    passing[2][nil]+=1
                    

def Analyze_The_Pass():
    pass
        
def Output_The_Result():
        tplt = "{0:^10}\t{1:^10}\t{2:^10}"
        print(tplt.format("传球者","接球者","传球次数"))
        for i in range(len(passing[0])):
            print(tplt.format(passing[0][i],passing[1][i],passing[2][i]))

def Write_The_Data():
    with open("D:\TEST\\winningpassingsummary.csv",'w',newline='') as f:
        writer=csv.writer(f)
        print(type(writer))
        writer.writerows(transpose(passing))
main()

