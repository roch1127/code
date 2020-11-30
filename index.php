
<?php
$insert=false;
if(isset($_POST['name'])){
$server="localhost";
$username="root";
$password="";

$con=mysqli_connect($server,$username,$password);
if(!$con){
    die("connection to this database failed due to ".mysqli_connect_error());
}
$name=$_POST['name'];
$age=$_POST['age'];
$gender=$_POST['gender'];
$email=$_POST['email'];
$phone=$_POST['phone'];
$other=$_POST['other'];
$sql="INSERT INTO `trip`.`trip` (`name`, `age`, `gender`, `email`, `phone`, `other`, `date`) VALUES ('$name', '$age', '$gender', '$email', '$phone', '$other', current_timestamp());"; 
// echo $sql;

if($con->query($sql)==true){
    // echo "successfully inserted";
    $insert=true;
}
else{
    echo "ERROR: $sql <br> $con->error";
}
$con->close();
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to travel form</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Sansita+Swashed:wght@300&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@700&display=swap" rel="stylesheet">
</head>
<body>
    <img class="bg" src="php_background.jpeg" alt="">
 <div class="container">
 <h1>Welcome to US trip form</h1>
 <p>Enter your details and submit this form to confirm your participation</p>
 <?php
 if($insert==true){
 echo "<p class='submitmesg'>Thanks for submitting your form. We are happy to see you joining for the US trip</p>";
 }
 ?>

 <form action="index.php" method="post">
     <input type="text" name="name" id="name" placeholder="Enter your name">
     <input type="text" name="age" id="age" placeholder="Enter your age">
     <input type="text" name="gender" id="gender" placeholder="Enter your gender">
     <input type="text" name="email" id="email" placeholder="Enter your email id">
     <input type="text" name="phone" id="phone" placeholder="Enter your phone no.">
     <textarea name="other" id="other" cols="10" rows="5" placeholder="Enter any other information here"></textarea>
<button class="butn">Submit</button>


 </form>

 </div>
   <script src="index.js"></script>
   
</body>
</html>