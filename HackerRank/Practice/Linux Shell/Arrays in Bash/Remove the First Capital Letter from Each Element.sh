while read country
do
    countries=("${countries[@]}" $country)
done

for country in ${countries[@]}
do
    result=("${result[@]}" .${country:1})
done

echo ${result[@]}

