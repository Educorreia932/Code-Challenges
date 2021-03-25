use v6;
unit module Solution;

sub past(Int $h, Int $m, Int $s --> Int) is export {
    (($h * 60 + $m) * 60 + $s) * 1000
}
