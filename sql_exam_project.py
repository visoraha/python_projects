import time
name=input('enter your name :')
exam=input(f'hai {name.upper()} do you want to write sql exam (say yes or no ):')
if exam!='yes':
    print(f'ok {name} prepare well and  when ever you are in free time then that time write this exam')
    quit()
print(f'ok {name} lets write an exam'.upper())
print('----------------------------------------------------------------------------------------------------------------------------')
score=0
wrong=0
total=0
start_time=time.time()
question=input('sql stands for :')
if question.lower()=='structured query language':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('dbms stands for :')
if question.lower()=='data base management system':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how many dql commands are there:')
if question.lower()=='3':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('what are the dql commands:')
if question.lower()=='select,from,where':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('which command is used to inserting the data into table:')
if question.lower()=='insert':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('dcl stands for:')
if question.lower()=='data control language':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('which command is used to update the data into tables:')
if question.lower()=='update':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how many aggregate functions(multi row functions) are there:')
if question=='5':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how to take back to the deleted table write syntax:')
if question.lower()=='flashback table table name to before drop':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how many constraints are there:')
if question=='6':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('Which SQL statement is used to extract data from a database?:')
if question.lower()=='select':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1   
question=input('Which SQL statement is used to delete data from a database?:')
if question.lower()=='delete':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how do you select a column named "FirstName" from a table named "Persons"?:')
if question.lower()=='select firstname from persons':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how do you select all the columns from a table named "Persons"?:')
if question.lower()=='select * from persons':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how do you select all the records from a table named "Persons" where the value of the column "FirstName" is "vinay"?:')
if question.lower()=="select * from persons where firstname='vinay'":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')

total+=1
question=input('how do you select all the records from a table named "Persons" where the value of the column "FirstName" starts with an "a"?:')
if question.lower()=="select * from persons where firstname like 'a%'":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')

total+=1
question=input('how do you select all the records from a table named "Persons" where the "FirstName" is "Peter" and the "LastName" is "vinay"?:')
if question.lower()=="select * from persons where firstname='peter' and lastname='vinay'":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')

total+=1
question=input('Which SQL statement is used to return only different values?:')
if question.lower()=='distinct':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')

total+=1
question=input('Which SQL keyword is used to sort the result-set?:')
if question.lower()=='order by':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how can you return all the records from a table named "Persons" sorted descending by "FirstName"?:')
if question.lower()=='select * from persons order by firstname desc':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how can you insert "kumar" as the "LastName" in the "Persons" table?:')
if question.lower()=="insert into persons(lastname) values('kumar')":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1   
question=input('How can you change "vinay" into "vicky" in the "LastName" column in the Persons table?:')
if question.lower()=="update persons set lastname='vicky' where lastname='vinay'":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1   
question=input('how can you delete the records where the "FirstName" is "Hari" in the Persons Table?:')
if question.lower()=="delete from persons where firstname='hari'":
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('how can you return the number of records in the "Persons" table?:')
if question.lower()=='select count(*) from persons':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('Which operator is used to select values within a range?:')
if question.lower()=='between':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('The NOT NULL constraint enforces a column to not accept NULL values(true or false):')
if question.lower()=='true':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
question=input('Which operator is used to search for a specified pattern in a column?:')
if question.lower()=='like':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')

total+=1
question=input('Which SQL statement is used to create a database table called "Customers"?:')
if question.lower()=='like':
    score+=1
    print('correct')
else:
    wrong+=1
    print('in correct')
total+=1
end_time=time.time()
print(f'{name} your sql exam was completed see your score below')
print('total number of question'.title(),total)
print('total correct answers is'.upper(),score)
print('total wrong answers is'.title(),wrong)
print('total time taken for this test :',end_time-start_time)

print('-----------------------------------------------------------------------------------------------------------------------------')
if score==total:
    print(f'wow welldone {name} you answered all coorrect answers'.upper())

    
    




    
    




    
    




    
    




    
    



    
    
