read N

sum=0

for (( i = 0; i <= $N; i++ )) 
do
    read n
    sum=$(( sum + n )) 
done

printf "%.*f\n" 3 $(bc <<< "scale = 3; $sum / $N")

