
inputfile=open("input2.txt","r")
outputfile=open("output2.txt","w")
size1=inputfile.readline()
arr1=inputfile.readline().strip().split()
size2=inputfile.readline()
arr2=inputfile.readline().strip().split()

min=min(int(size1),int(size2))
print(min)
newarr=[]
i,j=0,0
while i<=min-1 and j<=min-1:
  if int(arr1[i])==int(arr2[j]):
    newarr.append(arr1[i])
    newarr.append(arr2[j])
    i+=1
    j+=1
  elif int(arr1[i])>int(arr2[j]):
    newarr.append(arr2[j])
    j+=1
  elif int(arr1[i])<int(arr2[j]):
    newarr.append(arr1[i])
    i+=1
if int(size1)>int(size2):
  newarr+=(arr1[i:])
elif int(size1)<int(size2):
  newarr+=(arr2[j:])
elif int(size1)==int(size2):
  if i>j:
    newarr+=(arr2[j:])
  else:
    newarr+=(arr1[i:])

outputfile.write(f"{newarr}")