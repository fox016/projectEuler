<?php

/*
 * Complete the 'twoStacks' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER maxSum
 *  2. INTEGER_ARRAY a
 *  3. INTEGER_ARRAY b
 */

function twoStacks($maxSum, $a, $b)
{
  // First row
  $value = 0;
  $posX = 0;
  $posY = 0;
  foreach($a as $i=>$n) {
    $next = $n + $value;
    if($next > $maxSum)
      break;
    $value = $next;
    $posX = $i+1;
  }
  $largestDist = $posX + $posY;

  // Climb up the staircase (up and left)
  $maxY = count($b);
  // While within left and top boundaries
  while($posX > -1 && $posY < $maxY) {
    // Climb up until value is too large
    $posY++;
    $value = $b[$posY-1] + $value;
    if($value <= $maxSum) {
      if($posX + $posY > $largestDist) {
        $largestDist = $posX + $posY; 
      }
    }
    else {
      // Go left until value is back in range
      while($value > $maxSum) {
        $posX--;
        if($posX < 0)
          break;
        $value = $value - $a[$posX];
      }
      if($posX + $posY > $largestDist) {
        $largestDist = $posX + $posY; 
      }
    }
  }

  return $largestDist;
}

$infile = fopen("./two_stack_in1.txt", "r");
$g = intval(trim(fgets($infile)));

for ($g_itr = 0; $g_itr < $g; $g_itr++) {
    $first_multiple_input = explode(' ', rtrim(fgets($infile)));

    $n = intval($first_multiple_input[0]);

    $m = intval($first_multiple_input[1]);

    $maxSum = intval($first_multiple_input[2]);

    $a_temp = rtrim(fgets($infile));

    $a = array_map('intval', preg_split('/ /', $a_temp, -1, PREG_SPLIT_NO_EMPTY));

    $b_temp = rtrim(fgets($infile));

    $b = array_map('intval', preg_split('/ /', $b_temp, -1, PREG_SPLIT_NO_EMPTY));

    $result = twoStacks($maxSum, $a, $b);

    echo $result . "\n";
}
fclose($infile);
