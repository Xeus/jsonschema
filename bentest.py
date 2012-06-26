from jsonschema import validate, ValidationError, Validator, ErrorTree
# schema = {
# 	"items" : {"enum" : [1, 2, 3]},
# 	"maxItems" : 0,
# 	"properties" : {
# 		"price" : {"type" : "string", "minLength" : 3},
# 		"minimumL" : {"type" : "object"}
# 	}
# }


schema = {
	"type" : "object",
	"properties" : {
		"label" : {"type" : "string", "minLength" : 3},
		"name" : {"type" : "string", "minLength" : 3},
		"email" : {"type" : "string", "email" : "[a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?" },
	},
}

instance = { "name" : "ef", "label" : "i", "email" : "joe@test" }

# try:
# 	validate(instance, schema, stop_on_error=False)
# except ValidationError, e:
# 	print e
# 	print e.errors

def validate(instance,schema, **kargs):
	v = Validator()
	errorObj = []

	#iter_errors was deprecated in the jsonschema code
	for error in v.iter_errors(instance, schema):	
		newstr =  error.path[0]
		errorMsg = "ERROR #" + str(error.errorCode) + " in '" + newstr + "': " + str(error)
		errorObj.append({ 'code' : error.errorCode, 'msg' : errorMsg, 'key' : newstr, 'field' : error.validator })
	if len(errorObj) != 0:
		# Create exception load withj errorOBj and throw it
		raise ValidationError("Validation error...", errorObj)

try:	
	validate(instance,schema)
except ValidationError, e:
	print e.errorCode