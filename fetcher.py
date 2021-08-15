import mysql.connector

con = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1', database='computer',
                              auth_plugin='mysql_native_password')
cur = con.cursor()

print(con)

def getCPU(platform,cpuBudget):

    cur = con.cursor()

    query = " select * from computer.cpu where manufacturer = '{}' and price < {} order by price ".format(platform,cpuBudget)

    cur.execute(query)

    for r in cur:
        cpu = r

    return cpu

def getGPU(gpuBudget):

    cur = con.cursor()

    gpu ='NA'
    if gpuBudget != 0:

        query = " select * from computer.gpu where price < {} order by price ".format(gpuBudget)

        cur.execute(query)

        for r in cur:
            gpu = r
    return gpu


def getMobo(socket,moboBudget):

    cur = con.cursor()

    query = " select * from computer.motherboard where socket = '{}' and price < {} order by price ".format(socket , moboBudget)

    cur.execute(query)

    for r in cur:
        mobo = r

    return mobo

def getCase(formfactor,caseBudget):

    cur = con.cursor()

    query = " select * from computer.case where formfactor = '{}' and price < {} order by price ".format(formfactor , caseBudget)

    cur.execute(query)

    for r in cur:
        case = r

    return case

def getHDD(hddBudget):

    cur = con.cursor()

    query = " select * from computer.hdd where price < {} order by price ".format(hddBudget)

    cur.execute(query)

    for r in cur:
        hdd = r

    return hdd


def getSSD(ssdBudget):

    cur = con.cursor()

    query = " select * from computer.ssd where price < {} order by price ".format(ssdBudget)

    cur.execute(query)

    for r in cur:
        ssd = r

    return ssd

def getRAM(ramBudget):

    cur = con.cursor()

    query = " select * from computer.ram where price < {} order by price ".format(ramBudget)

    cur.execute(query)

    for r in cur:
        ram = r

    return ram

def getPSU(psuBudget):

    cur = con.cursor()

    query = " select * from computer.psu where price < {} order by price ".format(psuBudget)

    cur.execute(query)

    for r in cur:
        psu = r
    return psu



