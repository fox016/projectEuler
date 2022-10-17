<?php

function hourglassSum($arr) {
  $max = PHP_INT_MIN;
  for($row = 0; $row < 4; $row++) {
    for($col = 0; $col < 4; $col++) {
      $sum = calcSum($arr, $row, $col);
      if($sum > $max)
        $max = $sum;
    }
  }
  return $max;
}

function calcSum($arr, $startRow, $startCol) {
  $sum = $arr[$startRow][$startCol];
  $sum += $arr[$startRow][$startCol+1];
  $sum += $arr[$startRow][$startCol+2];
  $sum += $arr[$startRow+1][$startCol+1];
  $sum += $arr[$startRow+2][$startCol];
  $sum += $arr[$startRow+2][$startCol+1];
  $sum += $arr[$startRow+2][$startCol+2];
  return $sum;
}


$test1 = 
[
[-9,-9,-9,1,1,1],
[0,-9,0,4,3,2],
[-9,-9,-9,1,2,3],
[0,0,8,6,6,0],
[0,0,0,-2,0,0],
[0,0,1,2,4,0],
];

echo hourglassSum($test1);
