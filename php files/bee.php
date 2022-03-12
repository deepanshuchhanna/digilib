<?php
header("Content-disposition: attachment; filename=bee.pdf");
header("Content-type: application/pdf");
readfile("bee.pdf");
?>
