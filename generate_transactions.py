from datetime import datetime
import sys
import random
from time import sleep


# We will imagine that we have 8 rooms installed with light sensors
# and we constantly capture the light levels of these 8 rooms every 5 seconds
# in the subfolder iotdata

# Read data
import pandas as pd
df = pd.read_csv("bakeinc_products.csv") 

product_id = df['ProductID']

while True:
    try:
        dt = datetime.now()
        # Start a new file based on current timestamp
        fn = "{}{}{}{}{}{}".format(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
        f = open("data/" + fn + ".txt","w+") # Open the file for writing
        for product in product_id:
            quantity = random.randint(30,50) # Generate a random quantity purchased
            data = "{},{},{}\n".format(product,quantity,dt)
            f.write(data) # Write into the file
            print(data)
        f.close() 
        sleep(5) # Wait another 5 seconds before collecting the next batch of data
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit()
    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
