<?php
header("Content-disposition: attachment; filename=math.pdf");
header("Content-type: application/pdf");
readfile("math.pdf");
?>
