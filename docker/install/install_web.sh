echo "Install virtualenv and requirements !"
cd /app/DoorManagerTools && make installenv

echo "Copy Nginx and Supervisor Config Fle !"
cp /app/DoorManagerTools/docker/nginx/default /etc/nginx/sites-enabled/default
cp /app/DoorManagerTools/docker/supervisor/doormanagertools.conf /etc/supervisor/conf.d/doormanagertools.conf

echo "Install Finished !" 
