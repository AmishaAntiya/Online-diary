<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Untitled Document</title>
</head>

<body>
<?php
session_start();
$username=$_POST['username'];

$password=$_POST['password'];
$cpassword=$_POST['cpassword'];


if ($username&&($password==$cpassword))
{
$connect = mysql_connect("localhost","root","");
mysql_select_db("bluewings") or die("couldn't find database");
$query = mysql_query("select * from user where username='$username'");
$numrows = mysql_num_rows($query);


	mysql_query("UPDATE user SET password='$password' WHERE username='$username'");
	echo 'Registered Successfully';

}
else
die("passwords didn't match");
mysql_close($connect);
?>
</body>
</html>