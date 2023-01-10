package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func checkBorder(position [2]int, size int) bool {
	var x int = position[0]
	var y int = position[1]
	return x == 0 || y == 0 || x == size-1 || y == size-1
}

func display(size int, playerPosition [2]int) {
	var output string = ""
	for y := 0; y < size; y++ {
		for x := 0; x < size; x++ {
			if [2]int{x, y} == playerPosition {
				output += "@"
			} else if checkBorder([2]int{x, y}, size) {
				output += "#"
			} else {
				output += " "
			}

			output += " "
		}
		output += "\n"
	}

	fmt.Print(output)
}

func doAction(input string, playerPosition [2]int, size int) [2]int {
	var newPlayerPosition = playerPosition

	switch input {
	case "w":
		newPlayerPosition[1] -= 1

	case "s":
		newPlayerPosition[1] += 1

	case "d":
		newPlayerPosition[0] += 1

	case "a":
		newPlayerPosition[0] -= 1

	case "q":
		os.Exit(1)

	case "die":
		os.Exit(1)
	}

	if !checkBorder(newPlayerPosition, size) {
		playerPosition = newPlayerPosition
	}

	return playerPosition
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	var size int = 10
	playerPosition := [2]int{2, 2}

	for {
		display(size, playerPosition)
		input, _ := reader.ReadString('\n')
		input = strings.Replace(input, "\n", "", -1)

		playerPosition = doAction(input, playerPosition, size)
	}
}
