package com.example.crud.dto;

import com.example.crud.entity.Role;

public record UserDTO(
        Long id,
        String email,
        String password,
        String nickname,
        Role role,
        Boolean isDeleted
) {
    
    // 생성자
    // factory method of
    public static UserDTO of (Long id, String email, String password, String nickname, Role role, Boolean isDeleted) {
        return new UserDTO(id, email, password, nickname, role, isDeleted);
    }  
    
    // 생성자
    // security에서 사용할 factory method
    public static UserDTO of (String email) {
        return new UserDTO(
                null, email, null,null,null,null
        );
    }
}

/* 팩토리 메서드 패턴이란?
 *
 * 객체 생성을 추상화하고 캡슐화하는 디자인 패턴
 * 스프링에서 이 패턴은 BeanFactory와 ApplcationContext를 통해 구현된다.
 * 객체를 직접 생성하는 대신, 팩토리를 통해 객체를 요청하면,
 * 이 팩토리가 객체 생성의 복잡성을 숨기고 필요한 객체를 제공한다.
 *
 * 1. 정의
 * : 팩토리 메서드 패턴은 객체의 생성 과정을 서브 클래스에 위임하는 디자인 패턴이다.
 * 이를 통해 클라이언트 코드는 구체적인 클래스의 인스턴스화 과정을 알 필요 없이 객체를 생성할 수 있다.
 *
 * 2. 구현 방식
 * : 팩토리 메서드를 정의하여, 이 메서드가 객체를 생성하고 변환하는 역할을 한다.
 * 클라이언트는 팩토리 메서드를 호출하여 필요한 객체를 받는다.
 *
 * 3. 장점
 * : 객체 생성 로직의 변경이나 확장이 필요할 때, 클라이언트 코드를 변경하지 않고도 새로운 객체 생성 로직을 쉽게 추가할 수 있다.
 *
 */

/* 스프링 프레임워크에서의 팩토리 메서드 패턴
 *
 * 1. 스프링 빈 팩토리
 * : 스프링의 BeanFactory 인터페이스는 객체(Bean) 생성과 관리의 복잡성을 추상화하는 팩토리 메서드 패턴의 한 예이다.
 * 이를 통해 스프링 컨테이너는 빈의 생명주기를 관리하며, 개발자는 생성된 빈을 사용할 수 있다.
 *
 * 2. 빈 생성 과정의 추상화
 * : 스프링에서 빈 생성 과정은 팩토리 메서드를 통해 추상화된다.
 * 개발자는 구체적인 객체 생성 과정을 몰라도 스프링 컨테이너를 통해 필요한 빈을 요청하고 사용할 수 있다.
 *
 * 3. ApplicationContext의 BeanFactory
 * : ApplicationContext는 BeanFacotry를 확장한 고급 인터페이스로,
 * 객체 생성 뿐만 아니라 다양한 추가 기능(이벤트 발행, 리소스 로딩)을 제공한다.
 *
 */