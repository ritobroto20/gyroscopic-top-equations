# Behaviour of simple FODE with varying initial conditions
Consider a first order differential equation of the following form-
$$\frac{dy}{dx}=f(x,y)$$

Say we take $f(x,y)$ in the form of $f(y)$, where the function has only output dependence.
In this section we have analysed how the the differential behaves with varying initial conditions, and tried find out the patterns.

### We have taken the following differenential equations:
1. $\frac{dy}{dx}=\sin(y)$
2. $\frac{dy}{dx}=\cos(y)$
3. $\frac{dy}{dx}=(x^2-1)$

### Observtions
- From the graphs we have plotted it can be seen that the asymptotic behaviour of $y(x)$ is dependent on the the roots of f(y).
- If the initial condition is situated at a root of f(y). This means at initial time x=0, the value of $y$ is such that $f(y_{root})=0$. This makes the differential equation at that point $\frac{dy}{dx}=0$ at $(0,y_{root}). Applying RK4 to get the value of $y$ at time $x=0+\delta x$ gives 