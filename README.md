# YTCP
Youtube comment profile picture downloader

For obtaining a JSON file of URLs, you can use Copy all links and image links to CSV or JSON extension from the Google website.
Get it from here - https://chromewebstore.google.com/detail/copy-all-links-and-image/ccddopnnikeeoogpfbnfommfoeliaidg

Steps!

Go to the video which you need to download commenters' profile pictures.
Tap on the JSON link downloader extension and download the data as JSON
![image](https://github.com/user-attachments/assets/d8b03769-c132-4ba7-98d2-2785cdf73bd5)

save it as input.json.
Go to the jsontoimagelinkstxt.py file and run it. 
You will get an image_links.txt file, which includes links for all the comments.

Now go to yctp.py file and run it.

You will see a zip file as downloaded images. Congrats, you have made it. Now unzip and view your saved profile pictures. you can change the image size from yctp file before downloading (the default is set for 800).
