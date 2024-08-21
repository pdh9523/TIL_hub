package com.example.crud.service;

import com.example.crud.dto.UserDTO;
import com.example.crud.dto.mapper.UserMapper;
import com.example.crud.entity.Role;
import com.example.crud.entity.UserEntity;
import com.example.crud.repository.UserRepository;
import com.example.crud.repository.specification.UserSpecification;
import lombok.RequiredArgsConstructor;
import org.springframework.data.jpa.domain.Specification;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private UserMapper userMapper;

    public UserDTO convertToDTO(UserEntity userEntity) {
        return userMapper.userEntityToUserDTO(userEntity);
    }

    public UserEntity convertToEntity(UserDTO userDTO) {
        return userMapper.userDTOToUserEntity(userDTO);
    }

    public UserDTO createUser(UserDTO userDTO) {
        UserEntity userEntity = convertToEntity(userDTO);
        UserEntity savedUser = userRepository.save(userEntity);
        return convertToDTO(savedUser);
    }

    public UserDTO getUser(Long userId) {
        UserEntity userEntity = userRepository.findById(userId).orElseThrow(() -> new RuntimeException("User not found"));
        return convertToDTO(userEntity);
    }

    public List<UserEntity> findUsers(String email, Role role, Boolean isDeleted) {
        Specification<UserEntity> spec = Specification.where(UserSpecification.hasEmail(email))
                .and(UserSpecification.hasRole(role))
                .and(UserSpecification.isDeleted(isDeleted));

        return userRepository.findAll(spec);
    };
}
