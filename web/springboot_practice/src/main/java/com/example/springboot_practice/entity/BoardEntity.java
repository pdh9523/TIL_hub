package com.example.springboot_practice.entity;


import com.example.springboot_practice.dto.BoardDTO;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

// DB의 테이블 역할을 하는 클래스
@Entity
@Getter
@Setter
@Table(name = "board_table")
public class BoardEntity extends BaseEntity {
    @Id // pk 컬럼 지정. 필수
    @GeneratedValue(strategy = GenerationType.IDENTITY) // AUTO_INCREMENT
    private Long id;

    @Column(length = 20, nullable = false) // 크기 20, NOT NULL, (unique = true) 속성도 있음
    private String boardWriter;

    @Column // 기본값: 크기 255, NULLABLE
    private String boardPass;

    @Column
    private String boardTitle;

    @Column(length = 500)
    private String boardContents;

    @Column
    private int boardHits;

    // DTO에서 온 값을 Entity로 변환하는 작업
    // builder 패턴? 찾아보기
    public static BoardEntity toSaveEntity(BoardDTO BoardDTO) {
        BoardEntity boardEntity = new BoardEntity();

        boardEntity.setBoardWriter(BoardDTO.getBoardWriter());
        boardEntity.setBoardPass(BoardDTO.getBoardPass());
        boardEntity.setBoardTitle(BoardDTO.getBoardTitle());
        boardEntity.setBoardContents(BoardDTO.getBoardContents());
        boardEntity.setBoardHits(0);

        return boardEntity;
    }
}
