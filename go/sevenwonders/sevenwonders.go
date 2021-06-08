package main

import (
	"fmt"
	"math"
)

func main() {
	var cards string

	fmt.Scanln(&cards)

	cardsMap := map[string]int{
		"T": 0,
		"C": 0,
		"G": 0,
	}

	for _, r := range cards {
		cardsMap[string(r)] += 1
	}

	min := cardsMap["T"]
	score := 0
	for _, v := range cardsMap {
		if v < min {
			min = v
		}

		score += int(math.Pow(float64(v), 2))
	}

	fmt.Println(score + min * 7)
}