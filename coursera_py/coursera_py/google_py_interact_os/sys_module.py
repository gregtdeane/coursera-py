import sys
print(sys.argv)

#running this using "poetry run python sys_module.py" returns the name of the py file itself only
# but running using "poetry run python sys_module.py one to three" returns ['sys_module.py', 'one', 'to', 'three']
sys.exit(1)
#will make "echo $?" return 1 instead of 0