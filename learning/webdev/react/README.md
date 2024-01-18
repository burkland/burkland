## React Foundations

[Course Link](https://nextjs.org/learn/react-foundations/what-is-react-and-nextjs)

#### Chapter 1

###### Key Questions
- What is React? What is Next.js? How do they differ?
_See definitions_

Modern Application Considerations
- User Interface - how users will consume and interact with your application
- Routing - how users navigate between different parts of your application
- Data Fetching - where your data lives and how to get it
- Rendering - when and where you render static or dynamic content
- Integrations - what third-party services you use (for CMS, auth, payments, etc.) and how you connect to them
- Infrastructure - where you deploy, store, and run your application code (serverless, CDN, edge, etc.)
- Performance - how to optimize your application for end-users
- Scalability - how your application adapts as your team, data, and traffic grow
- Developer Experience - your team's experience building and maintaining your application


React - An unopinionated JavaScript library for building UIs (solves only one of the above considerations)
Next.js - A React framework to build web applications (routing, fetching, catching, etc.)

#### Chapter 2

###### Key Questions
- How do browsers render web pages?
_The browser converts the served HTML to a DOM which can then be updated by the various scripts loaded with it_

DOM - An tree-like object representation of the HTML elements in the served file, has methods that can be called upon with JavaScript

###### Quiz
1. True or False: You can update the page content by manipulating the DOM.
_True: The DOM is an object representation of the HTML elements. It acts as a bridge between your code and the user interface, and has a tree-like structure with parent and child relationships._

### Chapter 3

###### Key Question
- Is JavaScript a strongly typed language?
_No, that was the catalyst for TypeScript_
- What does `appendChild()` do?
_Adds a given node to the end of Parent's list of children node ([documentation](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild))_
- What is Imperative Programming? What is Declarative Programming? How do they differ?


DOM can create elements outside of the original HTML source, DOM was adjusted with JavaScript, although a lot of code was written just to add a header

Imperative Programming - A programming paradigm that requires each solution be coded with step-by-step instructions
Declarative Programming - A programming paradigm that requires solutions be coded with an expectation of the result

React is a declarative library for building UIs.

###### Quiz
1. Which of the following statements is more declarative?
~~_"Knit the dough, roll the dough, add tomato sauce, add cheese, add ham, add pineapple, bake at 200 degrees celsius in a stone oven for..."_~~
_"A Hawaiian pizza please."_ _Declarative programming allows you to describe what you want to happen, rather than the steps to make it happen._