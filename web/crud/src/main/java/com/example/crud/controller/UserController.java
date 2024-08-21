package com.example.crud.controller;

import com.example.crud.dto.UserDTO;
import com.example.crud.entity.Role;
import com.example.crud.entity.UserEntity;
import com.example.crud.service.UserService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@RequestMapping("/user")
public class UserController {

    private UserService userService;

    @PostMapping("/signin")
    public ResponseEntity<UserDTO> createUser(@RequestBody UserDTO userDTO) {
        UserDTO createdUser = userService.createUser(userDTO);
        return ResponseEntity.ok(createdUser);
    }

    @GetMapping("/{userId}")
    public ResponseEntity<UserDTO> getUser(@PathVariable Long userId) {
        UserDTO userDTO = userService.getUser(userId);
        return ResponseEntity.ok(userDTO);
    }

    @GetMapping("/search")
    public ResponseEntity<List<UserEntity>> searchUsers(
            @RequestParam(required = false) String email,
            @RequestParam(required = false) Role role,
            @RequestParam(required = false) Boolean isDeleted) {
        List<UserEntity> users = userService.findUsers(email, role, isDeleted);

        if (users.isEmpty()) {
            return new ResponseEntity<>(HttpStatus.NO_CONTENT);
        }
        return new ResponseEntity<>(users, HttpStatus.OK);
    }
}
