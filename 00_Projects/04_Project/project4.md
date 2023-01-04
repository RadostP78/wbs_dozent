# Project 4 

## Part One
Develop a Webservice which use the pretrained model to predict the area prices.

When the requester sends the required area:
1.  store the requested area into a SQLite DB
2.  predict the area price
3.  store the predicted price to the SQLite
4.  return the predicted price with the primary key of the record to the requestor



## Part Two

Imagine you have a table with areas and roomcounts but without price. So you need to run a python program to estimate the prices for the records without predictions (price value).

1. Insert some manual data into the table.
2. Use your pre-trained model to predict price only for the records without prices.



# Topics to use

1. Functions
2. Logging