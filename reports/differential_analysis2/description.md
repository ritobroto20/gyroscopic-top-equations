# Behaviour of simple FODE with varying initial conditions
Consider a first order differential equation of the following form (eqn(1))-
$$\frac{dy}{dx}=f(x,y)$$

Say we take $f(x,y)$ in the form of $f(y)$, where the function has only output dependence.
In this section we have analysed how the the differential behaves with varying initial conditions, and tried find out the patterns.

### We have taken the following differenential equations:
1. $\frac{dy}{dx}=\sin(y)$
2. $\frac{dy}{dx}=\cos(y)$
3. $\frac{dy}{dx}=(y^2-1)$

### Observtions
- From the graphs we have plotted it can be seen that the asymptotic behaviour of $y(x)$ is dependent on the the roots of f(y).
- If the initial condition is situated at a root of f(y). This means at initial time x=0, the value of $y$ is such that $f(y_{root})=0$. This makes the differential equation at that point $\frac{dy}{dx}=0$ at $(0,y_{root})$. Applying RK4 to get the value of $y$ at time $x=0+\delta x$ gives 
- Breaking the domain and range into discrete parts to make it numerically computable. Consider the $x$ values in the dicrete domain ranging from $x_0$ to $x_L$ and the corresponding y values ranging from $y_0$ to $y_L$.
- We have the initial condition $(x_0,y_0)$ where $f(y_0)=0$. 
- Here we have implemented Runge-Kutta4 algorithm to numerically calculate the values of $(x_i,y_i)$ for the differential equation eqn(1). In the RK4 algorithm we find $y_{i+1}$ given $y_i$ by the following rule:\\
-  a <br />
b <br />

Putting it into eqn(1) we 