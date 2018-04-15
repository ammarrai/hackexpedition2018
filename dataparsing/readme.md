The code is all over the place , but basically this : 

1. Gather data on VA businessed from http://www.scc.virginia.gov/site_map.aspx . Had a csv downloaded , but also have web parsing options through BS4 fo proof of concept . 
After this , using here maps API , get lat lon data by sending batched requests to save time. ALso , the csv download on the SSC website does not work.

2. Have access to the Dun and Bradstreet API , through which I was able to pull info. Part 1 was a search endpoint to get all businesses in VA , part 2 was getting specific business info based on a unique id. 

3. Clean , merge all of the content in there. No data files being uploaded by me. 

4. Also calculate haversine distance to figure out which two businesses are closeby. 
