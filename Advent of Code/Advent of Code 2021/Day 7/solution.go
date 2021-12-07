package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strconv"
	"strings"
)

func CalculateFuel(crabs []int, constantRate bool) int {
	minimumFuel := math.MaxInt32

	for a := 0; a < crabs[len(crabs)-1]; a++ {
		fuelTotal := 0

		for _, b := range crabs {
			fuel := 0

			if a < b {
				fuel = b - a
			} else {
				fuel = a - b
			}

			if !constantRate {
				fuel = fuel * (fuel + 1) / 2
			}

			fuelTotal += fuel
		}

		if fuelTotal < minimumFuel {
			minimumFuel = fuelTotal
		}
	}

	return minimumFuel
}

func PartOne(crabs []int) int {
	return CalculateFuel(crabs, true)
}

func PartTwo(crabs []int) int {
	return CalculateFuel(crabs, false)
}

func main() {
	input, _ := ioutil.ReadFile("input.txt")
	crabs := []int{}

	for _, s := range strings.Split(string(input), ",") {
		crab, _ := strconv.Atoi(s)

		crabs = append(crabs, crab)
	}

	sort.Ints(crabs)

	fmt.Printf("Part 1: %d\n", PartOne(crabs))
	fmt.Printf("Part 2: %d\n", PartTwo(crabs))
}
