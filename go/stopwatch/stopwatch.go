package main

import (
	"fmt"
)

func main() {
	var n int
	var time int
	var sum int

	fmt.Scanln(&n)

	lastTime := 0
	for i := 0; i < n; i++ {
		fmt.Scanln(&time)

		if (i + 1) % 2 == 0 {
			sum += time - lastTime
		}

		lastTime = time
	}

	if n % 2 == 0 {
		fmt.Println(sum)
	} else {
		fmt.Println("still running")
	}
	
}
