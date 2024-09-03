package com.example.crud.config.jwt;

import com.example.crud.dto.UserDTO;
import io.jsonwebtoken.*;
import io.jsonwebtoken.security.Keys;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;
import java.security.Key;
import java.time.Duration;
import java.time.Instant;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@Slf4j
@Component
public class TokenUtils {
    private static final String jwtSecretKey = "엥?jwt?그거완전존마탱키아니냐";
    private static final Key key = Keys.hmacShaKeyFor(jwtSecretKey.getBytes(StandardCharsets.UTF_8));
    private static final String JWT_TYPE = "JWT";
    private static final String ALGORITHM = "HS256";
    private static final String LOGIN_ID = "email";
    private static final String USERNAME = "nickname";

    public static String generateJwtToken(UserDTO userDTO) {

        JwtBuilder builder = Jwts.builder()
                .setHeader(createHeader())
                .setClaims(createClaims(userDTO))
                .setSubject(String.valueOf(userDTO.email()))
                .setIssuer("profile")
                .signWith(key, SignatureAlgorithm.HS256)
                .setExpiration(createExpiredDate());

        return builder.compact();
    }

    public static boolean isValidToken(String token) {
        try {
            Claims claims = getClaimsFormToken(token);

            log.info("expired token: {}", claims.getExpiration());
            log.info("email token: {}", claims.get(LOGIN_ID));
            log.info("nickname token: {}", claims.get(USERNAME));

            return true;
        } catch (ExpiredJwtException expiredJwtException) {
            log.error("Token has expired", expiredJwtException);
            return false;
        } catch (JwtException jwtException) {
            log.error("Invalid token", jwtException);
            return false;
        } catch (NullPointerException nullPointerException) {
            log.error("Null pointer exception", nullPointerException);
            return false;
        }
    }

    private static Map<String, Object> createHeader() {
        Map<String, Object> header = new HashMap<>();

        header.put("typ", JWT_TYPE);
        header.put("alg", ALGORITHM);
        header.put("regDate", System.currentTimeMillis());
        return header;
    }

    private static Map<String, Object> createClaims(UserDTO userDTO) {
        Map<String, Object> claims = new HashMap<>();

        log.info("email token: {}", userDTO.email());
        log.info("nickname token: {}", userDTO.nickname());

        claims.put(LOGIN_ID, userDTO.email());
        claims.put(USERNAME, userDTO.nickname());
        return claims;
    }

    private static Date createExpiredDate() {
        Instant now = Instant.now();
        Instant expiryDate = now.plus(Duration.ofHours(8)); // 8시간 후 만료
        return Date.from(expiryDate);
    }

    private static Claims getClaimsFormToken(String token) {
        return Jwts.parserBuilder().setSigningKey(key)
                .build().parseClaimsJws(token).getBody();
    }

    public static String getUserIdFromToken(String token) {
        Claims claims = getClaimsFormToken(token);
        return claims.get(LOGIN_ID).toString();
    }
}
