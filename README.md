The web application has been developed using modern full-stack technologies listed below:
Front-end - NextJS
Back-end - FastAPI (Python)
Database - Oracle (hosted on Ryerson moons)

The application has been deployed on the web at the following url:
https://library-dbms-frontend.vercel.app/

We are hosting our back-end as a serverless function which uses SSH tunnel to connect with our Ryerson Oracle Database. This is then interfaced with the frontend using CRUD operation endpoints to get our Web GUI synced with the Oracle Database.

Screenshot above shows how each of the tables are formatted on the application to display all the records. Features are implemented on individual records to update, delete and add. Furthermore, all the tables also have pre-configured queries which were written in previous assignments.
				
Moreover, for creating new records, forms are validated to ensure data validation throughout the application pipeline. Screenshot below outlines the validation features.


Lastly, the application also has capabilities to run queries on the front-end views to enhance user experience.
