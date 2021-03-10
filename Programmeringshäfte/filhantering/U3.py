import matplotlib.pyplot as plt

Ma2C = []
Ma2A = []
labels = 'A','B','C','D','E','F'

def sucki1A():
    with open('NPvt19Ma2A.txt', 'r') as f1:
        for rad1 in f1:
            rad1 = rad1.strip(' \n')
            rad1 = rad1.replace('%','')
            rad1 = rad1.split(' ')
            Ma2A.append(float(rad1[1]))
        figur1, axis1 = plt.subplots()
        axis1.pie(Ma2A, labels = labels, autopct = '%1.1f%%',startangle = 90)
        axis1.axis('equal')
        axis1.set_title('Matte 2A NP resultater')
        plt.show()
    

def sucki1C():
    with open('NPvt19Ma2C.txt', 'r') as f2:
        for rad2 in f2:
            rad2 = rad2.strip(' \n')
            rad2 = rad2.replace('%','')
            rad2 = rad2.split(' ')
            Ma2C.append(float(rad2[1]))
        figur1, axis1 = plt.subplots()
        axis1.pie(Ma2C, labels = labels, autopct = '%1.1f%%', startangle = 90)
        axis1.axis('equal')
        axis1.set_title('Matte 2C NP resultater')
        plt.show()

sucki1A()
sucki1C()