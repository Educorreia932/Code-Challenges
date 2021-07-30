tr -s ' ' '\n' < words.txt |
    sort |
    uniq -c |
    sort -r |
    awk '{print $2, $1}'
