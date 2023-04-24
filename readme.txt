This is a project is about communicating through the sockets. It is small replication of chat application. 
Where two users can exchange messages as well as transfer files with each other.

This project has only one file:
1) main.py

Program Description:
Text messages and files can be transfered through the sockets. This program will create two threads a writing thread and a reading thread.
the writing thread will allow the user to write the messages and initiate the file transfers. The reading thread will allow to read the messages and files that are sent by the writing thread of the other user. 

The program must run in two different terminals lets say termianl1 and terminal2. then a writing thread and a reading thread is created for both the terminals.

The below steps will explain step by step of project flow:


Step-1: The Reading thread in terminal1 creates a socket at a random port and it is displayed on the terminal to which address it is connected to.

Step-2: Similarly, The Reading thread in terminal2 will also create a socket at a random port which is also displayed on termianl.

Step-3: Now user at terminal1 should give a port number of reading thread of termianl2 as an input for writing thread from keyboard. Now, the writing thread of terminal1 is connected to the reading thread of terminal2.

Step-4: Similarly, user at termianl2 will give port number of the reading thread of termianl1 click enter. Now the writing thread of terminal2 is connected to reading thread of terminal1.

Step-5: Now both terminals will be able to send messages to each other.

Step-6: if any message is in the form of "transfer file_name" then a file is sent with filename "file_name".




