<?php
header("Content-disposition: attachment; filename=pps.pdf");
header("Content-type: application/pdf");
readfile("pps.pdf");
?>
