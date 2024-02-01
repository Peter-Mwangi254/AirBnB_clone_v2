#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt -y update

# Install Nginx if it not already installed
command -v nginx || sudo apt install nginx

# Create the folder /data/ if it doesn’t already exist
mkdir -p /data/

# Create the folder /data/web_static/ if it doesn’t already exist
mkdir -p /data/web_static/

# Create the folder /data/web_static/releases/ if it doesn’t already exist
mkdir -p /data/web_static/releases/

# Create the folder /data/web_static/shared/ if it doesn’t already exist
mkdir -p /data/web_static/shared/

# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
mkdir -p /data/web_static/releases/test/

# Create a fake HTML file /data/web_static/releases/test/index.html
FILE="/data/web_static/releases/test/index.html"
mkdir -p "$(dirname "$FILE")"
cat <<EOF > "$FILE"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo rm -f /data/web_static/current && sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Define the path to the Nginx configuration file
nginx_config_file="/etc/nginx/sites-available/default"

# Define the path to the web_static directory
web_static_dir="/data/web_static/current/"

# Define the URL path for serving static content
static_url_path="/hbnb_static"

# Add alias directive and location block for serving static content to Nginx configuration
cat <<EOF | sudo tee -a $nginx_config_file > /dev/null
    location $static_url_path {
        alias $web_static_dir;
        # Add any additional directives here if needed
    }
EOF

# Restart Nginx to apply changes
sudo systemctl restart nginx
