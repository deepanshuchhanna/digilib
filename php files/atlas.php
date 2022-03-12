<?php
header("Content-disposition: attachment; filename=atlas.pdf");
header("Content-type: application/pdf");
readfile("atlas.pdf");
?>