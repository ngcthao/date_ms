DATE MICROSERVICE FOR MATH WORKSHEET GENERATOR<br/>
WRITTEN BY: NGOC-THAO LY

IMPORTS<br/>
Python Sockets Module<br/>
Datetime Module<br/>

INSTRUCTIONS/COMMUNICATION CONTRACT<br/>
Run the client and the microservice in two separate terminals to establish a connection.<br/>
---Enter <py \date_ms.py> in terminal 1<br/>
---Enter <py \date_client.py> in terminal 2

To Request Data:<br/>
Input any 0 or positive integer value in the client and press enter.<br/>
---Assume today's date is May 14, 2024<br/>
---Enter <2> in the client

To Receive Data:<br/>
You will automatically receive the corresponding date in MONTH DAY, YEAR format.<br/>
---You will receive <May 16, 2024> in the client

To Close:<br/>
Enter "exit" in the client input to close both the client and the microservice.<br/>
---Enter <exit> in the client<br/>
---Both the client and server will close

UML SEQUENCE DIAGRAM<br/>
![Model](./uml-diagram.png)

LIMITATIONS<br/>
The date microservice only handles single client connections.

CREDITS<br/>
The client and server code are based off of the following tutorial--<br/>
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
