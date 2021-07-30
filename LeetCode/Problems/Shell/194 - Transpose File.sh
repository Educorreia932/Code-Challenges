n_cols=$(head -n 1 file.txt | awk '{printf NF}')

for ((i = 1; i <= n_cols; i++)); do
    echo $(cut -d " " -f $i file.txt)
done
