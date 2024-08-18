package com.example.springboot_practice.service;

import com.example.springboot_practice.dto.BoardDTO;
import com.example.springboot_practice.entity.BoardEntity;
import com.example.springboot_practice.repository.BoardRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

// DTO -> Entity (Entity 에서)
// Entity -> DTO (DTO 에서)
// entity 클래스는 db와 연관이 있기 때문에 최대한 서비스 클래스 까지만 사용할 것
// 그래서 서비스 클래스에서 변환 과정이 많이 사용됨

@Service
@RequiredArgsConstructor
public class BoardService {
    private final BoardRepository boardRepository;

    public void save(BoardDTO boardDTO) {
        BoardEntity boardEntity = BoardEntity.toSaveEntity(boardDTO);
        boardRepository.save(boardEntity);
    }
}
