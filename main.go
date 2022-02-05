package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
)

func main() {
	f, err := os.Open("./password.txt")
	handleErr(err)

	defer f.Close()

	scanner := bufio.NewScanner(f)

	password := ""

	for scanner.Scan() {
		password = scanner.Text()
	}

	fmt.Printf("The goal of this program is to find the following password through bruteforce dictionnay attack : %s\n\n", password)

	cpuNumber := runtime.NumCPU()

	for i := 0; i < cpuNumber; i++ {
		// Starts as many goroutines as there is threads on the device used
		go goroutine()
	}

	fmt.Println("FIRST STEP : MOST PROBABLE PASSWORDS")
	// 12 645 tests

	fmt.Println("SECOND STEP : MOST PROBABLE PASSWORDS + MIDDLE NAMES")
	// 12 645 x 3 897 = 49 277 565 tests

	fmt.Println("THIRD STEP : MOST PROBABLE PASSWORDS")

}

func goroutine() {

}

func handleErr(err error) {
	if err != nil {
		fmt.Printf("Une erreur est survenu : ")
		fmt.Println(err)
	}
}
