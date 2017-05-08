import subprocess

submit_params = {
    'Universe': 'vanilla',
    'Run_as_owner': 'True',
    'cmd': '/bin/cat',
    'args': '/proc/self/status',
    'when_to_transfer_output': 'ON_EXIT_OR_EVICT',
}

# lines = ['%s=%s' % (k, v) for k, v in submit_params.iteritems()]
# lines.append('Queue')
# job_params = '\n'.join(lines)

job_params =  "\n".join("=".join(_) for _ in submit_params.items())
job_params += '\n queue'

submit_cmd = """echo \"{0}\" | condor_submit""".format(job_params)

print 'executing', submit_cmd

output = subprocess.check_output(submit_cmd, shell=True)

# pipe = subprocess.Popen(
#     template,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.STDOUT
# )
# 
# #pipe.stdin.write(job_params)
# #pipe.stdin.close()
# output = pipe.stdout.read()
# status = pipe.wait()
print ' O: ', output
