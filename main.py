import mysql.connector

def polling_unit(self):

    self.execute("SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid=8;")

    for x in self:
        print(x)


def polling_unit_total(self, lga):

    self.execute("SELECT party_score FROM announced_lga_results WHERE lga_name=" + str(lga))

    total = 0
    for x in self:
        for item in x:
            total += item
    print("Total results of polling units in " + str(lga), "= " + str(total) )
       


def main():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mysql"
)

    mycursor = mydb.cursor()

    # polling_unit(mycursor)    
    polling_unit_total(mycursor, 19)   

if __name__ == '__main__':
    main()    