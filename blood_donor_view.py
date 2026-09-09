import mysql.connector
import datetime
class BloodDonorManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nikheth@20",
            database="blood_db"
        )
        print("Connected successfully")
    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = ("insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)")
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor Added Successfully")
        except Exception as e:
            print(e)


    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for rec in records:
                print(rec)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=[id]
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record == None:
                print("Donor Not found")
            else:
                print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query ="select * from donor where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record != None:
                query = "delete from donor where id =%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor deleted successfully")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query ="select * from donor where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return  record
        except Exception as e:
            return None

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record != None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s ,"
                placeholder=placeholder.rstrip(",")
                    #SET name="%s",bloodgroup="%s" .........
                query=f"update donor set {placeholder} where id=%s"
                #
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor details updated Successfully")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)

donor_instance=BloodDonorManager()
#donor_instance.post(name="Raman",blood_group="B+",phone="9174490522",city="Kakkand",last_donation="2025-10=25")
#donor_instance.post(name="Mathew",blood_group="A+",phone="8074470518",city="Kochi",last_donation="2026-03-15")
#donor_instance.get()
#donor_instance.retrieve(5)
# donor_instance.delete(8)
donor_instance.put(8,name="Rahul")
donor_instance.get()