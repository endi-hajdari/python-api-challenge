#!/usr/bin/env python
# coding: utf-8

# # VacationPy
# ---
# 
# ## Starter Code to Import Libraries and Load the Weather and Coordinates Data

# In[6]:


get_ipython().system(' pip install hvplot')

# Dependencies and Setup
import hvplot.pandas
import pandas as pd
import requests
import json

# Importing API key
from api_keys import geoapify_key


# In[ ]:


# Loading the CSV file created in Part 1 into a Pandas DataFrame
city_data_df = pd.read_csv("output_data/cities.csv")

# Displaying sample data
city_data_df.head()


# ---
# 
# ### Step 1: Create a map that displays a point for every city in the `city_data_df` DataFrame. The size of the point should be the humidity in each city.

# In[ ]:


get_ipython().run_cell_magic('capture', '--no-display', '\n# Configuring the map plot\ncity_map_plot = city_data_df.hvplot.points("Lng", "Lat", geo = True, size = "Humidity", scale = 1, color = "City", alpha = 0.5, tiles = "OSM", frame_width = 700, frame_height = 500)\n\n# Displaying the map\ncity_map_plot')


# ### Step 2: Narrow down the `city_data_df` DataFrame to find your ideal weather condition

# In[4]:


# Narrowing down cities that fit criteria and drop any results with null values
# Dropping any rows with null values
narrowed_city_df = city_data_df.loc[(city_data_df["Wind Speed"]<= 4.5) & (city_data_df["Cloudiness"] == 0) & (city_data_df["Max Temp"]>= 21) & (city_data_df["Max Temp"]<= 27)].dropna()


# Displaying sample data
narrowed_city_df


# ### Step 3: Create a new DataFrame called `hotel_df`.

# In[5]:


# Using the Pandas copy() function to create DataFrame called hotel_df to store the city, country, coordinates, and humidity
hotel_df = narrowed_city_df[["City","Country", "Lat", "Lng"]].copy()

# Adding an empty column, "Hotel Name," to the DataFrame so you can store the hotel found using the Geoapify API
hotel_df["Hotel Name"] = " "

# Displaying sample data
hotel_df


# ### Step 4: For each city, use the Geoapify API to find the first hotel located within 10,000 metres of your coordinates.

# In[6]:


# Setting parameters to search for a hotel
radius = 10000
params = {"apiKey": geoapify_key}

# Printing a message to follow up the hotel search
print("Starting hotel search")

# Iterating through the hotel_df DataFrame
for index, row in hotel_df.iterrows():
    # Getting the latitude and longitude from the DataFrame using the loc() pandas function
    lat = hotel_df.loc[index, "Lat"]
    long = hotel_df.loc[index, "Lng"]
    
    # Adding filter and bias parameters with the current city's latitude and longitude to the params dictionary
    params["filter"] = "circle:{long},{lat},{radius}"
    params["bias"] = "proximity:{long},{lat}"
    
    # Setting base URL
    base_url = "https://api.geoapify.com/v2/places"


    # Making an API request using the params dictionaty
    name_address = requests.get(base_url, params=params)
    
    # Converting the API response to JSON format
    name_address = name_address.json()
    
    # Grabbing the first hotel from the results and store the name in the hotel_df DataFrame
    try:
        hotel_df.loc[index, "Hotel Name"] = name_address["features"][0]["properties"]["name"]
    except (KeyError, IndexError):
        # If no hotel is found, set the hotel name as "No hotel found".
        hotel_df.loc[index, "Hotel Name"] = "No hotel found"
        
    # Logging the search results
    print(f"{hotel_df.loc[index, 'City']} - nearest hotel: {hotel_df.loc[index, 'Hotel Name']}")

# Displaying sample data
hotel_df


# ### Step 5: Add the hotel name and the country as additional information in the hover message for each city in the map.

# In[7]:


get_ipython().run_cell_magic('capture', '--no-display', '\n# Configuring the map plot\nhotel_map_plot = hotel_df.hvplot.points("Lng","Lat", geo = True, scale = 5 color = "City", alpha = 0.5, tiles = "OSM", frame_width = 700, frame_height = 500)\n\n# Displaying the map\nhotel_map_plot')


# In[ ]:




