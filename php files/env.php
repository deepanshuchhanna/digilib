<?php
header("Content-disposition: attachment; filename=env.pdf");
header("Content-type: application/pdf");
readfile("env.pdf");
?>