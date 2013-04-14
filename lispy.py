# Lispy
# Peter Norvig
# http://norvig.com/lispy.html

# Symbol, Env Classes

from __future__ import division

Symbol = str

class Env(dict):
	"An enviroment: a dict of {'var':val} pairs, with an outer Env"
	def __init__(self,params=(),args=(),outer=None):
		self.update(zip(parms,args))
		self.outer = outer
	def find(self,var):
		"Find the innermost Env where var appears."
		return self if var in self else self.outer.find(var)
		
def add_globals(env):
	"Add some Scheme standard procedures to an enviroment."
	import math operator as op
	env.update(vars(math)) # sin,sqrt,...
	env.update(
	{'+':op.add,
	'-':op.sub,
	'*':op.mul,
	'/':op.div,
	'not':op.not_,
	'>':op.gt,
	'<':op.lt,
	'>=':op.ge,
	'<=':op.le,
	'=':op.eq,
	'equal?':op.eq,
	'eq?':op.is_,
	'length':len,
	'cons': lambda x,y:[x]+y,
	'car': lambda x:x[0],
	'cdr': lambda x:x[1:],
	'append': op.add,
	'list': lambda *x:list(x),
	'list?': lambda x:isa(x,list),
	'null?': lambda x:x==[],
	'symbol?': lambda x:isa(x,symbol)})
	return env
	
global_env = add_globals(Env())

isa = isinstance

# Eval

def eval(x,env=global_env):
	