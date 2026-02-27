<html>
<head>
    <title>PHP Test</title>
</head>
<body>
    <?php
    $server = "localhost";
    $username = "root";
    $password = "giyu2112001";
    $connection = mysqli_connect($server, $username, $password);
    if (!$connection) {
    die("Connection failed");
    }
    echo "Connected successfully";
    ?>
</body>
</html>