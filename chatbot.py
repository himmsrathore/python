db={
    'hello':'hi',
    'what is name':'bot',

}
while True:
    key=input('Please Enter Your Q :').lower().strip()
    if key=='out':
        break
    elif key not in db.keys():  
         print('Try again')

    else:
        print('Bot :',db[key])
       
