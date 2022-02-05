package main

import (
	"bufio"
	"fmt"
	"os"
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

	fmt.Println(password)

}

func handleErr(err error) {
	if err != nil {
		fmt.Printf("Une erreur est survenu : ")
		fmt.Println(err)
	}
}
