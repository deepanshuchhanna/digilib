<?php
header("Content-disposition: attachment; filename=india.pdf");
header("Content-type: application/pdf");
readfile("india.pdf");
?>
