read expression

printf "%.*f\n" 3 $(bc <<< "scale = 4; $expression")

