from tinydb import TinyDB, Query
# Creating an instance VVV
db = TinyDB('./db.json')

# db.insert({'Subject': 'Math', 'Color': 'Red'})
# user = Query()
# onedata = db.search(user.Subject == 'Math')
# alldata = db.all()
# add =  db.insert({'Subject': 'Math', 'Color': 'Red'})
# create(insert function)
# read(calling db.all/db.search)

#OPT delete = db.remove(user.Subject == 'Math')
#OPT update = db.update({'Subject': 'ELA}, user.Subject == 'ERWC')
#OPT update()
#OPT delete(db.remove)
todo = Query()

def create():
    print('What task would you like to create?:')
    createinput = input()
    print('Add a description to your task:')
    descinput = input()
    db.insert({'Name': str(createinput), 'Desc': str(descinput)})

def read():
    print('Would you like to see all your tasks, or just one?(all, one):')
    allorone = input()
    if allorone == 'all':
        alltasks = db.all()
        print(alltasks)
    elif allorone == 'one':
        print('Type in the name of your task:')
        print('(NOTE - this is case sensitive!!!!)')
        taskwanted = input()
        taskfind = db.search(todo.Name == str(taskwanted))
        print(taskfind)

def update():
    print('Which task would you like to update?:')
    print('(NOTE - this is case sensitive!!!!)')
    taskupdate = input()
    print('Would you like to update the name, description, or both?(name, desc, both):')
    specupdate = input()
    if specupdate == 'name':
        print('Enter the new name you would like for this task (' + taskupdate + '):')
        newname = input()
        db.update({'Name': str(newname)}, todo.Name == taskupdate)
    elif specupdate == 'desc':
        print('Enter the new description you would like for this task (' + taskupdate + '):')
        newdesc = input()
        db.update({'Desc': str(newdesc)}, todo.Name == taskupdate)
    elif specupdate == 'both':
        print('Enter the new name you would like for this task (' + taskupdate + '):')
        newname = input()
        print('Enter the new description you would like for this task (' + taskupdate + '):')
        newdesc = input()
        db.update({'Name': str(newname), 'Desc': str(newdesc)}, todo.Name == taskupdate)
    else:
        print('That is not a valid command, choose from the list within the parenthesis/().')

def delete():
    print('Would you like to delete one task, or multiple?(all, one):')
    allorone = input()
    

while True:
    userinput = input('Enter your command(create, read, update, delete): ')
    if userinput == 'create':
        create()
    elif userinput == 'read':
        read()
    elif userinput == 'update':
        update()
    elif userinput == 'delete':
        delete()
    else:
        print('That is not a valid command, choose from the list within the parenthesis/().')
