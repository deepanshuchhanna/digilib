<?php
header("Content-disposition: attachment; filename=chemistry.pdf");
header("Content-type: application/pdf");
readfile("chemistry.pdf");
?>
