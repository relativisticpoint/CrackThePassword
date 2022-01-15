package main

import (
	"fmt"
	"sync"
	"time"
)

var password int
var wg sync.WaitGroup

func main() {
	password = 9999999999
	fmt.Printf("#DEBUT DU CODE\n")
	start := time.Now()

	for i := 0; i < 10; i++ {
		go testInterval(10000000000*i, 10000000000*(i+1))
	}

	elapsed := time.Now().Sub(start)
	fmt.Printf("Temps écoulé : %v\n", elapsed)
	fmt.Printf("#FIN DU CODE\n")
}

func testInterval(from int, to int) {
	for i := from; i <= to; i++ {
		if i == password {
			fmt.Printf("Code trouvé ! C'était : %d\n", password)
			break
		}
	}
}
