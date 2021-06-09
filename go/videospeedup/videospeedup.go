package main

import (
	"fmt"
	"io"
)

func main() {
	var n, p, k int
	var next int
	var timestamps []int

	fmt.Scanln(&n, &p, &k)
	
	for {
		n, err := fmt.Scanf("%d", &next)

		if err == io.EOF || n == 0 {
			break
		}

		timestamps = append(timestamps, next)
	}

	timestamps = append(timestamps, k)

	last_event := 0
	orig_length := 0.0
	multiplier := 1.0
	for i, event := range timestamps {
		orig_length += float32(event - last_event) * multiplier
		multiplier = (100 + (float64(p * (i+1)))) / 100
		last_event = event
	}

	fmt.Println(orig_length)
}