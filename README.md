[![Slack Status][slack-status-icon]][slack-status]

# AGU-2020

This repository contains materials for the 2020 AGU Fall Meeting Workshop: [SCIWS8 - Working with Cloud-Based NASA Earth Observations Data and Tools](https://agu.confex.com/agu/fm20/meetingapp.cgi/Session/105465)

The links below will launch an interactive environment on [binder.pangeo.io](https://binder.pangeo.io/) Note that binder environments are ephemeral. Any changes you make will be lost once your session ends, and you shouldn't store passwords.
[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=AWS+us-west2&color=blue)](https://aws-uswest2-binder.pangeo.io/v2/gh/podaac/AGU-2020/binder?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fpodaac%252FAGU-2020%26urlpath%3Dlab%252Ftree%252FAGU-2020%252F%26branch%3Dmain)

This workshop, hosted by NASA's Physical Oceanography and National Snow and Ice Data Center Distributed Active Archive Centers (PO.DAAC and NSIDC DAAC), is presented in three parts:

| Topic                                                                        | Description                                                                                                                             | Time (UTC)                                                                                                    |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Part I: Welcome: Overview and Context for NASA EOSDIS evolution to the Cloud | Presentation with Q&A                                                                                                                   | 16:00 - 16:35                                                                                                 |
| Part II: Science Use Case Demonstrations                                     | Jupyter Notebook demonstrations, highlighting NASA EOSDIS tools and services applied across several science use cases (15 min each)     | Demonstrations (including breaks): 16:35 - 18:45|
| Part III: Hands-on data discovery, access, and analysis in the cloud         | Jupyter Notebook tutorial providing step-by-step guidance on cloud-based data access and cloud compute based on previous demonstrations | 18:45 - 21:00 (including 5-min break and wrap up)                                                             |

This repository is structured accordingly. All materials for this workshop can be found in each Part's respective folder.

## Learning Objectives

Upon completion of this workshop, you will have a better understanding of what the new cloud-based paradigm for data archiving, distribution, and particularly data access and use would mean for you, and your science or application workflow:

* Examine the changes, impacts, and opportunities provided by the Earthdata Cloud infrastructure, including cloud vendor (AWS) information, cost, and compute resources.
* Reflect on how the Earth and Space science, data science and informatics communities are evolving, including the acquisition, archiving, distribution, and use of big data, and how that evolution impacts scientific research and application of Earth observations. 
* Investigate user stories across ocean, hydrology, and cryospheric science disciplines utilizing NASA EOSDIS capabilities within python-based Jupyter notebooks.
* Select and compare data transformation services and access methods within and outside of the Earthdata Cloud.
* Execute programmatic data access queries, basic GIS operations, plotting, and direct in-region cloud access using open source Python libraries.
* Identify where and when Earthdata Cloud components are implemented across data discovery, subsetting, access, and analysis/compute workflows.
* Develop new strategies for leveraging and integrating Earthdata Cloud capabilities within your own work.
* Identify resources, including the [Earthdata Cloud Primer](https://earthdata.nasa.gov/learn/user-resources/webinars-and-tutorials/cloud-primer), for getting started with Amazon Web Services outside of the Workshop to access and work with data with a cloud environment. 

## Workshop Usage

The [![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=AWS+us-west2&color=blue)](https://aws-uswest2-binder.pangeo.io/v2/gh/podaac/AGU-2020/binder?urlpath=git-pull%3Frepo%3Dhttps%253A%252F%252Fgithub.com%252Fpodaac%252FAGU-2020%26urlpath%3Dlab%252Ftree%252FAGU-2020%252F%26branch%3Dmain) Binder button allows you to explore and run the notebook in a shared cloud computing environment without the need to install dependencies on your local machine. This environment is running in the AWS us-west-2 region, which is where all Earthdata Cloud data and transformation service outputs are located. Note that this Binder environment will only be available during the Workshop event. See below for how to run the Workshop materials outside of the workshop.

## Local setup 

Many of the Jupyter Notebook materials presented during the Workshop can be run locally outside of Amazon Web Services using the following guidance. __XXX Tutorials demonstrating AWS in-region access/analysis need to be run within an AWS EC2 instance, which is described in more detail in the Part III Hands-on notebook.__ 

1. Install miniconda3 (Python 3.8) for your platform from https://docs.conda.io/en/latest/miniconda.html

2. Download the AGU-2020 repository from Github by clicking the green 'Code' button located at the top right of the repository page, then select 'Download Zip'.

3. Unzip the file, and open a command line or terminal window in the AGU-2020 folder's location.

4. From a command line or terminal window, install the required environment with the following command (__NEEDS UPDATING ONCE ENV IS SET UP__):

`conda env create -f binder/environment.yml`

You should now see that the dependencies were installed and our environment is ready to be used.

5. Activate the environment with

`conda activate tutorials`

6. Launch the notebook locally with the following command:

`jupyter lab`

This should open a browser window with the JupyterLab IDE, showing your current working directory on the left-hand navigation. 


## Authors and Presenters

Catalina M Oaida, NASA Jet Propulsion Laboratory 

Amy Steiker, NASA National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC), University of Colorado

Andrew P Barrett, National Snow and Ice Data Center, University of Colorado

Walt Meier, NASA National Snow and Ice Data Center Distributed Active Archive Center (NSIDC DAAC), University of Colorado

Jack McNelis, NASA Jet Propulsion Laboratory

Mike Gangl, NASA Jet Propulsion Laboratory

Luis Alberto Lopez, National Snow and Ice Data Center, University of Colorado

Stepheny Perez, NASA Jet Propulsion Laboratory (JPL)


### Contacts

PO.DAAC Contacts

Catalina Oaida - PO.DAAC Applied Science SE Team lead
catalina.oaida@jpl.nasa.gov

## Acknowledgements

This tutorial was put together by the Authors and Presenters listed above, with support from their institutions, NASA EOSDIS [PO.DAAC](https://podaac.jpl.nasa.gov/) at Jet Propulsion Laboratory California Institute of Technology and NASA EOSDIS [NSIDC DAAC](https://nsidc.org/daac).

This tutorial runs on top of Pangeo's Binderhub.
Pangeo is [supported](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1740633&HistoricalAwards=false) by the [National Science Foundation (NSF)](https://www.nsf.gov/) via the [EarthCube Program](https://www.earthcube.org/) and the [National Aeronautics and Space Administration](https://www.nasa.gov/) via the [ACCESS Program](https://earthdata.nasa.gov/community/community-data-system-programs/access-projects).

[slack-status-icon]: https://img.shields.io/badge/Slack-AGU--tutorial-blue.svg
[slack-status]: https://nasadaacagu20-5ai7790.slack.com/archives/C01ETUUUDN3
