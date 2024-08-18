package com.example.springboot_practice.dto;

import java.time.LocalDateTime;

import lombok.*;

// DTO(Data Transfer Object), VO, Bean, Entity, ...
@Getter                 // get Method 를 만들어줌
@Setter                 // set Method 를 만들어줌
@ToString               // ToString()을 통해 테이블 확인을 가능하게 해줌 (선택사항)
@NoArgsConstructor      // 기본 생성자
@AllArgsConstructor     // 모든 필드를 매개변수로 하는 생성자
public class BoardDTO {
    private Long id;
    private String boardWriter;
    private String boardPass;
    private String boardContents;
    private String boardTitle;

    // 조회수
    private int boardHits;

    // 작성, 수정시간
    private LocalDateTime boardCreatedTime;
    private LocalDateTime boardUpdatedTime;
}
