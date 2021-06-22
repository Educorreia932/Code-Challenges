read n1
read n2

if (( $n1 > $n2 ));
then
    echo X is greater than Y 
elif (( $n1 < $n2 ));
then
    echo X is less than Y 
else
    echo X is equal to Y 
fi



