import csv
def update_users(first_name, last_name, new_fname, new_lname):
    with open("users.csv", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)
    with open("users.csv", "w",newline='', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == first_name and user[1] == last_name:
                csv_writer.writerow([new_fname, new_lname])
            else: 
                csv_writer.writerow(user)
            
        

#update_users("Sadık", "Turan", "Ali", "Kaya")
                

def delete_users(first_name, last_name):
    with open("users.csv", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)
    with open("users.csv", "w",newline='', encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        for user in users:
            if user[0] == first_name and user[1] == last_name:
                pass
            else: 
                csv_writer.writerow(user)

delete_users("Emel","Turan")