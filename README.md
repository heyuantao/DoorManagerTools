
一、以容器方式运行
1.1 构建容器
```
docker build -t doormanagertools:1.0 .
```
1.2 运行容器
先运行redis：
```
sudo mkdir -p /app/
sudo chown -R ${USER}:${USER} /app/
git clone https://github.com/heyuantao/DoorManagerTools.git /app/DoorManagerTools/
docker run -d --name redis --restart=always --network=host -v /app/DoorManagerTools/docker/redis/redis.conf:/etc/redis/redis.conf redis:5.0 redis-server /etc/redis/redis.conf
```
然后运行应用
```
docker run -d --name doormanagertools --restart=always --net=host -v /app/data/logs:/var/log/supervisor/  doormanagertools:1.0 
```

二、源代码方式安装和调试
2.1 启用应用

gunicorn -w 6 -b 0.0.0.0:5000 --log-level=ERROR --timeout 30 -k gevent DoorManagerToolsAPP:application


2.2、使用nginx进行流量转发

对于匹配 /  的流量转发到对应的后端接口

类似如下
````
server {
        listen 80;
        server_name webstorage.x.y;
	    client_max_body_size 15m; 
        location / {
                proxy_pass http://x.x.x.x:5000;
                charset utf-8;
                proxy_set_header Host $host;
                proxy_set_header X-Forwarded-for $remote_addr;
                proxy_set_header X-Real-IP $remote_addr;
        }
}
````


其他：
1.调试模式请设置
```
--log-level=DEBUG
```
