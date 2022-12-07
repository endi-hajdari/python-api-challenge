# Project Title
```Module 6 Challenge:``` Python API Challenge

# Project Overview
This challenge is associated with ```Module 6``` of **UofT's 2022-2023 Data Analytics Bootcamp**. This challenge involved the creation of two Python scripts that made use of several Python libraries and APIs. The first script created titled ```WeatherPy``` used the ```citipy``` Python library and the ```OpenWeatherMap``` API to produce plots that depicted the weather of over 500 cities of varying distances from the equator. The second script created titled ```VactionPy``` made use of the ```geoViews``` Python library and the ```Geoapify``` API to create map visualizations.

# Repository Structure and Breakdown
The following contents may be found in this repository:

> A folder titled ```VacationPy``` that contains the following files:
> - A Jupiter notebook file named ```main_r2.ipynb``` that contains the complete analysis code;
> - A Python file named ```main_r2.py``` that contains the complete analysis code; and
> - A Jupiter notebook filed named ```VacationPy.ipynb``` that contains the starter code provided.

> A folder titled ```WeatherPy``` tha contains the following files:
> - A Jupiter notebook file named ```main_r1.ipynb``` that contains the complete analysis code;
> - A Python file named ```main_r1.py``` that contains the complete analysis code; and
> - A Jupiter notebook filed named ```WeatherPy.ipynb``` that contains the starter code provided.

> A folder titled ```Output Data``` that contains the following files that were produced in Part 1:
> - A scatter plot of maximum temperature as a function of latitude titled ```Fig1.png```;
> - A scatter plot of humidity as a function of latitude titled ```Fig2.png```;
> - A scatter plot of cloudiness as a function of latitude titled ```Fig3.png```; 
> - A scatter plot of wind speed as a function of latitude titled ```Fig4.png```; and 
> - A ```CSV``` file titled ```cities```.

- A ```.gitignore``` file to ensure that the ```api_keys.py``` file that contains the API key is kept from being shared with the public;
- A ```README.md``` file that contains a description of this project;

# Part 1: WeatherPy
In this part of the challenge, a Python script was created to visualize the weather of over 500 cities of varying distances from the equator. The ```citipy```, ```Matplotlib```, ```NumPy```, ```pandas```, and ```scipy.stats``` Python libraries, as well as the ```OpenWeatherMap``` API were used to create a representative model of weather across cities. For this part, the ```WeatherPy.ipynb``` Jupyter notebook provided in the starter code ```ZIP``` file was used as a guide. The starter code already had generated the random geographic coordinates and the nearest city to each latitude and longitude combination. 

### Visualizing the Relationship Between Weather Variables and Latitude
The first requirement involved creating scatter plots to showcase the relationship between different weather variables and latitude. Moreover, the ```OpenWeatherMap``` API was used to retrieve weather data from the cities list generated in the starter code. Next, a series of scatter plots were created to showcase the following relationships:
- Latitude vs. Temperature (F)
- Latitude vs. Humidity (%)
- Latitude vs. Cloudiness (%)
- Latitude vs. Wind Speed (m/s)

### Linear Regression Analysis of Each Relationship
The second requirement involved computing the linear regression for each relationship. Plots were separated into Northern Hemisphere (i.e., greater than or equal to 0 degrees latitude) and Southern Hemisphere (i.e., less than 0 degrees latitude). Next, a series of scatter plots were created that included the linear regression line, the model's formula, and the r-values. Moreover, the following plots were generated:
- Northern Hemisphere: Temperature (F) vs. Latitude
- Southern Hemisphere: Temperature (F) vs. Latitude
- Northern Hemisphere: Humidity (%) vs. Latitude
- Southern Hemisphere: Humidity (%) vs. Latitude
- Northern Hemisphere: Cloudiness (%) vs. Latitude
- Southern Hemisphere: Cloudiness (%) vs. Latitude
- Northern Hemisphere: Wind Speed (m/s) vs. Latitude
- Southern Hemisphere: Wind Speed (m/s) vs. Latitude

After each pair of plots, an explanation of what the linear regression was modelling, as well as any relationships/trends that were identified were provided in the Markdown language.  

# Part 2: VacationPy
In this part of the challenge, weather data was leveraged to aid in the planning of future vacations by using the Jupyter notebooks, the ```geoViews``` and ```pandas``` Python libraries, alongside the ```Geoapify``` API. The main tasks in this section were to use the ```Geoapify``` API and the ```geoViews``` Python library to create map visualizations. The starter file provided the code that imported the required libraries and the ```CSV``` file with the weather and coordinates data for each city created in ```Part 1``` as a starting point. Moreover, the ```VacationPy.ipynb``` starter code was accessed and the following steps were completed:

- A map that displayed a point for every city in the ```city_data_df``` DataFrame was created. Note that the size of the points were equivalent to the humidity in each respective city.
- The ```city_data_df``` DataFrame was narrowed down to find a specified ideal weather condition (i.e., a max temperature lower than 27 degrees but higher than 21 degrees; Wind speeds less than 4.5 m/s; and Zero cloudiness).
