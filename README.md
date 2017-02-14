[![Build Status](https://travis-ci.org/GeoNode/geonode-risk_management_tools.svg?branch=master)](https://travis-ci.org/GeoNode/geonode-risk_management_tools)
[![Coverage Status](https://coveralls.io/repos/github/GeoNode/geonode-risk_management_tools/badge.svg?branch=master)](https://coveralls.io/github/GeoNode/geonode-risk_management_tools?branch=master)

# geonode-risk_management_tools
GeoNode Risk Management Tools is a GeoNode Extension built by WorldBanck GFDRR which adds the capability of extracting and managing Hazard Risks on geographical areas.

## Overview
The World Bank and GFDRR are leading an ongoing Technical Assistance (TA) to the Government of Afghanistan on Disaster Risk Management. As part of this TA, a multi-hazard risk assessment was conducted. An international consortium was hired to produce new information on hazard, exposure, vulnerability and risk, for flooding, earthquake, landslide, avalanche, and drought. Hazard and loss for different return periods was computed for all districts and regions. In addition, a cost-benefit analysis was conducted for a select number of risk reduction options for floods and earthquakes (e.g. flood levees; earthquake-proofing of buildings).

A GeoNode (http://disasterrisk.af.geonode.org/) was developed by ENEA to host and share the data. Many of the data layers have been uploaded and stylized on this GeoNode. The GeoNode is currently following the standard format. World Bank has an interest in improving the decision-making and data-extraction capabilities by expanding this GeoNode with two modules. One module should allow the user to dynamically explore the potential costs and benefits of the pre-calculated risk management options, by sliding bars, changing numbers and getting outputs in graphs, charts and a simple map. The second module should allow the user to easily extract maps and tabular results for their area and indicator of interest, again using drop-down menus and boxes that filter existing information and maps.

### Module 1: Cost-benefit Analysis & Decision Tool
This module should allow the user to use an interactive user interface (drop-down menus; slide bars; buttons) to access pre-processed tables and maps related to cost-benefit analysis of risk management options.

### Module 2: Risk Data Extraction and Visualization
This module should enable the user to easily show and extract data for the area (district, province, national) of interest. Based on the user's selection of area (linked to admin 1 and admin 2 shapefiles), indicator (linked to table and/or map), and indicator property (linked to rows and columns in the table), the user should get the correct map and a chart/graph.

## Installation
To install the module follow the steps below:

    # Install Ubuntu dependencies
    sudo apt-get update
    sudo apt-get install python-virtualenv python-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev libjpeg-dev libpq-dev libgdal-dev git default-jdk

    # Install Java 8 (needed by latest GeoServer 2.9)
    sudo apt-add-repository ppa:webupd8team/java
    sudo apt-get update
    sudo apt-get install oracle-java8-installer

    # Create and activate the virtulenv
    virtualenv --no-site-packages venv
    source venv/bin/activate

    # Install pip dependencies
    pip install -r requirements.txt

    sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
    sudo apt-get install gdal-bin
    # check GDAL version
    gdalinfo --version

    # install the correct PyGDAL version (>1.10.1)
    pip install pygdal==`gdal-config --version`

    # if you cannot find exactly the same version, be sure to install at least the closer major one e.g. 2.1.2 -> 2.1.2.3
