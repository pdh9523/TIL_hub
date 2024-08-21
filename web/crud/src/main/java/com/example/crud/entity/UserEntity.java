package com.example.crud.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.time.LocalDateTime;

import static jakarta.persistence.EnumType.STRING;

@Entity
@Getter
@Setter
@Table(name = "user")
@ToString
public class UserEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String password;
    private String nickname;
    @Column(updatable = false, nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();

    @Enumerated(STRING)
    private Role role;

    private Boolean isDeleted = false;
}
