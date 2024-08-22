package com.example.crud.config;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.core.Ordered;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Slf4j
@RequiredArgsConstructor
public class WebConfig implements WebMvcConfigurer {
    
//    어케 쓰나요
//    private final JwtTokenInterceptor jwtTokenInterceptor;
//
//    @Override
//    public void addInterceptors(InterceptorRegistry registry) {
//        registry.addInterceptor(jwtTokenInterceptor)
//                .addPathPatterns("/**")
//                .excludePathPatterns("/user/login", "/login", "/main/rootPage");
//    }


    private static final String[] CLASSPATH_RESOURCE_LOCATIONS = {
            "classpath:/",
            "classpath:/static/",
            "classpath:/public/",
            "classpath:/resources/",
            "classpath:/META-INF/resources/",
            "classpath:/META-INF/resources/webjars/"
    };

    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        log.debug(" [+] WebConfig start ");
        registry.addRedirectViewController("/", "/login");
        registry.setOrder(Ordered.HIGHEST_PRECEDENCE);
    }

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/**")
            .addResourceLocations(CLASSPATH_RESOURCE_LOCATIONS);
    }

}
