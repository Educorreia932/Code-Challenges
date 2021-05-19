package main

import "fmt"

func main() {
    var a0, a1, a2 int

    fmt.Scanf("%d\n%d\n%d", &a0, &a1, &a2)

    triangle_type := "Scalene"
    fmt.Println(a0 + a1 + a2)
    if a0 + a1 + a2 != 180 {
        triangle_type = "Error"
    } else if a0 == a1 && a1 == a2 {
        triangle_type = "Equilateral"
    } else if a0 == a1 || a1 == a2 || a0 == a2 {
        triangle_type = "Isosceles"
    }

    fmt.Println(triangle_type)
}
