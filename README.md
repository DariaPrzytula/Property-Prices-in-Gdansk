# Project: Property Prices in Gdańsk, Poland
This project is aimed at analyzing apartment prices in Gdansk, Poland. It contains several visualizations, including:

* scatter plots showing the relationship between apartment price and size in different districts of Gdańsk
* the histogram showing the distribution of apartment prices in Gdańsk
* bar plots showing the average apartment prices in different districts of Gdańsk

Additionally, the project includes a machine learning model that allows for the prediction of apartment prices based on several factors, such as size, year of construction, number of rooms, floor, and district.

## Data
Data were downloaded from www.trojmiasto.pl by Data Miner on 07.01.2023 r.
The dataset includes information on apartment prices, sizes, districts, and other features.

## Requirements
The following Python packages are required to run the code:

* pandas
* numpy
* scikit-learn
* plotly
* dash

## Instructions

The repository contains files such as:
* raw_data.xlsx - file with source data
* data_to_dashboard.xlsx - a file with cleaned data used for the dashboard
* data_to_model.csv - file with data prepared for the model
* cleaning_and_preparing_code.py - a file containing code for cleaning and preparing data
* app.py - file containing the dashboard code
* Prezentacja Projekt.pptx - file with presentation in Power Point [pl]

To open the Dash application, you need to run the **app.py** code for example in **PyCharm**. All necessery files are added in code as links from this repository.  
After running the app.py code a local server will be launched. This server will host your Dash application and make it accessible via a URL. You can then open your web browser and navigate to this URL to access your Dash application.\
The application enables interactive exploration of data on housing prices, as well as prediction of housing prices based on data entered by the user. This will start a Dash application that can be accessed in a web browser.
The application allows for interactive exploration of the apartment price data, as well as prediction of apartment prices based on user input.




