package com.example.crud.entity;

import com.example.crud.entity.constants.Role;
import com.example.crud.entity.constants.UserStatus;
import jakarta.persistence.*;
import lombok.*;


@ToString(callSuper = true) // callSuper: 자식엔티티에서 부모가 가지고 있는 필드까지 적용시키고 싶은 경우 사용
@NoArgsConstructor(access = AccessLevel.PROTECTED) // 파라미터가 없는 디폴트 생성자를 생성
@Getter @Setter // Getter,Setter: 각 컬럼의 Get 메서드와 Set 메서드를 만들어 준다.
@Table(name = "USERS") // Table: name = 매핑할 테이블의 이름을 지정, catalog = DB의 catalog를 매핑, schema = DB의 스키마와 매핑, uniqueConstraint = DDL 쿼리를 작성할 때 제약 조건을 생성
@Entity // Entity로 선언하는 경우 그 클래스는 JPA가 관리를 하게 됨 -> final, enum, interface, class 사용 불가
public class UserEntity {

    @Id // JPA가 식별할 기본 키 pk
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    // GeneratedValue: 기본 키를 자동으로 할당한다.
    // strategy -- 자동 할당 전략
    // IDENTITY: 기본키 생성을 데이터베이스에 위임 (Mysql)
    // SEQUENCE: 시쿼스를 사용 -> 이 경우 @SequenceGenerator 필요 (Oracle)
    // TABLE: 키 생성용 테이블 사용 -> 이 경우 @TableGenerator 필요 (모든 DBMS)
    // AUTO: 데이터베이스 Dialect 에 따라 자동 지정(기본값)
    @Column(name = "id") // 객체 필드와 DB 테이블 컬럼을 매핑.
    private Long id;                                // 계정 번호 Id (pk)

    // nullable: DB에서 NULL을 허용할지, 허용하지 않을지 결정
    @Column(name = "email", nullable = false)
    private String email;                           // 이메일

    @Column(name = "password", nullable = false)
    private String password;                        // 비밀번호

    @Column(name = "nickname", nullable = false)
    private String nickname;

    @Column(name = "role", nullable = false)
    @Enumerated(EnumType.STRING)  
    // 필드에 Enum 타입을 사용하는 경우 enum 인덱스를 사용할지, 이름값을 사용할지 선택할 수 있다.
    // EnumType.ORIGINAL: enum 인덱스를 사용
    // EnumType.STRING: enum 이름값을 사용
    private Role role;                              // 권한 (ADMIN, USER, BANNED)

    @Column(name = "isDeleted", nullable = false)
    private Boolean isDeleted = false;              // 계정 정지 여부
    // 이렇게 기본값을 설정해둘 수 있다.

    @Column(name = "status", nullable = false)
    @Enumerated(EnumType.STRING)
    private UserStatus userStatus;

    @Builder
    private UserEntity(Long id, String email, String password, String nickname, Role role, Boolean isDeleted, UserStatus userStatus) {
        this.id = id;
        this.email = email;
        this.password = password;
        this.nickname = nickname;
        this.role = role;
        this.isDeleted = isDeleted;
        this.userStatus = userStatus;
    }
}
