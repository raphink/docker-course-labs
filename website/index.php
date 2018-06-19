<html>
    <head>
        <title>C2C Shop</title>
    </head>

    <body>
        <h1>Welcome to C2C</h1>
        <ul>
            <?php

            $json = file_get_contents('http://product-service/');
            $obj = json_decode($json);

            $products = $obj->products;

            foreach ($products as $product) {
                echo "<li>$product</li>";
            }

            ?>
        </ul>
        <ul>
        <h1> Using the database </h1>
         <?php
             $jsons = file_get_contents('http://product-service/db');
             $results = json_decode($jsons);
             foreach ($results as $result) {
                 echo "<li>$result</li>";
            }
            ?>
        </ul>
    </body>
</html>
