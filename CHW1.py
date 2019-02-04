import numpy as np

'''
CONSTANTS / INITIATION
'''

NLINE = 7 # number of lines
NBUS = 6 # number of buses


R = [0] * NLINE # line resistances
X = [0.1, 0.05, 0.1, 0.14, 0.1, 0.05, 0.05] # line reactances

# line admittances
G = [0] * NLINE
B = [0] * NLINE

for line in range(0, NLINE - 1):
    z_squared = R[line] * R[line] + X[line] * X[line]
    G[line] = R[line] / z_squared
    B[line] = -X[line] / z_squared

BC = [0] * NLINE # shunt capacitances

# trans line buses
START_BUS = [1, 1, 2, 3, 3, 4, 5]
END_BUS = [4, 2, 5, 4, 6, 5, 6]

# real/reactive power for bus loads (p.u.)
P_load = [0, 0, 0, 1, 0.5, 1.1]
Q_load = [0, 0, 0, 0.4, 0.3, 0.4]

# real power for gen loads (p.u.)
P_gen = [0.7, 0.9, 1, 0, 0, 0]

# gen sequence reactances (p.u.)
X_g0 = [0.02, 0.02, 0.02, 0, 0, 0] # zero seq
X_g1 = [0.02, 0.02, 0.01, 0, 0, 0] # pos seq
X_g2 = [0.005, 0.005, 0.005, 0, 0, 0] # neg seq

# gen grounded (1 = grounded Y, 0 = ungrounded)
gen_ground = [0, 1, 1, 0, 0, 0]

# prefault voltage magnitude and angle (p.u.)
V_pf = [1.05, 1.05, 1.05, 1.021, 1.017, 1.015]
theta_pf = [0, 0.164, -1.645, -4.083, -4.328, -5.278] # degrees

'''
FAULT LOCATION
'''

fault_location = input("Please identify fault location")


'''
FAULT TYPE
'''

fault_type = input("Please identify fault type:")

if fault_type == "3 Phase":
    # run 3 phase method
elif fault_type == "SLG":
    # run SLG method
elif fault_type == "LL":
    # run LL method
elif fault_type == "DLG":
    # run DLG method
else:
    # don't do anything/ask again

'''
FAULT IMPEDANCE
'''

fault_impedance = input("Please identify fault impendance")

'''
RESULTS BUS
'''

results_bus = input("Please identify fault results bus")

# look at index in bus start and end list that faulted bus # at start and results bus # at end.
# fault stuff in between
