# This file contains file mappings and utilities to read/wrte output files
import csv

# file names for reading/writing
analytic_python_file_prefix = 'analytic_python'
boris_python_file_prefix = 'boris_python'
analytic_gitr_file_prefix = 'analytic_gitr'
boris_gitr_file_prefix = 'boris_gitr'
simple_pusher_file_prefix = 'simple_python'

def dump_csv_rows( file_name, vv ):

  with open( file_name, 'w', newline = '' ) as csv_file:
  
    csv.writer( csv_file, delimiter = ' ' ).writerows( [ v ] for v in vv )

# write data file
def write_data_file( t, vx, vy, vz, x, y, z, file_name ):

  # verify lengths of data files
  assert( len( t ) == len( vx ) )
  assert( len( t ) == len( vy ) )
  assert( len( t ) == len( vz ) )

  assert( len( t ) == len( x ) )
  assert( len( t ) == len( y ) )
  assert( len( t ) == len( z ) )

  dump_csv_rows( f'{file_name}_vx.csv', vx )
  dump_csv_rows( f'{file_name}_vy.csv', vy )
  dump_csv_rows( f'{file_name}_vz.csv', vz )

  dump_csv_rows( f'{file_name}_x.csv', x )
  dump_csv_rows( f'{file_name}_y.csv', y )
  dump_csv_rows( f'{file_name}_z.csv', z )
  
  dump_csv_rows( f'{file_name}_t_values.csv', t )

# read data file as a vector command needed here
def read_data_file( file_name ):

  with open( file_name, newline='' ) as csv_file:

    csv_reader = csv.reader( csv_file, delimiter = ' ' )

    return [ float( row.pop() ) for row in csv_reader if len( row ) == 1 ]
