# My Django Geo-location App

## Description

My Django geo-location application is an interactive mapping interface that allows you to visualize the geographical
location of your users. From your database models, this application fetches the coordinates of each user and plots them
on a map, powered by the popular JavaScript library, "Leaflet.js", and the Python library, "Folium".

## Models

The main model used in this application is the "CustomUser" model, which holds 'latitude' and 'longitude' fields amongst
others. These fields store the coordinates for each user.

## The Geo App

The main work of fetching user coordinates and mapping them takes place in the 'geo' app. Depending on the branch of the
application, either Leaflet.js or Folium is used for this purpose. Leaflet.js is a powerful open-source JavaScript
library for mobile-friendly interactive maps. Folium, on the other hand, makes it easy to visualize data that’s been
manipulated in Python on an interactive Leaflet map.

## User Interface

The application uses a default Bootstrap template for its user interface, to keep things simple and minimal. The focus
of the project is functionality over aesthetics. The only view available in the application is the map itself, which
features each of your users' locations. By clicking on a particular location on the map, a popup will appear, providing
more information about the user at that location.

## Branching

Currently, there are two main branches for this project. One branch utilizes 'Leaflet.js' while the other uses 'Folium'.
Although both tools provide robust mapping functionalities, there is a high probability that we will settle with '
Folium' for the final version of the application. This is because 'Folium' is more Pythonic and easier to work with in a
Python-based Django environment.

## Future Development

As the development progresses, we will be dropping 'Leaflet.js' and fully adopting 'Folium' for all mapping
functionalities. This decision is pending further testing and confirmation.

## .env

The environment variables you mentioned are widely used in Django projects for configuration:

```ENV```: This variable represents the environment where the application is running. The 'development' environment is
represented by ENV=dev. When deploying this application to a production server, this should be set to ENV=production.
This variable is very useful for setting up environment-specific configurations such as databases, cache settings, debug
statuses, and static files.

```SECRET_KEY```: This variable holds a secret key for a unique Django installation. This is used to provide
cryptographic signing and must be kept safe. The actual key itself should be unpredictable and unique. In this
application, the variable SECRET_KEY is set to a django generated secret key. For deployment, this should be replaced by
a key unique to your application.

```DEBUG```: This variable is a boolean that, when set to True, Django will display detailed error pages if an HTTP
request results in some form of exception. During production, it is recommended to set DEBUG to False to prevent
exposure of sensitive data in a production environment.

```ALLOWED_HOSTS```: This is a list of strings representing host/domain names that this Django site can serve. In this
case, ALLOWED_HOSTS is set to 127.0.0.1, which represents this localhost. For production, you should replace it with
your server's IP address or domain name.