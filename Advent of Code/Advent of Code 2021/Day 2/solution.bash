function part_1 {
    horizontal_position=0
    depth=0

    while IFS= read -r line; do
        command="${line%% *}"
        X="${line##* }"

        case $command in
            "forward")
                let "horizontal_position+=$X"
                ;;
            "down")
                let "depth+=$X"
                ;;
            "up")
                let "depth-=$X"
                ;;
        esac
    done < "input.txt"

    echo $(($horizontal_position * $depth))
}

function part_2 {
    horizontal_position=0
    depth=0
    aim=0

    while IFS= read -r line; do
        command="${line%% *}"
        X="${line##* }"

        case $command in
            "forward")
                let "horizontal_position+=$X"
                let "depth+=$aim * $X"
                ;;
            "down")
                let "aim+=$X"
                ;;
            "up")
                let "aim-=$X"
                ;;
        esac
    done < "input.txt"

    echo $(($horizontal_position * $depth))
}

printf "Part 1: %s\n" $(part_1)
printf "Part 2: %s\n" $(part_2)
