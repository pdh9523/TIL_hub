package com.example.crud.config.handler;

import com.example.crud.config.jwt.TokenUtils;
import com.example.crud.dto.UserDTO;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.Authentication;
import org.springframework.security.web.authentication.SavedRequestAwareAuthenticationSuccessHandler;
import org.json.JSONObject;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Objects;

@Slf4j
@RequiredArgsConstructor
@Component
public class CustomAuthSuccessHandler extends SavedRequestAwareAuthenticationSuccessHandler {

    @Override
    public void onAuthenticationSuccess(
            HttpServletRequest request,
            HttpServletResponse response,
            Authentication authentication
    ) throws IOException, ServletException {
        log.debug("onAuthenticationSuccess");
        // 1. 사용자와 관련된 정보를 모두 조회한다.
        UserDTO userDTO = ((SecurityUserDetailsDTO) authentication.getPrincipal().getUserDTO());


        // 2. 조회한 데이터를 Json Object 형태로 파싱한다.
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.registerModule(new JavaTimeModule());
        JSONObject userDTOObject = new JSONObject(objectMapper.writeValueAsString(userDTO));

        HashMap<String, Object> responseMap = new HashMap<>();
        JSONObject jsonObject;

        // TODO: BANNED에 대한 응답도 만들어보기
        // 3-1. 사용자의 상태가 '휴먼 상태'인 경우 응답값으로 전달할 데이터
        if (Objects.equals(userDTO.userStatus(), "D")) {
            responseMap.put("userInfo", userDTOObject);
            responseMap.put("resultCode", 9001);
            responseMap.put("token", null);
            responseMap.put("failMessage", "휴면 계정입니다.");
            jsonObject = new JSONObject(responseMap);
        }
        // 3-2. 사용자의 상태가 '휴먼 상태'가 아닌 경우 응답값으로 전달할 데이터
        else {
            // 1. 일반 계정일 경우 데이터 세팅
            responseMap.put("userInfo", userDTOObject);
            responseMap.put("resultCode", 200);
            responseMap.put("failMessage", null);
            jsonObject = new JSONObject(responseMap);

            // JWT 토큰 생성
            String token = TokenUtils.generateJwtToken(userDTO);
            responseMap.put("token", token);

            // 쿠키에 JWT 토큰 저장
            Cookie jwtCookie = new Cookie("jwt", token);
            jwtCookie.setHttpOnly(true);                        // JS에서 쿠키에 접근할 수 없도록 설정
            jwtCookie.setPath("/");                             // 모든 경로에서 쿠키에 접근 가능하도록 설정
            response.addCookie(jwtCookie);                      // 응답에 쿠키 추가
        }

        // 응답에 대한 구성값 설정
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json");

        // 슛
        try (PrintWriter out = response.getWriter()) {
            out.print(jsonObject);
            out.flush();
        }

    }
}
