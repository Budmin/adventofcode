package advent2015

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// calculates the square feet of wrapping you need
func calculateWrapping(l int, w int, h int) int {

	side1 := (l * w)

	// used to calculate extra paper
	smallestSideSqFt := side1

	side2 := (w * h)

	if smallestSideSqFt > side2 {
		smallestSideSqFt = side2
	}

	side3 := (h * l)

	if smallestSideSqFt > side3 {
		smallestSideSqFt = side3
	}

	surfaceArea := 2*side1 + 2*side2 + 2*side3

	return surfaceArea + smallestSideSqFt
}

func calculateRibbon(l int, w int, h int) int {

	dimensions := []int{l, w, h}

	sort.Ints(dimensions)

	ribbon := 2*dimensions[0] + 2*dimensions[1]

	bow := l * w * h

	return ribbon + bow
}

func IWasToldThereWouldBeNoMath() {

	totalWrappingSqFt := 0
	totalRibbonFt := 0

	// path hardcoded and janky. but who cares
	readFile, err := os.Open("./advent2015/2input.txt")

	if err != nil {
		fmt.Println(err)
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)

	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {

		dimensions := fileScanner.Text()

		// parse string of dimensions
		split := strings.Split(dimensions, "x")

		// there should never be an issue that would cause this, but just in case
		if len(split) != 3 {
			panic("split isn't 3 values: " + dimensions)
		}

		l, lErr := strconv.Atoi(split[0])
		w, wErr := strconv.Atoi(split[1])
		h, hErr := strconv.Atoi(split[2])

		if lErr != nil || wErr != nil || hErr != nil {
			fmt.Printf("%v %v %v\n", lErr, wErr, hErr)
			panic("couldn't parse dimenisons into numbers")
		}

		totalWrappingSqFt += calculateWrapping(l, w, h)
		totalRibbonFt += calculateRibbon(l, w, h)

	}

	fmt.Println("Total wrapping paper needed:", fmt.Sprint(totalWrappingSqFt), "sqft")
	fmt.Println("Total ribbon needed:", fmt.Sprint(totalRibbonFt), "ft")

}
