# Modeling and simulation project 

[UNAM - ENES Morelia](https://www.enesmorelia.unam.mx/)

## Team members
- Public relations: Gerardo
- Technology leader: Juan Pablo Maldonado Castro (maldonadocastrojp@gmail.com)
- Project leader: María Lucrecia Beltz Gonzalez

## Area
Dynamical systems

### Examples of Dynamical Systems

A dynamical system determines future states from a model given its current state. There are lots of different examples regarding these, some are:

* N-body model: consists of a dynamical system of particles that interact through physical forces such as gravity.
* Elastic pendulum model: a system which consists of a mass attached to a spring and its future movement behavior is established by its initial conditions.
* Population dynamical system: these are models that evaluate size and age of populations through mathematical interpretations.
* Double pendulum: in a similar fashion to the elastic pendulum mode, it consists of a pendulum attached to another pendulum whose movement will depend on its initial conditions.
* Bouncing ball dynamic model: given an initial throw, this model evaluates the bouncing of the ball according to the conditions of the surface, the ball and its throw.

The main reference for this information was extracted from [this Wikipedia article](https://en.wikipedia.org/wiki/Dynamical_system). For a further understanding of the examples of these systems, there are more articles and information about them online.

## Programming Language
Python3

## Introduction

### The N-body problem

One of the most well-known physics problems in dynamical systems is the **N-body problem**. It consists in predicting the movement of various celestial bodies that are in constant interaction by theNewton's Law of Gravity. The classical physical problem is as follows:

Given the initial orbital properties (current position, speed and time) of a group of celestial bodies; predict all their interactive forces resulting in the prediction of its future orbits.

The equations of motion for a particle of index $i$ in a system containing $N$ particles are:

![equation](https://latex.codecogs.com/gif.latex?\ddot{\textbf{r}}&space;=&space;-G\sum_{j=1;j\neq&space;i}^{N}\frac{m_j(\textbf{r}_i&space;-&space;\textbf{r}_j)}{|\textbf{r}_i&space;-&space;\textbf{r}_j|^3})



### Mars

Mars, the fourth planet in the Solar System and second smallest (just after Mercury). It counts with a total of two natural satellites: *Fobos* and *Deimos*.

## Hypothesis 

Given the initial data of a set of celestial bodies (position, speed and mass), it's possible to simulate its orbits. This would be done with the help of the Newton's Law of Gravity and the implementation of the N-body problem. 

## Objective

Simulate the orbits of a set of celestial bodies from the Solar System. This will be done through the implementation of an N-body simulation using one of the different numerical integration methods applied to this problem (some of them are force polynomials, Hermite and individual time-steps).

For this implementation, the data from celestial bodies within our Solar System can be extracted from [Horizon's System](https://ssd.jpl.nasa.gov/horizons/app.html#/). This site provides real-time position and velocity components of planets, satellites, asteroids, spacecraft, etc., alongisde some future predictions.

## Justification

The basic idea of the N-body problem came in 1687 with Isaac Newton's work *Principia*. The capability of describing the interaction between different particles through Newton's second law of motion with equations brought a lot of attention and investigation to reach the solution of the problem. Later, the limitations of this problem were found by Henry Poincaré: something known as the non-integrability principle. Which would occur whenever there were three or more bodies in the problem.

Due to these issues, there aren't analytical solutions to the N-Body problem. Leading us to the use of numerical methods that are capable of tracking and moving the position of each particle in the system given some initial data. This results in numerical solutions whose accuracy tends to have really satisfactory results for long periods of time. Allowing us to give approximate solution to lots of problems of this nature.

## Bibliography

Aarseth, S. (2003). *Gravitational N-Body Simulations: Tools and Algorithms*. Cambridge Press.
Batnagar and Saha (1992). *N-Body Problem*. Astronomical Society of India, Bulletin. http://adsabs.harvard.edu/full/1993BASI...21....1B 
Greengard, L. (1990). *The Numerical Solution of the N-Body Problem*. https://aip.scitation.org/doi/pdf/10.1063/1.4822898
