package com.example.springboot_practice.controller;

import com.example.springboot_practice.dto.BoardDTO;
import com.example.springboot_practice.service.BoardService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
@RequiredArgsConstructor
@RequestMapping("/board")
public class BoardController {
    // 의존성 주입
    private final BoardService boardService;

//  이 부분을 "RequiredArgsConstructor" 가 해결해줌
//  생성자를 통해 의존성 주입
//    public BoardController(BoardService boardService) {
//        this.boardService = boardService;
//    }

    // 이런식의 Get 매핑들은 나중에 사용하지 않을거지만 일단 인강 따라가기위해서 사용
    @GetMapping("/save")
    public String saveForm() {
        return "save";
    }

    @PostMapping("/save")
    public String save(@ModelAttribute BoardDTO boardDTO) {
        System.out.println("boardDTO = " + boardDTO);
        boardService.save(boardDTO);
        return "index";
    }

    @GetMapping("/")
    public String finAll(Model model) {
        // DB에서 전체 게시글 데이터 가져와서 list.html.html에 보여준다.
        List<BoardDTO> boardDTOList = boardService.findAll();
        model.addAttribute("boardList", boardDTOList);
        return "list";
    }

    @GetMapping("/{id}")
    public String findById(@PathVariable Long id, Model model) {
        boardService.updateHits(id);
        BoardDTO boardDTO = boardService.findById(id);
        model.addAttribute("board", boardDTO);
        return "detail";
    }
}
