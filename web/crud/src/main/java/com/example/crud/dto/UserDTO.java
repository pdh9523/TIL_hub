package com.example.crud.dto;

import lombok.*;

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class UserDTO {
    private String email;
    private String password;
    private String nickname;
}
