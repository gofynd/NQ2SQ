Welcome !!!

NQ2SQ: Natural Query to SQL Query
=======

Tool to convert natural language questions as input and query over MYSQL db to 
answer that questions by transforming questions to appropriate SQL query. 

Initially the scope of this tool is limited to single table only.


Intial Release - Dev.Version (Ask instead SELECT)

Description:
============
    In this Dev version namely Ask instead SELECT, I have implemented select functionality of mysql.
    See the below steps for more.
         
Usage:
=======
Setup: 
```
pip install -e git+git@gitlab.com:fynd/NQ2SQ.git@#egg=NQ2SQ

Import:

from NQ2SQ.parsing_agent import parser

table_schema = {
'cl1':'number'
}


qparser = Parse(table_schema)
sql_query = qparser.parse("get id and emp_name from Askme table ")

```


1.Step:
=======
You have to configure your Database schema in the file 
"database.py" . 

Only column name and anyone appropriate type from this("number", "str","boolean" , "timestamp")


2.Step:
===========
Then you can directly ask your question against this schema like shown in usage.


Example:
========
from parser import Parser

p = Parser()

p.parse("get id and emp_name from Askme table ")
p.parse("get id and emp_name from Askme table ")



Output:
=======

sentence = get id and emp_name from Askme table  

SELECT id,emp_name FROM Askme 


Limitations:
=============
It's just a kick start and there are many thigs yet to be done,
aggregation, filters, self join capabilities etc., 

Thanks for your time.
