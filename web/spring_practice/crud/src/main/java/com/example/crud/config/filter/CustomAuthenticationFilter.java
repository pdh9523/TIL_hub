package com.example.crud.config.filter;

import com.example.crud.dto.UserDTO;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

// 진짜 아무생각없이 Authentication 같은거
// 바로바로 import 하면 이상한거 import 돼서 꼬일 수 있습니다 조심하세요

@Slf4j
public class CustomAuthenticationFilter extends UsernamePasswordAuthenticationFilter {

    public CustomAuthenticationFilter(AuthenticationManager authenticationManager) {
        super(authenticationManager);
    }

    /**
     * 이 메서드는 사용자가 로그인을 시도할 때 호출됩니다.
     * HTTP요청에서 사용자 이름과 비밀번호를 추출하여 UsernamePasswordAuthenticationToken 객체를 생성하고,
     * 이를 AuthenticationManager에 전달하여 인증을 시도합니다.
     *
     * @param request from which to extract parameters and perform the authentication
     * @param response the response, which may be needed if the implementation has to do a
     * redirect as part of a multi-stage authentication process (such as OIDC).
     * @return
     * @throws AuthenticationException
     */
    @Override
    public Authentication attemptAuthentication(
            HttpServletRequest request,
            HttpServletResponse response
    ) throws AuthenticationException {

        UsernamePasswordAuthenticationToken authRequest;

        try {
            authRequest = getAuthRequest(request);
            setDetails(request, authRequest);
        } catch (Exception e) {
            throw new ProfileApplicationException(ErrorCode.BUSINESS_EXCEPTION_ERROR);
        }

        // Authentication 객체를 반환한다.
        return this.getAuthenticationManager().authenticate(authRequest);
    }


    /**
     * 이 메서드는 HTTP 요청에서 사용자 이름과 비밀번호를 추출하여
     * UsernamePasswordAuthenticationToken 객체를 생성하는 역할을 한다.
     * HTTP 요청의 입력 스트림에서 JSON 형태의 사용자 이름과 비밀번호를 읽어 UserDTO 객체를 생성하고,
     * 이를 기반으로 UsernamePasswordAuthenticationToken 객체를 생성한다.
     * @param request
     * @throws Exception
     */
    private UsernamePasswordAuthenticationToken getAuthRequest(
            HttpServletRequest request
    ) throws Exception {

        try{
            ObjectMapper objectMapper = new ObjectMapper();
            objectMapper.registerModule(new JavaTimeModule());
            objectMapper.configure(JsonParser.Feature.AUTO_CLOSE_SOURCE, true);

            UserDTO userDTO = objectMapper.readValue(request.getInputStream(), UserDTO.class);

            log.debug("1.CustomAuthenticationFilter :: loginId: " + userDTO.email() + "userPw: " + userDTO.password());

            return new UsernamePasswordAuthenticationToken(userDTO.email(), userDTO.password());
        } catch (UsernameNotFoundException e) {
            throw new UsernameNotFoundException(e.getMessage());
        } catch (Exception e) {
            throw new ProfileApplicationExcpetion(ErrorCode.IO_ERROR);
        }
    }
}
