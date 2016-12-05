# Spring Generator

Project to bring similar functionality found in Rails to the Spring Boot platform. Currently only supports maven-enabled projects.

For Example:

    > python main.py g scaffold User name:string age:integer

Will create the following files:
* Model - root/model/User.java
* Repository - root/repository/UserRepository.java
* Service - root/service/UserService.java
* Controller - root/controller/UsersController.java

The root is calculated upon script start. For example, if being run on a project with the following in `pom.xml`:

    <groupId>com.example</groupId>

the root will be `src/main/com/example/`

### Customization
Per default, Spring Generator will auto-discover necessary configurations and then use best-practices to decide
where and how to generate files. However, if you would like to customize the generation of the files, Spring Generator
gives you the ability to alter defaults by placing `bootgen.yml` in the root of the project. The following configurations
are supported:

| Property       	| Description                                 	| Type   	|
|----------------	|---------------------------------------------	|--------	|
| dir.model      	| Directory in which to generate models       	| String 	|
| dir.repository 	| Directory in which to generate repositories 	| String 	|
| dir.controller 	| Directory in which to generate controllers  	| String 	|
| dir.service    	| Directory in which to generate services     	| String 	|
| lombok.enabled    | Should we enable generation in lombok mode   	| Boolean 	|


### Lombok Support
Generation of models will change if a lombok dependency is found in `pom.xml`. This will import lombok and annotate
the model differently. For example:

    //NO LOMBOK
    @Entity
    public class Example {

        @Id
        @GeneratedValue(strategy = GenerationType.AUTO)
        private Integer id;

        public Integer getId() {
            return this.id;
        }

        public void setId(Integer id) {
            this.id = id;
        }

    }
<!-- separate -->

    import lombok.AllArgsConstructor;
    import lombok.Builder;
    import lombok.Data;
    import lombok.NoArgsConstructor;

    @AllArgsConstructor
    @Builder
    @Data
    @NoArgsConstructor
    public class Example {

        @Id
        @GeneratedValue(strategy = GenerationType.AUTO)
        private Integer id;

    }

For lombok information, visit the project's [homepage](https://projectlombok.org/).

