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
$email=$_POST['email'];
$password=$_POST['password_1'];

$contact=$_POST['mobno'];
if ($email && $password)
{
$connect = mysql_connect("localhost","root","");
mysql_select_db("bluewings") or die("couldn't find database");
$query = mysql_query("select * from user where email='$email'");
$numrows = mysql_num_rows($query);

if($numrows!=0){
echo 'Usename already exist';
}
else
{
	mysql_query("insert into user(username,email,password,contact) values('$username','$email','$password','$contact')");
	echo 'Registered Successfully';
}
}
else
die("Please enter username and password");
mysql_close($connect);
?>
</body>
</html>