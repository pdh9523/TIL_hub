package com.example.crud.repository.specification;

import com.example.crud.entity.Role;
import com.example.crud.entity.UserEntity;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Root;
import org.springframework.data.jpa.domain.Specification;

public class UserSpecification {

    public static Specification<UserEntity> hasEmail(String email) {
        return (Root<UserEntity> root, CriteriaQuery<?> query, CriteriaBuilder criteriaBuilder) -> {
            if (email == null || email.isEmpty()) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.equal(root.get("email"), email);
        };
    }

    public static Specification<UserEntity> hasRole(Role role) {
        return (Root<UserEntity> root, CriteriaQuery<?> query, CriteriaBuilder criteriaBuilder) -> {
            if (role == null) {
                return criteriaBuilder.conjunction();
            }
            return criteriaBuilder.equal(root.get("role"), role);
        };
    }

    public static Specification<UserEntity> isDeleted(Boolean isDeleted) {
        return (Root<UserEntity> root, CriteriaQuery<?> query, CriteriaBuilder criteriaBuilder) -> {
          if (isDeleted == null) {
              return criteriaBuilder.conjunction();
          }
          return criteriaBuilder.equal(root.get("isDeleted"), isDeleted);
        };
    }
}
