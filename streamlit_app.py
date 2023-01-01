import streamlit as st
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Assigning title and subtitle to the app

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
# here more description will be given
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
fig, ax = plt.subplots()
ax.plot(t, y1, 'r', label='Species 1')
ax.plot(t, y2, 'b', label='Species 2')
ax.legend(loc='best')
ax.set_xlabel('Time')
ax.set_ylabel('Population Size(N)')
st.pyplot(fig)


CV_link = {"Know the Developer !!":"https://mohit254-portfolio-cv-t4bwqw.streamlit.app/#mohit-poudel"}
st.markdown("## Developed By: ")
st.markdown("
            ### Mohit Poudel
            #### Junior Researcher at the Central Lab of Biotechnology, Agriculture and Fprestry University
            ")
for (platform, link) in SOCIAL_MEDIA.items():
    st.write(f"[{platform}]({link})")

        
            
            
