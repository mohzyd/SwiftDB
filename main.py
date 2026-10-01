import os
import json
import swift_exceptions as swift_exceptions

class Database:
    def __init__(self):
        self.db_name = None

    def load(self, database_name):
        DBname = str(database_name)

        if not database_name or len(database_name.replace(" ", "")) == 0:
            raise swift_exceptions.Missing_Database_Name()
    
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
            raise swift_exceptions.No_Loaded_Database()
        
        print(ActiveDB)
        with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as add_info:
            information = json.load(add_info)
            add_info.seek(0)
            target = information

            #dot notation
            if key.count(".") > 0:
                nested_keys = key.split(".")
                add_target = nested_keys.pop()

                for key in nested_keys:
                    print(key)
                    try:
                        target = target[key]
                    except:
                        target[key] = {}
                        target = target[key]

                target[add_target] = data
                add_info.seek(0)
                add_info.truncate()
                json.dump(information,add_info, indent=2)
            else:
                dblength = len(add_info.read())
                if dblength == 0:
                    add_info.seek(0)
                    template = {f"{key}": data}
                    json.dump(template, add_info, indent=2)
                    return
                else:
                    add_info.seek(0)
                    print(information)
                    information[key] = data
                    add_info.seek(0)
                    add_info.truncate()
                    json.dump(information,add_info, indent=2)
                return
        

    def remove(self, key=None, data=None):
        ActiveDB = self.db_name
        if ActiveDB == None:
            raise swift_exceptions.No_Loaded_Database()

        if key == None:
            raise swift_exceptions.Invalid_Key()
        
        with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as remove_info:
            dblength = len(remove_info.read())
            if dblength == 0:
                raise swift_exceptions.Empty_Database()
            else:
                remove_info.seek(0)
                loaded_info = json.load(remove_info)
                try:
                    remove_info.seek(0)
                    #Deleting the data from first layer of nested json
                    if data != None:
                        loaded_info[key].pop(data)

                    #dot_based_multi_notiation_method
                    target = loaded_info
                    if key.count(".") > 0:
                        nested_keys = key.split(".")
                        delete_target = nested_keys.pop()

                        for key in nested_keys:
                            target = target[key]
                        target.pop(delete_target)

                   # loaded_info.pop(key)
                    remove_info.seek(0)
                    remove_info.truncate()
                    json.dump(loaded_info, remove_info, indent=2)
                    print("[SwiftDB] | Removing key is complete")
                except:
                    raise swift_exceptions.Invalid_Key()

    def get(self, key):
        database = self.db_name
        if not database == None:
            ActiveDB = database
            if not os.path.isfile(f"./RegisteredDBs/{ActiveDB}.json"):
                raise swift_exceptions.No_Loaded_Database()
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
                        raise swift_exceptions.Invalid_Key()

    def update(self, key=None, data=None):
        database = self.db_name
        if not database == None:
            ActiveDB = database
            if not os.path.isfile(f"./RegisteredDBs/{ActiveDB}.json"):
                raise swift_exceptions.No_Database
            else:
                if data == None or key == None:
                    raise swift_exceptions.Missing_Args()
                
                with open(f"./RegisteredDBs/{ActiveDB}.json", "r+") as search_function:
                    loaded_info = json.load(search_function)
                    search_function.seek(0)

                    #dot syntax method + does the job
                    target = loaded_info
                    if key.count(".") > 0:
                        nested_keys = key.split(".")
                        set_target = nested_keys.pop()

                        for key in nested_keys:
                            target = target[key]
                        target[set_target] =  data
                        print("Set operation sucessful!")
                    else:
                        if key in loaded_info:
                            loaded_info[key] = data
                        else:
                            raise swift_exceptions.Invalid_Key()
                        return

                    search_function.seek(0)
                    search_function.truncate()
                    json.dump(loaded_info, search_function, indent=2)
