# API Documentation

This Rest API uses the data provided in the file `Aircraft Database - Sheet1.csv` to allow users to search for planes by model, weight class, and tags. There currently is one endpoint with examples shown below.
## Requirements
This app uses the Python 3.8.10 packages Flask and Pandas to serve the endpoint on the localhost:5000 and clean the data fields in the dataframe. Below are the list of full requirements.

``` text
click==8.1.3
Flask==2.1.2
importlib-metadata==4.11.4
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
numpy==1.22.4
pandas==1.4.2
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
Werkzeug==2.1.2
zipp==3.8.0
```

## Data Cleaning

Before building the API endpoint, I decided to analyze the data and remove all rows that are null, and fill the remaining null data with a string "No Value". Normally this data should be thoroughly cleaned and documented and placed in either a relational or non relational database.

## API Endpoint

URI: `GET /api/v1/planes?page=1&model=string&weightClass=string&tag=string&tag=string`
Below is the body schema accepted by the search endpoint. It accepts a string for modelId, weightClass and a list of strings representing the tags. All fields are optional and if given no fields and asked to search this endpoint will retrieve everything in the dataframe. This endpoint does support pagination as well. The default page is set to 1 if no page is given.

#### Example Request

URL: ` GET /api/v1/planes?page=1&model=cougar&weightClass=small%20eqpt&tags=military`

#### Example Response
```JSON
{
  "page": 1,
  "planes": [
    {
      "# Engines": "2",
      "AAC": "A",
      "ADG": "I",
      "ATCT Weight Class": "Small Eqpt",
      "Approach Speed (Vref)": "82.0",
      "Cockpit to Main Gear (CMG)": "tbd",
      "Date Completed": "2018-Jun-5",
      "ICAO Code": "GA7",
      "Length, ft": "28.67",
      "MGW (Outer to Outer)": "tbd",
      "MTOW": "3,800",
      "Main Gear Config": "S",
      "Manufacturer": "Grumman American",
      "Max Ramp Max Taxi": "3,800",
      "Model": "GA-7 Cougar",
      "Note": "tbd",
      "Physical Class (Engine)": "Piston",
      "TDG": "1A",
      "Tag Match": true,
      "Tags": "single,military",
      "Tail Height, ft (@ OEW)": "10.33",
      "Wake Category": "L",
      "Wheelbase, ft": "tbd",
      "Wingspan, ft": "36.83",
      "Wingtip Configuration": "no winglets",
      "Years Manufactured": "tbd"
    }
  ]
}
```
## Run The Server
You may start the server with `python app.py`. If you would like to set the server to listen on a specific port set the environment variable `PORT` to an open part of your choosing with 
`export PORT=<PORTNUMBER>`.
