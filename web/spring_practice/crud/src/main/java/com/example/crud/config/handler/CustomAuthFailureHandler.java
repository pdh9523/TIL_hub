package com.example.crud.config.handler;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.json.JSONObject;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.*;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.web.authentication.AuthenticationFailureHandler;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;

@Slf4j
@Configuration
@Component
public class CustomAuthFailureHandler implements AuthenticationFailureHandler {

    /**
     * 이 메서드는 HTTP 요청과 응답, 그리고 인증 예외를 인자로 받아 예외 타입에 따라 실패 메시지를 정하고, 클라이언트에 응답한다.
     * @param request the request during which the authentication attempt occurred.
     * @param response the response.
     * @param e the exception which was thrown to reject the authentication
     * request.
     * @throws IOException
     * @throws ServletException
     */
    @Override
    public void onAuthenticationFailure(
            HttpServletRequest request,
            HttpServletResponse response,
            AuthenticationException e
    ) throws IOException, ServletException {
        JSONObject jsonObject = new JSONObject();
        String failMessage = "";

        if (e instanceof AuthenticationServiceException) {
            failMessage = "로그인 정보가 일치하지 않습니다.";
        } else if (e instanceof LockedException) {
            failMessage = "계정이 잠겨있습니다.";
        } else if (e instanceof DisabledException) {
            failMessage = "계정이 비활성화되어 있습니다.";
        } else if (e instanceof AccountExpiredException) {
            failMessage = "계정이 만료되었습니다.";
        } else if (e instanceof CredentialsExpiredException) {
            failMessage = "인증 정보가 만료되었습니다.";
        }

        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json");

        try (PrintWriter out = response.getWriter()) {
            log.debug(failMessage);

            HashMap<String, Object> resultMap = new HashMap<>();
            resultMap.put("userInfo", null);
            resultMap.put("resultCode", 9999);
            resultMap.put("failMessage", failMessage);
            jsonObject = new JSONObject(resultMap);

            out.print(jsonObject);
            out.flush();
        }
    }


}
