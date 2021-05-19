package main

import "fmt"

func main() {
    var antenna, eyes int

    fmt.Scanf("%d\n%d", &antenna, &eyes)
 
    if antenna >= 3 && eyes <= 4 {
        fmt.Println("TroyMartian")
    }

    if antenna >= 6 && eyes >= 2 {
        fmt.Println("VladSaturnian")
    }

    if antenna <= 2 && eyes <= 3 {
        fmt.Println("VladSaturnian")
    }
}
