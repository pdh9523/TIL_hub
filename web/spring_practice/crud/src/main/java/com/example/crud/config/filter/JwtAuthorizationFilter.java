package com.example.crud.config.filter;

import com.example.crud.config.jwt.TokenUtils;

import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.JwtException;
import jakarta.annotation.Nonnull;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.NonNull;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.json.JSONObject;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.io.PrintWriter;
import java.security.SignatureException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;


/* JwtAuthorizationFilter 는 클라이언트의 요청이 서버의 리소스에 도달하기 전에 JWT 토큰의 유효성을 검사하고,
* 해당 토큰을 기반으로 사용자를 인증하는 역할을 수행한다.
* 유효하지 않은 토큰 또는 인증되지 않은 요청의 경우, 적절한 오류 응답을 클라이언트에 반환하여 요청을 거부한다.
*/

@Slf4j
@RequiredArgsConstructor
// OncePerRequestFilter를 상속받아 요청당 한 번만 이 필터가 실행되도록 한다.
public class JwtAuthorizationFilter extends OncePerRequestFilter {
    // 의존성 주입
    private final UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            @NonNull HttpServletResponse response,
            @Nonnull FilterChain filterChain
    ) throws ServletException, IOException {
        // 여기는 토큰이 필요하지 않은 API URL의 리스트
        List<String> list = Arrays.asList(
                "/user/login",
                "/login",
                "/css/**",
                "/js/**",
                "/images/**"
        );

        // 토큰이 필요하지 않은 API의 경우 로직 처리 없이 다음 필터로 이동한다.
        if (list.contains(request.getRequestURI())) {
            filterChain.doFilter(request, response);
            return;
        }

        // 그 외, 토큰이 필요한 경우

        // 1. Client에서 API를 요청할 때 쿠키를 확인한다.
        Cookie[] cookies = request.getCookies();
        String token = null;
        if (cookies != null) {
            for (Cookie cookie: cookies) {
                if ("jwt".equals(cookie.getName())) {
                    token = cookie.getValue();
                    break;
                }
            }
        }
        // 2. 토큰의 유효성을 확인한다.
        try {
            // 2-1. 쿠키내에 토큰이 존재하는지
            if (token != null && !token.equalsIgnoreCase("")) {

                // 2-2. 토큰이 유효한지
                if (TokenUtils.isValidToken(token)) {
                    // 토큰이 유효하다면, 추출한 토큰을 기반으로 사용자 아이디를 반환한다.
                    String loginId = TokenUtils.getUserIdFromToken(token);

                    // 2-3. 사용자 아이디가 존재하는지
                    if (loginId != null && !loginId.equalsIgnoreCase("")) {
                        UserDetails userDetails = userDetailsService.loadUserByUsername(loginId);
                        UsernamePasswordAuthenticationToken authentication = new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                        filterChain.doFilter(request, response);
                    }
                    // 2-4. 사용자 아이디가 존재하지 않는다면
                    else {
                        throw new ProfileApplicationException(ErrorCode.USER_NOT_FOUND);
                    }
                }
                // 2-5. 토큰이 유효하지 않다면
                else {
                    throw new ProfileApplicationException(ErrorCode.TOKEN_NOT_VALID);
                }
            }
            // 2-6. 토큰이 존재하지 않는다면
            else {
                throw new ProfileApplicationException(ErrorCode.TOKEN_NOT_FOUND);
            }
        } catch (Exception e) {
            // 로그 메시지 생성
            String logMessage = jsonResponseWrapper(e).getString("message");
            log.error(logMessage, e);

            // 클라이언트에게 전송할 메시지
            response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            response.setCharacterEncoding("UTF-8");
            response.setContentType("application/json");

            PrintWriter writer = response.getWriter();
            JSONObject jsonObject = new JSONObject();
            jsonObject.put("error", true);
            jsonObject.put("message", "로그인 에러");

            writer.print(jsonObject);
            writer.flush();
            writer.close();
        }
    }

    /**
     * 토큰 관련 Exception 발생 시 예외 응답값을 반환한다.
     * @param e 오류 메시지
     * @return 예외 응답값
     */
    private JSONObject jsonResponseWrapper(Exception e) {
        String resultMessage = "";

        if (e instanceof ExpiredJwtException) {
            resultMessage = "TOKEN_EXPIRED";
        } else if (e instanceof SignatureException) {
            resultMessage = "TOKEN_SIGNATURE_EXCEPTION_LOGIN";
        } else if (e instanceof JwtException) {
            resultMessage = "TOKEN_PARSING_JWT_EXCEPTION";
        } else {
            resultMessage = "OTHER_TOKEN_ERROR";
        }

        HashMap<String, Object> jsonMap = new HashMap<>();
        jsonMap.put("status", 401);
        jsonMap.put("code", "9999");
        jsonMap.put("message", resultMessage);
        jsonMap.put("reason", e.getMessage());
        JSONObject jsonObject = new JSONObject(jsonMap);
        log.error(resultMessage, e);
        return jsonObject;
    }
}
