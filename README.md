# SP-Streaming-CA
 SP-Streaming-CA

The youtube link to show to eh whole project process:
- https://youtu.be/mNPKHdfJAaU

First, you will code a Python application generate_transactions.py that periodically spills out logfiles of “customer transactions” in a folder named bakeinc/transactions.

This will act as the simulation of ‘streaming data’ that will be the input to the PySpark streaming application you will write later.

Each logfile will have three columns of data similar to that below, where 

- Column 1 is the ProductID that a customer purchase
-	Column 2 is the quantity purchased for that transaction
-	Column 3 is the timestamp of the purchase transaction

Second, you will design and create a database to store the data needed for the real-time graph.

Your intention is to compute aggregated totals of customer transactions every 1 minute from the streaming data and use the aggregated data points to display the graph.  

These aggregated data points would need to be stored somewhere.  The problem is, where?

You are aware that NoSQL databases are the most suitable for this purpose; however, you are not yet very proficient at using them.  Hence, you decide that for this POC system, you would just use a relational database to store the aggregated data first; if time permits, you might try out a NoSQL solution instead.

The following aggregated data would need to be stored inside this intermediate database, regardless of which platform you use eventually

-	There will be a column called time_window that indicates the timestamp of the start time of a 1 minute window
-	There will be a column called num_transactions that keeps track of the total number of transactions during that 1 minute time window

With these two columns of data, you would be able to generate the real-time graph as you planned.

Another challenge that you face as a junior developer is that, after you have stored the aggregated data, what mechanism should you use to display a real-time, constantly updating graph that can be viewed from any other computer inside your company’s intranet?

After doing some research, you decide that you would use a library called Dash (https://plot.ly/products/dash/).

