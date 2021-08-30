package main

import "fmt"

func main() {
    var a0, a1, a2, m int

    fmt.Scanf("%d\n%d\n%d", &a0, &a1, &a2)

    if (a0 > a1 && a0 < a2) || (a0 < a1 && a0 > a2) {
        m = a0
    } else if (a1 > a0 && a1 < a2) || (a1 < a0 && a1 > a2) {
        m = a1
    } else if (a2 > a0 && a2 < a1) || (a2 < a0 && a2 > a1) {
        m = a2
    }

    fmt.Println(m)
}
