package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

/**　indexを返す
func index(slice []int, number int) int{
	for i, value := range slice {
		if value == number {
			return i
		}
	}
	return -1
}
**/

//b11.txt通っていない　よくわからない.
func main() {
	r := bufio.NewReader(os.Stdin)
	var x, n int
	fmt.Fscan(r, &x, &n)

	if n == 0{
		fmt.Println(x)
		os.Exit(0)
	}

	p := make([]int, n)
	for i := 0; i < n; i++ {
		var tmp int
		fmt.Fscan(r, &tmp)
		p[i] = tmp
	}

	sort.Ints(p)
	//x_index := index(p, x)
	var up_x int
	var up_i int
	//上を探す
	for i := 0; i < n; i++ {
		if i == n-1 {
			up_x = p[i] + 1
			up_i = i
			break
		}
		if p[i] >= x{
			if p[i+1] - p[i] > 1{
				up_x = p[i] + 1
				up_i = i
				break
			}
		}
	}
	//下を探す
	var down_x int
	for i := up_i; i >= 0; i-- {
		if i == 0 {
			down_x = p[i] - 1
			break
		}
		if p[i] <=  x{
			if  p[i] - p[i-1] > 1{
				down_x = p[i] - 1
				break
			}
		}
	}
	up_sabun := up_x - x
	down_sabun := x - down_x
	if up_sabun < down_sabun{
		fmt.Println(up_x)
	}else if up_sabun > down_sabun{
		fmt.Println(down_x)
	}else {
		fmt.Println(down_x)
	}
}
