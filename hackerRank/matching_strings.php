<?php

function matchingStrings($stringList, $queries) {
  $counts = array();
  foreach($queries as $query) {
    $counts[] = getCount($stringList, $query);
  }
  return $counts;
}

function getCount($stringList, $query) {
  $count = 0;
  foreach($stringList as $str) {
    if($str == $query)
      $count++;
  }
  return $count;
}
