# Log-Analysis

## About
This is the third project for the Udacity Full Stack Web Developer Nanodegree. In this project, an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like is built. This reporting tool is a Python program using the psycopg2 module to connect to the database and will prints out reports (in plain text) based on the data in the database.

The database includes three tables:

Authors table
Articles table
Log table

## To Run

### Software:
Python3
Vagrant
VirtualBox

### Setup
* <h4>Install <a href="https://www.vagrantup.com/">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads">VirtualBox.</a></h4>
* <h4>Clone the repository to your local machine</h4>
* <h4>Start the virtual machine</h4>
  From your terminal, run the command `vagrant up`. 
  When vagrant up is finished running, run `vagrant ssh` to log in to your Linux VM.
* <h4>Download the <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip">data</a></h4>
  You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.
* <h4>Setup Database</h4>
  To load the database use the following command:
  <pre>psql -d news -f newsdata.sql;</pre>
* <h4>Run Module</h4>
  <pre>python log.py</pre>
  
