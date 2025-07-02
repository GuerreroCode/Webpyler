Webpyler v0.3.0 - static webpage builder
****************************************

Webpyler is an open-source static wepbage builder that is simple to use. Think of it like a simple html
compiler running on an https server

WHY:
For simpler websites, this will prevent the need to copy and paste the same html over and over again.
Lets say you have a header, you can simply add a tag with the  webpyler and it will be dynamically built
for each page. 

The main benefit is for simple websites. Of course other frameworks such as ASP.NET already have this feature
but this will allow for simpler webpage construction for less effort.


******************************************
How to use Webpyler
******************************************
STEP 1||CONFIG||

At the top of the webpyler.py file, there are some config variables, such as the certificate,
keyfile, hostname, and port. You will need to generate your own SSL files for running in order
for the file to run.
You can configure the host and port to your desired IP/DNS rather than just the localhost

For server setups, you must also config your domain name in redirect.py. This will ensure that
all http redirects to https for your website 



STEP 2||HTML SET UP||
there are 2 directories

html: the main pages that hold the content 
parts: the sub-parts that are copied into the main html pages

place your files accordingly


STEP 3||TAGS||

each part in the directory has a corresponding tag. they are formatted <*.html> where * is the filename

In your main html pages, paste your tag where you want your html to appear

For example

index.html may have 
<header.html>
<h1>Example text</h1>

and your filename in /parts will be header.html


STEP 4||RUN||

run the code with python3 webpyler.py, loading a page will dynamically write the page

for http -> https redirects, also run python3 redirect.py (not needed for local testing)

All the html from the /parts will be written where the tag is written in the html

Feel free to manipulate and reproduce this code!

********************************************************
Future Plans
********************************************************
Other request handlers (POST, UPDATE, DELETE, etc.)
Templates, allowing for simply new text or data, which will populate in a template 
Building html differently based on desktop or mobile
SQL integration
