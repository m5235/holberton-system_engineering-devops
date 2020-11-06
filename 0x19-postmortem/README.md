##Post-mortem
_______________________________________________________________________________________________________________________________________
![alt text](https://memecrunch.com/meme/SG2E/hey-hey-over-here/image.jpg)


1. Issue Summary:
_______________________________________________________________________________________________________________________________________

Between 17:30 and 18:15 on January 10, 2020, 500 users encountered without access to the platform to push their products
Image for post
The event was triggered by an update at 17:30 for the wp-settings.php file.
The update contained a new method such as enabling users to push their products, with the aim of giving the best user experience without many steps for that. ![alt text](https://miro.medium.com/max/400/0*bsfOPg-aqSyfkY3O.png)

An error in this code is caused by human failure, at the moment of the update the file was an error in the file extension, change php to phpp and this was the error that caused the server to fail.
The event was detected by the monitoring system. The team started working on the event by initiating the debugging process, analyzing the cause of errors, and using various methods such as using the strace command and activating the debugging tool in WordPress.
This low incident affected 10% of users.

2. Timeline :
- 17:30 Post the new update.
- 17:33 Report an issue with making payments to social media.
- 17: 38 Building engineering reports a server issue with 500 lines
- 18:07 Starting the server systems debugging process
- 18:13 A problem has been detected in wp-settings.php file
- 18:15 Publish the new code in production.
3. The root cause and the decision:
_______________________________________________________________________________________________________________________________________

Currently at 17:39 PM the wp-settings push file has been called up and wrote a file extension like phpp.
The decision was to implement a dummy file that would help change the line of code and fix the problem

4. Corrective and preventative
For the future, we create a new step for the update any feature of the page like improve the test of all page and create new for all features that will be deployed and prepare feedback with the team most frequently with the purpose of prevent this kind of issues.