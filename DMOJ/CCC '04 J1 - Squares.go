package main

import "fmt"
import "math"

func main() {
    var a int

    fmt.Scanf("%d", &a)

    s := int(math.Sqrt(float64(a)))

    fmt.Printf("The largest square has side length %d.\n", s)
}

