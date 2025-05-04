import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


# Geração de Pontos no plano R^3

x = np.linspace(-2, 2, 6)
y = np.linspace(-2, 2, 6)
z = np.linspace(0.5, 2, 6)
x, y, z = np.meshgrid(x, y, z)


# Campo Vetorial F(x,y,z) = <y/z, -x/z, z/4>

P = y/z
Q = -x/z
R = z/4

ax = plt.axes(projection = '3d')


# Plotagem do Gráfico

ax.quiver(x, y, z, P, Q, R, length=0.5, normalize=True, color='orange')
ax.set_title('Campo Vetorial 3D: F(x, y, z) = <y/z, -x/z, z/4>')
ax.set_xlabel(' eixo x')
ax.set_ylabel(' eixo y')
ax.set_zlabel(' eixo z')
plt.show()