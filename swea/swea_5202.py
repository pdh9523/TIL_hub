for idx in range(int(input())):
    schedule = [tuple(map(int,input().split())) for _ in range(int(input()))]
    schedule.sort(key = lambda x: (x[1],x[0]))      # 뒷 타임 기준으로 정렬

    end = 0
    cnt = 0
    for st,en in schedule:                  # 시작, 끝 언패킹 후 순회
        if st >= end :                      # 시작이 전타임의 끝과 비교해서 더 크거나 같으면
            end = en                        # end를 다시 설정하고
            cnt += 1                        # cnt + 1
    print(f"#{idx+1} {cnt}")                