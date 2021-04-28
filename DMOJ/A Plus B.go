package main

import "fmt"

func main() {
    var n, a, b int

    fmt.Scanf("%d", &n)

    for i := 0; i < n; i++ {
        fmt.Scanf("%d %d", &a, &b)
        fmt.Println(a + b)
    }
}
