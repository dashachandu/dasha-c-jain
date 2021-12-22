g = dict()
input_file=open('input.txt','r')
for each_line in input_file:
    if each_line != '\n':
        a=each_line.split(":")
        a[1]=a[1][1:]
        if a[1] != "":
            if a[1][-1] == "\n":
                a[1]=a[1][:-1]
            g[a[0]]=int(a[1])
input_file.close()

m = g["Number of employees"]
del g["Number of employees"]
s_value=sorted(g.values())
l=len(s_value)
min = s_value[-1] - s_value[0]                                              
f=0 
for i in range((l-m)+1):
    k = s_value[i+(m-1)] - s_value[i]
    if k < min:
        min=k
        f=i

output_file=open('output.txt','w')
output_file.write("goodies selected for distribution are: \n")
output_file.write("\n")
for i in range(f,f+m):
    for j in g.keys():
        if g[j]==s_value[i]:
            output_file.write(j+":  ")
            output_file.write(str(g[j]))
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("and the difference between the choosen goodie with the highest and the lowest prise is ")
output_file.write(str(min))
output_file.close()
