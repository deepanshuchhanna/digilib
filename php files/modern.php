<?php
header("Content-disposition: attachment; filename=modern.pdf");
header("Content-type: application/pdf");
readfile("modern.pdf");
?>