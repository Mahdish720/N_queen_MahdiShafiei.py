import random

def tabe_barazesh(nemoone):
    sum=0 # tedad vazirayi ke hamdigaro tahdid mikonanad -> tabe barazesh mishe (n*(n-1))/2 - sum , n=len(nemoone)
    for i in range(len(nemoone)):
        sum=sum+nemoone.count(nemoone[i])-1
    sum=sum/2
    z=0
    for i in range(len(nemoone)):
        ban1 = []
        ban2 = []
        for j in range(1,i+1):
            ban1.append(nemoone[i]-j)
            ban2.append(nemoone[i]+j)
        ban1.reverse()
        ban2.reverse()
        ban1.append(0)
        ban2.append(0)
        for j in range(1,len(nemoone)-i):
            ban1.append(nemoone[i]-j)
            ban2.append(nemoone[i]+j)


        for k in range(len(nemoone)):
            if nemoone[k]==ban1[k] or nemoone[k]==ban2[k]:
                z=z+1
    sum=sum+z/2
    return (len(nemoone)*(len(nemoone)-1)/2 -sum)

def ehtemal(sum_barazesh_jamiat,nemoone):
    return tabe_barazesh(nemoone)/sum_barazesh_jamiat

def entekhab_halat(jamiat,sum_barazesh_jamiat):
    pick=[]
    for i in range(len(jamiat)):
        movafaghiat=False
        while not movafaghiat:
            sum=0 # baray inke biam yek nemoone ro ba yek ehtemal entekhab konam miam ye adad bain 0 ta 1 be shekl random
                  # dorost mikonam va baad mibinam age adadam az p(nemoone(1)) kamtar bood nemoone 1 ro barmidaram age nabood
                  # miam mibinam age az p(nemoone(1))+p(nemoone(2)) kamtar hast ya na va age bood nemoone 2 ro barmidaram va
                  # be hamin tartib
            r=random.random()
            for j in range(len(jamiat)):
                sum=sum+ehtemal(sum_barazesh_jamiat,jamiat[j])
                if r<sum:
                    pick.append(j)
                    break
            if i%2==0 or (i%2==1 and pick[i]!=pick[i-1]):
                movafaghiat=True
            else:
                pick.pop()

    return(pick)

def concat_2nemoone(nemoone1 , nemoone2):
    shansjahesh=0.05
    r1jahesh=random.random()
    r2jahesh=random.random()
    r=random.randint(0,len(nemoone1)-1)
    javab1=nemoone1[0:r] + nemoone2[r:len(nemoone2)]
    javab2=nemoone2[0:r] + nemoone1[r:len(nemoone1)]

    if r1jahesh<shansjahesh:
        index1=random.randint(0,len(nemoone1)-1)
        value1=random.randint(1,len(nemoone1))
        javab1[index1]=value1

    if r2jahesh < shansjahesh:
        index2 = random.randint(0, len(nemoone2) - 1)
        value2 = random.randint(1, len(nemoone2))
        javab2[index2] = value2

    javab = []
    javab.append(javab1)
    javab.append(javab2)

    return(javab)

def rasmjadval(javabha):
    for nemoone in range(len(javabha)):
        for i in range(len(javabha[nemoone])):
            for j in range(len(javabha[nemoone])):
                if javabha[nemoone][j]==i+1:
                    print('Q',end=" ")
                else:
                    print('-',end=" ")
            print("\n")
        print("---------------------------")
def main():
    n=5#tedad vazir ha dar jadval n*n (age mikhain baray test 5 bezarin chon 10*10 kheili tool mikeshid baray test kheili ziad...)
    k=20 #tedad jamiat
    h=0
    javab_haymokhtalef=5 # tedad javab hay mokhtalefi ke mikhahim
    hmarahel=[]
    jamiat=[[random.randint(1,n) for i in range(n)] for i in range(k)]
    barazesh_jamiat=[tabe_barazesh(jamiat[i]) for i in range(len(jamiat))]
    print(sum(barazesh_jamiat))
    jamiat2=[]
    javabha=[]
    flag=False


    while (len(javabha)<javab_haymokhtalef):

        pick=entekhab_halat(jamiat,sum(barazesh_jamiat))
        for i in range(0,len(jamiat),2):
            jamiat2=jamiat2 + concat_2nemoone(jamiat[pick[i]],jamiat[pick[i+1]])
        jamiat = jamiat2
        jamiat2=[]
        barazesh_jamiat=[tabe_barazesh(jamiat[i]) for i in range(len(jamiat))]

        if n*(n-1)/2 in barazesh_jamiat:
            indexha=[i for i,x in enumerate(barazesh_jamiat) if x==n*(n-1)/2]
            flag=True
        for i in range(0,len(jamiat)):
            print("nemoone : {s1} \t tabe_barazesh : {s2} \t javabhay be dast amade ta alan :{s3}".format(s1=jamiat[i],s2=tabe_barazesh(jamiat[i]),s3=javabha))


        if flag==True:
            print("index nemoone hay kamel : {s1}".format(s1=indexha))
            for i in indexha:
                if not jamiat[i] in javabha and len(javabha)<=javab_haymokhtalef:
                    javabha.append(jamiat[i])
                    hmarahel.append(h)
                    print("javab nahayi ta alan : {s1}".format(s1=javabha))
            jamiat=[[random.randint(1,n) for h in range(n)] for h in range(k)]
            barazesh_jamiat=[tabe_barazesh(jamiat[i]) for i in range(len(jamiat))]
        print("marhale {s1} \n .................................".format(s1=h))
        h=h+1
        flag=False

    print("javab nahayi : {s1} \n marhael:{s2}".format(s1=javabha , s2=hmarahel))
    print("--------------------------------------")
    rasmjadval(javabha)
if __name__ == '__main__':
    main()


