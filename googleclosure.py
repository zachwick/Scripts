#!/usr/bin/python2.7
# Argument 1: javascript file available via http
# Argument 3: one of {'WHITESPACE_ONLY','SIMPLE_OPTIMIZATIONS','ADVANCED_OPTIMIZATIONS'}
# Argument 2: externs file available via http
import httplib,urllib,sys

params = urllib.urlencode([
   ('code_url',sys.argv[1]),
   ('compilation_level',sys.argv[3]),
   ('output_format','text'),
   ('output_info','statistics'), #Other options are 'compiled_code'
   ('externs_url',sys.argv[2]),
  ])

# Always use this value for header Content-type!!!!
headers = { "Content-type":"application/x-www-form-urlencoded" }
conn = httplib.HTTPConnection('closure-compiler.appspot.com')
conn.request('POST','/compile',params,headers)
response = conn.getresponse()
data = response.read()
print data
conn.close


