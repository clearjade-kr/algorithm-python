package main

import "fmt"

func containsDuplicate(nums []int) bool {
	seen := map[int]bool{}
	for _, v := range nums {
		if seen[v] {
			return true
		}
		seen[v] = true
	}
	return false
}

func main() {
	fmt.Println(containsDuplicate([]int{1, 2, 3, 1}))
	fmt.Println(containsDuplicate([]int{1, 2, 3, 4}))
}
