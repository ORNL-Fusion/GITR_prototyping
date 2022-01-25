import argparse
import csv
from file_map import *
from matplotlib import pyplot

# set the high level plot information:
def plot_data_set( prefix, color, axis_1d, axis_3d_position, axis_3d_velocity ):

  vx = read_data_file( f'{prefix}_vx.csv' )
  vy = read_data_file( f'{prefix}_vy.csv' )
  vz = read_data_file( f'{prefix}_vz.csv' )

  x = read_data_file( f'{prefix}_x.csv' )
  y = read_data_file( f'{prefix}_y.csv' )
  z = read_data_file( f'{prefix}_z.csv' )

  t = read_data_file( f'{prefix}_t_values.csv' )

# for all flags specified, plot the 
# vx, vy, vz
# x,  y,  z

# vx
  axis_1d[ 0, 0 ].plot( t, vx, color )

# vy
  axis_1d[ 0, 1 ].plot( t, vy, color )

# vz
  axis_1d[ 0, 2 ].plot( t, vz, color )

# x
  axis_1d[ 1, 0 ].plot( t, x, color )

# y
  axis_1d[ 1, 1 ].plot( t, y, color )

# z
  axis_1d[ 1, 2 ].plot( t, z, color )

# 3d plot of position and velocity
  axis_3d_position.plot(x, y, z, color )

  axis_3d_velocity.plot( vx, vy, vz, color )

# start of main code

# get command line arguments
parser = argparse.ArgumentParser()

# if present, store the variable
parser.add_argument( '--boris_python', action= 'store_true', help = 'python boris impl.' )
parser.add_argument( '--boris_gitr', action= 'store_true', help = 'gitr\'s boris' )
parser.add_argument( '--analytic_python', action= 'store_true', help = 'analytical python' )
parser.add_argument( '--analytic_gitr', action= 'store_true', help = 'analytical gitr' )
parser.add_argument( '--simple', action= 'store_true', help = 'simple pusher' )

args = parser.parse_args()

# create figures
figure_1d, axes_1d = pyplot.subplots( 2, 3 )

axes_1d[ 0, 0 ].set_title( "vx(t)" )
axes_1d[ 0, 1 ].set_title( "vy(t)" )
axes_1d[ 1, 2 ].set_title( "vz(t)" )
axes_1d[ 1, 0 ].set_title( "x(t)" )
axes_1d[ 1, 1 ].set_title( "y(t)" )
axes_1d[ 1, 2 ].set_title( "z(t)" )

figure_3d_position, axis_3d_position = pyplot.subplots( subplot_kw = dict( projection = "3d" ) )

axis_3d_position.set_title( "position" )

figure_3d_velocity, axis_3d_velocity = pyplot.subplots( subplot_kw = dict( projection = "3d" ) )

axis_3d_velocity.set_title( "velocity" )

legend_labels = []

# if (option), open files with certain names set by previous scripts. Read filenames. 
if args.boris_python:

  print( 'Ahoy! boris_python activated' )

  plot_data_set( boris_python_file_prefix, 'b', axes_1d, axis_3d_position, axis_3d_velocity )

  legend_labels.append( boris_python_file_prefix )

else:

  print( 'Ahoy! boris_python NOT activated' )

if args.boris_gitr:

  print( 'Ahoy! boris_gitr activated' )

  plot_data_set( boris_gitr_file_prefix, 'r', axes_1d, axis_3d_position, axis_3d_velocity )

  legend_labels.append( boris_gitr_file_prefix )

else:

  print( 'Ahoy! boris_gitr NOT activated' )

if args.analytic_python:

  print( 'Ahoy! analytical_python activated' )
  
  plot_data_set( analytic_python_file_prefix, 'g', axes_1d, axis_3d_position, axis_3d_velocity )

  legend_labels.append( analytic_python_file_prefix )

else:

  print( 'Ahoy! analytical_python NOT activated' )

if args.analytic_gitr:

  print( 'Ahoy! analytical_gitr activated' )
  
  plot_data_set( analytic_gitr_file_prefix, 'k', axes_1d, axis_3d_position, axis_3d_velocity )

  legend_labels.append( analytic_gitr_file_prefix )

else:

  print( 'Ahoy! analytical_python NOT activated' )

if args.simple:

  print( 'Ahoy! simple activated' )

else:

  print( 'Ahoy! simple NOT activated' )

# activate figure legends
axis_3d_position.legend( legend_labels )
axis_3d_velocity.legend( legend_labels )
axes_1d[ 0, 0 ].legend( legend_labels )
'''
axis_1d[ 0, 1 ].legend()
axis_1d[ 0, 2 ].legend()
axis_1d[ 1, 0].legend()
axis_1d[ 1, 1 ].legend()
axis_1d[ 1, 2 ].legend()
'''

# Display the figures after populating them
pyplot.show()
