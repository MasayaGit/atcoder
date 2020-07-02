package main

import (
	"bufio"
	"fmt"
	"os"
)

func solve(n int64, str string) string {
	n--
	m := n % 26
	str = string(rune('a' + m)) + str 
	n /= 26
	if n <= 0 {
		return str
	}
    return solve(n,str)
}

func main() {
	r := bufio.NewReader(os.Stdin)
	var n int64
	fmt.Fscan(r, &n)
	str := ""
	str = solve(n,str)
	fmt.Println(str)
}
