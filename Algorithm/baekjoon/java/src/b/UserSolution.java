package b;

import java.util.*;

class UserSolution {

    static class Student {
        int id;
        int grade;
        String gender;
        int score;

        public Student(int id, int grade, String gender, int score) {
            this.id = id;
            this.grade = grade;
            this.gender = gender;
            this.score = score;
        }
    }

    // 학년과 성별 조합을 키로 생성
    private String getKey(int grade, String gender) {
        return grade + "-" + gender;
    }

    // 학생 id : 학생
    static HashMap<Integer, Student> studentMap;
    // 학년-성별 : { 점수 : { ID- treeSet } }
    static HashMap<String, TreeMap<Integer, TreeSet<Integer>>> gradeGenderMap;

    public void init() {
        studentMap = new HashMap<>();
        gradeGenderMap = new HashMap<>();
    }

    public int add(int mId, int mGrade, char mGender[], int mScore) {
        String gender = String.valueOf(mGender);
        String key = getKey(mGrade, gender);

        Student student = new Student(mId, mGrade, gender, mScore);
        studentMap.put(mId, student);

        // 학생 - 성별 그룹을 TreeMap에서 따로 처리
        gradeGenderMap.putIfAbsent(key, new TreeMap<>());

        TreeMap<Integer, TreeSet<Integer>> scoreMap = gradeGenderMap.get(key);
        scoreMap.putIfAbsent(mScore, new TreeSet<>());
        scoreMap.get(mScore).add(mId);

        return scoreMap.lastEntry().getValue().last();
    }

    public int remove(int mId) {
        if (!studentMap.containsKey(mId)) return 0;
        // 지우기
        Student student = studentMap.remove(mId);
        String key = getKey(student.grade, student.gender);

        TreeMap<Integer, TreeSet<Integer>> scoreMap = gradeGenderMap.get(key);
        scoreMap.get(student.score).remove(mId);

        if (scoreMap.get(student.score).isEmpty()) {
            scoreMap.remove(student.score);
        }

        if (scoreMap.isEmpty()) return 0;
        return scoreMap.firstEntry().getValue().first();
    }

    public int query(int mGradeCnt, int mGrade[], int mGenderCnt, char mGender[][], int mScore) {
        Integer resultId = Integer.MAX_VALUE;
        int minScore = Integer.MAX_VALUE;

        for (int i = 0; i < mGradeCnt; i++) {
            for (int j = 0; j < mGenderCnt; j++) {
                String key = getKey(mGrade[i], String.valueOf(mGender[j]));

                if (!gradeGenderMap.containsKey(key)) continue;

                TreeMap<Integer, TreeSet<Integer>> scoreMap = gradeGenderMap.get(key);
                // tailMap에서 mScore 이상인 점수들만 가져옴
                // NavigableMap: 확장된 Map으로, Key를 기준으로 오름차순 정렬된 순서를 유지하며, 탐색 관련해서 강화된 맵이다.
                NavigableMap<Integer, TreeSet<Integer>> filteredMap = scoreMap.tailMap(mScore, true);

                // 이미 최소 점수보다 큰 점수들은 건너뜀
                if (filteredMap.isEmpty()) continue;

                for (Map.Entry<Integer, TreeSet<Integer>> entry : filteredMap.entrySet()) {
                    int score = entry.getKey();

                    // 최소 점수를 넘어가면 더 이상 검사할 필요 없음 (Early stopping)
                    if (score > minScore) break;

                    TreeSet<Integer> ids = entry.getValue();
                    Integer candidateId = ids.first();

                    if (score < minScore) {
                        minScore = score;
                        resultId = candidateId;
                    } else if (score == minScore) {
                        resultId = Math.min(resultId, candidateId);
                    }
                }
            }
        }
        return resultId == Integer.MAX_VALUE ? 0 : resultId;
    }
}