Matrix=[]
x=[]
def Enter():
    global Matrix
    global x
    try:
        n=input("Size of matrix: ")
    except NameError:
        print("Invalid data")
        return
    except EOFError:
        print("Empty data")
        return  
    if (not(type(n) is int)):
        print("Number must be Integer")
        return
    if (n<1):
        print("Count must be greater than zero")
        return
    i=0
    j=0
    x=[]
    while (i<n):
        lst=[]
        while (j<=n):
            try:
                lst.append(input("Element["+str(i)+","+str(j)+"]: "))
                j=j+1
            except NameError:
                print("Invalid data")
                Matrix=[]
                return  
            except EOFError:
                print("Empty data")
                Matrix=[]
                return  
        Matrix.append(lst)
        x.append(0)
        i=i+1
        j=0
def Print():
    global Matrix
    i=0
    n=len(Matrix)
    while (i<n):
        print Matrix.__getitem__(i)
        i=i+1
        
def Solve():
    global Matrix
    global x
    if (Matrix==[]):
        print "Empty matrix"
        return
    print ("Matrix:")
    Print()
    n=len(Matrix)
    k=0
    while(k<n-1):
        p=k
        m=k+1
        while (m<n):
            if (abs(Matrix[p][k])<abs(Matrix[m][k])):
                p=m
            m=m+1
        j=k
        while (j<n):
            r=Matrix[k][j]
            Matrix[k][j]=Matrix[p][j]
            Matrix[p][j]=r
            j=j+1
        r=Matrix[k][n]
        Matrix[k][n]=Matrix[p][n]
        Matrix[p][n]=r
        m=k+1
        while(m<n):
            c=float(Matrix[m][k])/Matrix[k][k]
            Matrix[m][n]=Matrix[m][n]-c*Matrix[k][n]
            i=k
            while(i<n):
                Matrix[m][i]=Matrix[m][i]-c*Matrix[k][i]
                i=i+1
            m=m+1
        k=k+1
    try:
        x[n-1]=round(float(Matrix[n-1][n])/Matrix[n-1][n-1],4)
    except ZeroDivisionError:
        print "Float division by zero"
        return
    k=n-2
    while (k>=0):
        s=0
        i=k+1
        while(i<n):
            s=s+Matrix[k][i]*x[i]
            i=i+1
        x[k]=round((Matrix[k][n]-s)/Matrix[k][k],4)
        k=k-1
    print "Result: ",x
            
print ("Program for solving SLAE Gauss method")
flag=True
while (flag):
    print("Select the menu item:")
    print("0. Help")
    print("1. Enter the matrix")
    print("2. Print the matrix")
    print("3. Solve")
    print("4. Exit")
    try:
        option=input("You choose ")
    except NameError:
        print("Invalid data")
        continue
    except EOFError:
        print("Empty data")
        continue
    if (not type(option)):
        print("Number must be Integer")
        continue
    if ((option<0)or(option>4)):
        print("Wrong data")
        continue
    if (option==0):
        print("Specify the size of the matrix. Enter a cell array n x n+1, where the column n+1 is column of constant terms.")
    if (option==1):
        Matrix=[]
        b=[]
        Enter()
    if (option==2):
        Print()
    if (option==3):
        Solve()
    if (option==4):
        exit()
    