<?php
header("Content-disposition: attachment; filename=geoindia.pdf");
header("Content-type: application/pdf");
readfile("geoindia.pdf");
?>