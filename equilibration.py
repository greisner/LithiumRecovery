import numpy as np
import plotly as

# calculation of mass transport and concentrations for lithium recovery process

# start stream definition

Q1 = 200 # l/h
liC1 = 200 # mg/l
reC1 = 2000 # meq/l

Q2 = 200 # l/h
liC2 = 0 # mg/l
reC2 = 0 # meq/l

Q3 = 100 # l/h
liC3 = 0 # mg/l
reC3 = 0 # meq/l

Q4 = 100 # l/h
liC4 = 0 # mg/l
reC4 = 0 # meq/l

Q5 = 200 # l/h
liC5 = 0 # mg/l
reC5 = 0 # meq/l

Q6 = 100 # l/h
liC6 = 0 # mg/l
reC6 = 0 # meq/l

Q7 = 200 # l/h
liC7 = 0 # mg/l
reC7 = 0 # meq/l

Q8 = 0 # l/h
liC8 = 0 # mg/l
reC8 = 0 # meq/l

Q9 = 0 # l/h
liC9 = 0 # mg/l
reC9 = 0 # meq/l

Q10= 100 # l/h
liC10 = 0 # mg/l
reC10 = 0 # meq/l

Q11 = 0 # l/h
liC11 = 0 # mg/l
reC11 = 0 # meq/l

Q12 = 100 # l/h
liC12 = 0 # mg/l
reC12 = 0 # meq/l

Q12 = 100 # l/h
liC12 = 0 # mg/l
reC12 = 0 # meq/l

Q13 = 0 # l/h
liC13 = 0 # mg/l
reC13 = 0 # meq/l

Q14 = 100 # l/h
liC14 = 0 # mg/l
reC14 = 0 # meq/l

Q15 = 100 # l/h
liC15 = 0 # mg/l
reC15 = 0 # meq/l

Q16 = 100 # l/h
liC16 = 0 # mg/l
reC16 = 0 # meq/l

Q17 = 100 # l/h
liC17 = 0 # mg/l
reC17 = 0 # meq/l

Q18 = 100 # l/h
liC18 = 0 # mg/l
reC18 = 0 # meq/l

# loop ratios
rQ24 = 0.4 # Q4/Q2
rQ78 = 0.0 # Q8/Q7
rQ79 = 0.0 # Q9/Q7
rQ611 = 0.0 # Q11/Q6
rQ1713 = 0.0 # Q13/Q17

# electrodialysis parameter
rliC56 = 0.9 # liC6/liC5
rreC56 = 0.9 # reC6/reC5
rliC57 = 0.1 # liC7/liC5
rreC57 = 0.1 # liC7/liC5

# softening ix parameter

# lithium ix parameter
rliC1415 = 0 # li15/li14

for i in range(100):
    # bulk stream equilibrations

    # point A
    Q2 = Q1
    liC2 = liC1
    reC2 = reC1

    Q16 = Q15
    liC16 = liC15
    reC16 = liC15

    # point B
    Q3 = Q2 - Q4
    liC3 = liC2
    reC3 = reC2

    if rQ24 > 0:
        Q4 = Q2 * rQ24
        liC4 = liC2 * Q2 / Q4
        reC4 = reC2

    else:
        Q4 = 0
        liC4 = 0
        reC4 = 0

    # point C
    Q5 = Q3 + Q9
    liC5 = (liC3 * Q3 + liC9 * Q9) / Q5
    reC5 = (reC3 * Q3 + reC9 * Q9) / Q5

    # point D
    Q7 = Q5
    liC7 = liC5 * rliC57
    reC7 = reC5 * rreC57

    Q6 = Q12
    liC6 = Q12 * liC12 + Q5 * rliC56
    reC6 = Q12 * reC12 + Q5 * rreC56

    # point E
    Q14 = Q6 - Q11
    liC14 = liC6
    reC14 = reC6

    if rQ611 > 0:
        Q11 = Q6 * rQ611
        liC11 = liC6
        reC11 = reC6

    else:
        Q11 = 0
        liC11 = 0
        reC11 = 0

    # point F
    Q15 = Q14
    liC15 = liC14 * rliC1415
    reC15 = reC14

    Q17 = Q10
    liC17 = liC14 * Q14 / Q17
    reC17 = reC10

    # point G
    Q12 = Q11 + Q4 + Q13
    liC12 = (Q11 * liC11 + Q4 * liC4 + Q13 * liC13)/Q12
    reC12 = (Q11 * reC11 + Q4 * reC4 + Q13 * reC13)/Q12

    # point H
    Q10 = Q7 - Q9 - Q8
    liC10 = liC7
    reC10 = reC7

    if rQ78 > 0:
        Q8 = Q7 * rQ78
        liC8 = liC7
        reC8 = reC7

    else:
        Q8 = 0
        liC8 = 0
        reC8 = 0

    if rQ79 > 0:
        Q9 = Q7 * rQ79
        liC9 = liC7
        reC9 = reC7

    else:
        Q9 = 0
        liC9 = 0
        reC9 = 0

    # point I
    Q18 = Q17 - Q13
    liC18 = liC17
    reC18 = reC17

    if rQ1713 > 0:
        Q13 = Q17 * rQ1713
        liC13 = liC17
        reC13 = reC17

    else:
        Q13 = 0
        liC13 = 0
        reC13 = 0

for i in range(1, 19):
    print("Strom", i, ":", "Q=", round(eval("Q" + str(i))), "l/h", "Lithiumkonzentration", round(eval("liC" + str(i))), "mg/l", "Restkonzentration", round(eval("reC" + str(i))), "meq/l")
