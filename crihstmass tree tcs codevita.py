
st="*"
sp=" "

j=[]

n=int(input())
for i in range((n)):
    k=int(input())
    sa=0
    x=0
    if(k<=1):
        print("You cannot generate christmas tree")
    elif(k>20):
        print("Tree is no more")
    elif(k==2):
        for i in range(2+1,0,-1):
            for j in range(i-1,0,-1):
                print(" ",end="")
            print(st)
            st=st+2*"*"
         
        for i in range((1+k*2)//2+1-1):
            print(" ",end="")
        print("*")
        for i in range((1+k*2)//2+1-1):
            print(" ",end="")
        print("*")
    elif(k>2):
        st="*"
        for i in range(k+1,0,-1):
            for j in range(i-1,0,-1):
                 print(" ",end="")
            print(st)
            st=st+2*"*"
        st="*"+2*"*"
        for i in range(k-1,0,-1):
            for j in range(i+1-1,0,-1):
                     print(sp,end="")
            print(st)
            st=st+2*"*"
        for i in range(((k+1)-3),1,-1):
            sa=sa+1
            st="*"+2*"*"
            x=x+1
           # print(k,x)
            for i in range((k-1)-x,0,-1):
                    for j in range(i+1+sa-1,0,-1):
                        print(sp,end="")
                    print(st)
                    st=st+2*"*"
            
        for i in range((1+k*2)//2+1-1):
            print(" ",end="")
        print("*")
        for i in range((1+k*2)//2+1-1):
            print(" ",end="")
        print("*")
         

                    
   

         
