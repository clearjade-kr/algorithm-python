package main

import "testing"

func TestTwoSum(t *testing.T) {
	cases := []struct {
		nums   []int
		target int
		want   []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for _, tc := range cases {
		got := twoSum(tc.nums, tc.target)
		if len(got) != len(tc.want) {
			t.Fatalf("twoSum(%v, %d) = %v; want %v", tc.nums, tc.target, got, tc.want)
		}
		for i := range got {
			if got[i] != tc.want[i] {
				t.Fatalf("twoSum(%v, %d) = %v; want %v", tc.nums, tc.target, got, tc.want)
			}
		}
	}
}
