# Module list for Backend with Python

Following list contains topics useful for Backend Python Engineers in Tooploox, divided into modules.
It's neither final nor unchangeable list, but we think it covers most important parts. Some modules are more,
some less specified - the final shape is created by mentor.

In every module there is a section for links to external resources. You can use it for self-development, but also
update, send new links and remove no longer useful ones. It's a place for sharing interesting materials associated
with module's topic. Feel free to contribute!

> When you are looking into new topics, it's always better to use already recommended materials.
> So, when you find something that could be useful for others as well, just send a PR with it!

Modules aren't ordered - numbers are only to help identifying them.

- [Module list for Backend with Python](#module-list-for-backend-with-python)
  - [1. Basic unit testing in Python](#1-basic-unit-testing-in-python)
  - [2. REST API programming in Flask](#2-rest-api-programming-in-flask)
  - [3. Contributing to a team project](#3-contributing-to-a-team-project)
  - [4. Python kick-start](#4-python-kick-start)
  - [5. Basic database programming in Python](#5-basic-database-programming-in-python)
  - [6. Development with Docker](#6-development-with-docker)
  - [7. Backend architecture basics](#7-backend-architecture-basics)
  - [8. Integration and end-to-end testing](#8-integration-and-end-to-end-testing)
  - [9. Advanced unit testing in Python](#9-advanced-unit-testing-in-python)
  - [10. CI/CD basics](#10-cicd-basics)
  - [11. Clean code](#11-clean-code)
  - [12. 12-factor basics](#12-12-factor-basics)
  - [13. Advanced REST in Flask](#13-advanced-rest-in-flask)
  - [Other ideas](#other-ideas)

<!-- 
## X. Module name

* Mentor: 
* Purposes / topics to cover:
  * A

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 
-->

## 1. Basic unit testing in Python

* Mentor: 
* Purposes / topics to cover:
  * Why to test and what to test
  * Running tests
    * All tests
    * Subsets of tests
  * Basic mocking
  * Basic usage of pytest and unittest

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details>

## 2. REST API programming in Flask

* Mentor: Roman Koziołek ([module repo](https://github.com/tooploox/mentoring/tree/master/python_backend/2_REST_API_basics))
* Prerequisites: 
  * [Basic unit testing in Python](#1-basic-unit-testing-in-python)
  * [Python kick-start](#4-python-kick-start)
* Purposes / topics to cover:
  * Flask basics
  * REST API basics
    * handling and role of HTTP methods POST/GET/PUT/DELETE
    * different Content-Type (text, image/file, json)
  * Implementing REST API
  * Using external APIs (ML?)
  * Flask unit testing
  * Writing basic integration tests for the API
  * Basic tools
    * curl
    * Postman/Insomnia

<details>
  <summary>Useful resources for self-development</summary>

  * [RESTfulapi.net](https://restfulapi.net/) - a general introduction to REST API
</details>

## 3. Contributing to a team project

* Mentor: 
* Purposes / topics to cover:
  * Git intro
  * Git flow: branching, committing, rebasing and merging
  * Conflicts
  * Github
  * Code reviews
  * Merge-to-master checklist
  * Changelogs

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details>

## 4. Python kick-start

* Mentor: 
* Purposes / topics to cover:
  * Setting up a development environment
    * Setting up an editor (Any / VSCode / PyCharm?)
    * Environment management (different Python versions, virtualenvs)
  * Installing libraries
  * Hello world (using a third-party library)
  * Basic rules
    * No hard-coded values ?

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details>
 

## 5. Basic database programming in Python

* Mentor: 
* Purposes / topics to cover:
  * psycog2
  * ORM basics (SQLAlchemy or other)
  * SQL basics

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 6. Development with Docker

* Mentor: 
* Purposes / topics to cover:
  * Docker intro
  * Dockerfile (write basic)
  * docker-compose for local development
  * Local environment variables (.env)
  * A few tips for dockerizing Python apps

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 7. Backend architecture basics

* Mentor: 
* Purposes / topics to cover:
  * Larger scale
  * Design architecture easy-to-scale

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 8. Integration and end-to-end testing

* Mentor: 
* Purposes / topics to cover:
  * Why and what
  * Pytest/unittest
  * Behave (gherkin)

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 9. Advanced unit testing in Python

* Mentor: 
* Purposes / topics to cover:
  * Fixtures
  * Mocking
    * Why: difficult to set up
    * Why: external dependencies
    * Why: repeatable tests (time)
  * Looking for edge cases
  * Debugging tests
    * No extra tooling
    * PyCharm, Visual Studio Code

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 10. CI/CD basics

* Mentor: 
* Purposes / topics to cover:
  * Contributing to a project with already existing CI/CD
  * Small changes in existing CI/CD jobs

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 

## 11. Clean code

* Mentor: 
* Purposes / topics to cover:
    * Selected patterns with python implementations
      * Dependency injection
      * Adapter, facade
      * Observer
      * Singleton
      * Factory methods
    * Side-effects vs pure functions
    * OOP basics

<details>
  <summary>Useful resources for self-development</summary>

  * [Tooploox "Golden Standards"](https://docs.google.com/document/d/1vQ2UWA_eAWPIJAfmZ__KWub-2Ogz-NjDLBBVTHWuMm4/edit#)

</details>

## 12. 12-factor basics

* Mentor: 
* Purposes / topics to cover:
  * 12-factor 

<details>
  <summary>Useful resources for self-development</summary>

  * [The Twelve-Factor App](https://12factor.net/)  

</details>

## 13. Advanced REST in Flask

* Mentor: 
* Prerequisites:
  * [REST API programming in Flask](#2-rest-api-programming-in-flask)
* Purposes / topics to cover:
  * Document API (Swagger)
  * Flask extension(s) to build API
    * like `flask_resful`
  * Tool(s) for validation and formatting input/output
    * e.g. `marshmallow`
  * Basic caching responses (files?)

<details>
  <summary>Useful resources for self-development</summary>

  None yet, feel free to contribute  
</details> 


## Other ideas
* Devops
  * CI/CD
  * Dockerization
  * Deployment
  * Automation
  * Monitoring
* Opinionated testing approaches
