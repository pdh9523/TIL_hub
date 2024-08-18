package com.example.springboot_practice.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    // 해당 주소로 매핑이 되면
    @GetMapping("/")
    // 함수가 실행되고, 값을 반환
    public String home() {
        return "home";
    }
}
