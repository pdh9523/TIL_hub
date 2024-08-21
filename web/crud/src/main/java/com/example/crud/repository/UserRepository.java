package com.example.crud.repository;

import com.example.crud.entity.Role;
import com.example.crud.entity.UserEntity;
import io.micrometer.common.lang.Nullable;
import lombok.NonNull;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
import org.springframework.data.jpa.domain.Specification;

import java.util.List;
import java.util.Optional;

public interface UserRepository extends JpaRepository<UserEntity, Long>, JpaSpecificationExecutor<UserEntity> {



    /**
    * @param email 조회할 이메일
    * @return 조회한 유저
     **/
    Optional<UserEntity> findByEmail(String email);

    /**
    * @param nickname 조회할 닉네임
    * @return 조회한 유저
     **/
    Optional<UserEntity> findByNickname(String nickname);

    /**
    * @param email 조회할 이메일
    * @param password 조회할 비밀번호
    * @return 해당 이메일과 비밀번호를 가진 사용자 목록
     **/
    Optional<UserEntity> findByEmailAndPassword(String email, String password);

    /**
     * @param role 제외할 역할 (ADMIN or BANNED)
     * @return 제외한 역할 외의 사용자 목록
     **/
    List<UserEntity> findByRoleNot(Role role);

    /**
     * 명시적으로 작성해둡니다.
     * JpaRepository 있어서 굳이 만들 필요는 없습니다.
     * @param userEntity 입력한 유저
     * @return 저장 (회원가입)
     **/
    default UserEntity createUser(UserEntity userEntity) {
        return save(userEntity);
    }

    @Override
    @NonNull
    List<UserEntity> findAll(@Nullable Specification<UserEntity> spec);
}
