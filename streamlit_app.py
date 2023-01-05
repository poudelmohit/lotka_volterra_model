import streamlit as st
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Assigning title and subtitle to the app
st.set_page_config(page_title="Lotka-Volterra Simulator", page_icon=":heart:")

st.title("Lotka-Volterra Model Simulator")
st.subheader("An Interactive App to learn Predator-Prey Equations")

# Display the Lotka-Volterra competition equations
st.markdown(
    r"""
    The Lotka-Volterra competition equations describe the dynamics of two species competing for the same resource in an ecosystem. The equations are given by:

    $$\frac{dN_1}{dt} = r_1 N_1 \left( 1 - \frac{N_1 + a N_2}{K_1} \right)$$

    $$\frac{dN_2}{dt} = r_2 N_2 \left( 1 - \frac{N_2 + b N_1}{K_2} \right)$$

    where,

    $N_1$ and $N_2$ are the populations of the two species,

    $r_1$ and $r_2$ are the intrinsic growth rates of the species, 

    $a$ and $b$ are the interaction coefficients that describe the effect of one species on the other, and 

    $K_1$ and $K_2$ are the carrying capacities of the species.
    """
)

# Explaining in more depth:
st.markdown("### Let's understand the model with an example: ")
st.markdown('''
The Lotka-Volterra competition model is a mathematical model that describes the interactions between two species in a competitive environment. The model is named after Alfred J. Lotka and Vito Volterra, who independently developed the model in the early 20th century.

The model is based on the assumption that each species has a certain reproductive rate, which determines how quickly it can reproduce and increase its population size. The model also assumes that each species has a certain level of resource use, which determines how much of a particular resource (such as food or habitat) it consumes.

The model predicts that the population sizes of both species will change over time based on their reproductive rates and resource use. If one species has a higher reproductive rate and/or lower resource use than the other species, it is likely to outcompete the other species and increase in population size. If both species have similar reproductive rates and resource use, they may coexist in a stable equilibrium.

Here is an example of how the Lotka-Volterra competition model works:

Imagine that there are two species of rabbits living in a grassy meadow. One species of rabbit, species A, has a high reproductive rate and low resource use, while the other species, species B, has a low reproductive rate and high resource use.

Initially, the meadow has a finite amount of grass (the resource) and both species of rabbits are present in equal numbers. Over time, the population of species A will increase because it is able to reproduce more quickly and consume fewer resources than species B. As the population of species A grows, the population of species B will decline because it is unable to compete with species A for resources.

Eventually, the population of species A may reach a stable equilibrium, where it is able to maintain its population size without continuing to increase. The population of species B, on the other hand, may continue to decline until it becomes locally extinct.

This is a simplified example of how the Lotka-Volterra competition model works, but it illustrates the basic principles of competition between two species in a finite environment.
''')


# defining a formula:


def lv(y, t, r1, r2, a, b, K1, K2):
    N1 = y[0]
    N2 = y[1]
    dN1dt = r1 * N1 * (1 - (N1 + a * N2) / K1)
    dN2dt = r2 * N2 * (1 - (N2 + b * N1) / K2)
    return [dN1dt, dN2dt]


# Define the growth rates and interaction coefficients as streamlit sliders


st.sidebar.markdown("## Input Parameters")
r1 = st.sidebar.slider('Growth rate of species 1 (r1)', 0.01, 1.0, 0.01)
r2 = st.sidebar.slider('Growth rate of species 2 (r2)', 0.01, 1.0, 0.01)
K1 = st.sidebar.number_input('Carrying capacity of species 1 (K1)', value=100, step=1)
K2 = st.sidebar.number_input('Carrying capacity of species 2 (K2)', value=100, step=1)
a = st.sidebar.slider('Interaction coefficient \'a\' (effect of species 2 on species 1)', 0.0, 1.0, 0.5)
b = st.sidebar.slider('Interaction coefficient \'b\' (effect of species 1 to species 2)', 0.0, 1.0, 0.5)
N1 = st.sidebar.number_input("Population size of species 1 (N1)", step=1)
N2 = st.sidebar.number_input("Population size of species 2 (N2)", step=1)
T = st.sidebar.slider('Length of simulation', 1, 1000, 1)

# Set the time range for the simulation
t = np.linspace(0, T, 100)

# Solve the equations using the odeint function from scipy
y = odeint(lv, [N1, N2], t, args=(r1, r2, a, b, K1, K2))

# Extract the population sizes for each species
y1 = y[:, 0]
y2 = y[:, 1]

# Plot the results
st.markdown("### Plotting the values:")
fig, ax = plt.subplots()
ax.plot(t, y1, 'r', label='Species 1')
ax.plot(t, y2, 'b', label='Species 2')
ax.legend(loc='best')
ax.set_xlabel('Time')
ax.set_ylabel('Population Size(N)')
st.pyplot(fig)

st.markdown("## Developed By: ")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("https://mohit254-portfolio-cv-t4bwqw.streamlit.app/~/+/media/511fd1351113b1b2f0acc6c65d463c50c4155c521ee6fce285af2566.png", width=230)

with col2:
    st.title("Mohit Poudel")
    st.write("Bioinformatics & population genetics enthusiast, self-taught python programmer")
    st.write("Agriculture and Forestry University")
    st.write("Chitwan, Nepal")
st.markdown("##### [Know more about the developer !!](https://mohit254-portfolio-cv-t4bwqw.streamlit.app/#mohit-poudel)")




        
            
            
