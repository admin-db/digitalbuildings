import strictyaml as syaml
import ruamel
import sys
from validate import generate_universe
from validate import entity_instance
from validate import instance_parser
import argparse

#theoretically works, issue validating
def create_ontology(yaml_filepath):

	print('Generating universe ...')
	universe = generate_universe.BuildUniverse(yaml_filepath)

	if universe is None:
	  print('\nError generating universe')
	  sys.exit(0)

	print('Universe generated successfully')
	return universe

if __name__ == "__main__":
	ont_universe = create_ontology("C:/Users/Andrew/Documents/GitHub/digitalbuildings/ontology")
