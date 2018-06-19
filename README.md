Creates a simple webapp with python's flask
and php to render a simple hello page with data from the python app


docker run -d -P -p 5558:80 --link pyapp webphp

docker run --name pyapp -d -P -p 7555:80 product-service  
