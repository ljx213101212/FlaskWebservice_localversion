# DocHeroku

This is the back end for the doctor finding app. If you want to run it just follow the right way of running a flask
project. But use **sudo** when run it. 

If you don't have the database file you can always create one yourself.

The API provided so far:
- http://localhost:5000/deleteById/<ID_num>
- http://localhost:5000/queryById/<ID_num>
- http://localhost:5000/update        
- http://localhost:5000/createClinic

The update and createClinic, these two are POST requests and the information you should provide should look like this :
{

  "id" : blabla,
  
  "name": hospital name,
  
  "address1": first line of address,
  
  "address2": second line of address

}
