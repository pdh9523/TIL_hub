def count_subsets_with_sum(nums, target_sum, current_sum, index, subset_size):
    # Base case: subset size is reached
    if subset_size == 0:
        # If current sum is equal to target sum, return 1; otherwise, return 0
        return 1 if current_sum == target_sum else 0
    
    # Base case: index reaches the end of the array
    if index == len(nums):
        return 0
    
    # Include the current element in the subset and move to the next element
    count_include = count_subsets_with_sum(nums, target_sum, current_sum + nums[index], index + 1, subset_size - 1)
    
    # Exclude the current element from the subset and move to the next element
    count_exclude = count_subsets_with_sum(nums, target_sum, current_sum, index + 1, subset_size)
    
    # Return the sum of counts
    return count_include + count_exclude

def main():
    # 입력 받기
    T = int(input())  # 테스트 케이스 개수

    for test_case in range(1, T + 1):
        N, K = map(int, input().split())  # 부분집합 원소의 수 N과 부분집합의 합 K
        nums = list(range(1, 13))  # 1부터 12까지의 숫자로 구성된 집합 A

        # 부분집합의 개수 계산
        result = count_subsets_with_sum(nums, K, 0, 0, N)

        # 결과 출력
        print("#{} {}".format(test_case, result))

if __name__ == "__main__":
    main()