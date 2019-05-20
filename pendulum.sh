#!/usr/bin/bash
./pendulum
echo "Be patient. plotting and animation-maker are in progress..."
python pendulum_ploter.py
python pendulum_anim.py
python pendulum_simul1.py
python pendulum_simul2.py
