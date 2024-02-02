#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt -y update

# Install Nginx if it not already installed
sudo apt -y install nginx

# Create the folder if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Add alias directive and location block for serving static content to Nginx configuration
sudo sed -i "48i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default


# Restart Nginx to apply changes
sudo service nginx restart
