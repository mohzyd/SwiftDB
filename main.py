import os
import json

class database:
    def __init__(self):
        self.db_name = None

    def load(self, database_name):
        DBname = str(database_name)


        if not os.path.isdir("./RegisteredDBs"):
            os.makedirs("./RegisteredDBs")
        
        if not os.path.isfile(f'./RegisteredDBs/{DBname}.json'):
            print(f"[SwiftDB] | There is no registered database under the name {DBname}. Would you like to create this database? (Y/N):")
            creationanswer = input("[User] | Your answer is:").lower()
            agreement_ques = ["yes", "y", "sure", "ok", "okay"]
            if creationanswer in agreement_ques:
                with open(f"./RegisteredDBs/{DBname}.json", "w") as file:
                    print("[SwiftDB] | Database has been created")
                    file.write(json.dumps({}))
                    file.close()
                    pass
            else:
                print("[SwiftDB] | Database not created.")
                return

        
        if not database_name:
            print("Please specify a name for the Database. Usage: Database.load(\"Name goes here!\")")
            raise TypeError("Please specify a name for the Database. Usage: Database.load(\"Name goes here!\")")
        
        print(f"./RegisteredDBs/{DBname}.json")
        isRegisteredAlready = os.path.isfile(f"./RegisteredDBs/{DBname}.json")
        print(isRegisteredAlready)

        if isRegisteredAlready:
            ActiveDB = DBname
            self.db_name = ActiveDB
            print(f"[SwiftDB] | Successfully switched active database to: {ActiveDB}")
            return
        elif not isRegisteredAlready:
            print("[SwiftDB] | Cannot load database because its not registered.")
            return
        pass
    
    def add(self, key, data):
        ActiveDB = self.db_name
        if ActiveDB == None:
            print("please load a database using the database.load() command.")
            return
        print(ActiveDB)
        with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as add_info:
            dblength = len(add_info.read())
            if dblength == 0:
                add_info.seek(0)
                template = {f"{key}": data}
                json.dump(template, add_info, indent=2)
                return
            else:
                add_info.seek(0)
                information = json.load(add_info)
                print(information)
                information[key] = data
                add_info.seek(0)
                add_info.truncate()
                json.dump(information,add_info, indent=2)
            return
        

    def remove(self, key):
        ActiveDB = self.db_name
        if ActiveDB == None:
            print("please load a database using the database.load() command.")
            return
        
        with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as remove_info:
            dblength = len(remove_info.read())
            if dblength == 0:
                print("[SwiftDB] | This database is empty. There is no data to delete.")
                return
            else:
                remove_info.seek(0)
                loaded_info = json.load(remove_info)
                try:
                    remove_info.seek(0)
                    loaded_info.pop(key)
                    remove_info.seek(0)
                    remove_info.truncate()
                    json.dump(loaded_info, remove_info, indent=2)
                    print("Removing key is complete")
                except:
                    print("there is no such key with this name")
                    return

    def search(self, key):
        database = self.db_name
        if not database == None:
            ActiveDB = database
            if not os.path.isfile(f"./RegisteredDBs/{ActiveDB}.json"):
                print("There is no database with such name. You can create one using database.load() command.")
                return
            else:
                with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as search_function:
                    loaded_info = json.load(search_function)
                    search_function.seek(0)
                    if key in loaded_info:
                        search_result = loaded_info.get(key)
                        return search_result
                    else:
                        print("This key has not been found. Make sure to check Capitalization as it may help.")
                        return
        else:
            ActiveDB = self.db_name
            if not os.path.isfile(f"./RegisteredDBs/{ActiveDB}.json"):
                print("There is no database with such name. You can create one using database.load() command.")
                return
            else:
                with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as search_function:  
                    loaded_info = json.load(search_function)
                    search_function.seek(0)
                    if key in loaded_info:
                        search_result = loaded_info.get(key)
                        return search_result
                    else:
                        print("This key has not been found. Make sure to check Capitalization as it may help.")
                        return

    def show(self):
        print(self.active_name)
